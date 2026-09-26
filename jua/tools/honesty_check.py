#!/usr/bin/env python3
"""Honesty gate for Jua, built on TypeSafe (Jev) — enforces "never invent".

  claims:   every sentence in a text (explainer, end card, submission, subtitles) is
            checked against evidence (testimony transcript, research.md, logs).
  coverage: the face cam explainer covers all 8 items the organizers require.

Usage:
  python3 jua/tools/honesty_check.py claims  jua/delivery/explainer_thumbnail.md --evidence jua/05_audio/transcript.md jua/02_source/research.md
  python3 jua/tools/honesty_check.py coverage jua/delivery/explainer_script.md
  python3 jua/tools/honesty_check.py selftest      # offline check of the parsing/verdict logic

Needs TYPESAFE_API_KEY. Exit code 1 if anything needs Marty's attention.
Pattern: docs.typesafe.ai/cookbooks/citation_check (Choice supports/contradicts/says_nothing, auto-accept ≥ 0.8).
"""
import json, os, re, sys, urllib.request

API = "https://api.typesafe.ai/v1/systemone"
AUTO_ACCEPT = 0.8  # cookbook default; ponytail: tune on our own cases if it over/under-flags
BATCH = 20  # claims per request (independent questions over the same state run in parallel)

ITEMS = {
    "inspiration": "what inspired the project",
    "what_it_is": "what the project is",
    "how_built": "how the project was built",
    "challenges": "challenges the maker ran into",
    "proud_of": "accomplishments the maker is proud of",
    "learned": "what the maker learned",
    "next": "what's next for the project",
    "tools": "the tools used to build the project",
}


def sentences(text):
    """Factual sentences only: drop markdown syntax, SRT numbers/timecodes, placeholders."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):  # headings are labels, not claims
            continue
        line = " ".join(re.sub(r"^[#>*\-|\s\d.]+", "", line).replace("|", " ").replace("**", "").split())
        if not line or "-->" in line or "[" in line:  # [brackets] = not yet filled, skip
            continue
        out += [s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if len(s.split()) >= 5]
    return out


def verdict(answer):
    choice, conf = answer["choice"], answer.get("confidence", 0)
    if conf < AUTO_ACCEPT:
        return "REVIEW"
    return {"supports": "verified", "contradicts": "CONTRADICTED", "says_nothing": "UNSUPPORTED"}[choice]


def ask(state, questions):
    body = json.dumps({"model": "jev-latest", "state": state, "questions": questions}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": "Bearer " + os.environ["TYPESAFE_API_KEY"], "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=120))["answers"]


def check_claims(path, evidence_paths):
    claims = sentences(open(path).read())
    evidence = "\n\n".join(f"## {p}\n{open(p).read()}" for p in evidence_paths)
    bad = 0
    for i in range(0, len(claims), BATCH):
        chunk = claims[i:i + BATCH]
        qs = {f"c{j}": {
            "type": "choice",
            "instructions": f"How does `evidence` relate to the claim `claims[{j}]`?",
            "criteria": {
                "supports": "The evidence states the claim or directly implies that it is true",
                "contradicts": "The evidence states the opposite of the claim or implies it is false",
                "says_nothing": "The evidence does not address what the claim asserts, either way",
            }} for j in range(len(chunk))}
        answers = ask({"evidence": evidence, "claims": chunk}, qs)
        for j, claim in enumerate(chunk):
            a = answers[f"c{j}"]
            v = verdict(a)
            bad += v != "verified"
            print(f"{v:<13} {a.get('confidence', 0):.2f}  {claim}")
    print(f"\n{len(claims) - bad}/{len(claims)} verified" + ("" if not bad else " — review the rest with Marty (never ship an UNSUPPORTED/CONTRADICTED fact)"))
    return bad


def check_coverage(path):
    qs = {k: {"type": "noul",
              "instructions": f"Does `script` explicitly talk about {desc}?",
              "criteria": {"true": f"The script says something concrete about {desc}",
                           "false": f"The script does not address {desc}"}} for k, desc in ITEMS.items()}
    answers = ask({"script": open(path).read()}, qs)
    missing = [k for k in ITEMS if answers[k]["noul"] < 0.5]
    for k in ITEMS:
        print(f"{'ok' if k not in missing else 'MISSING':<8} {answers[k]['noul']:.2f}  {ITEMS[k]}")
    return len(missing)


def selftest():
    s = sentences("# Title that is long enough here\n| 1 | Hook | \"AI can bring back a face from a photo.\" |\n12\n00:00:01,000 --> 00:00:03,000\n"
                  "[Real struggle, e.g. blink]\nShe sold fabric at the market in Kinshasa. Short one.")
    assert s == ['Hook "AI can bring back a face from a photo."', "She sold fabric at the market in Kinshasa."], s
    assert verdict({"choice": "supports", "confidence": 0.9}) == "verified"
    assert verdict({"choice": "says_nothing", "confidence": 0.95}) == "UNSUPPORTED"
    assert verdict({"choice": "supports", "confidence": 0.5}) == "REVIEW"
    print("selftest ok")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "selftest":
        sys.exit(selftest())
    if mode == "claims" and "--evidence" in sys.argv:
        k = sys.argv.index("--evidence")
        sys.exit(1 if check_claims(sys.argv[2], sys.argv[k + 1:]) else 0)
    if mode == "coverage" and len(sys.argv) == 3:
        sys.exit(1 if check_coverage(sys.argv[2]) else 0)
    sys.exit(__doc__)

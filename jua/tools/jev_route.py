#!/usr/bin/env python3
"""Jev first, then the LLM. Run on every request from Marty before acting.

Jev (TypeSafe System One) returns fast typed judgments about the request; the agent (LLM)
then acts on them: open the right phase, respect the flagged rules, stop where approval is needed.

Usage:
  python3 jua/tools/jev_route.py "redo shot 03, the light is too strong"
  python3 jua/tools/jev_route.py selftest

Prints one JSON line: {"phase", "task", "flags": {...}, "low_confidence": [...]}. Needs TYPESAFE_API_KEY.
"""
import json, os, sys, urllib.request

API = "https://api.typesafe.ai/v1/systemone"
MIN_CONF = 0.6  # ponytail: below this, the LLM should ask Marty instead of trusting the route

PHASES = {
    "p0_kickoff": "start or restart a session, read the rules, report the plan",
    "p1_source_lockset": "the source photo, research, or the locked reference images (hands, room, table, sleeve)",
    "p2_animatic": "the rough cut / animatic of all shots",
    "p3_restoration": "restoring the photograph in stages",
    "p4_hero_shots": "generating or fixing a video shot (01, 03, 04, 05)",
    "p5_testimony": "the witness testimony, transcript, script or subtitles",
    "p6_music": "the music, Tabu Ley 'Pitié' excerpts, or the backup score",
    "p7_assembly": "editing / assembling the cut, end card, loudness",
    "p8_review": "reviewing or critiquing the cut against the brief",
    "p9_delivery": "the submission form, YouTube links, thumbnail, face cam explainer",
    "other": "setup, tools, repo, questions, or anything not about a production phase",
}
TASKS = {
    "generate": "create new media or files",
    "revise": "change or redo something that already exists",
    "approve": "approve, lock, or pick an option",
    "review": "check, critique, or verify",
    "question": "ask for information or an explanation",
    "admin": "git, setup, credentials, tooling, or file housekeeping",
}
FLAGS = {  # each: (instruction, true meaning, false meaning)
    "spends_credits": ("Will fulfilling `request` require running NEW AI generations of images, video, or music (spending Arcads credits)? Locking, approving, picking, or editing existing files is not a new generation.",
                       "It requires new AI generations", "It only uses, picks, locks, or edits existing files"),
    "risks_invented_fact": ("Does `request` ask to state or add a fact about the woman in the photo (name, place, date, life detail, clothing) that must come from real evidence?",
                            "It touches facts about her that need evidence", "It does not add facts about her"),
    "moves_portrait_face": ("Does `request` ask to animate, speak, or change the face of the person in the photograph?",
                            "It would move or change her face, or make her speak", "It leaves her face untouched"),
    "needs_marty_approval": ("Does `request` lock, approve, delete, publish, or otherwise make a hard-to-reverse choice?",
                             "It is a hard-to-reverse or approval step", "It is exploratory or easily reversible"),
}


def questions():
    q = {"phase": {"type": "choice", "instructions": "Which production phase of the short film is `request` about?", "criteria": PHASES},
         "task": {"type": "choice", "instructions": "What kind of task is `request`?", "criteria": TASKS}}
    for k, (ins, t, f) in FLAGS.items():
        q[k] = {"type": "noul", "instructions": ins, "criteria": {"true": t, "false": f}}
    return q


def compose(answers):
    out = {"phase": answers["phase"]["choice"], "task": answers["task"]["choice"],
           "flags": {k: round(answers[k]["noul"], 2) for k in FLAGS},
           "low_confidence": [k for k in ("phase", "task") if answers[k].get("confidence", 0) < MIN_CONF]}
    out["rules"] = [msg for k, msg in (
        ("spends_credits", "check credits first; 2 variants; checkpoint after"),
        ("risks_invented_fact", "facts only from transcript/research; run honesty_check.py before shipping"),
        ("moves_portrait_face", "FORBIDDEN on the portrait — refuse and propose a camera/light move instead"),
        ("needs_marty_approval", "stop and confirm with Marty before acting"),
    ) if out["flags"][k] >= 0.5]
    return out


def route(request):
    body = json.dumps({"model": "jev-latest", "state": {"project": "Jua — More Than a Photograph (short film)", "request": request},
                       "questions": questions()}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": "Bearer " + os.environ["TYPESAFE_API_KEY"], "Content-Type": "application/json"})
    return compose(json.load(urllib.request.urlopen(req, timeout=60))["answers"])


def selftest():
    fake = {"phase": {"choice": "p4_hero_shots", "confidence": 0.9}, "task": {"choice": "revise", "confidence": 0.4},
            "spends_credits": {"noul": 0.9}, "risks_invented_fact": {"noul": 0.1},
            "moves_portrait_face": {"noul": 0.8}, "needs_marty_approval": {"noul": 0.2}}
    r = compose(fake)
    assert r["phase"] == "p4_hero_shots" and r["low_confidence"] == ["task"], r
    assert len(r["rules"]) == 2 and "FORBIDDEN" in r["rules"][1], r
    assert set(questions()) == {"phase", "task", *FLAGS}
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        selftest()
    elif len(sys.argv) == 2:
        print(json.dumps(route(sys.argv[1]), ensure_ascii=False))
    else:
        sys.exit(__doc__)

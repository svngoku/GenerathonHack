import numpy as np
def dilate(m, r):
    """binary dilation by a (2r+1)^2 square, numpy only"""
    out = m.copy(); H, W = m.shape
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out[max(dy,0):H+min(dy,0), max(dx,0):W+min(dx,0)] |= m[max(-dy,0):H+min(-dy,0), max(-dx,0):W+min(-dx,0)]
    return out

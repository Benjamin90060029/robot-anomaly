import numpy as np
from fk import fk, L0, L1
def elbow(t1, t2):
    r = L1 * np.cos(t2)
    z = L0 + L1 * np.sin(t2)
    x = r * np.cos(t1)
    y = r * np.sin(t1)
    return np.array([x, y, z])
def arm_points(t1, t2, t3):
    base = np.array([0, 0, 0])
    shoulder = np.array([0, 0, L0])
    return np.array([base, shoulder, elbow(t1, t2), fk(t1, t2, t3)])


deg = [0, 30, 30]
t = np.radians(deg)
pts = arm_points(t[0], t[1], t[2])
print(np.round(pts, 3))

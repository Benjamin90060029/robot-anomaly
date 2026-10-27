import numpy as np

L0 = 0.10 
L1 = 0.25
L2 = 0.20

def fk(t1, t2, t3):
    r = L1 * np.cos(t2) + L2 * np.cos(t2 + t3)
    z = L0 + L1 * np.sin(t2) + L2 * np.sin(t2 + t3)
    x = r * np.cos(t1)
    y = r * np.sin(t1)
    return np.array([x, y, z])


tests = [
    [0, 0, 0],
    [0, 90, 0],
    [90, 0, 0],
    [0, 90, -90],
    [0, 30, 30],
]

for deg in tests:
    t = np.radians(deg)
    pos = fk(t[0], t[1], t[2])
    print(deg, "->", np.round(pos, 3))
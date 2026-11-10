import numpy as np
import pybullet as p
from fk import fk

p.connect(p.DIRECT)                                 #只計算，不顯示畫面
robot = p.loadURDF("arm.urdf", useFixedBase=True)   #3


def pybullet_ee(t1, t2, t3):
    p.resetJointState(robot, 0, t1)
    p.resetJointState(robot, 1, t2)
    p.resetJointState(robot, 2, t3)
    state = p.getLinkState(robot, 3, computeForwardKinematics=True)
    return np.array(state[4])


tests = [
    [0, 0, 0],
    [0, 90, 0],
    [90, 0, 0],
    [0, 90, -90],
    [0, 30, 30],
]
for deg in tests:
    t = np.radians(deg)                          # 換成弧度
    mine = fk(t[0], t[1], t[2])                  # 你的 fk 算的
    sim = pybullet_ee(t[0], t[1], t[2])          # PyBullet 算的
    err = np.linalg.norm(mine - sim)             # 兩點距離 = 誤差
    print(deg, "fk:", np.round(mine, 3), "PyBullet:", np.round(sim, 3), "誤差:", err)

rng = np.random.default_rng(0)
max_err = 0

for i in range(1000):
    t1 = rng.uniform(-np.pi, np.pi)
    t2 = rng.uniform(-np.pi / 2, np.pi / 2)
    t3 = rng.uniform(-2.6, 2.6)
    err = np.linalg.norm(fk(t1, t2, t3) - pybullet_ee(t1, t2, t3))
    if err > max_err:
        max_err = err

print("1000 組隨機角度，最大誤差 =", max_err)

if max_err < 1e-6:
    print("通過！你的 fk 和 PyBullet 完全一致")
else:
    print("誤差太大，檢查 fk.py 或 arm.urdf")

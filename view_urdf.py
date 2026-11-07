import pybullet as p
import numpy as np
import time

p.connect(p.GUI)
robot = p.loadURDF("arm.urdf", useFixedBase=True)
p.resetDebugVisualizerCamera(0.9, 45, -25, [0, 0, 0.2])

print("關節數量：", p.getNumJoints(robot))

s1 = p.addUserDebugParameter("theta1 (deg)", -180, 180, 0)
s2 = p.addUserDebugParameter("theta2 (deg)", -90, 90, 0)

while p.isConnected():
    t1 = np.radians(p.readUserDebugParameter(s1))
    t2 = np.radians(p.readUserDebugParameter(s2))
    p.resetJointState(robot, 0, t1)
    p.resetJointState(robot, 1, t2)
    p.stepSimulation()
    time.sleep(1 / 240)
import pybullet as p
import time

p.connect(p.GUI) #打開PyBullet
robot = p.loadURDF("arm.urdf", useFixedBase= True) #讀取設計圖 建出手臂 useFixedbase=true->代表把底座固定
p.resetDebugVisualizerCamera(0.9, 45, -25, [0,0, 0.2]) #設定相機：距離0.9m,水平轉45 往下看 25°，對準 (0, 0, 0.2)


while p.isConnected():
    time.sleep(0.1)

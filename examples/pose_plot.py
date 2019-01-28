import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose

GraphicsRenderer('VTK')  # Sets graphics.gRenderer type to VtkPipeline

def main():
    
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot()

    pose.SE3.Rx(theta=[45, 90], x=[1, 1], y=[1, 0], z=[0, 0], unit='deg').plot()

    pose.SO2(45, unit='deg').plot()

    pose.SO3.Rx(theta=[45, 80], unit='deg').plot()

    pose.SE2(theta=[45], unit='deg').plot()

    pose.SE2(theta=[45, 80], x=[0, 2], y=[0, 1], unit='deg').plot()

    print("Wait until animation is done before interaction with rendering.")
    other = pose.SO3.Rx(theta=90, unit='deg')
    pose.SO3.Rx(theta=45, unit='deg').animate(other=other, duration=5, 
                                                           gif="pose_SO3", 
                                                           frame_rate=30)

if __name__ == '__main__':
    
    main()

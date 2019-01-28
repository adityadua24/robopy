import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose

GraphicsRenderer('VTK')  # Sets graphics.gRenderer type to VtkPipeline

def main():

    #  In this case timer_rate refers to the number of image renders
    #  produced per timer_tick.
    # 
    other = pose.SO3.Rx(theta=90, unit='deg')
    
    # Without image save
    pose.SO3.Rx(theta=45, unit='deg').animate(other=other, duration=5, 
                                                           timer_rate=10,
                                                           gif=None, 
                                                           frame_rate=10)
    # With image save
    print("Wait until animation is done before interaction with rendering.")
    pose.SO3.Rx(theta=45, unit='deg').animate(other=other, duration=5, 
                                                           timer_rate=10,
                                                           gif="poseSO3", 
                                                           frame_rate=10)

if __name__ == '__main__':
    
    main()

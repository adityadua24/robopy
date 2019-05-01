import robopy.base.model as model
import numpy as np

def main():
    robot = model.Puma560()
    
    '''zero angle'''
    qn = np.matrix([0,0,0,0,0,0])
    robot.plot(qn)
    
    '''ready, the arm is straight and vertical''
    qn = np.matrix([0,np.pi/2,-np.pi/2,0,0,0])
    robot.plot(qn)
    
    '''stretch, the arm is straight and horizontal'''
    qn = np.matrix([0,0,-np.pi/2,0,0,0])
    robot.plot(qn)
    
    '''nominal, the arm is in a dextrous working pose'''
    qn = np.matrix([0,(np.pi/4),-np.pi,0,(np.pi/4),0])
    robot.plot(qn)


if __name__ == '__main__':
    main()

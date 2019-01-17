from robopy.base.graphics import GraphicsRenderer
import robopy.base.model as model
import numpy as np


def main():
    robot = model.Puma560()

    a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
    b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
    c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
    d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
    e = np.asmatrix(np.zeros((500, 1)))
    f = np.concatenate((d, b, a, e, c, d), axis=1)

    robot.animate(stances=f, unit='deg', timer_rate=60, gif="Puma560", 
                             frame_rate=30, dispMode='VTK')


if __name__ == '__main__':
    main()



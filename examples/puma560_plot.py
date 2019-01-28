import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.model as model


def main():

    ### Select a Graphics Rendering package to use.
    gobj = GraphicsRenderer('VTK')  # this sets graphics.gRenderer

    # Puma560 manipulator arm pose plot
    robot = model.Puma560()
    robot.plot(robot.qn, dispMode='VTK', z_up=False, limits=None)


if __name__ == '__main__':
main()
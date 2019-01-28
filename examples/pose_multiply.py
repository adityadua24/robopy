import _robopy
import robopy.base.pose as pose


def main():
    x = pose.SE3.rand()
    y = pose.SE3.rand()

    z = x * y

    print(z)


if __name__ == '__main__':
    main()

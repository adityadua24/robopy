import robopy.base.model as model


def main():
    robot = model.Puma560()
    robot.plot('qn')


if __name__ == '__main__':
    main()
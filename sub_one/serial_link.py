class SerialLink():

    def __init__(self):
        self.links = []



class link():

    def __init__(self, j, theta, d, a, alpha, offset, type=''):
        self.theta = theta
        self.d = d
        self.j = j
        self.a = a
        self.alpha = alpha
        self.offset = offset
        self.type = type


class revolute(link):
    pass

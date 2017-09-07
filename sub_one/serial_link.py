class SerialLink:
    def __init__(self):
        self.links = []
        self

    def fkine(self, q=None):
        # q is vector of real numbers (List of angles)
        pass

    def plot(self, q=None):
        # PLot the serialLink object
        pass


class Link:
    # Abstract methods
    def __init__(self, j, theta, d, a, alpha, offset, type=''):
        self.theta = theta
        self.d = d
        self.j = j
        self.a = a
        self.alpha = alpha
        self.offset = offset
        # self.type = type

class Revolute(Link):
    def A(cls, q):
        # If insiatn
        pass
    pass

class Prismatic(Link):
    def A(cls, q):
        # If insiatn
        pass
    pass

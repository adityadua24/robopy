import numpy as np
from termcolor import colored

class RTBMatrix(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __mul__(self, other):
        return self.dot(other)

    def __str__(self):
        return self.__repr__()

    def to_ndarray(self):
        return np.asarray(self)

    def round(self, decimals=0):
        return np.round_(self, decimals)
    """
    def __repr__(self):
        output_str = ''
        for i in range(len(self)):
            output_str += colored('{0:10.4f}{1:10.4f}{2:10.4f}'.format(*self[i, :3]), 'red')
            output_str += colored('{0:10.4f}\n'.format(self[i, 3]), 'blue')
        output_str += colored('{0:10.4f}{1:10.4f}{2:10.4f}{3:10.4f}'.format(*self[3, :4]), 'white')
        return output_str
    """
import numpy as np
import math
from abc import ABC, abstractmethod


class Pose(ABC):
    @property
    @abstractmethod
    def data(self):
        raise NotImplementedError()

    def commonMethod(self):
        self._data = np.eye(2, 2)

    @abstractmethod
    def do_something_sub_class_specific(self):
        raise NotImplementedError()

    def __repr__(self):
        array = np.asarray(self._data)
        str = np.array2string(array)
        return str

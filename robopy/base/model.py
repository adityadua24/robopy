# Created by: Aditya Dua
# 5 October 2017
from .serial_link import SerialLink
from .serial_link import Revolute
from math import pi
import numpy as np
from . import transforms as tr
from . import graphics


class Puma560(SerialLink):
    def __init__(self):
        self.q = {'qr': np.matrix([[0, pi / 2, -pi / 2, 0, 0, 0]]),
                  'qz': np.matrix([[0, 0, 0, 0, 0, 0]]),
                  'qs': np.matrix([[0, 0, -pi / 2, 0, 0, 0]]),
                  'qn': np.matrix([[0, pi / 4, pi, 0, pi / 4, 0]])}

        links = [Revolute(d=0, a=0, alpha=pi / 2, j=0, theta=0, offset=0),
                 Revolute(d=0, a=0.4318, alpha=0, j=0, theta=0, offset=0),
                 Revolute(d=0.15005, a=0.0203, alpha=-pi / 2, j=0, theta=0, offset=0),
                 Revolute(d=0.4318, a=0, alpha=pi / 2, j=0, theta=0, offset=0),
                 Revolute(d=0, a=0, alpha=-pi / 2, j=0, theta=0, offset=0),
                 Revolute(d=0, a=0, alpha=0, j=0, theta=0, offset=0)]

        base_matrix = tr.trotx(-90, unit='deg')
        file_names = ["link0.stl", "link1.stl", "link2.stl", "link3.stl", "link4.stl", "link5.stl", "link6.stl"]
        colors = graphics.vtk_colors(["Red", "DarkGreen", "Blue", "Cyan", "Magenta", "Yellow", "White"])

        super().__init__(links=links, base=base_matrix, name='puma_560', stl_files=file_names, colors=colors)

    def plot(self, stance, unit='rad'):
        if type(stance) is str:
            stance = self.q[stance]
        elif type(stance) is np.matrix:
            if unit == 'deg':
                stance = self.q[stance] * (pi / 180)
        else:
            raise AttributeError("Type of stance must be numpy matrix of dim (1, n).\n Or you could pass one of the "
                                 "default stances")
        super().plot(stance=stance, unit=unit)

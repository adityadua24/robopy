# Created by: Aditya Dua
# 5 October 2017
from .serial_link import SerialLink
from .serial_link import Revolute
from math import pi
import numpy as np


class Puma560(SerialLink):
    def __init__(self):
        links = []
        link0 = Revolute(d=0, a=0, alpha=pi/2, j=0, theta=0, offset=0)
        links.append(link0)
        link1 = Revolute(d=0, a=0.4318, alpha=0, j=0, theta=0, offset=0)
        links.append(link1)
        link2 = Revolute(d=0.15005, a=0.0203, alpha=-pi/2, j=0, theta=0, offset=0)
        links.append(link2)
        link3 = Revolute(d=0.4318, a=0, alpha=pi/2, j=0, theta=0, offset=0)
        links.append(link3)
        link4 = Revolute(d=0, a=0, alpha=-pi/2, j=0, theta=0, offset=0)
        links.append(link4)
        link5 = Revolute(d=0, a=0, alpha=0, j=0, theta=0, offset=0)
        links.append(link5)
        super().__init__(links=links, name='puma560')

    def plot(self, stance='qr', unit='rad'):
        self.file_names = ["link0.stl", "link1.stl", "link2.stl", "link3.stl", "link4.stl", "link5.stl", "link6.stl"]

        qz = np.matrix([[0, 0, 0, 0, 0, 0]])
        qr = np.matrix([[0, pi/2, -pi/2, 0, 0, 0]])
        qs = np.matrix([[0, 0, -pi/2, 0, 0, 0]])
        qn = np.matrix([[0, pi/4, pi, 0, pi/4, 0]])

        stance_angles = 0

        if stance == 'qz':
            stance_angles = qz
        elif stance == 'qr':
            stance_angles = qr
        elif stance == 'qs':
            stance_angles = qs
        elif stance == 'qn':
            stance_angles = qn
        else:
            stance_angles = qr

        if unit == 'deg':
            stance_angles = stance_angles * (pi/180)
        super().plot(stance=stance_angles, unit=unit)

    def animate(self, stances, unit='rad', frame_rate=None):
        if frame_rate is None:
            frame_rate = 25
        if unit == 'deg':
            stances = stances * (pi/180)

        # TODO Intelligent way -> os.path.join()
        self.file_names = ["link0.stl", "link1.stl", "link2.stl", "link3.stl", "link4.stl", "link5.stl", "link6.stl"]

        qz = np.matrix([[0, 0, 0, 0, 0, 0]])
        qr = np.matrix([[0, pi/2, -pi/2, 0, 0, 0]])
        qs = np.matrix([[0, 0, -pi/2, 0, 0, 0]])
        qn = np.matrix([[0, pi/4, pi, 0, pi/4, 0]])

        stance_angles = 0
        super().animate(stances, unit=unit, frame_rate=frame_rate)



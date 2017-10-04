# puma560 model
# page 202, 203
from .serial_link import SerialLink
from .serial_link import Revolute
from math import pi
from . import graphics
from . import transforms
import os
import platform


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

    def plot(self, stance='qr'):
        filenames = ["link0.stl", "link1.stl", "link2.stl", "link3.stl", "link4.stl", "link5.stl", "link6.stl"]
        files_loc = 0
        if platform.system() == 'Windows':
            files_loc = '\\sub_one\\media\\puma_560\\'
        else:
            files_loc = '/sub_one/media/puma_560/'

        qz = [0, 0, 0, 0, 0, 0]
        qr = [0, pi/2, -pi/2, 0, 0, 0]
        qs = [0, 0, -pi/2, 0, 0, 0]
        qn = [0, pi/4, pi, 0, pi/4, 0]

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

        super().plot(filenames=filenames, files_loc=files_loc, stance_angles=stance_angles)










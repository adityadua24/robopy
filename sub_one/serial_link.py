from abc import ABC, abstractmethod
from . import pose
import math
import numpy as np
import vtk
from . import transforms
from . import graphics
from math import pi
import os


class SerialLink:
    def __init__(self, links, name=None, base=None):
        # Argument checks
        self.links = links
        self.q = []  # List of al angles
        self.base = np.asmatrix(np.eye(4, 4))
        self.tool = np.asmatrix(np.eye(4, 4))

    @property
    def length(self):
        return len(self.links)

    def fkine(self, q):
        # q is vector of real numbers (List of angles)
        t = self.base
        for i in range(self.length):
            t = t * self.links[i].A(q[i])
        t = t * self.tool
        return t

    def plot(self, filenames, files_loc, stance_angles):
        # PLot the serialLink object
        reader_list = []
        actor_list = []
        mapper_list = []
        for file in filenames:
            reader_list.append(0)
            actor_list.append(0)
            mapper_list.append(0)

        nc = vtk.vtkNamedColors()
        colors = ["Red", "DarkGreen", "Blue", "Cyan", "Magenta", "Yellow", "White"]
        colors_r_g_b = [0] * len(colors)
        for i in range(len(colors)):
            colors_r_g_b[i] = list(nc.GetColor3d(colors[i]))

        robopy_dir = os.getcwd()
        robopy_dir += files_loc

        for i in range(len(filenames)):
            reader_list[i] = vtk.vtkSTLReader()
            reader_list[i].SetFileName(robopy_dir + filenames[i])
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(reader_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(colors_r_g_b[i]) # (R,G,B)

        ren, ren_win, iren = graphics.setupStack()

        t = self.base

        for i in range(self.length):
            actor_list[i].SetUserMatrix(transforms.np2vtk(t))
            t = t * self.links[i].A(stance_angles[i])
        t = t * self.tool
        actor_list[6].SetUserMatrix(transforms.np2vtk(t))

        for each in actor_list:
            ren.AddActor(each)

        graphics.render(ren, ren_win, iren)


class Link(ABC):
    # Abstract methods
    def __init__(self, j, theta, d, a, alpha, offset=None, kind='', mdh=0, flip=None):
        self.theta = theta
        self.d = d
        # self.j = j
        self.a = a
        self.alpha = alpha
        self.offset = offset
        self.kind = kind
        self.mdh = mdh
        self.flip = flip

    def A(self, q):
        sa = math.sin(self.alpha)
        ca = math.cos(self.alpha)
        if self.flip:
            q = -q + self.offset
        else:
            q = q + self.offset
        st = 0
        ct = 0
        d = 0
        if self.kind == 'r':
            st = math.sin(q)
            ct = math.cos(q)
            d = self.d
        elif self.type == 'p':
            st = math.sin(self.theta)
            ct = math.cos(self.theta)
            d = q

        se3_np = 0
        if self.mdh == 0:
            se3_np = np.matrix([[ct, -st * ca, st * sa, self.a * ct],
                                [st, ct * ca, -ct * sa, self.a * st],
                                [0, sa, ca, d],
                                [0, 0, 0, 1]])

        return se3_np


class Revolute(Link):
    def __init__(self, j, theta, d, a, alpha, offset):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='r')
        pass


class Prismatic(Link):
    def __init__(self, j, theta, d, a, alpha, offset):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='p')
        pass

    pass

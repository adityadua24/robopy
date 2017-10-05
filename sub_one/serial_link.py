from __future__ import print_function
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
        # Arguments initialised by plot function and animate functions only
        self.file_names = 0
        self.files_loc = 0

    @property
    def length(self):
        return len(self.links)

    def fkine(self, stance, unit='rad', apply_stance=False, actor_list=None, timer=None):
        # q is vector or matrix of real numbers (List of angles)
        # apply_stance, actor_list are only used for plotting
        # timer is used for animation
        if timer is None:
            timer = 0
        t = self.base
        for i in range(self.length):
            if apply_stance:
                actor_list[i].SetUserMatrix(transforms.np2vtk(t))
            t = t * self.links[i].A(stance[timer, i])
        t = t * self.tool
        if apply_stance:
            actor_list[self.length].SetUserMatrix(transforms.np2vtk(t))
        return t

    def plot(self, stance, unit='rad'):
        # PLot the serialLink object
        reader_list = []
        actor_list = []
        mapper_list = []
        for file in self.file_names:
            reader_list.append(0)
            actor_list.append(0)
            mapper_list.append(0)

        nc = vtk.vtkNamedColors()
        colors = ["Red", "DarkGreen", "Blue", "Cyan", "Magenta", "Yellow", "White"]
        colors_r_g_b = [0] * len(colors)
        for i in range(len(colors)):
            colors_r_g_b[i] = list(nc.GetColor3d(colors[i]))

        robopy_dir = os.getcwd()
        robopy_dir += self.files_loc

        for i in range(len(self.file_names)):
            reader_list[i] = vtk.vtkSTLReader()
            reader_list[i].SetFileName(robopy_dir + self.file_names[i])
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(reader_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(colors_r_g_b[i])  # (R,G,B)

        ren, ren_win, iren = graphics.setupStack()

        self.fkine(stance, unit=unit, apply_stance=True, actor_list=actor_list)

        for each in actor_list:
            ren.AddActor(each)

        graphics.render(ren, ren_win, iren)

    def animate(self, stances, unit, frame_rate):
        class vtkTimerCallback():
            def __init__(self, robot, stances, unit, actors):
                self.timer_count = 0
                self.robot = robot
                self.stances = stances
                self.actor_list = actors
                self.unit = unit

            def execute(self, obj, event):
                print(self.timer_count)
                self.timer_count += 1
                if self.timer_count == self.stances.shape[0]:
                    obj.DestroyTimer()
                    return

                self.robot.fkine(self.stances, unit=self.unit, apply_stance=True, actor_list=actor_list, timer=self.timer_count)
                iren = obj
                iren.GetRenderWindow().Render()

        reader_list = []
        actor_list = []
        mapper_list = []
        for file in self.file_names:
            reader_list.append(0)
            actor_list.append(0)
            mapper_list.append(0)

        nc = vtk.vtkNamedColors()
        colors = ["Red", "DarkGreen", "Blue", "Cyan", "Magenta", "Yellow", "White"]
        colors_r_g_b = [0] * len(colors)
        for i in range(len(colors)):
            colors_r_g_b[i] = list(nc.GetColor3d(colors[i]))

        robopy_dir = os.getcwd()
        robopy_dir += self.files_loc

        for i in range(len(self.file_names)):
            reader_list[i] = vtk.vtkSTLReader()
            reader_list[i].SetFileName(robopy_dir + self.file_names[i])
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(reader_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(colors_r_g_b[i])  # (R,G,B)

        ren, ren_win, iren = graphics.setupStack()

        self.fkine(stances, apply_stance=True, actor_list=actor_list)

        for each in actor_list:
            ren.AddActor(each)

        ren.ResetCamera()
        ren_win.Render()
        iren.Initialize()
        cb = vtkTimerCallback(robot=self, stances=stances, unit=unit, actors=actor_list)
        iren.AddObserver('TimerEvent', cb.execute)
        timerId = iren.CreateRepeatingTimer((int)(1000/frame_rate))
        iren.Start()


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

# Created by: Aditya Dua
# 30 September 2017
from __future__ import print_function
from abc import ABC
import math
import numpy as np
import vtk
from . import transforms
from .graphics import VtkPipeline
from .graphics import axesCube
from .graphics import vtk_colors
from .graphics import cylinder
import pkg_resources
from scipy.optimize import minimize
from math import sqrt


class SerialLink:
    def __init__(self, links, name=None, base=None, stl_files=None, q=None, colors=None, stick_fig=False):
        # Argument checks
        self.links = links
        if q is None:
            q = [0 for each in links]
        if base is None:
            self.base = np.asmatrix(np.eye(4, 4))
        else:
            assert type(base) is np.matrix
            assert base.shape == (4, 4)
            self.base = base
        self.tool = np.asmatrix(np.eye(4, 4))
        # Arguments initialised by plot function and animate functions only
        if stl_files is None:
            self.stick_fig = True
        else:
            self.stick_fig = False
            self.stl_files = stl_files
        if name is None:
            self.name = ''
        else:
            self.name = name
        if colors is None:
            self.colors = vtk_colors(["Grey"] * len(links))
        else:
            self.colors = colors

    def __iter__(self):
        return (each for each in self.links)

    @property
    def length(self):
        return len(self.links)

    def fkine(self, stance, unit='rad', apply_stance=False, actor_list=None, timer=None, trace=False):
        # q is vector or matrix of real numbers (List of angles)
        # apply_stance, actor_list are only used for plotting
        # timer is used for animation
        trace = []
        if type(stance) is np.ndarray:
            stance = np.asmatrix(stance)
        if unit == 'deg':
            stance = stance * math.pi / 180
        if timer is None:
            timer = 0
        t = self.base
        trace.append(t)
        for i in range(self.length):
            if apply_stance:
                actor_list[i].SetUserMatrix(transforms.np2vtk(t))
            t = t * self.links[i].A(stance[timer, i])
            trace.append(t)

        t = t * self.tool
        trace.append(t)
        if apply_stance:
            actor_list[self.length].SetUserMatrix(transforms.np2vtk(t))
        if trace:
            return t, trace
        else:
            return t

    def ikine(self, end_effector, q0=None, unit='rad'):
        assert type(end_effector) is np.matrix and end_effector.shape == (4, 4)
        bounds = [(link.qlim[0], link.qlim[1]) for link in self]
        print(bounds)
        print('\nlength of bounds is: ', len(bounds))
        # print(upper_bound, lower_bound)
        print('\n\n')
        reach = 0
        for link in self:
            reach += abs(link.a) + abs(link.d)
        omega = np.diag([1, 1, 1, 3 / reach])
        if q0 is None:
            q0 = np.asmatrix(np.zeros((1, self.length)))

        def objective(x):
            return (
                np.square((np.linalg.lstsq(end_effector, self.fkine(x))[0]) - np.asmatrix(np.eye(4, 4)) * omega)).sum()

        sol = minimize(objective, x0=q0, bounds=bounds)
        return np.asmatrix(sol.x)

    def plot(self, stance, unit='rad'):
        # PLot the serialLink object
        if unit == 'deg':
            stance = stance * math.pi / 180
        if self.stick_fig:
            actor_list, actor_axes_list = self.__setup_pipeline_objs_stick_fig()
        else:
            actor_list = self.__setup_pipeline_objs_stl()
        pipeline = VtkPipeline()

        actor_list, actor_axes_list = self.__setup_pipeline_objs_stick_fig()
        # actor_list = self.__setup_pipeline_objs_stl()

        self.fkine(stance, apply_stance=True, actor_list=actor_list)
        t, trace = self.fkine(stance, apply_stance=True, actor_list=actor_axes_list, trace=True)

        for each in trace:
            print(each.round(15))

        for each in actor_list:
            pipeline.add_actor(each)

        actor_axes_list[1].SetAxisLabels(1)

        # for each in actor_axes_list[3:5]:
        #     pipeline.add_actor(each)

        vtk_links = []
        if self.stick_fig:
            vtk_links = self.__compute_links(trace)

        # for i in range(len(vtk_links)):
        #     vtk_links[i].SetUserMatrix(actor_list[i].GetUserMatrix())

        for each in vtk_links:
            pipeline.add_actor(each)

        cube_axes = axesCube(pipeline.ren)
        pipeline.add_actor(cube_axes)
        pipeline.render()

    def __setup_pipeline_objs_stl(self):
        reader_list = [0] * len(self.stl_files)
        actor_list = [0] * len(self.stl_files)
        mapper_list = [0] * len(self.stl_files)
        for i in range(len(self.stl_files)):
            reader_list[i] = vtk.vtkSTLReader()
            loc = pkg_resources.resource_filename(__name__, '/'.join(('media', self.name, self.stl_files[i])))
            reader_list[i].SetFileName(loc)
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(reader_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(self.colors[i])  # (R,G,B)

        return actor_list

    def __setup_pipeline_objs_stick_fig(self):
        actor_list = [0] * len(self.links)
        source_list = [0] * len(self.links)
        mapper_list = [0] * len(self.links)
        for i in range(len(self.links)):
            source_list[i] = cylinder(0.125, 0.05)
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(source_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])

        source = cylinder(0.125, 0.05)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor_list.append(actor)
        actor_list2 = []
        for i in range(len(actor_list)):
            actor_list2.append(vtk.vtkAxesActor())
        for each in actor_list2:
            each.SetAxisLabels(0)
            each.SetConeRadius(0.2)

        return actor_list, actor_list2

    def __compute_links(self, trace):
        actor_list = [0] * (len(trace) - 1)
        source_list = [0] * (len(trace) - 1)
        mapper_list = [0] * (len(trace) - 1)
        alpha = []
        # a = []
        # d = []
        for each in self.links:
            alpha.append(each.alpha)
        #     a.append(each.a)
        #     d.append(each.d)
        #
        # a.append(0)
        # d.append(0)
        alpha.append(0)
        alpha.insert(0, 0)
        # a.insert(0, 0)
        # d.insert(0, 0)
        #
        # transformations = []
        # for i in range(len(a)):
        #     if (a[i] == 0) and (d[i]) == 0:
        #         transformations.append(np.asmatrix(np.eye(4, 4)))
        #     elif a[i] > 0:
        #         transformations.append(transforms.trotx(90, unit='deg'))
        #     elif d[i] > 0:
        #         transformations.append(transforms.trotz(90, unit='deg'))
        #     else:
        #         transformations.append(np.asmatrix(np.eye(4, 4)))
        print(alpha)
        for i in range(len(trace) - 1):
            link_length = sqrt(np.asmatrix(np.square(trace[i + 1] - trace[i]))[0:3, 3].sum())
            pos = (trace[i + 1][0:3, 3] + trace[i][0:3, 3]) / 2
            movement = (trace[i + 1][0:3, 3] - trace[i][0:3, 3])
            link_t = trace[i]
            if movement[0, 0] > movement[2, 0]:
                link_t = transforms.trotz(math.pi/2 + alpha[i+1], xyz=[pos[0, 0], pos[1, 0], pos[2, 0]])
            elif movement[0, 0] < movement[2, 0]:
                link_t = transforms.trotx(math.pi/2, xyz=[pos[0, 0], pos[1, 0], pos[2, 0]])
                pass

            # print(alpha)
            # link_t = transforms.trotz(alpha[i+1], unit='deg', xyz=[pos[0, 0], pos[1, 0], pos[2, 0]])
            # link_t = transformations[i]
            link_t[0:3, 3] = pos
            source_list[i] = cylinder(link_length, 0.025)
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(source_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(0, 0, 1)
            actor_list[i].SetUserMatrix(transforms.np2vtk(link_t))
            # actor_list[i].SetPosition(pos)

        return actor_list

    def animate(self, stances, unit='rad', frame_rate=25):
        class vtkTimerCallback():
            def __init__(self, robot, stances, actors):
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

                self.robot.fkine(self.stances, apply_stance=True, actor_list=actor_list, timer=self.timer_count)
                pipeline.iren = obj
                pipeline.iren.GetRenderWindow().Render()

        if unit == 'deg':
            stances = stances * (math.pi / 180)

        reader_list, actor_list, mapper_list = self.__setup_pipeline_objs_stl()
        pipeline = VtkPipeline()

        self.fkine(stances, apply_stance=True, actor_list=actor_list)

        for each in actor_list:
            pipeline.add_actor(each)

        cube_axes = axesCube(pipeline.ren)
        pipeline.add_actor(cube_axes)

        pipeline.ren.ResetCamera()
        pipeline.ren_win.Render()
        pipeline.iren.Initialize()

        cb = vtkTimerCallback(robot=self, stances=stances, actors=pipeline.actor_list)
        pipeline.iren.AddObserver('TimerEvent', cb.execute)
        timerId = pipeline.iren.CreateRepeatingTimer((int)(1000 / frame_rate))
        pipeline.iren.Start()


class Link(ABC):
    # Abstract methods
    def __init__(self, j, theta, d, a, alpha, offset=None, kind='', mdh=0, flip=None, qlim=None):
        self.theta = theta
        self.d = d
        # self.j = j
        self.a = a
        self.alpha = alpha
        self.offset = offset
        self.kind = kind
        self.mdh = mdh
        self.flip = flip
        self.qlim = qlim

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
        elif self.kind == 'p':
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
    def __init__(self, j, theta, d, a, alpha, offset, qlim):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='r', qlim=qlim)
        pass


class Prismatic(Link):
    def __init__(self, j, theta, d, a, alpha, offset, qlim):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='p', qlim=qlim)
        pass

    pass

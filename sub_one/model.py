# puma560 model
# page 202, 203
from .serial_link import SerialLink
from .serial_link import Revolute
from math import pi
from . import graphics
import vtk
from . import transforms


def puma560():

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

    robot = SerialLink(links=links, name='puma 560')

    filenames = ["link0.stl", "link1.stl", "link2.stl", "link3.stl", "link4.stl", "link5.stl", "link6.stl"]
    readerList = []
    actorList = []
    mapperList = []
    for file in filenames:
        readerList.append(0)
        actorList.append(0)
        mapperList.append(0)

    nc = vtk.vtkNamedColors()
    colors = ["Red", "DarkGreen", "Blue", "Cyan", "Magenta", "Yellow", "White"]
    colorsRGB = [0] * len(colors)
    for i in range(len(colors)):
        colorsRGB[i] = list(nc.GetColor3d(colors[i]))

    path_prefix = 'C:\\Users\\Aditya Dua\\Documents\\IdeaProjects\\robopy\\sub_one\\media\\puma_560\\'

    for i in range(len(filenames)):
        readerList[i] = vtk.vtkSTLReader()
        readerList[i].SetFileName(path_prefix + filenames[i])
        mapperList[i] = vtk.vtkPolyDataMapper()
        mapperList[i].SetInputConnection(readerList[i].GetOutputPort())
        actorList[i] = vtk.vtkActor()
        actorList[i].SetMapper(mapperList[i])
        actorList[i].GetProperty().SetColor(colorsRGB[i]) # (R,G,B)

    ren, ren_win, iren = graphics.setupStack()
    qz = [0, 0, 0, 0, 0, 0]
    qr = [0, pi/2, -pi/2, 0, 0, 0]
    qs = [0, 0, -pi/2, 0, 0, 0]
    qn = [0, pi/4, pi, 0, pi/4, 0]

    # actorList[6].SetUserMatrix(transforms.np2vtk(robot.fkine(qz)))
    t = robot.base

    for i in range(robot.length):
        t = t * robot.links[i].A(qz[i])
        actorList[i].SetUserMatrix(transforms.np2vtk(t))
    t = t * robot.tool
    actorList[6].SetUserMatrix(transforms.np2vtk(t))

    for each in actorList:
        ren.AddActor(each)


    graphics.render(ren, ren_win, iren)
    # return SerialLink object



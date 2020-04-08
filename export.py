from naca import naca
from dxfwrite import DXFEngine as dxf
import numpy as np

file_input = open('config.cfg', mode='r')
type_line = file_input.readlines()
read_type = type_line[0]
read_node = type_line[0]
fileNaca = read_type.replace('\n', '')
fileNode = read_node.replace('\n', '')

nPoints = fileNode
profNaca = [fileNaca]
naca_type = len(profNaca)

def airfoil(profNaca = profNaca, nPoints = nPoints, finite_TE = False, half_cosine_spacing = False):
    for i,p in enumerate(profNaca):
        X,Y = naca(p, nPoints, finite_TE, half_cosine_spacing)
    return X, Y

def txt():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('airfoil_coord.txt', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def flt():

    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('airfoil_project.flt', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def csv():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('airfoil_coord.csv', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s; %s\n" % item)

def dat():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('airfoil_coord.dat', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def xls():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('airfoil_coord.xls', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def dxfe():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    name = 'airfoil_draft.dxf'
    dwg = dxf.drawing(name)
    spline_points = textxy
    dwg.add(dxf.spline(spline_points, color=7))
    for point in spline_points:
        dwg.add(dxf.circle(radius=0, center=point, color=1))
    dwg.save()
from airfoilplot import airfoil_plot
from airfoilplot import naca
from dxfwrite import DXFEngine as dxf
import numpy as np

def airfoil(profNaca = ['6409'], nPoints = 240, finite_TE = False, half_cosine_spacing = False):
    for i,p in enumerate(profNaca):
        X,Y = naca(p, nPoints, finite_TE, half_cosine_spacing)
    return X, Y

def txt():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('export/airfoil_coord.txt', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def csv():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('export/airfoil_coord.csv', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s; %s\n" % item)

def dat():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('export/airfoil_coord.dat', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def excel():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    with open('export/airfoil_coord.xls', 'w') as txt_file:
        for item in textxy:
            txt_file.write("%s %s\n" % item)

def dxfe():
    X, Y = airfoil()
    txty = list(Y)
    txtx = list(X)
    zipxy = zip(X,Y)
    textxy = list(zipxy)

    name = 'export/airfoil_draft.dxf'
    dwg = dxf.drawing(name)
    spline_points = textxy
    dwg.add(dxf.spline(spline_points, color=7))
    for point in spline_points:
        dwg.add(dxf.circle(radius=0, center=point, color=1))
    dwg.save()

if __name__=="__main__":
    dxfe()
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

def airfoil_funct(profNaca = profNaca, nPoints = nPoints, finite_TE = False, half_cosine_spacing = False):
    for i,p in enumerate(profNaca):
        X,Y = naca(p, nPoints, finite_TE, half_cosine_spacing)
    return X, Y
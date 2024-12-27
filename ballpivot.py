# -*- coding: utf-8 -*-
"""
Reconstructs a base 3D model using the ball-pivoting algorithm
"""

import subprocess
import sys
import os
import open3d as o3d
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pointcloud as pcd

DIRECTORY = ""
IMAGE_NAME = ""

def get_path_name() -> str:
    '''
    generates a path and file name to save output file
    :return: output file path name
    '''
    path_name = f"{DIRECTORY}/ballpivot_{IMAGE_NAME}.ply"

    return path_name

def pointcloud():
    '''
    Prompts user to upload existing point cloud or generate a new one
    :return: point cloud
    '''
    print("This program supports pointclouds saved as .ply and .pcd files")
    existing_pcd = ("Do you have an existing, compatible pointcloud? {y/n): ").lower()

    if existing_pcd == "y":
        valid = False
        validTypes = ["ply", "pcd"]
        path = input("Enter Path of Point Cloud File: ")
        while not valid:
            if os.path.basename(path).split(".")[-1] in validTypes:
                valid = True
            else:
                path = input("File Not Compatible. Enter Path of Point Cloud File: ")
        pointcloud = o3d.io.read_point_cloud(path)

        DIRECTORY = os.path.dirname(path)
        imageBasename = os.path.basename(path)
        IMAGE_NAME = imageBasename.split(".")[0]

    else:

        pointcloud = pcd.get_pointcloud()
        DIRECTORY = pcd.DIRECTORY
        IMAGE_NAME = pcd.IMAGE_NAME

    return pointcloud

def generate_mesh(pointcloud):
    '''
    Generates mesh using ball pivoting algorithm
    :param pointcloud:
    :return: None
    '''

    radii = [0.005, 0.01, 0.02, 0.04]
    rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        pointcloud, o3d.utility.DoubleVector(radii))
    o3d.visualization.draw_geometries([pointcloud, rec_mesh])
    o3d.io.write_triangle_mesh(get_path_name(), mesh)

def main():

    pointcloud = pointcloud()
    generate_mesh(pointcloud)


if __name__ == "__main__":
    main()
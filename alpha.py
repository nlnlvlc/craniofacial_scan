# -*- coding: utf-8 -*-
"""
Reconstructs a base 3D model using the Alpha shapes as described at
https://graphics.stanford.edu/courses/cs268-11-spring/handouts/AlphaShapes/as_fisher.pdf
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
    path_name = f"{DIRECTORY}/alpha_{IMAGE_NAME}.ply"

    return path_name

def pointcloud():
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

def generate_mesh(pointcloud, alpha) -> None:
    '''
    Generates mesh using Alpha shapes
    :param pointcloud:
    :param alpha:
    :return: None
    '''
    print(f"alpha={alpha:.3f}")
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pointcloud, alpha)
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh])

    o3d.io.write_triangle_mesh(get_path_name(), mesh)

def main():

    pointcloud = pointcloud()
    alpha = float(input("Input Desired Alpha  <= 1: "))
    generate_mesh(pointcloud, alpha)

if __name__ == "__main__":
    main()
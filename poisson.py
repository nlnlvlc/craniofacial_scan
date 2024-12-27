# -*- coding: utf-8 -*-
"""
Reconstructs a base 3D model using poisson geometric generations
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
    path_name = f"{DIRECTORY}/poisson_{IMAGE_NAME}.ply"

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

def generate_mesh(pointcloud):
    '''
    Generates mesh and saves mesh using poisson algorithm
    :param pointcloud:
    :return: None
    '''
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            pointcloud, depth=12)
        mesh.compute_vertex_normals()
    print(mesh)

    o3d.visualization.draw_plotly([mesh])

    print('visualize densities')
    densities = np.asarray(densities)
    density_colors = plt.get_cmap('plasma')(
        (densities - densities.min()) / (densities.max() - densities.min()))
    density_colors = density_colors[:, :3]
    density_mesh = o3d.geometry.TriangleMesh()
    density_mesh.vertices = mesh.vertices
    density_mesh.triangles = mesh.triangles
    density_mesh.triangle_normals = mesh.triangle_normals
    density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
    o3d.visualization.draw_geometries([density_mesh])

    print('remove low density vertices')
    vertices_to_remove = densities < np.quantile(densities, 0.01)
    mesh.remove_vertices_by_mask(vertices_to_remove)
    mesh.compute_vertex_normals()
    print(mesh)
    o3d.visualization.draw_geometries([mesh])

    o3d.io.write_triangle_mesh(get_path_name(), mesh)

def main():

    pointcloud = pointcloud()
    generate_mesh(pointcloud)

if __name__ == "__main__":
    main()
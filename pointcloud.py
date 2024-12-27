'''
Produce and single pointcloud of image
'''
import subprocess
import os
import sys
import open3d as o3d
import numpy as np
from PIL import Image

DIRECTORY = ""
IMAGE_NAME = ""
FILE_TYPE = ""

def get_path_name() -> str:
    '''
    generates a path and file name to save output file
    :return: output file path name
    '''
    path_name = f"{DIRECTORY}/{IMAGE_NAME}{FILE_TYPE}"

    return path_name
def image_prep(imagePath, depthPath, directory, imageBasename) -> str:
    image = Image.open(imagePath)
    depth = Image.open(depthPath)

    print(f"Color Image dimensions: {image.size}")
    print(f"Depth Image dimensions: {depth.size}")

    new_image = image.resize(depth.size)

    print(f"Color Image Resized Dimensions: {new_image.size}")

    new_path = f"{directory}/resized-{imageBasename}"

    new_image.save(new_path)

    return new_path

def generate_pointcloud(colorPath, depthPath):
    color_image = o3d.io.read_image(colorPath)
    depth_image = o3d.io.read_image(depthPath)

    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_image, depth_image
    )

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault
        ),
    )

    pcd.normals = o3d.utility.Vector3dVector(np.zeros(
        (1, 3)))  # invalidate existing normals

    pcd.estimate_normals()

    return pcd

def get_pointcloud(view):
    # Open the image
    imagePath = input("Enter path for color image: ")
    depthPath = input("Enter path for depth image: ")

    filetypes = [".ply", ".pcd", ".obj"]

    fileType = input("Enter Desired Point Cloud File Extension: ").lower()
    writeType = input("Write output in ascii? (y/n): ").lower()

    writeType = True if writeType == "y" else writeType = False

    if fileType not in filetypes:
        print(f"File type {fileType} is unavailable. Saving as default {filetypes[0]}")
        FILE_TYPE = filetypes[0]
    else:
        FILE_TYPE = fileType

    DIRECTORY = os.path.dirname(imagePath)
    imageBasename = os.path.basename(imagePath)
    IMAGE_NAME = imageBasename.split(".")[0]


    colorPath = image_prep(imagePath, depthPath, DIRECTORY, imageBasename)
    pointcloud = generate_pointcloud(colorPath, depthPath)

    export_pointcloud(get_path_name(), pointcloud, writeType)

    if view:
        o3d.visualization.draw_geometries([pointcloud])

    return pointcloud

def export_pointcloud(path, pointcloud, writeType) -> None:
    o3d.io.write_point_cloud(path, pointcloud, write_ascii=writeType)

def main():

    view = input("View Point Cloud? (y/n): ").lower()
    view = True if view == "y" else view = False

    get_pointcloud(view)

if __name__ == "__main__":
    main()
import numpy as np
from stl import mesh
import porespy as ps
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def generate_voxels(shape, porosity, save_to_vtk=False, filename='voxels'):

    voxels = ps.generators.blobs(shape, porosity)

    if save_to_vtk:
        ps.io.to_vtk(voxels, path=filename, vox=False)

    # print(voxels)

    return voxels


def generate_voxels_mesh(voxels, save_to_stl=False, filename='stl_file.stl'):

    voxels_np = np.array(voxels, dtype=mesh.Mesh.dtype)
    voxels_mesh = mesh.Mesh(voxels_np, remove_empty_areas=False)

    if save_to_stl:
        voxels_mesh.save(filename)

    # print(voxels_mesh)

    return voxels_mesh


def show_generated_voxels(voxels):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, edgecolor='k')

    plt.show()


def show_stl_mesh(voxels_mesh):

    fig = plt.figure()
    axes = mplot3d.Axes3D(fig)

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(voxels_mesh.vectors))

    scale = voxels_mesh.points.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)

    plt.show()


def show_stl_mesh_from_stl_file(mesh_file):
    show_stl_mesh(mesh.Mesh.from_file(mesh_file))


porous_obj = generate_voxels(shape=[3, 3, 3], porosity=0.3)
# show_generated_voxels(porous_obj)

stl_file = 'stl_file.stl'
porous_mesh = generate_voxels_mesh(porous_obj, save_to_stl=True, filename=stl_file)

# show_stl_mesh(porous_mesh)
# # got ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

show_stl_mesh_from_stl_file(stl_file)

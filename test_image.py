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

    mesh_region = ps.tools.mesh_region(voxels)

    return mesh_region


def prepare_voxels_figure(voxels):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, edgecolor='k')


def prepare_stl_mesh_figure(voxels_mesh):

    fig = plt.figure()
    axes = mplot3d.Axes3D(fig)
    mesh_fig = mplot3d.art3d.Poly3DCollection(voxels_mesh.verts[voxels_mesh.faces])
    mesh_fig.set_edgecolor('k')
    axes.add_collection3d(mesh_fig)

    scale = voxels_mesh.verts.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)


size = 30
shape = [size, size, size]
porosity = 0.3

porous_obj = generate_voxels(shape, porosity)
# prepare_voxels_figure(porous_obj)

inverse_porous_obj = ~ porous_obj
prepare_voxels_figure(inverse_porous_obj)

# stl_file = 'stl_file.stl'
porous_mesh = generate_voxels_mesh(inverse_porous_obj)

prepare_stl_mesh_figure(porous_mesh)
# # got ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()


plt.show()

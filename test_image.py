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


def generate_mesh(voxels, save_to_stl=False, filename='stl_file.stl'):

    mesh_region = ps.tools.mesh_region(voxels)

    if save_to_stl:
        mesh_reg = list(map(lambda x: (0, x.tolist(), 0), mesh_region.verts[mesh_region.faces]))
        voxels_mesh = np.array(mesh_reg, dtype=mesh.Mesh.dtype)
        voxels_mesh = mesh.Mesh(voxels_mesh, remove_empty_areas=True)
        voxels_mesh.save(filename)

    return mesh_region


def prepare_voxels_figure(voxels):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, edgecolor='k')


def prepare_mesh_figure(voxels_mesh):

    fig = plt.figure()
    axes = mplot3d.Axes3D(fig)
    mesh_fig = mplot3d.art3d.Poly3DCollection(voxels_mesh.verts[voxels_mesh.faces])
    mesh_fig.set_edgecolor('k')
    axes.add_collection3d(mesh_fig)

    scale = voxels_mesh.verts.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)


size = 30
obj_shape = [size, size, size]
obj_porosity = 0.3

porous_obj = generate_voxels(obj_shape, obj_porosity)

# # Porespy generates an array with True values denoting the pore space
# # If we want True values denote the material we should inverse the array
porous_obj = ~ porous_obj

prepare_voxels_figure(porous_obj)

# stl_file = 'stl_file.stl'
porous_mesh = generate_mesh(porous_obj, save_to_stl=True)

prepare_mesh_figure(porous_mesh)

plt.show()

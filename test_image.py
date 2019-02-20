import numpy as np
from stl import mesh
import porespy as ps
# import matplotlib.pyplot as plt

voxels = ps.generators.blobs(shape=[10, 10, 10], porosity=0.3, blobiness=2)

voxels = np.array(voxels, dtype=mesh.Mesh.dtype)

print(np.empty([10, 10, 10])[0][0])
print(voxels.shape)
# print(voxels)

# for voxels_slice in voxels:
#     print(voxels_slice.shape)
#     for vx in voxels_slice:
#         print(vx.shape)

print(voxels[0][0])

# voxels_mesh = mesh.Mesh(voxels, remove_empty_areas=False)

# print(voxels_mesh)

# voxels_mesh.save('stl_file.stl')

# ps.io.to_vtk(voxels, path='voxels', vox=False)
#
# fig = plt.figure()
#
# ax = fig.gca(projection='3d')
# ax.voxels(voxels, edgecolor='k')
#
# plt.show()
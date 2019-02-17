import porespy as ps
import matplotlib.pyplot as plt

voxels = ps.generators.blobs(shape=[10, 10, 10], porosity=0.3, blobiness=2)

ps.io.to_vtk(voxels, path='voxels', vox=True)

fig = plt.figure()

ax = fig.gca(projection='3d')
ax.voxels(voxels, edgecolor='k')

plt.show()
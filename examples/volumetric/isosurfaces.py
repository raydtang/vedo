"""Interactively cut a set of meshes"""
from vedo import datadir, show, Volume

# generate an isosurface the volume for each thresholds
thresholds = [0.1, 0.25, 0.4, 0.6, 0.75, 0.9]

# isos is of type Mesh
isos = Volume(datadir+'quadric.vti').isosurface(thresholds)

show(isos, __doc__, axes=1, interactive=False).addCutterTool(isos)

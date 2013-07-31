#! /usr/bin/env pypy

import transvoxel
import noise

from vector import *
from euclid import *

CHUNK_SIZE=8

SIZE = CHUNK_SIZE+3
SIZE_SQ = SIZE**2
SIZE_CB = SIZE**3

class PlanetChunk(transvoxel.Chunk):
    def __init__(self, offset, lod, parent=None):
        transvoxel.Chunk.__init__(self, offset, CHUNK_SIZE, lod)

        self.parent = parent
        self.children = []

        self.center = vadds(offset, CHUNK_SIZE*lod/2)
        self.empty = False

class PlanetVolume:
    def __init__(self, radius, height, resolution, delegate=None):
        self.radius = radius
        self.height = height
        self.resolution = resolution
        self.delegate = delegate

        self.res = float(radius + height) * 2.0 / resolution

        self.normRad = radius / float(radius + height)
        self.normHeight = height / float(radius + height)

        self.deres = 1.0 / float(radius + height)

        self.extractor = transvoxel.VoxelExtractor(self)

        offset = -resolution/2
        self.chunks = [
            PlanetChunk((offset,offset,offset), resolution/CHUNK_SIZE)
        ]

        self.parents = []

        self._meshes = {}

        self.build(self.chunks[0])

        self.modelmatrix = Matrix4.new_scale(self.res, self.res, self.res)

    def get(self, chunk, pos):
        i, j, k = vdivs(vsub(pos, chunk.offset), chunk.lod)
        i, j, k = i+1, j+1, k+1

        return chunk.data[i*SIZE_SQ + j*SIZE + k] - 128

    def _getVal(self, pos):
        pos = vmuls(pos, 2.0 / self.resolution)

        base = self.normRad - vlen(pos)
        extra = noise.ridged_multifractal(4, pos[0], pos[1], pos[2], 2, 2, 1, 0.5, 1, 1) * self.normHeight

        val = min(1, max(-1, base + extra))
        return int(val * 127 + 128)

    def _addMesh(self, k, m):
        if self.delegate:
            self.delegate.add(m)

        self._meshes[k] = m

    def _removeMesh(self, k):
        if self.delegate:
            self.delegate.remove(self._meshes[k])

        del self._meshes[k]

    def meshes(self):
        return self._meshes.values()

    def build(self, chunk):
        self._buildData(chunk)

        mesh = self.extractor.extract(chunk)

        if len(mesh.indices):
            self._addMesh(chunk, mesh)
        else:
            chunk.empty = True

        del chunk.data

    def _buildData(self, chunk):
        chunk.data = bytearray(SIZE_CB)

        for i in range(SIZE):
            for j in range(SIZE):
                for k in range(SIZE):
                    pos = vadd(chunk.offset, vmuls((i-1, j-1, k-1), chunk.lod))
                    chunk.data[i*SIZE_SQ + j*SIZE + k] = self._getVal(pos)

    def split(self, chunk):
        if chunk.lod <= 1 or len(chunk.children) > 1 or chunk.empty:
            return

        pos = chunk.offset
        lod = chunk.lod/2
        s = lod*CHUNK_SIZE

        children = [
            PlanetChunk(vadd(pos, (0,0,0)), lod, chunk),
            PlanetChunk(vadd(pos, (s,0,0)), lod, chunk),
            PlanetChunk(vadd(pos, (0,0,s)), lod, chunk),
            PlanetChunk(vadd(pos, (s,0,s)), lod, chunk),
            PlanetChunk(vadd(pos, (0,s,0)), lod, chunk),
            PlanetChunk(vadd(pos, (s,s,0)), lod, chunk),
            PlanetChunk(vadd(pos, (0,s,s)), lod, chunk),
            PlanetChunk(vadd(pos, (s,s,s)), lod, chunk)
        ]

        for c in children:
            self.build(c)

        self._removeMesh(chunk)

        chunk.children = children

        self.chunks += children

        self.chunks.remove(chunk)
        self.parents.append(chunk)

        if chunk.parent != None:
            self.parents.remove(chunk)

    def merge(self, chunk):
        if len(chunk.children) == 0:
            return

        self.build(chunk)

        for c in chunk.children:
            self._removeMesh(c)
            self.chunks.remove[c]

        chunk.children = []

        self.parents.remove(chunk)
        self.chunks.append(chunk)

        if chunk.parent != None:
            self.parents.append(chunk)

    def update(self, viewer):
        merges, splits = {}, {}

        for p in self.parents:
            factor = self._splitFactor(p, viewer)
            if factor > 1:
                merges[factor] = p

        if len(merges):
            self.merge(merges[max(merges)])

        for c in self.chunks:
            factor = self._splitFactor(c, viewer)
            if factor < 1:
                splits[factor] = c

        if len(splits):
            self.split(splits[min(splits)])

    def _splitFactor(self, chunk, viewer):
            dist = 0.8*vlen(vsub(vmuls(chunk.center, self.res), viewer))
            size = chunk.lod*CHUNK_SIZE * self.res

            return dist / float(size)

if __name__ == "__main__":

    planet = PlanetVolume(90.0, 10.0, 256)

    for i in range(8):
        planet.update((90, 0, 0))

    k = 1
    for mesh in planet.meshes():
        print 'o chunk%d' % (id(mesh))

        for i in range(0, len(mesh.vertices), 3):
            print 'v %f %f %f' % (mesh.vertices[i], mesh.vertices[i+1], mesh.vertices[i+2])

        for i in range(0, len(mesh.indices), 3):
            print 'f %i %i %i' % (mesh.indices[i]+k, mesh.indices[i+1]+k, mesh.indices[i+2]+k)

        k += len(mesh.vertices)/3


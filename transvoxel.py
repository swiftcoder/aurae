#! /usr/bin/env python

import lengyel
import noise

from vector import *

class Chunk:
    def __init__(self, offset, size, lod=1):
        self.offset = offset
        self.size = size
        self.lod = lod

class StaticVolume:
    def __init__(self, size):
        self.size = (size, size, size)

    def extents(self):
        return self.size

    def get(self, chunk, pos):
        pos = vmuls(pos, 1.0/16.0)
        return min(127, max(-127, int(noise.fractal_brownian_motion(4, pos[0], pos[1], pos[2], 1.9, 0.65) * 128)))

class Mesh:
    def __init__(self):
        self.vertices = []
        self.indices = []

class VoxelExtractor:
    def __init__(self, volume):
        self.volume = volume

    def extract(self, chunk):
        mesh = Mesh()

        for i in range(chunk.size):
            for j in range(chunk.size):
                for k in range(chunk.size):
                    self.polygonise(chunk.offset, (i, j, k), mesh, chunk.lod, chunk)

        return mesh

    def polygonise(self, offset, pos, mesh, lod, chunk):
        assert lod >= 1

        offsetPos = vadd(offset, vmuls(pos, lod))

        directionMask = ((pos[0] > 0) | ((pos[2] > 0) << 1) | ((pos[1] > 0) << 2)) & 0xFF

        density = [self.volume.get( chunk, vadd(offsetPos, vmuls(lengyel.CornerIndex[i], lod)) ) for i in range(8)]

        caseCode = self.getCaseCode(density)
        if (caseCode ^ ((density[7] >> 7) & 0xFF)) == 0: # no geometry in this case
            return

        regularCellClass = lengyel.RegularCellClass[caseCode]
        vertexLocations = lengyel.RegularVertexData[caseCode]

        cell = lengyel.RegularCellData[regularCellClass]
        vertexCount = cell[0] >> 4
        triangleCount = cell[0] & 0x0F
        indexOffset = cell[1]
        mappedIndices = [0]*len(indexOffset)

        for i in range(vertexCount):
            edge = (vertexLocations[i] >> 8) & 0xFF
            reuseIndex = edge & 0xF
            rDir = (edge >> 4) & 0xFF

            v1 = vertexLocations[i] & 0x0F
            v0 = (vertexLocations[i] >> 4) & 0x0F

            assert v1 > v0

            d0 = density[v0]
            d1 = density[v1]

            t = (d1 << 8) / (d1 - d0)
            u = 256 - t
            t0 = t / 256.0
            t1 = u / 256.0

            self.generateVertex(offsetPos, pos, mesh, lod, t, v0, v1, d0, d1)
            mappedIndices[i] = len(mesh.vertices) - 1

        for t in range(triangleCount):
            for i in range(3):
                mesh.indices.append( mappedIndices[indexOffset[t * 3 + i]] )

    def getCaseCode(self, density):
        code = 0
        konj = 0x01

        for i in range(len(density)):
            code |= ((density[i] >> (len(density) - 1 - i)) & konj) & 0xFF
            konj <<= 1

        return code

    def generateVertex(self, offsetPos, pos, mesh, lod, t, v0, v1, d0, d1):
        P0 = vadd(offsetPos, vmuls(lengyel.CornerIndex[v0], lod))
        P1 = vadd(offsetPos, vmuls(lengyel.CornerIndex[v1], lod))

        Q = self.interpolateVoxelVector(t, P0, P1)

        mesh.vertices.append(Q)

    def interpolateVoxelVector(self, t, P0, P1):
        u = 256 - t
        s = 1.0 / 256.0
        Q = vadd( vmuls(P0, t), vmuls(P1, u) )
        return vmuls(Q, s)

if __name__ == '__main__':
    
    volume = StaticVolume(128)
    extractor = VoxelExtractor(volume)

    chunks = [
        Chunk((0,0,0), 16),
        Chunk((0,16,0), 16),
        Chunk((16,0,0), 16, 2)
    ]

    meshes = [extractor.extract(chunk) for chunk in chunks]

    k = 1
    for mesh in meshes:
        for x, y, z in mesh.vertices:
            print 'v %f %f %f' % (x, y, z)

        for i in range(0, len(mesh.indices), 3):
            print 'f %i %i %i' % (mesh.indices[i]+k, mesh.indices[i+1]+k, mesh.indices[i+2]+k)

        k += len(mesh.vertices)

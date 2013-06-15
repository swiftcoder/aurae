
from OpenGL.GL import *
from ctypes import c_float, c_ushort

class Mesh:
    def __init__(self, vertices, normals, indices):
        self.varray = glGenVertexArrays(1)
        self.vertices, self.normals, self.indices = glGenBuffers(3)
        self.count = len(indices)

        nativeVertices = (c_float * len(vertices))(*vertices)
        nativeNormals = (c_float * len(normals))(*normals)
        nativeIndices = (c_ushort *len(indices))(*indices)

        glBindVertexArray(self.varray)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertices)
        glBufferData(GL_ARRAY_BUFFER, nativeVertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, self.normals)
        glBufferData(GL_ARRAY_BUFFER, nativeNormals, GL_STATIC_DRAW)

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indices)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, nativeIndices, GL_STATIC_DRAW)

        glBindVertexArray(0)

        del nativeVertices
        del nativeNormals
        del nativeIndices

    def draw(self):
        glBindVertexArray(self.varray)

        glDrawElements(GL_TRIANGLES, self.count, GL_UNSIGNED_SHORT, None)

        glBindVertexArray(0)


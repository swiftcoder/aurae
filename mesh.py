
from OpenGL.GL import *
from ctypes import c_float, c_ushort

class Mesh:
    def __init__(self, vertices, normals=None, indices=None):
        self.varray = glGenVertexArrays(1)

        glBindVertexArray(self.varray)

        self.vertices = glGenBuffers(1)
        nativeVertices = (c_float * len(vertices))(*vertices)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertices)
        glBufferData(GL_ARRAY_BUFFER, nativeVertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        del nativeVertices

        if normals:
            self.normals = glGenBuffers(1)
            nativeNormals = (c_float * len(normals))(*normals)

            glBindBuffer(GL_ARRAY_BUFFER, self.normals)
            glBufferData(GL_ARRAY_BUFFER, nativeNormals, GL_STATIC_DRAW)

            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

            del nativeNormals

        if indices:
            self.indices = glGenBuffers(1)

            nativeIndices = (c_ushort *len(indices))(*indices)

            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indices)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, nativeIndices, GL_STATIC_DRAW)

            del nativeIndices

        glBindVertexArray(0)

        if indices:
            self.count = len(indices)
        else:
            self.count = len(vertices)/3

    def draw(self, type=GL_TRIANGLES):
        glBindVertexArray(self.varray)

        if hasattr(self, 'indices'):
            glDrawElements(type, self.count, GL_UNSIGNED_SHORT, None)
        else:
            glDrawArrays(type, 0, self.count)

        glBindVertexArray(0)



from OpenGL.GL import *

class Texture:
    def __init__(self, width, height, depth, data):
        self.handle = glGenTextures(1)
        glBindTexture(GL_TEXTURE_3D, self.handle)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_R, GL_REPEAT)
        glTexImage3D(GL_TEXTURE_3D, 0, GL_RED, width, height, depth, 0, GL_RED, GL_UNSIGNED_BYTE, data)

    def __enter__(self):
        glBindTexture(GL_TEXTURE_3D, self.handle)
        return self

    def __exit__(self, type, value, tb):
        glBindTexture(GL_TEXTURE_3D, 0)


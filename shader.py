
from OpenGL.GL import *
from ctypes import c_float

import euclid

class Shader:
    def __init__(self, vert = '', frag = '', geom = ''):
        self.handle = glCreateProgram()

        self.Linked = False
        self.uniforms = {}

        self.createShader(vert, GL_VERTEX_SHADER)
        self.createShader(frag, GL_FRAGMENT_SHADER)
        self.createShader(geom, GL_GEOMETRY_SHADER)

        # glProgrami(self.handle, GL_GEOMETRY_INPUT_TYPE, GL_TRIANGLES)
        # glProgrami(self.handle, GL_GEOMETRY_OUTPUT_TYPE, GL_TRIANGLE_STRIP)
        # glProgrami(self.handle, GL_GEOMETRY_VERTICES_OUT, 4)

        self.link()
        self.query_uniforms()

    def createShader(self, source, type):
        if len(source) == 0:
            return

        shader = glCreateShader(type)

        glShaderSource(shader, source)

        glCompileShader(shader)

        result = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if result != GL_TRUE:
            print glGetShaderInfoLog(shader)

        glAttachShader(self.handle, shader);

    def link(self):
        glLinkProgram(self.handle)

        result = glGetProgramiv(self.handle, GL_LINK_STATUS)
        if result:
            print glGetProgramInfoLog(self.handle)
        else:
            self.Linked = True

    def query_uniforms(self):
        count = glGetProgramiv(self.handle, GL_ACTIVE_UNIFORMS)

        for i in range(count):
            name, _, _ = glGetActiveUniform(self.handle, i)
            loc = glGetUniformLocation(self.handle, name)
            self.uniforms[name] = loc

    def __enter__(self):
        glUseProgram(self.handle)
        return self

    def __exit__(self, type, value, tb):
        glUseProgram(0)

    def uniform(self, name, vals):
        try:
            loc = self.uniforms[name]

            if len(vals) in range(1, 5):
                { 1 : glUniform1f,
                    2 : glUniform2f,
                    3 : glUniform3f,
                    4 : glUniform4f
                }[len(vals)](loc, *vals)
        except KeyError:
            print 'no such uniform: %s' % name

    def uniform_matrix_3x3(self, name, mat):
        loc = self.uniforms[name]

        glUniformMatrix3fv(loc, 1, False, (c_float * 9)(*mat))

    def uniform_matrix_4x4(self, name, mat):
        try:
            loc = self.uniforms[name]

            glUniformMatrix4fv(loc, 1, False, (c_float * 16)(*mat))
        except KeyError:
            print 'no such uniform: %s' % name

    def uniformi(self, name, val):
        try:
            loc = self.uniforms[name]

            glUniform1i(loc, val)
        except KeyError:
            print 'no such uniform: %s' % name

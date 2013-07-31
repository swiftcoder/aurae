#! /usr/bin/env pypy

from glfw.glfw import *
from OpenGL.GL import *
from OpenGL.arrays import *

import math
from math import radians
from euclid import *

from shader import Shader
from mesh import Mesh

from planet import PlanetVolume

glfwInit()

glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2)
glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE)
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

window = glfwCreateWindow(1024, 768, 'aurae - orbit')
glfwMakeContextCurrent(window)

shader = Shader('''
#version 140

uniform mat4 ModelViewProjMat;

in vec4 in_Position;
in vec3 in_Normal;

out vec3 v_Normal;

void main(void)
{
    gl_Position = ModelViewProjMat * in_Position;
    v_Normal = in_Normal;
}
''', '''
#version 140

precision highp float;

uniform vec4 DiffuseColor;

in vec3 v_Normal;

out vec4 out_Color;

const vec3 lightDir = vec3(0.1,-0.8,0.4);

void main(void)
{
    float NdotL = dot(normalize(v_Normal), lightDir);
    vec3 lit = DiffuseColor.rgb * clamp(NdotL, 0.2, 1.0);
    out_Color = vec4(lit.rgb, DiffuseColor.a);
}
''')

# mesh = Mesh([0,0,0, 1,0,0, 1,1,0, 0,1,0], [0,1,2, 0,2,3])

projection = Matrix4.new_perspective(math.radians(60.0), 1024/768.0, 1.0, 10000.0)
camera = Matrix4.new_look_at(Vector3(0,0,-250), Vector3(0,0,0), Vector3(0,1,0))


meshes = {}
class Delegate:
    def add(self, m):
        global meshes
        meshes[m] = Mesh(m.vertices, m.normals, m.indices)

    def remove(self, m):
        global meshes
        del meshes[m]

planet = PlanetVolume(90.0, 10.0, 1024, Delegate())

camLoc = camera * Point3(0,0,0)
for i in range(4):
    planet.update(camLoc)

print len(meshes), 'chunks'


glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)

curTime = glfwGetTime() - 1.0/30.0

speed = 20.0
rotSpeed = 100.0

while not glfwWindowShouldClose(window):
    glfwPollEvents()

    lastTime = curTime
    curTime = glfwGetTime()
    dt = curTime - lastTime

    if glfwGetKey(window, GLFW_KEY_W):
        camera.translate(0, 0, -speed*dt)
    if glfwGetKey(window, GLFW_KEY_S):
        camera.translate(0, 0,  speed*dt)

    if glfwGetKey(window, GLFW_KEY_LEFT):
        camera.rotate_euler(radians( rotSpeed*dt), 0, 0)
    if glfwGetKey(window, GLFW_KEY_RIGHT):
        camera.rotate_euler(radians(-rotSpeed*dt), 0, 0)
    if glfwGetKey(window, GLFW_KEY_UP):
        camera.rotate_euler(0, 0, radians( rotSpeed*dt))
    if glfwGetKey(window, GLFW_KEY_DOWN):
        camera.rotate_euler(0, 0, radians(-rotSpeed*dt))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = camera.inverse()

    camLoc = camera * Point3(0,0,0)
    planet.update(camLoc)

    with shader as s:
        s.uniform('DiffuseColor', (0.5, 0.5, 1, 1))
        s.uniform_matrix_4x4('ModelViewProjMat', projection * view * planet.modelmatrix)

        for k, m in meshes.iteritems():
            m.draw()

    glfwSwapBuffers(window)

glfwTerminate()

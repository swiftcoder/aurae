#! /usr/bin/env pypy

from glfw.glfw import *
from OpenGL.GL import *
from OpenGL.arrays import *

import math
from math import radians
from euclid import *

from shader import Shader
from texture import Texture
from mesh import Mesh

from ctypes import c_ubyte

from noise import *

glfwInit()

glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2)
glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE)
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

window = glfwCreateWindow(1024, 768, 'aurae - raycast')
glfwMakeContextCurrent(window)

shader = Shader('''
#version 150

uniform mat4 ModelViewInvMat;

in vec4 in_Position;

out vec3 vs_Position;

void main(void)
{
    vs_Position = (ModelViewInvMat * in_Position).xyz;

    gl_Position = in_Position;
}
''', '''
#version 150

precision highp float;

uniform sampler3D Density;
uniform vec3 EyePos;

in vec3 vs_Position;

out vec4 out_Color;

float sphere(vec3 p, float radius)
{
    return length(p) - radius;
}

float box(vec3 p, vec3 b)
{
    vec3 d = abs(p) - b;
    return min(max(d.x,max(d.y,d.z)),0.0) + length(max(d,0.0));
}

float distance(vec3 p)
{
    float columns = min(
        box(p + vec3(-20,0,0), vec3(5,25,5)),
        box(p + vec3( 20,0,0), vec3(5,25,5))
    );

    float scene = min(columns, sphere(p, 5));

    return scene - 0.1*texture(Density, p*0.1).x;
}

float map(vec3 pos) {
    return distance(pos);
}

vec3 calcNormal(vec3 pos) {
    vec3 eps = vec3( 0.001, 0.0, 0.0 );
    vec3 nor = vec3(
        map(pos+eps.xyy) - map(pos-eps.xyy),
        map(pos+eps.yxy) - map(pos-eps.yxy),
        map(pos+eps.yyx) - map(pos-eps.yyx)
    );
    return normalize(nor);
}

vec4 calcColor(vec3 pos, vec3 normal, float depth) {
    float bump = 0.2 + 0.8 * dot(normal, vec3(0,0.7,-0.7));
    return vec4(vec3(bump), 1.0);
}

void main(void)
{
    vec3 start = EyePos;
    vec3 dir = normalize(vs_Position - EyePos);

    float t = 0.0;

    for (int i = 0; i < 64; ++i) {
        float distance = map(start + dir * t);

        t += distance; //max(distance, 0.01);
    }

    vec3 pos = start + dir * t;

    vec3 normal = calcNormal(pos);
    out_Color = calcColor(pos, normal, t);
}
''')

mesh = Mesh([-1,-1,-1, 1,-1,-1, 1,1,-1, -1,1,-1], None, [0, 1, 2, 0, 2, 3])

SIZE = 64
SIZE1 = float(SIZE-1)

data = (c_ubyte * (SIZE**3))()

for i in range(SIZE):
    for j in range(SIZE):
        for k in range(SIZE):
            val = int(ridged_multifractal(4, i/SIZE1, j/SIZE1, k/SIZE1, 2, 2, 1, 0.5, 1, 1) * 127 + 127)
            data[i*SIZE*SIZE + j*SIZE + k] = val

texture = Texture(SIZE, SIZE, SIZE, data)


projection = Matrix4.new_perspective(math.radians(60.0), 1024/768.0, 0.1, 100.0)
camera = Matrix4.new_look_at(Vector3(-25,1,-25), Vector3(0,0,0), Vector3(0,1,0))


glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)

curTime = glfwGetTime() - 1.0/30.0

speed = 20.0

with shader as s:
    s.uniformi('Density', 0)

while not glfwWindowShouldClose(window):
    glfwPollEvents()

    lastTime = curTime
    curTime = glfwGetTime()
    dt = curTime - lastTime

    if glfwGetKey(window, GLFW_KEY_W):
        camera.translate(0, 0, -speed*dt)
    if glfwGetKey(window, GLFW_KEY_S):
        camera.translate(0, 0,  speed*dt)
    if glfwGetKey(window, GLFW_KEY_A):
        camera.translate(-speed*dt, 0, 0)
    if glfwGetKey(window, GLFW_KEY_D):
        camera.translate( speed*dt, 0, 0)

    if glfwGetKey(window, GLFW_KEY_LEFT):
        camera.rotate_euler(radians( 5*speed*dt), 0, 0)
    if glfwGetKey(window, GLFW_KEY_RIGHT):
        camera.rotate_euler(radians(-5*speed*dt), 0, 0)
    if glfwGetKey(window, GLFW_KEY_UP):
        camera.rotate_euler(0, 0, radians( 5*speed*dt))
    if glfwGetKey(window, GLFW_KEY_DOWN):
        camera.rotate_euler(0, 0, radians(-5*speed*dt))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = camera.inverse()

    with shader as s, texture as t:
        s.uniform_matrix_4x4('ModelViewInvMat', camera)
        s.uniform('EyePos', camera * Point3(0,0,0))

        mesh.draw()

    glfwSwapBuffers(window)

glfwTerminate()

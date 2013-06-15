
import math

perm = [151,160,137,91,90,15,
  131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
  190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
  88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
  77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
  102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
  135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
  5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
  223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
  129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
  251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
  49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
  138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180,
  151,160,137,91,90,15,
  131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
  190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
  88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
  77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
  102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
  135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
  5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
  223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
  129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
  251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
  49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
  138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

grad3 = [[0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1],
         [1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],
         [1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0], # 12 cube edges
         [1,0,-1],[-1,0,-1],[0,-1,1],[0,1,1]] # 4 more to make 16

simplex4 = [[0,64,128,192],[0,64,192,128],[0,0,0,0],
  [0,128,192,64],[0,0,0,0],[0,0,0,0],[0,0,0,0],[64,128,192,0],
  [0,128,64,192],[0,0,0,0],[0,192,64,128],[0,192,128,64],
  [0,0,0,0],[0,0,0,0],[0,0,0,0],[64,192,128,0],
  [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [64,128,0,192],[0,0,0,0],[64,192,0,128],[0,0,0,0],
  [0,0,0,0],[0,0,0,0],[128,192,0,64],[128,192,64,0],
  [64,0,128,192],[64,0,192,128],[0,0,0,0],[0,0,0,0],
  [0,0,0,0],[128,0,192,64],[0,0,0,0],[128,64,192,0],
  [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [128,0,64,192],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [192,0,64,128],[192,0,128,64],[0,0,0,0],[192,64,128,0],
  [128,64,0,192],[0,0,0,0],[0,0,0,0],[0,0,0,0],
  [192,64,0,128],[0,0,0,0],[192,128,0,64],[192,128,64,0]]

def fastfloor(x):
    y = int(x)
    return y if (x > 0) else (y - 1)

def step(a, b):
    return 0 if (a > b) else 1;

def dot(g, x, y, z):
    return g[0]*x + g[1]*y + g[2]*z;

def perm3(x, y, z):
    i = perm[(x + perm[y]) & 0xFF]
    return perm[(i + perm[z]) & 0xFF]

def simplex(x, y, z):
    # Simple skewing factors for the 3D case
    F3 = 0.333333333;
    G3 = 0.166666667;
        
    #float n0, n1, n2, n3; /* Noise contributions from the four corners */
    
    # var n0 : float;
    # var n1 : float;
    # var n2 : float;
    # var n3 : float;
    
    # Skew the input space to determine which simplex cell we're in
    s = (x+y+z)*F3; # Very nice and simple skew factor for 3D
    i = fastfloor(x + s);
    j = fastfloor(y + s);
    k = fastfloor(z + s);
    
    t = (i+j+k)*G3;
    X0 = i-t; # Unskew the cell origin back to (x,y,z) space
    Y0 = j-t;
    Z0 = k-t;
    x0 = x-X0; # The x,y,z distances from the cell origin
    y0 = y-Y0;
    z0 = z-Z0;
    
    # For the 3D case, the simplex shape is a slightly irregular tetrahedron.
    # Determine which simplex we are in.
    #int i1, j1, k1; /* Offsets for second corner of simplex in (i,j,k) coords */
    #int i2, j2, k2; /* Offsets for third corner of simplex in (i,j,k) coords */
    
    # var i1 : int;
    # var j1 : int;
    # var k1 : int;
    # var i2 : int;
    # var j2 : int;
    # var k2 : int;

    # /*int c1 = x>y ? 32 : 0;
    # int c2 = x>z ? 16 : 0;
    # int c3 = y>z ? 8 : 0;
    
    # int offset = c1+c2+c3;

    # i1 = step(96, simplex4[offset][0]);
    # j1 = step(96, simplex4[offset][1]);
    # k1 = step(96, simplex4[offset][2]);

    # i2 = step(32, simplex4[offset][0]);
    # j2 = step(32, simplex4[offset][1]);
    # k2 = step(32, simplex4[offset][2]);*/
    
    # This code would benefit from a backport from the GLSL version!
    if x0>=y0:
      if y0>=z0:
        i1=1; j1=0; k1=0; i2=1; j2=1; k2=0; # X Y Z order
      elif x0>=z0:
        i1=1; j1=0; k1=0; i2=1; j2=0; k2=1; # X Z Y order
      else:
        i1=0; j1=0; k1=1; i2=1; j2=0; k2=1; # // Z X Y order
    else:
      if y0<z0:
        i1=0; j1=0; k1=1; i2=0; j2=1; k2=1; # Z Y X order
      elif x0<z0:
        i1=0; j1=1; k1=0; i2=0; j2=1; k2=1; # Y Z X order
      else:
        i1=0; j1=1; k1=0; i2=1; j2=1; k2=0; # Y X Z order
    
    # A step of (1,0,0) in (i,j,k) means a step of (1-c,-c,-c) in (x,y,z),
    # a step of (0,1,0) in (i,j,k) means a step of (-c,1-c,-c) in (x,y,z), and
    # a step of (0,0,1) in (i,j,k) means a step of (-c,-c,1-c) in (x,y,z), where
    # c = 1/6.

    x1 = x0 - i1 + G3; # Offsets for second corner in (x,y,z) coords
    y1 = y0 - j1 + G3;
    z1 = z0 - k1 + G3;
    x2 = x0 - i2 + 2.0*G3; # Offsets for third corner in (x,y,z) coords
    y2 = y0 - j2 + 2.0*G3;
    z2 = z0 - k2 + 2.0*G3;
    x3 = x0 - 1.0 + 3.0*G3; # Offsets for last corner in (x,y,z) coords
    y3 = y0 - 1.0 + 3.0*G3;
    z3 = z0 - 1.0 + 3.0*G3;
    
    # Wrap the integer indices at 256, to avoid indexing perm[] out of bounds
    ii = i % 256;
    jj = j % 256;
    kk = k % 256;
    
    if ii < 0:
      ii += 256;
    if jj < 0:
      jj += 256;
    if kk < 0:
      kk += 256;
    
    gi0 = perm3(ii, jj, kk) % 12;
    gi1 = perm3(ii+i1, jj+j1, kk+k1) % 12;
    gi2 = perm3(ii+i2, jj+j2, kk+k2) % 12;
    gi3 = perm3(ii+1, jj+1, kk+1) % 12;

    # Calculate the contribution from the four corners
    t0 = 0.6 - x0*x0 - y0*y0 - z0*z0;
    if t0 < 0.0:
      n0 = 0.0;
    else:
      t0 *= t0;
      #n0 = t0 * t0 * grad(perm[ii+perm[jj+perm[kk]]], x0, y0, z0);
      n0 = t0 * t0 * dot(grad3[gi0], x0, y0, z0);
    
    t1 = 0.6 - x1*x1 - y1*y1 - z1*z1;
    if t1 < 0.0:
      n1 = 0.0;
    else:
      t1 *= t1;
      #n1 = t1 * t1 * grad(perm[ii+i1+perm[jj+j1+perm[kk+k1]]], x1, y1, z1);
      n1 = t1 * t1 * dot(grad3[gi1], x1, y1, z1);
    
    t2 = 0.6 - x2*x2 - y2*y2 - z2*z2;
    if t2 < 0.0:
      n2 = 0.0;
    else:
      t2 *= t2;
      #n2 = t2 * t2 * grad(perm[ii+i2+perm[jj+j2+perm[kk+k2]]], x2, y2, z2);
      n2 = t2 * t2 * dot(grad3[gi2], x2, y2, z2);
    
    t3 = 0.6 - x3*x3 - y3*y3 - z3*z3;
    if t3<0.0:
      n3 = 0.0;
    else:
      t3 *= t3;
      #n3 = t3 * t3 * grad(perm[ii+1+perm[jj+1+perm[kk+1]]], x3, y3, z3);
      n3 = t3 * t3 * dot(grad3[gi3], x3, y3, z3);
    
    # Add contributions from each corner to get the final noise value.
    # The result is scaled to stay just inside [-1,1]
    return 32.0 * (n0 + n1 + n2 + n3); # TODO: The scale factor is preliminary!

def fractal_brownian_motion(octaves, x, y, z, lacunarity, gain):
    #const double lacunarity = 1.9;
    #const double gain = 0.65;
    
    sum = 0.0
    amplitude = 1.0
    
    for i in range(octaves):
      sum += amplitude * simplex(x, y, z)

      amplitude *= gain

      x *= lacunarity
      y *= lacunarity
      z *= lacunarity
    
    return sum

def ridged_multifractal(octaves, x, y, z, lacunarity, gain, offset, h, weight, freq):
    #const double lacunarity = 2.0;
    #const double gain = 2.0;
    #const double offset = 1.0;
    #const double h = 1.0;
    
    signal = 0.0
    value = 0.0
    #double weight = 1.0;
    #double freq = 1.0;
    
    for i in range(octaves):
      signal = (offset - abs(simplex(x, y, z)))

      signal *= signal * weight
      
      weight = signal*gain

      weight = max(0.0, min(1.0, weight))

      value += signal * math.pow(freq, -h)
      
      freq *= lacunarity

      x *= lacunarity
      y *= lacunarity
      z *= lacunarity
    
    return value * 0.5

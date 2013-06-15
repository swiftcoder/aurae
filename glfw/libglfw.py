import ctypes


glfwLib_paths = ['glfw/glfw3.dll', 'glfw/libglfw3.so', 'glfw/glfw.dll', 'glfw/libglfw.so', 'glfw/libglfw.dylib']
glfwLib = None

for library_path in glfwLib_paths:
	try:
		glfwLib = ctypes.cdll.LoadLibrary(library_path)
		break
	except OSError:
		pass

if not glfwLib:
	raise Exception('Unable to find GLFW3 library: {}'.format(', '.join(glfwLib_paths)))


## MACROS
GLFW_VERSION_MAJOR = 3
GLFW_VERSION_MINOR = 0
GLFW_VERSION_REVISION = 1
GLFW_RELEASE = 0
GLFW_PRESS = 1
GLFW_REPEAT = 2
GLFW_KEY_UNKNOWN = -1
GLFW_KEY_SPACE = 32
GLFW_KEY_APOSTROPHE = 39
GLFW_KEY_COMMA = 44
GLFW_KEY_MINUS = 45
GLFW_KEY_PERIOD = 46
GLFW_KEY_SLASH = 47
GLFW_KEY_0 = 48
GLFW_KEY_1 = 49
GLFW_KEY_2 = 50
GLFW_KEY_3 = 51
GLFW_KEY_4 = 52
GLFW_KEY_5 = 53
GLFW_KEY_6 = 54
GLFW_KEY_7 = 55
GLFW_KEY_8 = 56
GLFW_KEY_9 = 57
GLFW_KEY_SEMICOLON = 59
GLFW_KEY_EQUAL = 61
GLFW_KEY_A = 65
GLFW_KEY_B = 66
GLFW_KEY_C = 67
GLFW_KEY_D = 68
GLFW_KEY_E = 69
GLFW_KEY_F = 70
GLFW_KEY_G = 71
GLFW_KEY_H = 72
GLFW_KEY_I = 73
GLFW_KEY_J = 74
GLFW_KEY_K = 75
GLFW_KEY_L = 76
GLFW_KEY_M = 77
GLFW_KEY_N = 78
GLFW_KEY_O = 79
GLFW_KEY_P = 80
GLFW_KEY_Q = 81
GLFW_KEY_R = 82
GLFW_KEY_S = 83
GLFW_KEY_T = 84
GLFW_KEY_U = 85
GLFW_KEY_V = 86
GLFW_KEY_W = 87
GLFW_KEY_X = 88
GLFW_KEY_Y = 89
GLFW_KEY_Z = 90
GLFW_KEY_LEFT_BRACKET = 91
GLFW_KEY_BACKSLASH = 92
GLFW_KEY_RIGHT_BRACKET = 93
GLFW_KEY_GRAVE_ACCENT = 96
GLFW_KEY_WORLD_1 = 161
GLFW_KEY_WORLD_2 = 162
GLFW_KEY_ESCAPE = 256
GLFW_KEY_ENTER = 257
GLFW_KEY_TAB = 258
GLFW_KEY_BACKSPACE = 259
GLFW_KEY_INSERT = 260
GLFW_KEY_DELETE = 261
GLFW_KEY_RIGHT = 262
GLFW_KEY_LEFT = 263
GLFW_KEY_DOWN = 264
GLFW_KEY_UP = 265
GLFW_KEY_PAGE_UP = 266
GLFW_KEY_PAGE_DOWN = 267
GLFW_KEY_HOME = 268
GLFW_KEY_END = 269
GLFW_KEY_CAPS_LOCK = 280
GLFW_KEY_SCROLL_LOCK = 281
GLFW_KEY_NUM_LOCK = 282
GLFW_KEY_PRINT_SCREEN = 283
GLFW_KEY_PAUSE = 284
GLFW_KEY_F1 = 290
GLFW_KEY_F2 = 291
GLFW_KEY_F3 = 292
GLFW_KEY_F4 = 293
GLFW_KEY_F5 = 294
GLFW_KEY_F6 = 295
GLFW_KEY_F7 = 296
GLFW_KEY_F8 = 297
GLFW_KEY_F9 = 298
GLFW_KEY_F10 = 299
GLFW_KEY_F11 = 300
GLFW_KEY_F12 = 301
GLFW_KEY_F13 = 302
GLFW_KEY_F14 = 303
GLFW_KEY_F15 = 304
GLFW_KEY_F16 = 305
GLFW_KEY_F17 = 306
GLFW_KEY_F18 = 307
GLFW_KEY_F19 = 308
GLFW_KEY_F20 = 309
GLFW_KEY_F21 = 310
GLFW_KEY_F22 = 311
GLFW_KEY_F23 = 312
GLFW_KEY_F24 = 313
GLFW_KEY_F25 = 314
GLFW_KEY_KP_0 = 320
GLFW_KEY_KP_1 = 321
GLFW_KEY_KP_2 = 322
GLFW_KEY_KP_3 = 323
GLFW_KEY_KP_4 = 324
GLFW_KEY_KP_5 = 325
GLFW_KEY_KP_6 = 326
GLFW_KEY_KP_7 = 327
GLFW_KEY_KP_8 = 328
GLFW_KEY_KP_9 = 329
GLFW_KEY_KP_DECIMAL = 330
GLFW_KEY_KP_DIVIDE = 331
GLFW_KEY_KP_MULTIPLY = 332
GLFW_KEY_KP_SUBTRACT = 333
GLFW_KEY_KP_ADD = 334
GLFW_KEY_KP_ENTER = 335
GLFW_KEY_KP_EQUAL = 336
GLFW_KEY_LEFT_SHIFT = 340
GLFW_KEY_LEFT_CONTROL = 341
GLFW_KEY_LEFT_ALT = 342
GLFW_KEY_LEFT_SUPER = 343
GLFW_KEY_RIGHT_SHIFT = 344
GLFW_KEY_RIGHT_CONTROL = 345
GLFW_KEY_RIGHT_ALT = 346
GLFW_KEY_RIGHT_SUPER = 347
GLFW_KEY_MENU = 348
GLFW_KEY_LAST = 348
GLFW_MOD_SHIFT = 0x0001
GLFW_MOD_CONTROL = 0x0002
GLFW_MOD_ALT = 0x0004
GLFW_MOD_SUPER = 0x0008
GLFW_MOUSE_BUTTON_1 = 0
GLFW_MOUSE_BUTTON_2 = 1
GLFW_MOUSE_BUTTON_3 = 2
GLFW_MOUSE_BUTTON_4 = 3
GLFW_MOUSE_BUTTON_5 = 4
GLFW_MOUSE_BUTTON_6 = 5
GLFW_MOUSE_BUTTON_7 = 6
GLFW_MOUSE_BUTTON_8 = 7
GLFW_MOUSE_BUTTON_LAST = 7
GLFW_MOUSE_BUTTON_LEFT = 0
GLFW_MOUSE_BUTTON_RIGHT = 1
GLFW_MOUSE_BUTTON_MIDDLE = 2
GLFW_JOYSTICK_1 = 0
GLFW_JOYSTICK_2 = 1
GLFW_JOYSTICK_3 = 2
GLFW_JOYSTICK_4 = 3
GLFW_JOYSTICK_5 = 4
GLFW_JOYSTICK_6 = 5
GLFW_JOYSTICK_7 = 6
GLFW_JOYSTICK_8 = 7
GLFW_JOYSTICK_9 = 8
GLFW_JOYSTICK_10 = 9
GLFW_JOYSTICK_11 = 10
GLFW_JOYSTICK_12 = 11
GLFW_JOYSTICK_13 = 12
GLFW_JOYSTICK_14 = 13
GLFW_JOYSTICK_15 = 14
GLFW_JOYSTICK_16 = 15
GLFW_JOYSTICK_LAST = 15
GLFW_NOT_INITIALIZED = 0x00010001
GLFW_NO_CURRENT_CONTEXT = 0x00010002
GLFW_INVALID_ENUM = 0x00010003
GLFW_INVALID_VALUE = 0x00010004
GLFW_OUT_OF_MEMORY = 0x00010005
GLFW_API_UNAVAILABLE = 0x00010006
GLFW_VERSION_UNAVAILABLE = 0x00010007
GLFW_PLATFORM_ERROR = 0x00010008
GLFW_FORMAT_UNAVAILABLE = 0x00010009
GLFW_FOCUSED = 0x00020001
GLFW_ICONIFIED = 0x00020002
GLFW_RESIZABLE = 0x00020003
GLFW_VISIBLE = 0x00020004
GLFW_DECORATED = 0x00020005
GLFW_RED_BITS = 0x00021001
GLFW_GREEN_BITS = 0x00021002
GLFW_BLUE_BITS = 0x00021003
GLFW_ALPHA_BITS = 0x00021004
GLFW_DEPTH_BITS = 0x00021005
GLFW_STENCIL_BITS = 0x00021006
GLFW_ACCUM_RED_BITS = 0x00021007
GLFW_ACCUM_GREEN_BITS = 0x00021008
GLFW_ACCUM_BLUE_BITS = 0x00021009
GLFW_ACCUM_ALPHA_BITS = 0x0002100A
GLFW_AUX_BUFFERS = 0x0002100B
GLFW_STEREO = 0x0002100C
GLFW_SAMPLES = 0x0002100D
GLFW_SRGB_CAPABLE = 0x0002100E
GLFW_REFRESH_RATE = 0x0002100F
GLFW_CLIENT_API = 0x00022001
GLFW_CONTEXT_VERSION_MAJOR = 0x00022002
GLFW_CONTEXT_VERSION_MINOR = 0x00022003
GLFW_CONTEXT_REVISION = 0x00022004
GLFW_CONTEXT_ROBUSTNESS = 0x00022005
GLFW_OPENGL_FORWARD_COMPAT = 0x00022006
GLFW_OPENGL_DEBUG_CONTEXT = 0x00022007
GLFW_OPENGL_PROFILE = 0x00022008
GLFW_OPENGL_API = 0x00030001
GLFW_OPENGL_ES_API = 0x00030002
GLFW_NO_ROBUSTNESS = 0
GLFW_NO_RESET_NOTIFICATION = 0x00031001
GLFW_LOSE_CONTEXT_ON_RESET = 0x00031002
GLFW_OPENGL_ANY_PROFILE = 0
GLFW_OPENGL_CORE_PROFILE = 0x00032001
GLFW_OPENGL_COMPAT_PROFILE = 0x00032002
GLFW_CURSOR = 0x00033001
GLFW_STICKY_KEYS = 0x00033002
GLFW_STICKY_MOUSE_BUTTONS = 0x00033003
GLFW_CURSOR_NORMAL = 0x00034001
GLFW_CURSOR_HIDDEN = 0x00034002
GLFW_CURSOR_DISABLED = 0x00034003
GLFW_CONNECTED = 0x00040001
GLFW_DISCONNECTED = 0x00040002


## TYPES
GLFWglproc = ctypes.CFUNCTYPE(None, )

class GLFWmonitor(ctypes.Structure):
	_fields_ = ()

class GLFWwindow(ctypes.Structure):
	_fields_ = ()

GLFWerrorfun = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)

GLFWwindowposfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)

GLFWwindowsizefun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)

GLFWwindowclosefun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow))

GLFWwindowrefreshfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow))

GLFWwindowfocusfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int)

GLFWwindowiconifyfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int)

GLFWframebuffersizefun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)

GLFWmousebuttonfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int, ctypes.c_int)

GLFWcursorposfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_double, ctypes.c_double)

GLFWcursorenterfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int)

GLFWscrollfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_double, ctypes.c_double)

GLFWkeyfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

GLFWcharfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow), ctypes.c_uint)

GLFWmonitorfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWmonitor), ctypes.c_int)

class GLFWvidmode(ctypes.Structure):
	_fields_ = (
		('width', ctypes.c_int),
		('height', ctypes.c_int),
		('redBits', ctypes.c_int),
		('greenBits', ctypes.c_int),
		('blueBits', ctypes.c_int),
		('refreshRate', ctypes.c_int),
	)

class GLFWgammaramp(ctypes.Structure):
	_fields_ = (
		('red', ctypes.POINTER(ctypes.c_ushort)),
		('green', ctypes.POINTER(ctypes.c_ushort)),
		('blue', ctypes.POINTER(ctypes.c_ushort)),
		('size', ctypes.c_uint),
	)


## FUNCTIONS
glfwInit = glfwLib.glfwInit
glfwInit.argtypes = ()
glfwInit.restype = ctypes.c_int

glfwTerminate = glfwLib.glfwTerminate
glfwTerminate.argtypes = ()
glfwTerminate.restype = None

glfwGetVersion = glfwLib.glfwGetVersion
glfwGetVersion.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetVersion.restype = None

glfwGetVersionString = glfwLib.glfwGetVersionString
glfwGetVersionString.argtypes = ()
glfwGetVersionString.restype = ctypes.c_char_p

glfwSetErrorCallback = glfwLib.glfwSetErrorCallback
glfwSetErrorCallback.argtypes = (GLFWerrorfun, )
glfwSetErrorCallback.restype = GLFWerrorfun

glfwGetMonitors = glfwLib.glfwGetMonitors
glfwGetMonitors.argtypes = (ctypes.POINTER(ctypes.c_int), )
glfwGetMonitors.restype = ctypes.POINTER(ctypes.POINTER(GLFWmonitor))

glfwGetPrimaryMonitor = glfwLib.glfwGetPrimaryMonitor
glfwGetPrimaryMonitor.argtypes = ()
glfwGetPrimaryMonitor.restype = ctypes.POINTER(GLFWmonitor)

glfwGetMonitorPos = glfwLib.glfwGetMonitorPos
glfwGetMonitorPos.argtypes = (ctypes.POINTER(GLFWmonitor), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetMonitorPos.restype = None

glfwGetMonitorPhysicalSize = glfwLib.glfwGetMonitorPhysicalSize
glfwGetMonitorPhysicalSize.argtypes = (ctypes.POINTER(GLFWmonitor), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetMonitorPhysicalSize.restype = None

glfwGetMonitorName = glfwLib.glfwGetMonitorName
glfwGetMonitorName.argtypes = (ctypes.POINTER(GLFWmonitor), )
glfwGetMonitorName.restype = ctypes.c_char_p

glfwSetMonitorCallback = glfwLib.glfwSetMonitorCallback
glfwSetMonitorCallback.argtypes = (GLFWmonitorfun, )
glfwSetMonitorCallback.restype = GLFWmonitorfun

glfwGetVideoModes = glfwLib.glfwGetVideoModes
glfwGetVideoModes.argtypes = (ctypes.POINTER(GLFWmonitor), ctypes.POINTER(ctypes.c_int))
glfwGetVideoModes.restype = ctypes.POINTER(GLFWvidmode)

glfwGetVideoMode = glfwLib.glfwGetVideoMode
glfwGetVideoMode.argtypes = (ctypes.POINTER(GLFWmonitor), )
glfwGetVideoMode.restype = ctypes.POINTER(GLFWvidmode)

glfwSetGamma = glfwLib.glfwSetGamma
glfwSetGamma.argtypes = (ctypes.POINTER(GLFWmonitor), ctypes.c_float)
glfwSetGamma.restype = None

glfwGetGammaRamp = glfwLib.glfwGetGammaRamp
glfwGetGammaRamp.argtypes = (ctypes.POINTER(GLFWmonitor), )
glfwGetGammaRamp.restype = ctypes.POINTER(GLFWgammaramp)

glfwSetGammaRamp = glfwLib.glfwSetGammaRamp
glfwSetGammaRamp.argtypes = (ctypes.POINTER(GLFWmonitor), ctypes.POINTER(GLFWgammaramp))
glfwSetGammaRamp.restype = None

glfwDefaultWindowHints = glfwLib.glfwDefaultWindowHints
glfwDefaultWindowHints.argtypes = ()
glfwDefaultWindowHints.restype = None

glfwWindowHint = glfwLib.glfwWindowHint
glfwWindowHint.argtypes = (ctypes.c_int, ctypes.c_int)
glfwWindowHint.restype = None

glfwCreateWindow = glfwLib.glfwCreateWindow
glfwCreateWindow.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(GLFWmonitor), ctypes.POINTER(GLFWwindow))
glfwCreateWindow.restype = ctypes.POINTER(GLFWwindow)

glfwDestroyWindow = glfwLib.glfwDestroyWindow
glfwDestroyWindow.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwDestroyWindow.restype = None

glfwWindowShouldClose = glfwLib.glfwWindowShouldClose
glfwWindowShouldClose.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwWindowShouldClose.restype = ctypes.c_int

glfwSetWindowShouldClose = glfwLib.glfwSetWindowShouldClose
glfwSetWindowShouldClose.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int)
glfwSetWindowShouldClose.restype = None

glfwSetWindowTitle = glfwLib.glfwSetWindowTitle
glfwSetWindowTitle.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_char_p)
glfwSetWindowTitle.restype = None

glfwGetWindowPos = glfwLib.glfwGetWindowPos
glfwGetWindowPos.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetWindowPos.restype = None

glfwSetWindowPos = glfwLib.glfwSetWindowPos
glfwSetWindowPos.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)
glfwSetWindowPos.restype = None

glfwGetWindowSize = glfwLib.glfwGetWindowSize
glfwGetWindowSize.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetWindowSize.restype = None

glfwSetWindowSize = glfwLib.glfwSetWindowSize
glfwSetWindowSize.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)
glfwSetWindowSize.restype = None

glfwGetFramebufferSize = glfwLib.glfwGetFramebufferSize
glfwGetFramebufferSize.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
glfwGetFramebufferSize.restype = None

glfwIconifyWindow = glfwLib.glfwIconifyWindow
glfwIconifyWindow.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwIconifyWindow.restype = None

glfwRestoreWindow = glfwLib.glfwRestoreWindow
glfwRestoreWindow.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwRestoreWindow.restype = None

glfwShowWindow = glfwLib.glfwShowWindow
glfwShowWindow.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwShowWindow.restype = None

glfwHideWindow = glfwLib.glfwHideWindow
glfwHideWindow.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwHideWindow.restype = None

glfwGetWindowMonitor = glfwLib.glfwGetWindowMonitor
glfwGetWindowMonitor.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwGetWindowMonitor.restype = ctypes.POINTER(GLFWmonitor)

glfwGetWindowAttrib = glfwLib.glfwGetWindowAttrib
glfwGetWindowAttrib.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int)
glfwGetWindowAttrib.restype = ctypes.c_int

glfwSetWindowUserPointer = glfwLib.glfwSetWindowUserPointer
glfwSetWindowUserPointer.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_void_p)
glfwSetWindowUserPointer.restype = None

glfwGetWindowUserPointer = glfwLib.glfwGetWindowUserPointer
glfwGetWindowUserPointer.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwGetWindowUserPointer.restype = ctypes.c_void_p

glfwSetWindowPosCallback = glfwLib.glfwSetWindowPosCallback
glfwSetWindowPosCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowposfun)
glfwSetWindowPosCallback.restype = GLFWwindowposfun

glfwSetWindowSizeCallback = glfwLib.glfwSetWindowSizeCallback
glfwSetWindowSizeCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowsizefun)
glfwSetWindowSizeCallback.restype = GLFWwindowsizefun

glfwSetWindowCloseCallback = glfwLib.glfwSetWindowCloseCallback
glfwSetWindowCloseCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowclosefun)
glfwSetWindowCloseCallback.restype = GLFWwindowclosefun

glfwSetWindowRefreshCallback = glfwLib.glfwSetWindowRefreshCallback
glfwSetWindowRefreshCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowrefreshfun)
glfwSetWindowRefreshCallback.restype = GLFWwindowrefreshfun

glfwSetWindowFocusCallback = glfwLib.glfwSetWindowFocusCallback
glfwSetWindowFocusCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowfocusfun)
glfwSetWindowFocusCallback.restype = GLFWwindowfocusfun

glfwSetWindowIconifyCallback = glfwLib.glfwSetWindowIconifyCallback
glfwSetWindowIconifyCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWwindowiconifyfun)
glfwSetWindowIconifyCallback.restype = GLFWwindowiconifyfun

glfwSetFramebufferSizeCallback = glfwLib.glfwSetFramebufferSizeCallback
glfwSetFramebufferSizeCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWframebuffersizefun)
glfwSetFramebufferSizeCallback.restype = GLFWframebuffersizefun

glfwPollEvents = glfwLib.glfwPollEvents
glfwPollEvents.argtypes = ()
glfwPollEvents.restype = None

glfwWaitEvents = glfwLib.glfwWaitEvents
glfwWaitEvents.argtypes = ()
glfwWaitEvents.restype = None

glfwGetInputMode = glfwLib.glfwGetInputMode
glfwGetInputMode.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int)
glfwGetInputMode.restype = ctypes.c_int

glfwSetInputMode = glfwLib.glfwSetInputMode
glfwSetInputMode.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int, ctypes.c_int)
glfwSetInputMode.restype = None

glfwGetKey = glfwLib.glfwGetKey
glfwGetKey.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int)
glfwGetKey.restype = ctypes.c_int

glfwGetMouseButton = glfwLib.glfwGetMouseButton
glfwGetMouseButton.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_int)
glfwGetMouseButton.restype = ctypes.c_int

glfwGetCursorPos = glfwLib.glfwGetCursorPos
glfwGetCursorPos.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
glfwGetCursorPos.restype = None

glfwSetCursorPos = glfwLib.glfwSetCursorPos
glfwSetCursorPos.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_double, ctypes.c_double)
glfwSetCursorPos.restype = None

glfwSetKeyCallback = glfwLib.glfwSetKeyCallback
glfwSetKeyCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWkeyfun)
glfwSetKeyCallback.restype = GLFWkeyfun

glfwSetCharCallback = glfwLib.glfwSetCharCallback
glfwSetCharCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWcharfun)
glfwSetCharCallback.restype = GLFWcharfun

glfwSetMouseButtonCallback = glfwLib.glfwSetMouseButtonCallback
glfwSetMouseButtonCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWmousebuttonfun)
glfwSetMouseButtonCallback.restype = GLFWmousebuttonfun

glfwSetCursorPosCallback = glfwLib.glfwSetCursorPosCallback
glfwSetCursorPosCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWcursorposfun)
glfwSetCursorPosCallback.restype = GLFWcursorposfun

glfwSetCursorEnterCallback = glfwLib.glfwSetCursorEnterCallback
glfwSetCursorEnterCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWcursorenterfun)
glfwSetCursorEnterCallback.restype = GLFWcursorenterfun

glfwSetScrollCallback = glfwLib.glfwSetScrollCallback
glfwSetScrollCallback.argtypes = (ctypes.POINTER(GLFWwindow), GLFWscrollfun)
glfwSetScrollCallback.restype = GLFWscrollfun

glfwJoystickPresent = glfwLib.glfwJoystickPresent
glfwJoystickPresent.argtypes = (ctypes.c_int, )
glfwJoystickPresent.restype = ctypes.c_int

glfwGetJoystickAxes = glfwLib.glfwGetJoystickAxes
glfwGetJoystickAxes.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))
glfwGetJoystickAxes.restype = ctypes.POINTER(ctypes.c_float)

glfwGetJoystickButtons = glfwLib.glfwGetJoystickButtons
glfwGetJoystickButtons.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))
glfwGetJoystickButtons.restype = ctypes.POINTER(ctypes.c_ubyte)

glfwGetJoystickName = glfwLib.glfwGetJoystickName
glfwGetJoystickName.argtypes = (ctypes.c_int, )
glfwGetJoystickName.restype = ctypes.c_char_p

glfwSetClipboardString = glfwLib.glfwSetClipboardString
glfwSetClipboardString.argtypes = (ctypes.POINTER(GLFWwindow), ctypes.c_char_p)
glfwSetClipboardString.restype = None

glfwGetClipboardString = glfwLib.glfwGetClipboardString
glfwGetClipboardString.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwGetClipboardString.restype = ctypes.c_char_p

glfwGetTime = glfwLib.glfwGetTime
glfwGetTime.argtypes = ()
glfwGetTime.restype = ctypes.c_double

glfwSetTime = glfwLib.glfwSetTime
glfwSetTime.argtypes = (ctypes.c_double, )
glfwSetTime.restype = None

glfwMakeContextCurrent = glfwLib.glfwMakeContextCurrent
glfwMakeContextCurrent.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwMakeContextCurrent.restype = None

glfwGetCurrentContext = glfwLib.glfwGetCurrentContext
glfwGetCurrentContext.argtypes = ()
glfwGetCurrentContext.restype = ctypes.POINTER(GLFWwindow)

glfwSwapBuffers = glfwLib.glfwSwapBuffers
glfwSwapBuffers.argtypes = (ctypes.POINTER(GLFWwindow), )
glfwSwapBuffers.restype = None

glfwSwapInterval = glfwLib.glfwSwapInterval
glfwSwapInterval.argtypes = (ctypes.c_int, )
glfwSwapInterval.restype = None

glfwExtensionSupported = glfwLib.glfwExtensionSupported
glfwExtensionSupported.argtypes = (ctypes.c_char_p, )
glfwExtensionSupported.restype = ctypes.c_int

glfwGetProcAddress = glfwLib.glfwGetProcAddress
glfwGetProcAddress.argtypes = (ctypes.c_char_p, )
glfwGetProcAddress.restype = GLFWglproc


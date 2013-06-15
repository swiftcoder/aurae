import libglfw
import ctypes


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


## Initialization
def glfwInit():
	'''
	This function initializes the GLFW library.

	Returns
		Raises an exception if an error occured.

	See Also
		glfwTerminate
	'''

	if not libglfw.glfwInit():
		raise Exception('Failed to initialize GLFW')


def glfwTerminate():
	'''
	This function destroys all remaining windows, frees any allocated resources and sets the library to an uninitialized state.

	See Also
		glfwInit
	'''

	libglfw.glfwTerminate()


## Versioning
def glfwGetVersion():
	'''
	This function retrieves the major, minor and revision numbers of the GLFW library.

	Returns
		(major, minor, revision) numbers

	See Also
		glfwGetVersionString
	'''

	major, minor, revision = ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
	libglfw.glfwGetVersion(major, minor, revision)
	return major.value, minor.value, revision.value


def glfwGetVersionString():
	'''
	This function returns a static string generated at compile-time according to which configuration macros were defined.

	Returns
		The GLFW version string

	See Also
		glfwGetVersion
	'''

	return libglfw.glfwGetVersionString()


## Error handling
def glfwSetErrorCallback(callback):
	'''
	This function sets the error callback, which is called with an error code and a human-readable description each time a GLFW error occurs.

	Args
		A python callable object or None to remove the currently set callback.
			callback(error_code, error_description)

		Error Codes
			GLFW_NOT_INITIALIZED  GLFW has not been initialized.
			GLFW_NO_CURRENT_CONTEXT  No context is current for this thread.
			GLFW_INVALID_ENUM  One of the enum parameters for the function was given an invalid enum.
			GLFW_INVALID_VALUE  One of the parameters for the function was given an invalid value.
			GLFW_OUT_OF_MEMORY  A memory allocation failed.
			GLFW_API_UNAVAILABLE  GLFW could not find support for the requested client API on the system.
			GLFW_VERSION_UNAVAILABLE  The requested client API version is not available.
			GLFW_PLATFORM_ERROR  A platform-specific error occurred that does not match any of the more specific categories.
			GLFW_FORMAT_UNAVAILABLE  The clipboard did not contain data in the requested format.
	'''

	libglfw.glfwSetErrorCallback(
		libglfw.GLFWerrorfun(callback)
	)


## Monitor handling
class glfwMonitor(object):
	def __init__(self, handle):
		self._handle = handle


def glfwGetMonitors():
	'''
	This function returns an array of monitors for all currently connected monitors.

	Returns
		An array of monitor handles, or None if an error occurred.

	See Also
		glfwGetPrimaryMonitor
	'''

	count = ctypes.c_int()
	monitors = libglfw.glfwGetMonitors(count)

	if not monitors:
		return None

	return [
		glfwMonitor(monitors[index].contents) for index in xrange(count.value)
	]


def glfwGetPrimaryMonitor():
	'''
	This function returns the primary monitor. This is usually the monitor where elements like the Windows task bar or the OS X menu bar is located.

	Returns
		The primary monitor, or None if an error occurred.

	See Also
		glfwGetMonitors
	'''

	monitor = libglfw.glfwGetPrimaryMonitor()

	if not monitor:
		return None

	return glfwMonitor(monitor.contents)


def glfwGetMonitorPos(monitor):
	'''
	This function returns the position, in screen coordinates, of the upper-left corner of the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		(x_position, y_position) integers
	'''

	x_position = ctypes.c_int()
	y_position = ctypes.c_int()
	libglfw.glfwGetMonitorPos(monitor._handle, x_position, y_position)

	return x_position.value, y_position.value


def glfwGetMonitorPhysicalSize(monitor):
	'''
	This function returns the size, in millimetres, of the display area of the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		(width, height) integers in millimetres
	'''

	width_mm = ctypes.c_int()
	height_mm = ctypes.c_int()
	libglfw.glfwGetMonitorPhysicalSize(monitor._handle, width_mm, height_mm)

	return width_mm.value, height_mm.value


def glfwGetMonitorName(monitor):
	'''
	This function returns a human-readable name, encoded as UTF-8, of the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		The UTF-8 encoded name of the monitor, or None if an error occurred.
	'''

	return libglfw.glfwGetMonitorName(monitor._handle)


def glfwSetMonitorCallback(callback):
	'''
	This function sets the monitor configuration callback, or removes the currently set callback. This is called when a monitor is connected to or disconnected from the system.

	Args
		A python callable object or None to remove the currently set callback.
			callback(monitor, event)

		Events
			GLFW_CONNECTED
			GLFW_DISCONNECTED
	'''

	libglfw.glfwSetMonitorCallback(
		libglfw.GLFWmonitorfun(lambda monitor, event: callback(glfwMonitor(monitor), event))
	)


def glfwGetVideoMode(monitor):
	'''
	This function returns the current video mode of the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		A dictionary with the fields: width, height, redBits, greenBits, blueBits, or None if an error occurred.

	See Also
		glfwGetVideoModes
	'''

	vidmode = libglfw.glfwGetVideoMode(monitor._handle)

	if not vidmode or vidmode.width == 0 and vidmode.height == 0:
		return None

	return {
		'width': vidmode.width,
		'height': vidmode.height,
		'redBits': vidmode.redBits,
		'greenBits': vidmode.greenBits,
		'blueBits': vidmode.blueBits,
	}


def glfwGetVideoModes(monitor):
	'''
	This function returns an array of all video modes supported by the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		An array of dictionaries with the fields: width, height, redBits, greenBits, blueBits, or None if an error occurred.

	See Also
		glfwGetVideoMode
	'''

	count = ctypes.c_int()
	vidmodes = libglfw.glfwGetVideoModes(monitor._handle, count)
	count = count.value

	if not count or not vidmodes:
		return None

	return [
		{
			'width': vidmodes[index].width,
			'height': vidmodes[index].height,
			'redBits': vidmodes[index].redBits,
			'greenBits': vidmodes[index].greenBits,
			'blueBits': vidmodes[index].blueBits,
		}
		for index in xrange(count)
	]


## Gamma ramp support
def glfwSetGamma(monitor, gamma):
	'''
	This function generates a gamma ramp from the specified exponent and then calls glfwSetGamma with it.

	Args
		The glfwMonitor object whose gamma ramp to set
		The desired exponent
	'''

	libglfw.glfwSetGamma(monitor._handle, gamma)


def glfwGetGammaRamp(monitor):
	'''
	This function retrieves the current gamma ramp of the specified monitor.

	Args
		The glfwMonitor object to query

	Returns
		A dictionary with three fields: red, green, blue
		Each field is an array of length GLFW_GAMMA_RAMP_SIZE
	'''

	gamma_ramp = libglfw.GLFWgammaramp()
	libglfw.glfwGetGammaRamp(monitor._handle, gamma_ramp)

	return {
		'red': list(gamma_ramp.red),
		'green': list(gamma_ramp.green),
		'blue': list(gamma_ramp.blue),
	}


def glfwSetGammaRamp(monitor, gammaramp):
	'''
	This function sets the current gamma ramp for the specified monitor.

	Args
		The glfwMonitor object whose gamma ramp to set
	'''

	gamma_ramp = libglfw.GLFWgammaramp()
	gamma_ramp.red = gamma_ramp._fields_[0][1](*gammaramp['red'])
	gamma_ramp.green = gamma_ramp._fields_[0][1](*gammaramp['green'])
	gamma_ramp.blue = gamma_ramp._fields_[0][1](*gammaramp['blue'])
	libglfw.glfwSetGammaRamp(monitor._handle, gamma_ramp)


## Window handling
class glfwWindow(object):
	def __init__(self, handle):
		self._handle = handle


def glfwDefaultWindowHints():
	'''
	This function resets all window hints to their default values.

	See Also
		glfwWindowHint
	'''

	libglfw.glfwDefaultWindowHints()


def glfwWindowHint(name, value):
	'''
	This function sets hints for the next call to glfwCreateWindow. The hints, once set, retain their values until changed by a call to glfwWindowHint or glfwDefaultWindowHints, or until the library is terminated with glfwTerminate.

	Args
		The window hint to set
		The new value of the window hint

		Hints
			http://www.glfw.org/docs/3.0/hints.html

	See Also
		glfwDefaultWindowHints
	'''

	libglfw.glfwWindowHint(name, value)


def glfwCreateWindow(width, height, title, monitor=None, share=None):
	'''
	This function creates a window and its associated context. Most of the options controlling how the window and its context should be created are specified via the glfwWindowHint function.

	Args
		The desired width, in pixels, of the window. This must be greater than zero.
		The desired height, in pixels, of the window. This must be greater than zero.
		The initial, UTF-8 encoded window title.
		The monitor to use for fullscreen mode, or None (default) to use windowed mode.
		The window whose context to share resources with, or None (default) to not share resources.

	Returns
		A glfwWindow object or None if an error occurred.

	See Also
		glfwDestroyWindow
	'''

	return glfwWindow(libglfw.glfwCreateWindow(width, height, title, monitor, share))


def glfwDestroyWindow(window):
	'''
	This function destroys the specified window and its context. On calling this function, no further callbacks will be called for that window.

	Args
		The glfwWindow object to destroy.

	See Also
		glfwCreateWindow
	'''

	libglfw.glfwDestroyWindow(window._handle)


def glfwWindowShouldClose(window):
	'''
	This function returns the value of the close flag of the specified window.

	Args
		The glfwWindow object to query.

	Returns
		The value of the close flag.
	'''

	return libglfw.glfwWindowShouldClose(window._handle)


def glfwSetWindowShouldClose(window, value):
	'''
	This function sets the value of the close flag of the specified window. This can be used to override the user's attempt to close the window, or to signal that it should be closed.

	Args
		The glfwWindow object whose value to change.
		The new value.
	'''

	return libglfw.glfwSetWindowShouldClose(window._handle, value)


def glfwSetWindowTitle(window, title):
	'''
	This function sets the window title, encoded as UTF-8, of the specified window.

	Args
		The glfwWindow object whose title to change.
		The UTF-8 encoded window title.
	'''

	return libglfw.glfwSetWindowTitle(window._handle, title)


def glfwGetWindowPos(window):
	'''
	This function retrieves the position, in screen coordinates, of the upper-left corner of the client area of the specified window.

	Args
		The glfwWindow object to query.

	Returns
		(x_coordinate, y_coordinate) of the upper-left corner of the client area.

	See Also
		glfwSetWindowPos
	'''

	x_coordinate = ctypes.c_int()
	y_coordinate = ctypes.c_int()

	libglfw.glfwGetWindowPos(window._handle, x_coordinate, y_coordinate)

	return x_coordinate.value, y_coordinate.value


def glfwSetWindowPos(window, x_coordinate, y_coordinate):
	'''
	This function sets the position, in screen coordinates, of the upper-left corner of the client area of the window.

	Args
		The glfwWindow object whose position to change.
		The x-coordinate of the upper-left corner of the client area.
		The y-coordinate of the upper-left corner of the client area.

	See Also
		glfwGetWindowPos
	'''

	libglfw.glfwSetWindowPos(window._handle, x_coordinate, y_coordinate)


def glfwGetWindowSize(window):
	'''
	This function retrieves the size, in pixels, of the client area of the specified window.

	Args
		The glfwWindow object to query.

	Returns
		(width, height) in pixels of the client area.

	See Also
		glfwSetWindowSize
	'''

	width = ctypes.c_int()
	height = ctypes.c_int()

	libglfw.glfwGetWindowSize(window._handle, width, height)

	return width.value, height.value


def glfwSetWindowSize(window, width, height):
	'''
	This function sets the size, in pixels, of the client area of the specified window.

	Args
		The glfwWindow object whose size to change.
		The desired width of the specified window.
		The desired height of the specified window.

	See Also
		glfwGetWindowSize
	'''

	libglfw.glfwSetWindowSize(window._handle, width, height)


def glfwIconifyWindow(window):
	'''
	This function iconifies/minimizes the specified window.

	Args
		The glfwWindow object to iconify.

	See Also
		glfwRestoreWindow
	'''

	libglfw.glfwIconifyWindow(window._handle)


def glfwRestoreWindow(window):
	'''
	This function restores the specified window.

	Args
		The glfwWindow object to restore.

	See Also
		glfwIconifyWindow
	'''

	libglfw.glfwRestoreWindow(window._handle)


def glfwShowWindow(window):
	'''
	This function makes the specified window visible.

	Args
		The glfwWindow object to make visible.

	See Also
		glfwHideWindow
	'''

	libglfw.glfwShowWindow(window._handle)


def glfwHideWindow(window):
	'''
	This function hides the specified window.

	Args
		The glfwWindow object to hide.

	See Also
		glfwShowWindow
	'''

	libglfw.glfwHideWindow(window._handle)


def glfwGetWindowMonitor(window):
	'''
	This function returns the handle of the monitor that the specified window is in fullscreen on.

	Args
		The glfwWindow object to query.

	Returns
		The glfwMonitor object, or None if the window is in windowed mode.
	'''

	monitor = libglfw.glfwGetWindowMonitor(window._handle)

	try:
		return glfwMonitor(monitor.contents)
	except ValueError:
		return None


def glfwGetWindowAttrib(window, attrib):
	'''
	This function returns an attribute of the specified window. There are many different properties, some related to the window and others to its context.

	Args
		The glfwWindow object to query.
		The parameter whose value to return.

	Returns
		The value of the parameter, or zero if an error occurred.
	'''

	return libglfw.glfwGetWindowAttrib(window._handle, attrib)


def glfwSetWindowUserPointer(window, pointer):
	'''
	This function sets the user-defined pointer of the specified window. The current value is retained until the window is destroyed. The initial value is None.

	Args
		The glfwWindow object whose pointer to set.
		The new value.

	See Also
		glfwGetWindowUserPointer
	'''

	libglfw.glfwSetWindowUserPointer(window._handle, pointer)


def glfwGetWindowUserPointer(window):
	'''
	This function returns the current value of the user-defined pointer of the specified window. The initial value is None.

	Args
		The glfwWindow object whose pointer to get.

	Returns
		???

	See Also
		glfwSetWindowUserPointer
	'''

	return libglfw.glfwGetWindowUserPointer(window._handle)


def glfwSetWindowPosCallback(window, callback):
	'''
	This function sets the position callback of the specified window, which is called when the window is moved.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, x_coordinate, y_coordinate)
	'''

	if callback is None:
		window._pos_callback = libglfw.GLFWwindowposfun()
	else:
		window._pos_callback = libglfw.GLFWwindowposfun(lambda win, x_coordinate, y_coordinate: callback(window, x_coordinate, y_coordinate))

	libglfw.glfwSetWindowPosCallback(
		window._handle,
		window._pos_callback,
	)


def glfwSetWindowSizeCallback(window, callback):
	'''
	This function sets the size callback of the specified window, which is called when the window is resized. The callback is provided with the size, in pixels, of the client area of the window.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, width, height)
	'''

	if callback is None:
		window._size_callback = libglfw.GLFWwindowsizefun()
	else:
		window._size_callback = libglfw.GLFWwindowsizefun(lambda win, width, height: callback(window, width, height))

	libglfw.glfwSetWindowSizeCallback(
		window._handle,
		window._size_callback,
	)


def glfwSetWindowCloseCallback(window, callback):
	'''
	This function sets the close callback of the specified window, which is called when the user attempts to close the window, for example by clicking the close widget in the title bar.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window)
	'''

	if callback is None:
		window._close_callback = libglfw.GLFWwindowclosefun()
	else:
		window._close_callback = libglfw.GLFWwindowclosefun(lambda win: callback(window))

	libglfw.glfwSetWindowCloseCallback(
		window._handle,
		window._close_callback,
	)


def glfwSetWindowRefreshCallback(window, callback):
	'''
	This function sets the refresh callback of the specified window, which is called when the client area of the window needs to be redrawn, for example if the window has been exposed after having been covered by another window.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window)
	'''

	if callback is None:
		window._fresh_callback = libglfw.GLFWwindowrefreshfun()
	else:
		window._fresh_callback = libglfw.GLFWwindowrefreshfun(lambda win: callback(window))

	libglfw.glfwSetWindowRefreshCallback(
		window._handle,
		window._fresh_callback,
	)


def glfwSetWindowFocusCallback(window, callback):
	'''
	This function sets the focus callback of the specified window, which is called when the window gains or loses focus.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, focused)

		Focused
			True if window has gained focus, False if window has lost focus.
	'''

	if callback is None:
		window._focus_callback = libglfw.GLFWwindowfocusfun()
	else:
		window._focus_callback = libglfw.GLFWwindowfocusfun(lambda win, focused: callback(window, focused))

	libglfw.glfwSetWindowFocusCallback(
		window._handle,
		window._focus_callback,
	)


def glfwSetWindowIconifyCallback(window, callback):
	'''
	This function sets the iconification callback of the specified window, which is called when the window is iconified or restored.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, iconified)

		Iconified
			True if the window was iconified, or False if it was restored.
	'''

	if callback is None:
		window._iconify_callback = libglfw.GLFWwindowiconifyfun()
	else:
		window._iconify_callback = libglfw.GLFWwindowiconifyfun(lambda win, iconified: callback(window, iconified))

	libglfw.glfwSetWindowIconifyCallback(
		window._handle,
		window._iconify_callback,
	)


def glfwPollEvents():
	'''
	This function processes only those events that have already been recevied and then returns immediately.

	See Also
		glfwWaitEvents
	'''

	libglfw.glfwPollEvents()


def glfwWaitEvents():
	'''
	This function blocks until at least one event has been recevied and then processes all received events before returning.

	See Also
		glfwPollEvents
	'''

	libglfw.glfwWaitEvents()


## Input handling
def glfwGetInputMode(window, mode):
	'''
	This function returns the value of the queried input mode.

	Args
		The glfwWindow object to query.
		One of GLFW_CURSOR_MODE, GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.

	Returns
		The value of the input mode.

	See Also
		glfwSetInputMode
	'''

	return libglfw.glfwGetInputMode(window._handle, mode)


def glfwSetInputMode(window, mode, value):
	'''
	This function sets the value of the selected input mode.

	Args
		The glfwWindow object whose mode to set.
		One of GLFW_CURSOR_MODE, GLFW_STICKY_KEYS or GLFW_STICKY_MOUSE_BUTTONS.
		The new value of the specified input mode.

		If mode is GLFW_CURSOR_MODE, the value must be one of the supported input modes:
			GLFW_CURSOR_NORMAL makes the cursor visible and behaving normally.
			GLFW_CURSOR_HIDDEN makes the cursor invisible when it is over the client area of the window.
			GLFW_CURSOR_CAPTURED makes the cursor invisible and unable to leave the window but unconstrained in terms of position.

		If mode is GLFW_STICKY_KEYS, the value must be either:
			True to enable sticky keys.
			False to disable it.
		If sticky keys are enabled, a key press will ensure that glfwGetKey returns GLFW_PRESS the next time it is called even if the key had been released before the call.

		If mode is GLFW_STICKY_MOUSE_BUTTONS, the value must be either:
			True to enable sticky mouse buttons.
			False to disable it.
		If sticky mouse buttons are enabled, a mouse button press will ensure that glfwGetMouseButton returns GLFW_PRESS the next time it is called even if the mouse button had been released before the call.

	See Also
		glfwGetInputMode
	'''

	libglfw.glfwSetInputMode(window._handle, mode, value)


def glfwGetKey(window, key):
	'''
	This function returns the last state reported for the specified key to the specified window.
	The returned state is one of GLFW_PRESS or GLFW_RELEASE. The higher-level state GLFW_REPEAT is only reported to the key callback.

	Args
		The glfwWindow object to query.
		The desired keyboard key.

	Returns
		One of GLFW_PRESS or GLFW_RELEASE.
	'''

	return libglfw.glfwGetKey(window._handle, key)


def glfwGetMouseButton(window, button):
	'''
	This function returns the last state reported for the specified mouse button to the specified window.
	If the GLFW_STICKY_MOUSE_BUTTONS input mode is enabled, this function returns GLFW_PRESS the first time you call this function after a mouse button has been pressed, even if the mouse button has already been released.

	Args
		The glfwWindow object to query.
		The desired mouse button.

	Returns
		One of GLFW_PRESS or GLFW_RELEASE.
	'''

	return libglfw.glfwGetMouseButton(window._handle, button)


def glfwGetCursorPos(window):
	'''
	This function returns the last reported position of the cursor to the specified window.

	Args
		The glfwWindow object to query.

	Returns
		(x_coordinate, y_coordinate) relative to the left top edge of the client area, or None.
	'''

	x_coordinate = ctypes.c_int()
	y_coordinate = ctypes.c_int()
	libglfw.glfwGetCursorPos(window._handle, x_coordinate, y_coordinate)

	return x_coordinate.value, y_coordinate.value


def glfwSetCursorPos(window, x_coordinate, y_coordinate):
	'''
	This function sets the position of the cursor. The specified window must be focused. If the window does not have focus when this function is called, it fails silently.

	Args
		The glfwWindow object to query.
		The desired x-coordinate, relative to the left edge of the client area, or None.
		The desired y-coordinate, relative to the top edge of the client area, or None.
	'''

	libglfw.glfwSetCursorPos(window._handle, x_coordinate, y_coordinate)


def glfwSetKeyCallback(window, callback):
	'''
	This function sets the key callback of the specific window, which is called when a key is pressed, repeated or released.
	The key functions deal with physical keys, with key tokens named after their use on the standard US keyboard layout. If you want to input text, use the character callback instead.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, key, action)

		Action
			One of GLFW_PRESS, GLFW_RELEASE or GLFW_REPEAT.
	'''

	if callback is None:
		window._key_callback = libglfw.GLFWkeyfun()
	else:
		window._key_callback = libglfw.GLFWkeyfun(lambda win, key, action: callback(window, key, action))

	libglfw.glfwSetKeyCallback(
		window._handle,
		window._key_callback,
	)


def glfwSetCharCallback(window, callback):
	'''
	This function sets the character callback of the specific window, which is called when a Unicode character is input.
	The character callback is intended for text input. If you want to know whether a specific key was pressed or released, use the key callback instead.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, character)

		Character
			The Unicode code point of the character.
	'''

	if callback is None:
		window._char_callback = libglfw.GLFWcharfun()
	else:
		window._char_callback = libglfw.GLFWcharfun(lambda win, character: callback(window, character))

	libglfw.glfwSetCharCallback(
		window._handle,
		window._char_callback,
	)


def glfwSetMouseButtonCallback(window, callback):
	'''
	This function sets the mouse button callback of the specified window, which is called when a mouse button is pressed or released.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, button, action)

		Action
			One of GLFW_PRESS or GLFW_RELEASE.
	'''

	if callback is None:
		window._button_callback = libglfw.GLFWmousebuttonfun()
	else:
		window._button_callback = libglfw.GLFWmousebuttonfun(lambda win, button, action: callback(window, button, action))

	libglfw.glfwSetMouseButtonCallback(
		window._handle,
		window._button_callback,
	)


def glfwSetCursorPosCallback(window, callback):
	'''
	This function sets the cursor position callback of the specified window, which is called when the cursor is moved.
	The callback is provided with the position relative to the upper-left corner of the client area of the window.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, x_coordinate, y_coordinate)
	'''

	if callback is None:
		window._cursorpos_callback = libglfw.GLFWcursorposfun()
	else:
		window._cursorpos_callback = libglfw.GLFWcursorposfun(lambda win, x_coordinate, y_coordinate: callback(window, x_coordinate, y_coordinate))

	libglfw.glfwSetCursorPosCallback(
		window._handle,
		window._cursorpos_callback,
	)


def glfwSetCursorEnterCallback(window, callback):
	'''
	This function sets the cursor boundary crossing callback of the specified window, which is called when the cursor enters or leaves the client area of the window.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, entered)

		Entered
			True if mouse has entered the window's client area, False if it has left.
	'''

	if callback is None:
		window._cursorenter_callback = libglfw.GLFWcursorenterfun()
	else:
		window._cursorenter_callback = libglfw.GLFWcursorenterfun(lambda win, entered: callback(window, entered))

	libglfw.glfwSetCursorEnterCallback(
		window._handle,
		window._cursorenter_callback,
	)


def glfwSetScrollCallback(window, callback):
	'''
	This function sets the scrolling callback of the specified window, which is called when scrolling a mouse wheel or a touchpad scrolling area.

	Args
		The glfwWindow object whose callback to set.
		A python callable object or None to remove the currently set callback.
			callback(window, x_position, y_position)
	'''

	if callback is None:
		window._scroll_callback = libglfw.GLFWscrollfun()
	else:
		window._scroll_callback = libglfw.GLFWscrollfun(lambda win, x_position, y_position: callback(window, x_position, y_position))

	libglfw.glfwSetScrollCallback(
		window._handle,
		window._scroll_callback,
	)


def glfwGetJoystickParam(joystick, parameter):
	'''
	This function returns a parameter of the specified joystick.

	Args
		The joystick to query.
		The parameter whose value to return.

	Returns
		The specified joystick's current value, or zero if the joystick is not present.
	'''

	return libglfw.glfwGetJoystickParam(joystick, parameter)


def glfwGetJoystickAxes(joystick, numaxes=None):
	'''
	This function returns the current positions of axes of the specified joystick.

	Args
		The joystick to query.
		The number of axes to poll, None for glfwGetJoystickParam(joystick, GLFW_AXES)

	Returns
		A list of values of the polled axes, or None if no axis is found.
	'''

	if numaxes is None:
		numaxes = glfwGetJoystickParam(joystick, libglfw.GLFW_AXES)

	if numaxes == 0:
		return None

	axes = (ctypes.c_float * numaxes)(*([0] * numaxes))
	count = libglfw.glfwGetJoystickAxes(joystick, axes, numaxes)

	return [
		axes[index] for index in xrange(count)
	]


def glfwGetJoystickButtons(joystick, numbuttons=None):
	'''
	This function returns the current state of buttons of the specified joystick.

	Args
		The joystick to query.
		The number of buttons to poll, None for glfwGetJoystickParam(joystick, GLFW_BUTTONS)

	Returns
		A list of values of the polled buttons, or None if no button is found.
	'''

	if numbuttons is None:
		numbuttons = glfwGetJoystickParam(joystick, libglfw.GLFW_BUTTONS)

	if numbuttons == 0:
		return None

	buttons = (ctypes.c_ubyte * numbuttons)(*([1] * numbuttons))
	count = libglfw.glfwGetJoystickButtons(joystick, buttons, numbuttons)

	return [
		buttons[index] for index in xrange(count)
	]


def glfwGetJoystickName(joystick):
	'''
	This function returns the name, encoded as UTF-8, of the specified joystick.

	Args
		The joystick to query.

	Returns
		The UTF-8 encoded name of the joystick, or None if the joystick is not present.
	'''

	return libglfw.glfwGetJoystickName(joystick)


## Clipboard
def glfwSetClipboardString(window, string):
	'''
	This function sets the system clipboard to the specified, UTF-8 encoded string. The string is copied before returning, so you don't have to retain it afterwards.

	Args
		The glfwWindow object that will own the clipboard contents.
		A UTF-8 encoded string.
	'''

	libglfw.glfwSetClipboardString(window._handle, string)


def glfwGetClipboardString(window):
	'''
	This function returns the contents of the system clipboard, if it contains or is convertible to a UTF-8 encoded string.

	Args
		The glfwWindow object that will request the clipboard contents.

	Returns
		The contents of the clipboard as a UTF-8 encoded string, or None if an error occurred.
	'''

	return libglfw.glfwGetClipboardString(window._handle)


## Time
def glfwGetTime():
	'''
	This function returns the value of the GLFW timer. Unless the timer has been set using glfwSetTime, the timer measures time elapsed since GLFW was initialized.

	Returns
		The current value, in seconds, or zero if an error occurred.
	'''

	return libglfw.glfwGetTime()


def glfwGetTime(time):
	'''
	This function sets the value of the GLFW timer. It then continues to count up from that value.
	'''

	libglfw.glfwSetTime(time)


## Context handling
def glfwMakeContextCurrent(window):
	'''
	This function makes the context of the specified window current on the calling thread.
	A context can only be made current on a single thread at a time and each thread can have only a single current context for a given client API (such as OpenGL or OpenGL ES).

	Args
		The glfwWindow object whose context to make current, or None to detach the current context.
	'''

	if not window:
		libglfw.glfwMakeContextCurrent()
	else:
		libglfw.glfwMakeContextCurrent(window._handle)


def glfwGetCurrentContext():
	'''
	This function returns the window whose context is current on the calling thread.

	Returns
		The glfwWindow object whose context is current, or None if no window's context is current.
	'''

	window = libglfw.glfwGetCurrentContext()

	if not window:
		return None

	return glfwWindow(window)


def glfwSwapBuffers(window):
	'''
	This function swaps the front and back buffers of the specified window. If the swap interval is greater than zero, the GPU driver waits the specified number of screen updates before swapping the buffers.

	Args
		The glfwWindow object whose buffers to swap.
	'''

	libglfw.glfwSwapBuffers(window._handle)


def glfwSwapInterval(interval):
	'''
	This function sets the swap interval for the current context, i.e. the number of screen updates to wait before swapping the buffers of a window and returning from glfwSwapBuffers.

	Args
		The minimum number of screen updates to wait for until the buffers are swapped by glfwSwapBuffers.
	'''

	libglfw.glfwSwapInterval(interval)


def glfwExtensionSupported(extension):
	'''
	This function returns whether the specified OpenGL or platform-specific context creation API extension is supported by the current context. For example, on Windows both the OpenGL and WGL extension strings are checked.

	Args
		The ASCII encoded name of the extension.

	Returns
		True if the extension is available, or False otherwise.
	'''

	return libglfw.glfwExtensionSupported(extension) == 1


def glfwGetProcAddress(procname):
	'''
	This function returns the address of the specified client API function, if it is supported by the current context.

	Args
		The ASCII encoded name of the function.

	Returns
		The address of the function, or None if the function is unavailable.
	'''

	return libglfw.glfwGetProcAddress(procname)

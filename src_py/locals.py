#    pygame - Python Game Library
#    Copyright (C) 2000-2003  Pete Shinners
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Library General Public
#    License as published by the Free Software Foundation; either
#    version 2 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Library General Public License for more details.
#
#    You should have received a copy of the GNU Library General Public
#    License along with this library; if not, write to the Free
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#    Pete Shinners
#    pete@shinners.org


"""Set of functions from PyGame that are handy to have in
the local namespace for your module"""

from pygame.constants import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
from pygame.rect import Rect
import pygame.color as color
Color = color.Color


__all__ = [
    'Rect',
    'Color',
    'ACTIVEEVENT',
    'ANYFORMAT',
    'APPACTIVE',
    'APPFOCUSMOUSE',
    'APPINPUTFOCUS',
    'ASYNCBLIT',
    'AUDIODEVICEADDED',
    'AUDIODEVICEREMOVED',
    'AUDIO_ALLOW_ANY_CHANGE',
    'AUDIO_ALLOW_CHANNELS_CHANGE',
    'AUDIO_ALLOW_FORMAT_CHANGE',
    'AUDIO_ALLOW_FREQUENCY_CHANGE',
    'AUDIO_S16',
    'AUDIO_S16LSB',
    'AUDIO_S16MSB',
    'AUDIO_S16SYS',
    'AUDIO_S8',
    'AUDIO_U16',
    'AUDIO_U16LSB',
    'AUDIO_U16MSB',
    'AUDIO_U16SYS',
    'AUDIO_U8',
    'BIG_ENDIAN',
    'BLENDMODE_ADD',
    'BLENDMODE_BLEND',
    'BLENDMODE_MOD',
    'BLENDMODE_NONE',
    'BLEND_ADD',
    'BLEND_MAX',
    'BLEND_MIN',
    'BLEND_MULT',
    'BLEND_PREMULTIPLIED',
    'BLEND_ALPHA_SDL2',
    'BLEND_RGBA_ADD',
    'BLEND_RGBA_MAX',
    'BLEND_RGBA_MIN',
    'BLEND_RGBA_MULT',
    'BLEND_RGBA_SUB',
    'BLEND_RGB_ADD',
    'BLEND_RGB_MAX',
    'BLEND_RGB_MIN',
    'BLEND_RGB_MULT',
    'BLEND_RGB_SUB',
    'BLEND_SUB',
    'BUTTON_LEFT',
    'BUTTON_MIDDLE',
    'BUTTON_RIGHT',
    'BUTTON_WHEELDOWN',
    'BUTTON_WHEELUP',
    'BUTTON_X1',
    'BUTTON_X2',
    'CONTROLLERAXISMOTION',
    'CONTROLLERBUTTONDOWN',
    'CONTROLLERBUTTONUP',
    'CONTROLLERDEVICEADDED',
    'CONTROLLERDEVICEREMAPPED',
    'CONTROLLERDEVICEREMOVED',
    'CONTROLLERDEVICEREMOVED',
    'JOYDEVICEADDED',
    'JOYDEVICEREMOVED',
    'CONTROLLER_AXIS_INVALID',
    'CONTROLLER_AXIS_LEFTX',
    'CONTROLLER_AXIS_LEFTY',
    'CONTROLLER_AXIS_MAX',
    'CONTROLLER_AXIS_RIGHTX',
    'CONTROLLER_AXIS_RIGHTY',
    'CONTROLLER_AXIS_TRIGGERLEFT',
    'CONTROLLER_AXIS_TRIGGERRIGHT',
    'CONTROLLER_BUTTON_A',
    'CONTROLLER_BUTTON_B',
    'CONTROLLER_BUTTON_BACK',
    'CONTROLLER_BUTTON_DPAD_DOWN',
    'CONTROLLER_BUTTON_DPAD_LEFT',
    'CONTROLLER_BUTTON_DPAD_RIGHT',
    'CONTROLLER_BUTTON_DPAD_UP',
    'CONTROLLER_BUTTON_GUIDE',
    'CONTROLLER_BUTTON_INVALID',
    'CONTROLLER_BUTTON_LEFTSHOULDER',
    'CONTROLLER_BUTTON_LEFTSTICK',
    'CONTROLLER_BUTTON_MAX',
    'CONTROLLER_BUTTON_RIGHTSHOULDER',
    'CONTROLLER_BUTTON_RIGHTSTICK',
    'CONTROLLER_BUTTON_START',
    'CONTROLLER_BUTTON_X',
    'CONTROLLER_BUTTON_Y',
    'DOUBLEBUF',
    'DROPBEGIN',
    'DROPCOMPLETE',
    'DROPFILE',
    'DROPTEXT',
    'FINGERDOWN',
    'FINGERMOTION',
    'FINGERUP',
    'FULLSCREEN',
    'GL_ACCELERATED_VISUAL',
    'GL_ACCUM_ALPHA_SIZE',
    'GL_ACCUM_BLUE_SIZE',
    'GL_ACCUM_GREEN_SIZE',
    'GL_ACCUM_RED_SIZE',
    'GL_ALPHA_SIZE',
    'GL_BLUE_SIZE',
    'GL_BUFFER_SIZE',
    'GL_CONTEXT_DEBUG_FLAG',
    'GL_CONTEXT_FLAGS',
    'GL_CONTEXT_FORWARD_COMPATIBLE_FLAG',
    'GL_CONTEXT_MAJOR_VERSION',
    'GL_CONTEXT_MINOR_VERSION',
    'GL_CONTEXT_PROFILE_COMPATIBILITY',
    'GL_CONTEXT_PROFILE_CORE',
    'GL_CONTEXT_PROFILE_ES',
    'GL_CONTEXT_PROFILE_MASK',
    'GL_CONTEXT_RELEASE_BEHAVIOR',
    'GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH',
    'GL_CONTEXT_RELEASE_BEHAVIOR_NONE',
    'GL_CONTEXT_RESET_ISOLATION_FLAG',
    'GL_CONTEXT_ROBUST_ACCESS_FLAG',
    'GL_DEPTH_SIZE',
    'GL_DOUBLEBUFFER',
    'GL_FRAMEBUFFER_SRGB_CAPABLE',
    'GL_GREEN_SIZE',
    'GL_MULTISAMPLEBUFFERS',
    'GL_MULTISAMPLESAMPLES',
    'GL_RED_SIZE',
    'GL_SHARE_WITH_CURRENT_CONTEXT',
    'GL_STENCIL_SIZE',
    'GL_STEREO',
    'GL_SWAP_CONTROL',
    'HAT_CENTERED',
    'HAT_DOWN',
    'HAT_LEFT',
    'HAT_LEFTDOWN',
    'HAT_LEFTUP',
    'HAT_RIGHT',
    'HAT_RIGHTDOWN',
    'HAT_RIGHTUP',
    'HAT_UP',
    'HIDDEN',
    'HWACCEL',
    'HWPALETTE',
    'HWSURFACE',
    'JOYAXISMOTION',
    'JOYBALLMOTION',
    'JOYBUTTONDOWN',
    'JOYBUTTONUP',
    'JOYHATMOTION',
    'KEYDOWN',
    'KEYUP',
    'KMOD_ALT',
    'KMOD_CAPS',
    'KMOD_CTRL',
    'KMOD_GUI',
    'KMOD_LALT',
    'KMOD_LCTRL',
    'KMOD_LGUI',
    'KMOD_LMETA',
    'KMOD_LSHIFT',
    'KMOD_META',
    'KMOD_MODE',
    'KMOD_NONE',
    'KMOD_NUM',
    'KMOD_RALT',
    'KMOD_RCTRL',
    'KMOD_RGUI',
    'KMOD_RMETA',
    'KMOD_RSHIFT',
    'KMOD_SHIFT',
    'KSCAN_0',
    'KSCAN_1',
    'KSCAN_2',
    'KSCAN_3',
    'KSCAN_4',
    'KSCAN_5',
    'KSCAN_6',
    'KSCAN_7',
    'KSCAN_8',
    'KSCAN_9',
    'KSCAN_A',
    'KSCAN_APOSTROPHE',
    'KSCAN_B',
    'KSCAN_BACKSLASH',
    'KSCAN_BACKSPACE',
    'KSCAN_BREAK',
    'KSCAN_C',
    'KSCAN_CAPSLOCK',
    'KSCAN_CLEAR',
    'KSCAN_COMMA',
    'KSCAN_CURRENCYSUBUNIT',
    'KSCAN_CURRENCYUNIT',
    'KSCAN_D',
    'KSCAN_DELETE',
    'KSCAN_DOWN',
    'KSCAN_E',
    'KSCAN_END',
    'KSCAN_EQUALS',
    'KSCAN_ESCAPE',
    'KSCAN_EURO',
    'KSCAN_F',
    'KSCAN_F1',
    'KSCAN_F10',
    'KSCAN_F11',
    'KSCAN_F12',
    'KSCAN_F13',
    'KSCAN_F14',
    'KSCAN_F15',
    'KSCAN_F2',
    'KSCAN_F3',
    'KSCAN_F4',
    'KSCAN_F5',
    'KSCAN_F6',
    'KSCAN_F7',
    'KSCAN_F8',
    'KSCAN_F9',
    'KSCAN_G',
    'KSCAN_GRAVE',
    'KSCAN_H',
    'KSCAN_HELP',
    'KSCAN_HOME',
    'KSCAN_I',
    'KSCAN_INSERT',
    'KSCAN_INTERNATIONAL1',
    'KSCAN_INTERNATIONAL2',
    'KSCAN_INTERNATIONAL3',
    'KSCAN_INTERNATIONAL4',
    'KSCAN_INTERNATIONAL5',
    'KSCAN_INTERNATIONAL6',
    'KSCAN_INTERNATIONAL7',
    'KSCAN_INTERNATIONAL8',
    'KSCAN_INTERNATIONAL9',
    'KSCAN_J',
    'KSCAN_K',
    'KSCAN_KP0',
    'KSCAN_KP1',
    'KSCAN_KP2',
    'KSCAN_KP3',
    'KSCAN_KP4',
    'KSCAN_KP5',
    'KSCAN_KP6',
    'KSCAN_KP7',
    'KSCAN_KP8',
    'KSCAN_KP9',
    'KSCAN_KP_0',
    'KSCAN_KP_1',
    'KSCAN_KP_2',
    'KSCAN_KP_3',
    'KSCAN_KP_4',
    'KSCAN_KP_5',
    'KSCAN_KP_6',
    'KSCAN_KP_7',
    'KSCAN_KP_8',
    'KSCAN_KP_9',
    'KSCAN_KP_DIVIDE',
    'KSCAN_KP_ENTER',
    'KSCAN_KP_EQUALS',
    'KSCAN_KP_MINUS',
    'KSCAN_KP_MULTIPLY',
    'KSCAN_KP_PERIOD',
    'KSCAN_KP_PLUS',
    'KSCAN_L',
    'KSCAN_LALT',
    'KSCAN_LANG1',
    'KSCAN_LANG2',
    'KSCAN_LANG3',
    'KSCAN_LANG4',
    'KSCAN_LANG5',
    'KSCAN_LANG6',
    'KSCAN_LANG7',
    'KSCAN_LANG8',
    'KSCAN_LANG9',
    'KSCAN_LCTRL',
    'KSCAN_LEFT',
    'KSCAN_LEFTBRACKET',
    'KSCAN_LGUI',
    'KSCAN_LMETA',
    'KSCAN_LSHIFT',
    'KSCAN_LSUPER',
    'KSCAN_M',
    'KSCAN_MENU',
    'KSCAN_MINUS',
    'KSCAN_MODE',
    'KSCAN_N',
    'KSCAN_NONUSBACKSLASH',
    'KSCAN_NONUSHASH',
    'KSCAN_NUMLOCK',
    'KSCAN_NUMLOCKCLEAR',
    'KSCAN_O',
    'KSCAN_P',
    'KSCAN_PAGEDOWN',
    'KSCAN_PAGEUP',
    'KSCAN_PAUSE',
    'KSCAN_PERIOD',
    'KSCAN_POWER',
    'KSCAN_PRINT',
    'KSCAN_PRINTSCREEN',
    'KSCAN_Q',
    'KSCAN_R',
    'KSCAN_RALT',
    'KSCAN_RCTRL',
    'KSCAN_RETURN',
    'KSCAN_RGUI',
    'KSCAN_RIGHT',
    'KSCAN_RIGHTBRACKET',
    'KSCAN_RMETA',
    'KSCAN_RSHIFT',
    'KSCAN_RSUPER',
    'KSCAN_S',
    'KSCAN_SCROLLLOCK',
    'KSCAN_SCROLLOCK',
    'KSCAN_SEMICOLON',
    'KSCAN_SLASH',
    'KSCAN_SPACE',
    'KSCAN_SYSREQ',
    'KSCAN_T',
    'KSCAN_TAB',
    'KSCAN_U',
    'KSCAN_UNKNOWN',
    'KSCAN_UP',
    'KSCAN_V',
    'KSCAN_W',
    'KSCAN_X',
    'KSCAN_Y',
    'KSCAN_Z',
    'K_0',
    'K_1',
    'K_2',
    'K_3',
    'K_4',
    'K_5',
    'K_6',
    'K_7',
    'K_8',
    'K_9',
    'K_AMPERSAND',
    'K_ASTERISK',
    'K_AT',
    'K_BACKQUOTE',
    'K_BACKSLASH',
    'K_BACKSPACE',
    'K_BREAK',
    'K_CAPSLOCK',
    'K_CARET',
    'K_CLEAR',
    'K_COLON',
    'K_COMMA',
    'K_CURRENCYSUBUNIT',
    'K_CURRENCYUNIT',
    'K_DELETE',
    'K_DOLLAR',
    'K_DOWN',
    'K_END',
    'K_EQUALS',
    'K_ESCAPE',
    'K_EURO',
    'K_EXCLAIM',
    'K_F1',
    'K_F10',
    'K_F11',
    'K_F12',
    'K_F13',
    'K_F14',
    'K_F15',
    'K_F2',
    'K_F3',
    'K_F4',
    'K_F5',
    'K_F6',
    'K_F7',
    'K_F8',
    'K_F9',
    'K_GREATER',
    'K_HASH',
    'K_HELP',
    'K_HOME',
    'K_INSERT',
    'K_KP0',
    'K_KP1',
    'K_KP2',
    'K_KP3',
    'K_KP4',
    'K_KP5',
    'K_KP6',
    'K_KP7',
    'K_KP8',
    'K_KP9',
    'K_KP_0',
    'K_KP_1',
    'K_KP_2',
    'K_KP_3',
    'K_KP_4',
    'K_KP_5',
    'K_KP_6',
    'K_KP_7',
    'K_KP_8',
    'K_KP_9',
    'K_KP_DIVIDE',
    'K_KP_ENTER',
    'K_KP_EQUALS',
    'K_KP_MINUS',
    'K_KP_MULTIPLY',
    'K_KP_PERIOD',
    'K_KP_PLUS',
    'K_LALT',
    'K_LCTRL',
    'K_LEFT',
    'K_LEFTBRACKET',
    'K_LEFTPAREN',
    'K_LESS',
    'K_LGUI',
    'K_LMETA',
    'K_LSHIFT',
    'K_LSUPER',
    'K_MENU',
    'K_MINUS',
    'K_MODE',
    'K_NUMLOCK',
    'K_NUMLOCKCLEAR',
    'K_PAGEDOWN',
    'K_PAGEUP',
    'K_PAUSE',
    'K_PERCENT',
    'K_PERIOD',
    'K_PLUS',
    'K_POWER',
    'K_PRINT',
    'K_PRINTSCREEN',
    'K_QUESTION',
    'K_QUOTE',
    'K_QUOTEDBL',
    'K_RALT',
    'K_RCTRL',
    'K_RETURN',
    'K_RGUI',
    'K_RIGHT',
    'K_RIGHTBRACKET',
    'K_RIGHTPAREN',
    'K_RMETA',
    'K_RSHIFT',
    'K_RSUPER',
    'K_SCROLLLOCK',
    'K_SCROLLOCK',
    'K_SEMICOLON',
    'K_SLASH',
    'K_SPACE',
    'K_SYSREQ',
    'K_TAB',
    'K_UNDERSCORE',
    'K_UNKNOWN',
    'K_UP',
    'K_a',
    'K_b',
    'K_c',
    'K_d',
    'K_e',
    'K_f',
    'K_g',
    'K_h',
    'K_i',
    'K_j',
    'K_k',
    'K_l',
    'K_m',
    'K_n',
    'K_o',
    'K_p',
    'K_q',
    'K_r',
    'K_s',
    'K_t',
    'K_u',
    'K_v',
    'K_w',
    'K_x',
    'K_y',
    'K_z',
    'LIL_ENDIAN',
    'MIDIIN',
    'MIDIOUT',
    'MOUSEBUTTONDOWN',
    'MOUSEBUTTONUP',
    'MOUSEMOTION',
    'MOUSEWHEEL',
    'MULTIGESTURE',
    'NOEVENT',
    'NOFRAME',
    'NUMEVENTS',
    'OPENGL',
    'OPENGLBLIT',
    'PREALLOC',
    'QUIT',
    'RESIZABLE',
    'RLEACCEL',
    'RLEACCELOK',
    'SCALED',
    'SCRAP_BMP',
    'SCRAP_CLIPBOARD',
    'SCRAP_PBM',
    'SCRAP_PPM',
    'SCRAP_SELECTION',
    'SCRAP_TEXT',
    'SHOWN',
    'SRCALPHA',
    'SRCCOLORKEY',
    'SWSURFACE',
    'SYSTEM_CURSOR_ARROW',
    'SYSTEM_CURSOR_CROSSHAIR',
    'SYSTEM_CURSOR_HAND',
    'SYSTEM_CURSOR_IBEAM',
    'SYSTEM_CURSOR_NO',
    'SYSTEM_CURSOR_SIZEALL',
    'SYSTEM_CURSOR_SIZENESW',
    'SYSTEM_CURSOR_SIZENS',
    'SYSTEM_CURSOR_SIZENWSE',
    'SYSTEM_CURSOR_SIZEWE',
    'SYSTEM_CURSOR_WAIT',
    'SYSTEM_CURSOR_WAITARROW',
    'SYSWMEVENT',
    'TEXTEDITING',
    'TEXTINPUT',
    'TIMER_RESOLUTION',
    'USEREVENT',
    'USEREVENT_DROPFILE',
    'VIDEOEXPOSE',
    'VIDEORESIZE',
    'WINDOWEVENT',
    'WINDOWEVENT_SHOWN',
    'WINDOWEVENT_HIDDEN',
    'WINDOWEVENT_EXPOSED',
    'WINDOWEVENT_MOVED',
    'WINDOWEVENT_RESIZED',
    'WINDOWEVENT_SIZE_CHANGED',
    'WINDOWEVENT_MINIMIZED',
    'WINDOWEVENT_MAXIMIZED',
    'WINDOWEVENT_RESTORED',
    'WINDOWEVENT_ENTER',
    'WINDOWEVENT_LEAVE',
    'WINDOWEVENT_FOCUS_GAINED',
    'WINDOWEVENT_FOCUS_LOST',
    'WINDOWEVENT_CLOSE',
    'WINDOWEVENT_TAKE_FOCUS',
    'WINDOWEVENT_HIT_TEST',
    'WINDOWSHOWN',
    'WINDOWHIDDEN',
    'WINDOWEXPOSED',
    'WINDOWMOVED',
    'WINDOWRESIZED',
    'WINDOWSIZECHANGED',
    'WINDOWMINIMIZED',
    'WINDOWMAXIMIZED',
    'WINDOWRESTORED',
    'WINDOWENTER',
    'WINDOWLEAVE',
    'WINDOWFOCUSGAINED',
    'WINDOWFOCUSLOST',
    'WINDOWCLOSE',
    'WINDOWTAKEFOCUS',
    'WINDOWHITTEST',

]

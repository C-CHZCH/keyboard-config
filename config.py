# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
#set timeout for the  _multipurpose_modmap 
define_timeout(0.5)
#the click is CapsLk -> F13,press is CapsLk->Left Ctrl
define_multipurpose_modmap(
    {Key.CAPSLOCK: [Key.F13, Key.LEFT_CTRL]}
)

#f13->Ctrl+Space
define_keymap(None, {
	K("f13"): K("C-space"),
	K("C-l"): K("right"),
	K("C-k"): K("up"),
	K("C-h"): K("left"),
	K("C-j"): K("down"),
	K("C-u"): K("home"),
	K("C-i"): K("end"),
})

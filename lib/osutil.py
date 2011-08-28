# Copyright (C) 2011 Michal Zielinski (michal@zielinscy.org.pl)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os
import sys

try:
    import android
except ImportError:
    android = None

is_android = bool(android)
is_desktop = not is_android

def init():
    if android:
        android.init()

def get_android_data(append=''):
    chdir = os.getcwd()
    if chdir.startswith('/sdcard/'):
        chdir = chdir[len('/sdcard/'):]
    if chdir.startswith('/mnt/sdcard/'):
        chdir = chdir[len('/mnt/sdcard/'):]
    if chdir.endswith('/'):
        chdir = chdir[:-1]
    id = chdir
    return '/data/data/%s/%s' % (id, append)

if is_android:
    logout = sys.stdout
    true_err = os.fdopen(2, 'w', 1)
    
    class MyStdout(object):
        def write(self, s):
            true_err.write(str(s))
            logout.write(str(s))
    
    sys.stdout = sys.stderr = MyStdout()
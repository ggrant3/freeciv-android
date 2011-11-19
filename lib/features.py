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

import sys

features = {}
appliers = {}
feature_types = {}
pernaments = {}

def get(name):
    return features[name]

def set_applier(name, func, type=str, default=None):
    appliers[name] = func
    feature_types[name] = type
    features[name] = default

def add_feature(name, default=None, type=str):
    appliers[name] = None
    features[name] = default
    feature_types[name] = type

def load_config():
    try:
        for line in open('features'):
            k, v = _parse_arg(line.rstrip())
            pernaments[k] = v
    except IOError:
        print 'feature config not read'

def parse_options():
    load_config()
    args = sys.argv[1:]
    unused = [sys.argv[0]]
    for arg in args:
        if arg.startswith('-f:'):
            arg = arg[len('-f:'):]
            _parse_arg(arg)
        else:
            unused.append(arg)
    sys.argv = unused

def _parse_arg(arg):
    if '=' in arg:
        key, val = arg.split('=', 1)
    else:
        key = arg
        val = 'true'
    set_feature(key, val)
    return key, val

def parse_type(t, v):
    if t == bool:
        if isinstance(v, bool):
            return v
        else:
            return v.lower() in ('true', 't', 'y', 'yes')
    elif t == str:
        return v
    elif t == int:
        return int(v)
    else:
        raise TypeError(t)

def set(name, value):
    if name not in appliers:
        raise ValueError('Unknown feature %r.' % name)
    features[name] = parse_type(feature_types[name], value)
    if appliers[name]:
        appliers[name](features[name])

def set_perm(name, value):
    assert '=' not in name and '\n' not in name and '\r' not in name
    
    set(name, value)
    pernaments[name] = value
    _store_pernaments()
    
    print 'changed pernament feature %s to %r' % (name, value)

def _store_pernaments():
    with open('features', 'w') as features_conf:
        features_conf.write('\n'.join([ '%s=%s' % (k, v) for k, v in pernaments.items() ]) + '\n')

set_feature = set
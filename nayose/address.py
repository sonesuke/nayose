import os
import pandas as pd
import re
from difflib import get_close_matches, SequenceMatcher

src_path = os.path.dirname(__file__)

_data = pd.read_feather(os.path.join(src_path, 'data/state.ft'))
states = list(_data['State'])

_data = pd.read_feather(os.path.join(src_path, 'data/city.ft'))
cities = list(_data['City'])

_data = pd.read_feather(os.path.join(src_path, 'data/address.ft'))
address = list(_data['Address'])


state_expression = '(' + '|'.join(states) + ')'
city_expression = '(' + '|'.join(cities) + ')'
state_regex = re.compile('^' + state_expression)
city_regex = re.compile('^' + city_expression)


def split_address(addr):
    m = state_regex.match(addr)
    if not m:
        return None, None, None
    state = m[1]
    m = city_regex.match(addr[len(state):])
    if not m:
        return state, None, None
    city = m[1]
    return state, city, addr[len(state) + len(city):]


def _complement(a, b):
    residual = a[len(b):]
    a = a[:len(b)]
    s = SequenceMatcher(None, a, b)

    res = ''
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'delete':
            pass
        elif tag == 'equal':
            res += a[i1:i2]
        elif tag == 'replace':
            res += b[j1:j2]
        elif tag == 'insert':
            res += b[j1:j2]
        else:
            pass
    return res + residual


def complement_address(addr):
    candidates = get_close_matches(addr, address)
    return _complement(addr, candidates[0]) if len(candidates) > 0 else addr

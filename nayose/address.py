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

_data = pd.read_feather(os.path.join(src_path, 'data/state_and_city.ft'))
states_and_cities = list(_data['StateAndCity'])


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


def _state_complement(_target):
    return _target if _target in states else None


def _city_complement(_target):
    matches = [c for c in states_and_cities if re.search(_target + "$", c)]
    return None if len(matches) == 0 else matches[0]


def _complement(a, b):
    if len(a) <= 10:
        res = _state_complement(a)
        if res is not None:
            return res
        res = _city_complement(a)
        if res is not None:
            return res

    s = SequenceMatcher(None, a, b)
    res = ''
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'equal':
            res += a[i1:i2]
        elif tag == 'replace':
            res += b[j1:j2]
        elif tag == 'insert':
            res += b[j1:j2]
        elif tag == 'delete' and len(b) == j1:
            res += a[i1:i2]
        else:
            pass
    return res


def complement_address(addr):
    candidates = get_close_matches(addr, address, n=1, cutoff=0.3)
    return _complement(addr, candidates[0]) if len(candidates) > 0 else addr

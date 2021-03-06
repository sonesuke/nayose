import os
import pandas as pd
import re
from difflib import get_close_matches, SequenceMatcher

_src_path = os.path.dirname(__file__)

_data = pd.read_feather(os.path.join(_src_path, 'data/state.ft'))
_states = list(_data['State'])

_data = pd.read_feather(os.path.join(_src_path, 'data/city.ft'))
_cities = list(_data['City'])

_data = pd.read_feather(os.path.join(_src_path, 'data/address.ft'))
address = list(_data['Address'])

_data = pd.read_feather(os.path.join(_src_path, 'data/state_and_city.ft'))
_states_and_cities = list(_data['StateAndCity'])

_state_expression = '(' + '|'.join(_states) + ')'
_city_expression = '(' + '|'.join(_cities) + ')'
_state_regex = re.compile('^' + _state_expression)
_city_regex = re.compile('^' + _city_expression)


def split_address(addr):
    m = _state_regex.match(addr)
    if not m:
        return None, None, None
    state = m[1]
    m = _city_regex.match(addr[len(state):])
    if not m:
        return state, None, None
    city = m[1]
    return state, city, addr[len(state) + len(city):]


def _state_complement(_target):
    return _target if _target in _states else None


def _city_complement(_target):
    matches = [c for c in _states_and_cities if re.search(_target + "$", c)]
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


def _normalize(address):
    m = re.search('^(.+?)([0-9０-９]+.*)', address)
    if m is not None:
        return m.group(1), m.group(2)
    return address, ''


def complement_address(addr):
    head, tail = _normalize(addr)
    candidates = get_close_matches(head, address, n=1, cutoff=0.3)
    complemented_head = _complement(head, candidates[0]) if len(candidates) > 0 else head
    return complemented_head + tail

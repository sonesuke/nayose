import os
import pandas as pd
import re

src_path = os.path.dirname(__file__)

_data = pd.read_feather(os.path.join(src_path, 'data/state.ft'))
states = list(_data['State'])

_data = pd.read_feather(os.path.join(src_path, 'data/city.ft'))
cities = list(_data['City'])

state_expression = '(' + '|'.join(states) + ')'
city_expression = '(' + '|'.join(cities) + ')'
state_regex = re.compile('^' + state_expression)
city_regex = re.compile('^' + city_expression)


def split_address(address):
    m = state_regex.match(address)
    if not m:
        return None, None, None
    state = m[1]
    m = city_regex.match(address[len(state):])
    if not m:
        return state, None, None
    city = m[1]
    return state, city, address[len(state) + len(city):]

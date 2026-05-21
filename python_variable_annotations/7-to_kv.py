#!/usr/bin/env python3
'''Module that defines a function to return a tuple'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and square of v as float."""
    return (k, float(v ** 2))

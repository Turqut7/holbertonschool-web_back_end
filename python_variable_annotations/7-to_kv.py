#!/usr/bin/env python3
"""Module for to_kv function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with string and square of number as float"""
    return (k, float(v * v))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2025/01/18 17:38
Desc: 首页-打板神器
https://api.duishu.com/lhbapp/zhangting/newDaban

"""

from datetime import datetime, timedelta

import pandas as pd
import requests

def _dxwsign(values:dict):
    sorted_keys = sorted(values.keys())
    headers = []
    for key in sorted_keys:
        value = values[key]
        headers.append(f"{key}:{value}")
    headers_str = "".join(headers)
    return
#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/10/02 23:28
# @Author  :Abner Wong
# @Software: PyCharm

from math import radians, cos, sin, asin, sqrt
import numpy as np


def get_max_index(la_ls, lo_ls, la_point, lo_point):
    max_index = 0
    for i in range(len(la_ls)):
        tmp_dis = havesine(la_ls[i], lo_ls[i], la_point, lo_point)
        if tmp_dis > max_dis:
            max_index = i
        else:
            continue
    return max_index


def havesine(lon1, lat1, lon2, lat2):
    """
    :param lon1: eg. 116.8066522020
    :param lat1: eg. 39.6057017009
    :param lon2: eg. 121.6406127537
    :param lat2: eg. 31.0152769039
    :return: diatance units: meters eg. 1050657.1943454074
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Earth radius
    return c * r * 1000


def get_max_distance(coordinate):
    """

    :param coordinate: list eg. ['39.60570,116.806','29.60570,126.806',]
    :return: diatance units: meters
    """
    coords = set(coordinate)
    if len(coords) < 2:
        return 0
    la_ls = list()
    lo_ls = list()
    for i in coords:
        la_ls.append(float(i.split(',')[0]))
        lo_ls.append(float(i.split(',')[1]))
        la_mean = np.array(la_ls).mean()
        lo_mean = np.array(lo_ls).mean()
        max_to_mean_index = get_max_index(la_ls, lo_ls, la_mean, lo_mean)
        max_to_max_index = get_max_index(la_ls, lo_ls, la_ls[max_to_mean_index], lo_ls[max_to_mean_index])
        max_distence = havesine(la_ls[max_to_max_index], lo_ls[max_to_max_index], la_ls[max_to_mean_index],
                                lo_ls[max_to_mean_index])
    return max_distence
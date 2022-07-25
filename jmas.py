#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import OrderedDict
from datetime import datetime
import json
import os
import requests
import sys

from const import JMA_AREA, JMA_ICON_BASEURL, JMA_COLORS, JMA_JSON_BASEURL, JMA_TELOPS


def format_date(dt):
    return datetime.strftime(
        datetime.strptime(
            dt,
            '%Y-%m-%dT%H:%M:%S%z'
        ),
        '%m/%d'
    )


def main():
    for i, area_id in enumerate(JMA_AREA.keys()):
        get_pref(area_id, i)


def get_pref(area_id, i):
    response = requests.get(JMA_JSON_BASEURL + area_id + '.json')

    if response.status_code != 200:
        sys.exit()

    data = json.loads(response.text, object_pairs_hook=OrderedDict)

    times = []

    area_publishing_office = ''
    for area in data:
        for ts in area['timeSeries']:
            if len(ts['timeDefines']) == 7:
                if i == 0 and len(times) == 0:
                    times = [format_date(n) for n in ts['timeDefines']]
                    print('times', ' '.join(times), '\n')

                area_name_wc = []
                weather_icons = []
                weather_telops = []

                # for area in ts['areas']:
                area = ts['areas'][0]

                if 'weatherCodes' in area:
                    area_name_wc = area['area']['name']
                    print('area_name_wc', area_name_wc)

                    weather_telops = [JMA_TELOPS[n] for n in area['weatherCodes']]
                    print('weather_telops', ' '.join(weather_telops))

                    weather_colors = ['({},{},{})'.format(*JMA_COLORS[n]) for n in area['weatherCodes']]
                    print('weather_colors', ' '.join(weather_colors))

                print('')
                # end for


if __name__ == '__main__':
    main()

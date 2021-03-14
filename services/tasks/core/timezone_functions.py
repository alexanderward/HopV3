import datetime

import pytz

from core.enums import DaysEnum


def tz_offset_to_hours(offset):
    return offset / 60


def tz_diff(timezone):
    tz_now = datetime.datetime.now(pytz.timezone(timezone))
    return (tz_now.utcoffset().total_seconds() / 60 / 60) * -1  # Calculates it away from UTC, -1 makes it to UTC


def convert_hours(hour_string, default='AM', timezone=None):
    assert timezone
    hour_string = hour_string.upper().replace('A.M.', 'AM').replace('P.M.', "PM")
    time_of_day = hour_string[-2:]
    if 'AM' not in time_of_day and 'PM' not in time_of_day:
        time_of_day = default
        hour_string += time_of_day
    if ':' in hour_string[:-2]:
        hour, minutes = hour_string[:-2].split(':')
    else:
        hour, minutes = hour_string[:-2], 0
    hour = float(hour)
    if time_of_day == 'AM' and hour == 12:
        hour = 0
    elif time_of_day == 'PM' and hour != 12:
        hour += 12
    if minutes:
        hour += float(minutes) / 60
    hour += tz_diff(timezone)
    if hour > 24:
        day_offset = 1
        hour -= 24
    elif hour < 0:
        day_offset = -1
        hour += 24
    else:
        day_offset = 0

    return hour, day_offset


def create_hour_dict(place_, record_):
    items_ = []
    for hour in record_['hours']:
        for hour_item in hour['hours_list']:
            if hour_item == 'Closed':
                items_.append(dict(place=place_,
                                   open_day=DaysEnum[hour['day'].upper()].value,
                                   open_hour=None,
                                   closed_day=DaysEnum[hour['day'].upper()].value,
                                   closed_hour=None,
                                   closed=True))
            elif hour_item == 'Open 24 hours':
                items_.append(dict(place=place_,
                                   open_day=DaysEnum[hour['day'].upper()].value,
                                   open_hour=None,
                                   closed_day=DaysEnum[hour['day'].upper()].value,
                                   closed_hour=None,
                                   open_all_day=True))
            else:
                open_, closed_ = hour_item.split('–')

                open_hour, open_day_offset = convert_hours(open_, default='AM', timezone=record_['timezone'])
                closed_hour, closed_day_offset = convert_hours(closed_, default='PM', timezone=record_['timezone'])

                open_day = DaysEnum[hour['day'].upper()].value
                closed_day = DaysEnum[hour['day'].upper()].value
                if open_day_offset != 0:
                    open_day += open_day_offset
                    closed_day += open_day_offset
                elif closed_day_offset != 0:
                    closed_day += closed_day_offset
                elif open_hour >= closed_hour:
                    closed_day += 1

                if open_day > 6:
                    open_day = 0
                if closed_day > 6:
                    closed_day = 0

                items_.append(dict(place=place_,
                                   open_day=open_day,
                                   open_hour=open_hour,
                                   closed_day=closed_day,
                                   closed_hour=closed_hour))
    return items_

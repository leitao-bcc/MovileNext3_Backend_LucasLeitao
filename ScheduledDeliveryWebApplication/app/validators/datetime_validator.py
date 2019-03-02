from datetime import datetime

WEEK_DAY = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
TIME_FORMAT = '%H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


def is_valid_week_day(var):
    if len(var) != 3:
        return False
    return var in WEEK_DAY


def is_valid_time_format(var):
    try:
        datetime.strptime(var, TIME_FORMAT)
    except ValueError:
        return False

    return True


def is_valid_datetime_format(var):
    try:
        datetime.strptime(var, DATETIME_FORMAT)
    except ValueError:
        return False

    return True

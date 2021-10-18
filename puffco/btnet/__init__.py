import struct


class Characteristics:
    COMMAND = "F9A98C15-C651-4F34-B656-D100BF580040"
    HEATER_TEMP = "F9A98C15-C651-4F34-B656-D100BF580025"
    DEVICE_NAME = "F9A98C15-C651-4F34-B656-D100BF58004D"
    OPERATING_STATE = "F9A98C15-C651-4F34-B656-D100BF580022"

    LANTERN_STATUS = "F9A98C15-C651-4F34-B656-D100BF58004A"
    LANTERN_COLOUR = "F9A98C15-C651-4F34-B656-D100BF580048"
    DABS_PER_DAY = "F9A98C15-C651-4F34-B656-D100BF58003B"
    TOTAL_DAB_COUNT = "F9A98C15-C651-4F34-B656-D100BF58002F"
    STEALTH_STATUS = "F9A98C15-C651-4F34-B656-D100BF580042"

    PROFILE_CURRENT = "F9A98C15-C651-4F34-B656-D100BF580041"
    PROFILE = "F9A98C15-C651-4F34-B656-D100BF580061"
    PROFILE_NAME = "F9A98C15-C651-4F34-B656-D100BF580062"
    PROFILE_PREHEAT_TEMP = "F9A98C15-C651-4F34-B656-D100BF580063"
    PROFILE_PREHEAT_TIME = "F9A98C15-C651-4F34-B656-D100BF580064"
    PROFILE_COLOUR = "F9A98C15-C651-4F34-B656-D100BF580065"

    BATTERY_SOC = 'F9A98C15-C651-4F34-B656-D100BF580020'


def parse(data):
    _struct = struct.unpack('f', data)
    remove = ['(', ',', ')']
    for chars in remove:
        _struct = str(_struct).replace(chars, "")
    return _struct
from color_codes import *


def color_codes_mapper():
    color_codes = []
    pair_number = 1
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            color_codes.append(list((pair_number, major_color, minor_color)))
            pair_number = pair_number + 1
    return color_codes


def print_reference_manual():
    color_codes = color_codes_mapper()
    for color_code in color_codes:
        print(color_code)

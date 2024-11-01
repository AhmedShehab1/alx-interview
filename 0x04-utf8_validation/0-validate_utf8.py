#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data: list) -> bool:
    """
    method that determines if a given data set represents
    a valid UTF-8 encoding
    Args:
        data (list): _description_

    Returns:
        bool: _description_
    """
    while True:
        if data:
            shifted_byte = data[0] >> 4
            if (shifted_byte) > 15:
                return False
            if (shifted_byte) < 8:
                data.pop(0)
                continue
            elif shifted_byte == 12 or shifted_byte == 13:
                try:
                    cont_byte = data[1] >> 4
                    if cont_byte <= 11 and cont_byte >= 8:
                        data.pop(1)
                    else:
                        return False
                    data.pop(0)
                    continue
                except Exception:
                    return False
            elif (shifted_byte) == 14:
                try:
                    for _ in range(2):
                        cont_byte = data[1] >> 4
                        if cont_byte <= 11 and cont_byte >= 8:
                            data.pop(1)
                        else:
                            return False
                    data.pop(0)
                except Exception:
                    return False
            elif (shifted_byte) == 15:
                try:
                    for _ in range(3):
                        cont_byte = data[1] >> 4
                        if cont_byte <= 11 and cont_byte >= 8:
                            data.pop(1)
                        else:
                            return False
                    data.pop(0)
                except Exception:
                    return False
            else:
                return False
        else:
            return True

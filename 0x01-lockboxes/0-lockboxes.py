#!/usr/bin/python3
import typing

"""
Technical Interview Preparation
"""


def canUnlockAll(boxes: typing.List[typing.List]) -> bool:
    """
    Method to determine if all boxes can be opened
    Args:
        boxes (typing.List[typing.List]): A list of lists containing boxes that
                                          contain keys for other boxes

    Returns:
        bool: True if all boxes can be opened else False
    """
    if len(boxes) == 1:
        return True
    boxes_dict = {0: boxes[0]}
    nextKey = 0
    currentKeys = [0]
    flag = True

    while boxes_dict:
        temp = 0
        for box in boxes_dict.get(nextKey):
            if box not in currentKeys and box in range(len(boxes)):
                if boxes[box]:
                    boxes_dict[box] = boxes[box]
                    if flag:
                        temp = box
                        flag = False
                currentKeys.append(box)
        if len(currentKeys) == len(boxes):
            break
        boxes_dict.pop(nextKey)
        nextKey = temp
        flag = True

    return len(currentKeys) == len(boxes)

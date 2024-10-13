#!/usr/bin/python3
"""
Technical Interview Preparation
"""
import typing
from collections import deque


def canUnlockAll(boxes: typing.List[typing.List]) -> bool:
    """
    Method to determine if all boxes can be opened
    Args:
        boxes (typing.List[typing.List]): A list of lists containing boxes that
                                          contain keys for other boxes

    Returns:
        bool: True if all boxes can be opened else False
    """
    opened_boxes = set([0])
    queue = deque([0])

    while queue:

        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)
        if len(opened_boxes) == len(boxes):
            break

    return len(opened_boxes) == len(boxes)

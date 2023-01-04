#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for Key_Box in boxes[key]:
            if Key_Box not in keys and Key_Box < len(boxes):
                keys.append(Key_Box)
    if len(keys) == len(boxes):
        return True
    return False

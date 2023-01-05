
#!/usr/bin/python3
"""
Task 0: Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    if boxes is None or len(boxes) is 0:
        return False

    status = ["T"]

    for box in range(1, len(boxes)):
        status.append("F")

    for box in range(0, len(boxes)):
        if (status[box] is "T" or box is 0):
            for key in boxes[box]:
                if int(key) < len(boxes) and status[key] is "F":
                    for k in boxes[key]:
                        if k < len(boxes):
                            status[k] = "T"
                if key < len(boxes):
                    status[key] = "T"

    if "F" in status:
        return False
    return True

#!/usr/bin/env python3

def canUnlockAll(boxes):
    # Set up a set to keep track of which boxes are open
    open_boxes = {0}

    # Set up a queue to hold the boxes that we need to check
    queue = [boxes[0]]

    # While there are boxes in the queue, check them
    while queue:
        box = queue.pop(0)
        for key in box:
            # If the key is a box that we haven't seen yet, add it to the open boxes and the queue
            if key not in open_boxes:
                open_boxes.add(key)
                queue.append(boxes[key])

    # Check if all boxes are open
    return len(open_boxes) == len(boxes)
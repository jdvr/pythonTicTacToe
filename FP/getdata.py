
def get_position_from_console():
    while True:
        row = raw_input("Type the row")
        if row < 3 or row > -1:
            break
    while True:
        col = raw_input("Type the col")
        if col < 3 or col > -1:
            break
    return [int(row), int(col)]



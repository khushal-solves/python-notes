def print_tables(low: int, high: int) -> None:
    """
    Print multiplication tables from `low` to `high`, side by side.
    Each table is printed from 1 to 10.
    """
    for i in range(1, 11):  # fixed 1–10
        row = []
        for j in range(low, high + 1):
            row.append(f"{j:2d} x {i:2d} = {i*j:4d}")
        print("\t".join(row))
    print()  # spacing after each block


# Controller logic (outside the function)
UPTO = 15       # Only printing till UPTO
COLUMNS = 4     # Number of tables on a row
START = 2       # Start tables from this value

for block_start in range(START, UPTO + 1, COLUMNS):
    block_end = min(block_start + COLUMNS - 1, UPTO)
    print_tables(block_start, block_end)


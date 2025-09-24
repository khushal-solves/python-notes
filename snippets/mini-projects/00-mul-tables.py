def table(low, high):
    """
    table(low, high): prints the table from low to high
    """
    
    for i in range(1,11):
        for j in range(low, high+1):
            # We are print table with specified format like : _5 x _1 = __5
            # to make the table neat
            print(f"{j:2d} x {i:2d} = {i*j:4d}", end="\t")
        print()
    print()

# Prinitng documentation for the table function
print(table.__doc__)

UPTO = 15       # Only printing till UPTO
COLUMN = 4      # Number of tables on a row
START = 2       # Start tables from this value
COUNT = (UPTO + COLUMN) // COLUMN

number = START
step = COLUMN - 1

for _ in range(1, COUNT+1):    
    if number > UPTO:
        break
    
    if number + step > UPTO:
        table(number, UPTO)
    else:
        # Printing in steps of COLUMN
        table(number, number+step)
    
    number += COLUMN

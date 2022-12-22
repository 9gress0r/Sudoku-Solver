from engine import get_table, print_tables_combined, Table
from copy import deepcopy

def main():
    raw_table = get_table()

    # Create a table object
    # NOTE: We have to copy the table because we are going to modify it, so we don't want to modify the original table

    solved = deepcopy(raw_table)

    # Solve the table
    solved.solve()

    # Print the tables
    print_tables_combined(raw_table, solved)

if __name__ == '__main__':
    main()

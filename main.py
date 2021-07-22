import output
from _input import getting_input
from TableClass import Table

raw = Table(getting_input())

table1 = output.make_table(raw(), False)

final = raw.solve()

table2 = output.make_table(final, True)

print(output.table_splitted(table1, table2))

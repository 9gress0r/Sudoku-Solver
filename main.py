import output
from TableClass import Table

raw = Table.get()

table1 = output.make_table(raw, False)

final = raw.solve()

table2 = output.make_table(final, True)

print(output.table_splitted(table1, table2))

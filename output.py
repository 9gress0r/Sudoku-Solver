def make_table(table, solved):
    """ 
    Creates a beautiful table
    """

    result = []

    header = '+---------FINAL---------+' if solved else '+----------RAW----------+'
    result.append(header)

    grid = table.table

    for row in range(9):
        first, second, third = ' '.join(map(str, grid[row][:3])), ' '.join(map(str, grid[row][3:6])), ' '.join(map(str, grid[row][6:]))
        result.append('| ' + first + ' | ' + second + ' | ' + third + ' |')
        if row in [2, 5]:
            result.append('| - - - + - - - + - - - |') 

    result.append(header)

    return result

def table_splitted(table1, table2):
	""" 
	Combines two tables
	"""

	result = [table1[line] + ' ' * 2 + table2[line] for line in range(len(table1))]

	return '\n'.join(result)

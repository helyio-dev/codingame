import sys

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    n = int(data[0])
    formulas = []
    for i in range(1, n + 1):
        formulas.append(data[i].split())

    cell_values = {}

    def get_arg_value(arg):
        if arg.startswith('$'):
            ref_index = int(arg[1:])
            return resolve_cell(ref_index)
        elif arg == '_':
            return 0
        else:
            return int(arg)

    def resolve_cell(index):
        if index in cell_values:
            return cell_values[index]

        operation, arg1, arg2 = formulas[index]
        result = 0

        val1 = get_arg_value(arg1)
        val2 = get_arg_value(arg2)

        if operation == 'VALUE':
            result = val1
        elif operation == 'ADD':
            result = val1 + val2
        elif operation == 'SUB':
            result = val1 - val2
        elif operation == 'MULT':
            result = val1 * val2

        cell_values[index] = result
        return result

    output = []
    for i in range(n):
        output.append(str(resolve_cell(i)))

    sys.stdout.write('\n'.join(output) + '\n')

solve()
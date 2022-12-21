from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)

operation_dict = {line.split(' ')[0][:-1]: ' '.join(line.split(' ')[1:]) for line in puzzle_input}


def evaluate_operation(variable):
    operation = operation_dict[variable]
    if type(operation_dict[variable]) == int:
        return operation_dict[variable]
    elif len(operation.split(' ')) == 1:
        operation_dict[variable] = int(operation_dict[variable])
        return operation_dict[variable]
    else:
        var1, operation, var2 = operation_dict[variable].split(' ')
        if operation == '+':
            operation_dict[variable] = evaluate_operation(var1) + evaluate_operation(var2)
            return operation_dict[variable]
        if operation == '-':
            operation_dict[variable] = evaluate_operation(var1) - evaluate_operation(var2)
            return operation_dict[variable]
        if operation == '*':
            operation_dict[variable] = evaluate_operation(var1) * evaluate_operation(var2)
            return operation_dict[variable]
        if operation == '/':
            operation_dict[variable] = evaluate_operation(var1) // evaluate_operation(var2)
            return operation_dict[variable]
        print(operation)
        raise


def reverse_operation(variable, value):
    if variable == 'humn':
        print(value)
        return
    var1, operation, var2 = operation_dict[variable].split(' ')
    try:
        var1 = evaluate_operation(var1)
        print(f"Finding {var2} using {var1}{operation}{var2}={value}")
        if operation == '==':
            return var2, var1
        if operation == '+':
            return var2, value - var1
        if operation == '-':
            return var2, var1 - value
        if operation == '*':
            return var2, value // var1
        if operation == '/':
            return var2, var1 // value
    except:
        var2 = evaluate_operation(var2)
        print(f"Finding {var1} using {var1}{operation}{var2}={value}")
        if operation == '==':
            return var1, var2
        if operation == '+':
            return var1, value - var2
        if operation == '-':
            return var1, value + var2
        if operation == '*':
            return var1, value // var2
        if operation == '/':
            return var1, var2 * value


print("Part 1: ", evaluate_operation('root'))

# Part 2:
operation_dict = {line.split(' ')[0][:-1]: ' '.join(line.split(' ')[1:]) for line in puzzle_input}
del operation_dict['humn']
# Make it as far as we can:
try:
    evaluate_operation(operation_dict['root'])
except:
    pass

operation_dict['root'] = operation_dict['root'].replace(' + ', ' == ')
variable = 'root'
value = 1
while variable != 'humn':
    variable, value = reverse_operation(variable, value)
print(value)

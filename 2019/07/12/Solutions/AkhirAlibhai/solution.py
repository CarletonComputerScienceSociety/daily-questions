def evaluate_equation_process_add_sub(operation):
    return (operation == '+' or operation == '-')


def evaluate_equation_process(equation, return_on_first_found):
    operators = {'/': (lambda a, b: a / b),
                 '*': (lambda a, b: a * b),
                 '+': (lambda a, b: a + b),
                 '-': (lambda a, b: a - b)
                 }

    curr_operator = None
    answer = None
    right_section = None
    keep_right_section = False

    x = 0
    while x < len(equation):
        if equation[x] == '(':
            my_return = evaluate_equation_process(equation[x + 1:], False)
            x += my_return[1] + 1

            if curr_operator:
                right_section = my_return[0]
                answer = operators[curr_operator](answer, right_section)
                curr_operator = None
                right_section = None
            else:
                answer = my_return[0]
        elif equation[x] == ')':
            if right_section:
                answer = operators[curr_operator](answer, right_section)
            return (answer, x)
        else:
            if right_section:
                if return_on_first_found:
                    answer = operators[curr_operator](answer, right_section)
                    return (answer, x)
                if curr_operator == '+' or curr_operator == '-':
                    if evaluate_equation_process_add_sub(equation[x]):
                        answer = operators[curr_operator](
                            answer, right_section)
                        curr_operator = None
                        right_section = None
                    else:
                        my_return = evaluate_equation_process(
                            equation[x - 1:], True)
                        right_section = my_return[0]
                        x += my_return[1] - 2
                        keep_right_section = True

                else:
                    answer = operators[curr_operator](answer, right_section)
                    curr_operator = None
                    right_section = None

            if equation[x] == '/':
                curr_operator = '/'
            elif equation[x] == '*':
                curr_operator = '*'
            elif equation[x] == '+':
                curr_operator = '+'
            elif equation[x] == '-':
                curr_operator = '-'
            elif not answer:
                answer = int(equation[x])
            else:
                if not keep_right_section:
                    right_section = int(equation[x])
                else:
                    keep_right_section = False
        x += 1

    if right_section:
        answer = operators[curr_operator](answer, right_section)
    return (answer, x)


def evaluate_equation(equation):
    equation = equation.replace('(', '( ').replace(')', ' )').split(' ')

    return evaluate_equation_process(equation, False)[0]
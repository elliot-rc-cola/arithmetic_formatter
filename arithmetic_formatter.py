def arithmetic_arranger(problems, show_answers=False):

    # error handling for lists longer than five equations
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # lists to break down the equations
    first_line = []
    second_line = []
    dash_line = []
    solutions = []
    
    # splitting the equations down to strings eg. from ['23 + 3'] to ['23', '+', '3']
    for problem in problems:
        equation = problem.split(' ')

        # handling other potential errors
        for i in equation:
            if i in ['+', '-']:
                continue
            elif i == '/' or i == '*':
                return "Error: Operator must be '+' or '-'."
            elif len(i) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            elif not i.isdigit():
                return 'Error: Numbers must only contain digits.'
            
        # now the errors are handled, we can start arranging the equations
        first_number = equation[0]
        operator = equation[1]
        second_number = equation[2]

        # Determine the width of the formatted problem
        width = max(len(first_number), len(second_number)) + 2
        
        # Format the problem
        top = first_number.rjust(width)
        bottom = operator + second_number.rjust(width - 1)
        
        
        first_line.append(top)
        second_line.append(bottom)
        dash_line.append('-' * width)
            
        # to show the correct answers for the equations
        if show_answers == True:
            # the operator needs to be extracted from the string
            op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}

            # formatting the answer
            answer = op[operator](int(first_number),int(second_number))
            solution = str(answer).rjust(width)

            solutions.append(solution)

    # joining the lists to create the final output    
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dash_line)
   
    # adjusting the output to show the answers only if show_answers is True
    if show_answers == False:
        return arranged_problems
    else:
        return arranged_problems + '\n' + '    '.join(solutions)
        
    return problems
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')


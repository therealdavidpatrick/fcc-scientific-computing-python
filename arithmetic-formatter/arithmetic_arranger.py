def arithmetic_arranger(problems, show_answers=False):

    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()

        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first_number), len(second_number)) + 2

        top_line = first_number.rjust(width)
        top_lines.append(top_line)

        bottom_line = operator + " " + second_number.rjust(width - 2)
        bottom_lines.append(bottom_line)

        dash_line = "-" * width
        dash_lines.append(dash_line)

        if show_answers:
            if operator == "+":
                answer = int(first_number) + int(second_number)
            else: 
                answer = int(first_number) - int(second_number)

            answer_line = str(answer).rjust(width)
            answer_lines.append(answer_line)

    first_line = "    ".join(top_lines)
    second_line = "    ".join(bottom_lines)
    third_line = "    ".join(dash_lines)
    answer_line = "    ".join(answer_lines)

    if show_answers:
        return first_line + "\n" + second_line + "\n" + third_line + "\n" + answer_line
        
    return first_line + "\n" + second_line + "\n" + third_line

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

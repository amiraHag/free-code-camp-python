def arithmetic_arranger(problem_string, addition_result=False):
    multiple_problem_space = ""
    arranged_problems_line1 = ""
    arranged_problems_line2 = ""
    arranged_problems_line3 = ""
    arranged_problems_line4 = ""
    count=0
    if isinstance(problem_string, str):
        problem_string = [problem_string]

    if len(problem_string) > 5:
        return "Error: Too many problems."


    for line in problem_string:
        assigment_operator = line.split()[1]
        if assigment_operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        first_number = line.split()[0]
        second_number = line.split()[2]
        max_len = len(second_number) if len(second_number) > len(first_number) else len(first_number)
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            first_number1 = int(line.split()[0])
            second_number1 = int(line.split()[2])
        except ValueError:
            return "Error: Numbers must only contain digits."
        if count > 0:
            multiple_problem_space = "    "
        arranged_problems_line1 += multiple_problem_space + f"{int(first_number)}".rjust(max_len+2)
        arranged_problems_line2 += multiple_problem_space + assigment_operator + " " + f"{int(second_number)}".rjust(max_len)
        arranged_problems_line3 += multiple_problem_space + "-"*int((max_len)+2)
        addition_value = int(first_number) + int(second_number) if assigment_operator == "+" else int(first_number) - int(second_number)
        arranged_problems_line4 += multiple_problem_space +f"{addition_value}".rjust(max_len+2," ")
        count+= 1

    arranged_problems = arranged_problems_line1 + "\n" + arranged_problems_line2 + "\n" + arranged_problems_line3 + ( "\n" + arranged_problems_line4 if addition_result else "")
    return arranged_problems

print(arithmetic_arranger(["44 + 8135", "123 + 49", "888 + 40", "653 + 87"]))
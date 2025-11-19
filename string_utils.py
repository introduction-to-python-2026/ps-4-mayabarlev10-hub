def split_at_first_digit(formula):
    first_digit_index = -1
    
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break
            

    
    if first_digit_index != -1:

        non_digit_part = formula[:first_digit_index]
        digit_and_rest_part = formula[first_digit_index:]
        return (non_digit_part, digit_and_rest_part) 
    else:

        non_digit_part = formula
        digit_and_rest_part = ""
        return (non_digit_part, digit_and_rest_part)
   


def split_before_each_uppercases(formula):

    parts_string = re.sub(r'(?<!^)(?=[A-Z])', r' ', formula)
    

    return parts_string.split(' ')

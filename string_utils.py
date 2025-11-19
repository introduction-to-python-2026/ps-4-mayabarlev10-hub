def split_at_first_digit(formula):
    word = ""
    num = ""
    for split in formula:
        if split.isdigit():
            num+=split
        else:
            word+=split
    if num == "":
        num = "1"
    num_int = int(num)
    return word , num_int


def split_before_each_uppercases(formula):
    word = ""
    new_formula = []
    word = formula [0]
    index = 1
    while index < len(formula):
        if formula[index].isupper() == False:
            word+=formula[index]
            index+=1
        else: 
            new_formula.append(word)
            word = formula[index]
            index+=1
    new_formula.append(word)
    return new_formula
            
            




 

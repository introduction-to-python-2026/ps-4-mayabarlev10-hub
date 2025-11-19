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
   


import re

def split_before_each_uppercases(formula):
    """
    מפצלת מחרוזת לרשימת מחרוזות, כאשר הפיצול מתבצע לפני כל אות רישית חדשה.
    הפיצול אינו מתבצע בתחילת המחרוזת.
    
    דוגמה: "IronOxide" -> ['Iron', 'Oxide']
    דוגמה: "someVariable" -> ['some', 'Variable']
    """
    
    # הדפוס: r'(?<!^)(?=[A-Z])'
    # (?<!^) : Negative Lookbehind - מוודא שהפיצול אינו מתבצע בתחילת המחרוזת.
    # (?=[A-Z]): Positive Lookahead - מחפש מיקום שבא אחריו אות רישית, ומחליף אותו ברווח.
    parts_string = re.sub(r'(?<!^)(?=[A-Z])', r' ', formula)
    
    # פיצול המחרוזת לפי הרווחים שהוספנו
    return parts_string.split(' ')

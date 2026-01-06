grade_map = {
    "A+": 4.3,
    "A" : 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B" : 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C" : 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D" : 1.0,
    "F" : 0.0,
}

def int_input(query_sentence: str):

    ii = input(query_sentence+"\n")
    
    is_input_valid = False
    
    while not is_input_valid:
        if not ii.isnumeric():
            ii = input("Please enter an number. \n")
        elif not int(ii) == float(ii):
            ii = input("Please enter an integer number. \n")
        else:
            return int(ii)

def grade_input(query_sentence: str):

    grade_map = {
        "A+": 4.3,
        "A" : 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B" : 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C" : 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D" : 1.0,
        "F" : 0.0,
    }

    ii = input(query_sentence+"\n")
    
    is_input_valid = False
    
    while not is_input_valid:
        if not ii in grade_map.keys(): 
            ii = input(
f"""
Please enter valid grade. \n
valid grades are: \n
{" ".join([g for g in grade_map.keys()])}\n"""
                        )
        else:
            return ii, grade_map[ii]

def GPA_calc(gctl: list):
    full_credit = sum([i[1] for i in gctl])
    grade_sum = sum([i[0]*i[1] for i in gctl])
    return "{:.1f}".format(grade_sum / full_credit)

grade_credit_tuple_list = []

print("++++++++++++++++++++++++++++++++")
sub_num = int_input("How many courses have you taken this sem.?")

for i in range(sub_num):
    print("++++++++++++++++++++++++++++++++")
    grade = grade_input(f"Your grade for course {i+1}?")[1]
    credit = int_input("Credit for this course?")
    grade_credit_tuple_list.append((grade,credit))

print(f"++++++++++++++++++++++++++++++++\nYour GPA for this semester is: {GPA_calc(grade_credit_tuple_list)}\n++++++++++++++++++++++++++++++++")

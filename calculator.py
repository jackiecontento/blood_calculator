def interface():
    print("My Program")
    while True:
        print("Options for you:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
            
   
def HDL_driver():
    # get input
    HDL_result = HDL_input_fun()
    # check if HDL is normal
    analyze_HDL_result = analyze_HDL_fun(HDL_result)
    # output
    output = output_HDL_analysis(HDL_result,analyze_HDL_result)
    
def HDL_input_fun():
    HDL_input = input("Enter the HDL test result: ")
    return int(HDL_input)

def analyze_HDL_fun(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif HDL_result < 40:
        return "Low"
    else:
        return "Borderline Low"

def output_HDL_analysis(HDL_result, analyze_HDL_result):
    print("The HDL result is {}".format(HDL_result))
    print("That is {}".format(analyze_HDL_result))

def LDL_driver():
    # get input
    LDL_result = LDL_input_fun()
    # check if HDL is normal
    analyze_LDL_result = analyze_LDL_fun(LDL_result)
    # output
    output = output_LDL_analysis(LDL_result,analyze_LDL_result)
    
def LDL_input_fun():
    LDL_input = input("Enter the LDL test result: ")
    return int(LDL_input)

def analyze_LDL_fun(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result <= 159:
        return "Borderline High"
    elif 160 <= LDL_result <= 189:
        return "High"
    else:
        return "Very High"

def output_LDL_analysis(LDL_result, analyze_LDL_result):
    print("The LDL result is {}".format(LDL_result))
    print("That is {}".format(analyze_LDL_result))


interface()


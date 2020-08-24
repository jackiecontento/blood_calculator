def interface():
    print("My Program")
    while True:
        print("Options for you:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
   
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


interface()


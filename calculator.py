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
    HDL_result = HLD_input_fun
    # check if HDL is normal
    check_HDL
    # output
    if check_HDL >= 60:
        print("HDL is normal")
    elif 40 <= check_HDL <60
        print("HDL is borderline low")
    else
        print("HDL is low")

def HDL_input_fun():
        HDL_input = input("Enter the HDL test result: ")
        return int(HDL_input)



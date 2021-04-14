#imports


#global variables


#functions
def print_menu():
    print("*** PyCalc ***")
    print("------------")
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[5] [x] Close')
    


#instructions

osc = ''
while(osc != 'x'):
    print_menu()

    osc = input("Please select an option: ")

    #this will break the loop. if i don't put this put put x, it will ask for more numbers. 
    if(osc == 'x'):
        break

    try:
        num1 = float(input("Provide Num 1: "))
        num2 = float(input("Provide Num 2: "))

        if (osc == '1'):
            res = num1 + num2    
    
        elif (osc == '2'):
            res = num1 - num2

        print(f"Result: {res}")

    except:
        print("**Error, verify and try again!")


print("Good bye!")


"""
               Hw:
                    -multiplication
                    -division:
                          NOTE: don't allow the user to divide by 0  9/0
                          SHOW AN ERROR


"""

    
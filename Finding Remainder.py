
def main():
    num1 = int(input("Your first number \t:"))
    num2 = int(input("your second number \t:"))

    a = int(num1/num2)
    print("                                               ", num2, end=' ')
    print([num1], end=' ')
    print(a)
    b = (num2*a)
    print("                                                  ", b)
    print("                                                  _____")
    c = num1-b
    print("                                                 ", c)
    repeat = input("Do you want to run again ?(y or n)")
    if repeat == "y":
        main()
    elif repeat == "n":
        exit()
main()

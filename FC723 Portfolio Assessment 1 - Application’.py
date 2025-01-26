 #creating a function for greatest common divisor 
def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

#creating the next function for least common multiple 
def find_lcm(a, b, gcd):
    return (a * b) // gcd


#checking the inputs if they are right to use
def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("add a positive integer")
        except ValueError:
            print("error try different number")


if __name__ == "__main__":
    
    #asking for two numbers input
    num1 = get_positive_integer("Enter the first positive integer: ")
    num2 = get_positive_integer("Enter the second positive integer: ")

    #calculating with functions
    gcd = find_gcd(num1, num2)
    lcm = find_lcm(num1, num2, gcd)

    # showing the results
    print(f"The GCD of {num1} and {num2} is: {gcd}")
    print(f"The LCM of {num1} and {num2} is: {lcm}")

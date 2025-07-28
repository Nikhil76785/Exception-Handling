try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is: ", result)

except ZeroDivisionError:
    print("Division by 0 is not alllowed.")

except ValueError:
    print("Please enter a numerical value.")

except NameError:
    print("Please check the variable name.")

except:
    print("Something went wrong!")

finally:
    print("I will execute no matter what happens.")
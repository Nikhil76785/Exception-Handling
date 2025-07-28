try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError as e:
    print("Exception: ", e)

print("I am outside the try block.")
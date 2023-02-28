try:
  num=int(input("Enter the numerator:"))
  den=int(input("Enter the denominator:"))
  result=num/den
  print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide the number by 0")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception as e:
    print(e)
    print("Some error occurs")
else:
    print("Result")
finally:
    print("This always executes")

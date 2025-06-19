class NegativeNumber(Exception):
    def __init__(self, message="Number should be greater than 0"):
        super().__init__(message)  

def check_number(number):
    if number < 0:
        raise NegativeNumber() 
    else:
        print("Valid number:", number)

try:
    num = int(input("Enter a number: "))
    check_number(num)
except NegativeNumber as e:
    print("Caught Custom Exception:", e)
except ValueError:
    print("Please enter a valid integer.")

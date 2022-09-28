# Exception Handling to get input a integer value

def main():
    x = get_int()
    print(f"x is {x}")



# This is a get_int function for Python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
            #print("X is not an Integer")

main()

# The while Loop

def main():

    total = 0
    while(total < 20):
        num = int(input("Please enter a number."))
        print(num)
        total = total + num
    print("Your total is " + str(total) + ".")

main()
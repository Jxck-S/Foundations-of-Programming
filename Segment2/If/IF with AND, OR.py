# Logical Operators

def main():

    a = 50

    print("Facts about a:")
    if( a > 10 and a < 75 ):
      print(" a is between 10 and 75 ")

    if( a < 10 or a > 75 ):
      print(" a less than 10 or greater than 75 ")

    if( not( a == 10 ) ):
      print(" a is not equal to 10 ")

main()
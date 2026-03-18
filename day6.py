
#functions

def add():
    n1= int(input("Enter first number: "))
    n2= int(input("Enter second number: "))
    sum= n1 + n2
    mul =n1*n2
    sub = n1-n2
    div = n1/n2
    return sum, mul, sub, div   
# returning multiple values as a tuple

result = add()
print("Result: ", result[2])

def profile(fname, lname):
    print("First name: ", fname)
    print("Last name: ", lname)

profile= profile("John", "Doe")

#default values
def city(name="nagpur"):
    print("City: ", name)

city()
city("Mumbai")


#solved hackerrank questions 1-6






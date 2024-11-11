def my_function():
    print("Hello From My Function!")

# calling function
my_function()

# arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("jftest", "the best")

# return value
def sum_two_numbers(a, b):
    return a + b

sum=sum_two_numbers(3, 2)
print("The sum is %d" %sum)

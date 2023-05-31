# Exceptions
# allows us to handle errors
# a try: block will allow us to do that with a except: block after
# Example of the try except which is like try-catch
#try:
    # some lines of code
#except <Error1>:
    # handle <Error1>
#except <Error2>:
    # handle <Error2>
#finally:
    # do something in case
# can catch all errors without the <Error) after the except
# can also place a else block that will run if there is no errors
# can also have a finally: block which will always run at the end 
# EOFError is a end of file error for example
# here is a code example of this in work
try:
    result = 2 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    result = 1

print(result)
# you can raise an error in your code intentionally by using the rais Exception
# here is an example of this
# does away with the red block of error message and just prints the error
try:
    raise Exception("An Error!")
except Exception as error:
    print(error)

# this also allows you to have a class of exceptions
class DogNotFoundException(Exception):
    print("Inside exception")
    pass # must use this when you have a method or function or class without code

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found")

# using the with function helps us with ease of programming
# allows more transparent code this will be examples of file stuff with the with function

# Example without the with function
#filename = '/Users/HP/test.txt'
#try:
    #file = open(filename, 'r')
    #content = file.read()
    #print(content)
#finally:
    #file.close()

# alternate way to do the above way with the with command
#filename = '/Users/HP/test.txt'
#with open(filename, 'r') as file:
    #content = file.read()
    #print(content)

class MyClass:
    static_var = 0

    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var

obj1 = MyClass()
print(obj1.instance_var) # Output: 1

obj2 = MyClass()
print(obj2.instance_var) # Output: 2

print(MyClass.static_var) # Output: 2

print("\n")
# Closure - Example 1
def outer(x):
    def inner(y):
        return x+y
    return inner

closure = outer(10)
# Now closure is a function that "remembers" the value of 'x'
result = closure(5)
print(result)

print("\n")
# Closure - Example 2
def callback_creator(prefix):
    def callback(message):
        print(prefix + ": " + message)
    return callback

callback1 = callback_creator("Info")
callback2 = callback_creator("Warning")

callback1("This is an information message")
callback2("This is a warning message")

print("\n")
# Decorator
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func() # Call the original function - hello()
        print("Something is happening after the function is called")
    return wrapper

# Applying the decorator to a function
@decorator
def hello():
    print("Hello!")

# Calling hte decorated function
hello()
print("\n")

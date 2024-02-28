import time # Time library
# Q1
def decorator_1(func): # Define  function
    def wrapper(): # Make wrapper
        start = time.time() # Begin the timer
        func() # Call onto decorator function
        end = time.time() # End timer
        time_taken = end - start # Calculate the result
        print("Start time: ", start)
        print("End time: ", end)
        print("Execution time: ", time_taken)
    return wrapper

@decorator_1
def timer(): # Define a function called timer
    num = 0 # Initialize int called num
    for i in range(100000000): # Loop many times
        num += i # Add i to num

timer() # Call onto decorated function


# Q2
def decorator_2(func):
    # Dictionairy to store cached results
    cache = {}
    # Inner function to perform memoization
    def memoized_func(*args):
        # Check if the arguements are already in cache
        if args in cache:
            # Return the cached result if avaliable
            return cache[args]
        else:
            # Compute the results using the decorated function
            result = func(*args)
            # Cache results for future use
            cache[args] = result
            # Return results
            return result
    # Return memoized function
    return memoized_func
# Create decorator
@decorator_2
# Create decorated function which adds 2 numbers
def add(a,b):
    result = a + b
    return result

print(add(1,5))
print(add(2,8))
print(add(5,10))
print(add(5,10))

# Q3
def decorator_31(func):
    def wrapper():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        func(username, password)
    return wrapper

@decorator_31
def UserCheck1(username, password):
        realUser = "Bob"
        realPass = "123"
        if username in realUser and password in realPass:
            print("You've logged in successfully")
        else:
            print("Password and or Username is incorrect")
        print("-" * 20)
UserCheck1()




# Q3
def decorator_32(func):
    realUser = "Bob"
    realPass = "123"
    def wrapper():
        RecievedUserInfo = func()  
        UserInfo = RecievedUserInfo.split()  
        Username, Password = UserInfo[0],UserInfo[1]
        #print ("User Info: ", x)
        print("Username: ", Username, ", Password: ", Password)
        if Username in realUser and Password in realPass:
            print("You've logged in succcessfully")
        else:
            print("Login Failed: Password and or Username is incorrect")
    return wrapper

@decorator_32
def UserCheck2():
         username = input("Enter your username: ")
         password = input("Enter your password: ")
         result = str(username + " " + password)
         return result

UserCheck2()
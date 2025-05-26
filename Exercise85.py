# Exercise 85: Generators in Python

# They generate values on th fly, rather than having to create
# and store the entire sequence in memory.
# Generators are special type of function that remenmbers its state and
# gives one value at a time, instead of giving all values at once

# It is used when you want to save memory. You want to generate 
# a sequence of values, but not storethem all in memory.


# Creating a Generator in Python
# In Python, you can create a generator by using the yield statement 
# in a function. The yiels statement returns a value from the generator 
# and suspends the execution of function unti next value is requested.
# Generators are henceforth lazy.

# Example 
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#or 
for j in gen:
    print(j)
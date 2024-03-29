print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6 
print(f"This should be five: {five}")

# Inside the function variables the variable is temporary. When you return it then it can be assigned to variable for later.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


# beans is a different name to the one in the secret_formula function, i.e. jelly_beans, as variables inside the function are temporary. 
# When you return the variable in the function then it can be assigned to a variable for later, I just made a new variable named beans to hold the return value.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string - for more info on placeholders and .format() check this link: https://www.w3schools.com/python/ref_string_format.asp#:~:text=The%20format()%20method%20formats,method%20returns%20the%20formatted%20string.
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string 
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10 

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string 
# uses *formula as there are multiple arguments that need to be unpacked for seceret_formula(start_point) i.e. beans, jars, crates.
print("We'd have {} beans, {} jars and {} crates.".format(*formula))

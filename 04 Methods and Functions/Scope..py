# varaible name getes something called namespace
# each namespace have its own visibility -
# Global, local, built-in, enclosing functions

x = 5 # global scope
def check():
    x = 10 # local scope
    return x

print(x) # is different from
print(check())

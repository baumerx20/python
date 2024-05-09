

def myRecA(a):
    def myRecB(b):
        return a + b
    return myRecB

my_var = myRecA(5)
add = my_var(5)
print(add)



    


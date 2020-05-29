

def is_convergent(function):
    """
    6.4b
    Takes in function as argument and returns true is the series is convergent. False is divergent. 
    """
    f = function
    def sum(f,terms:int):  # computing sum
        s = 0
        for i in range(1,terms):
            s += f(i)
        return s
    # limit definition check of convergence.
    for i in range(50,1000):
        if abs(sum(f,i) - sum(f, i*1000)) < 1*10**-2:
            return True
        else:
            continue
    return False
            
        

if __name__ == "__main__":
    ##print(write_encrypted("Z", 5))
    ##print(vig_cipher("cceefcceef", "aaaaaaaaaa"))
    def func(t):
        return 1/t**2
    print(is_convergent(func))

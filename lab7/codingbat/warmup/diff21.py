def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    else:
        return abs(n - 21)

##
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
##

##
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10
##

##
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10
##

##
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)
##

##
def not_string(s):
    if s.startswith("not"):
        return s
    else:
        return "not " + s
##

##
def missing_char(s, n):
    return s[:n] + s[n+1:]
##

def front_back(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]

def front3(s):
    front = s[:3]  
    return front * 3  

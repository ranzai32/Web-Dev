def cigar_party(cigars, is_weekend):
    return (40 <= cigars <= 60) or (is_weekend and cigars >= 40)

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90
    
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5  
    if speed <= 60:
        return 0 
    elif speed <= 80:
        return 1  
    else:
        return 2  

def sorta_sum(a, b):
    total = a + b
    if 10 <= total <= 19:
        return 20
    else:
        return total

def alarm_clock(day, vacation):
    if vacation:
        return "off" if day == 0 or day == 6 else "10:00"
    else:
        return "7:00" if day != 0 and day != 6 else "10:00"

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

def near_ten(num):
    return num % 10 == 0 or num % 10 == 1 or num % 10 == 9

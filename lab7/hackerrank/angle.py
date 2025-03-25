import math

def calculate_angle(a, b):
    angle_radians = math.atan(a / b)
    
    angle_degrees = math.degrees(angle_radians)
    
    return str(round(angle_degrees)) + "°"

if __name__ == "__main__":
    a = int(input()) 
    b = int(input())  
    
    result = calculate_angle(a, b)
    
    print(result)

def is_even(n):
    return n % 2 == 0
    


def grade(score):
    if score >= 90:  
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 60:
        return("C")
    else:
        return("D")
print(is_even(4))
print(grade(95))
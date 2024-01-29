# day 2/366 codewars

def even_or_odd(number):
    # 'Even' if number % 2 == 0 else 'Odd'
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(-12))
print(even_or_odd(-5))
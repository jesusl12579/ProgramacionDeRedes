#Actividad de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 3-Octubre-2024

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    # Check for invalid date
    md = days_in_month(year, month)
    if md is None or day < 1 or day > md:
        return None
    
    # Calculate days from previous months
    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)
    
    # Add days of the current month
    days += day
    return days

# Example usage
print(day_of_year(2000, 12, 31))  # This should return 366, since 2000 is a leap year

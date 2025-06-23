def cal_fahr(a):
    fahr = (a * (9/5)) + 32
    return fahr

def cal_cels(b):
    cels = (b - 32) * (5/9)
    return cels

k = 0

while k < 100:
    print("Convert Temperature, units in large case")
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Enter only a valid number")
        continue

    unit = str(input("Enter unit (C for Celsius, F for Fahrenheit): ")).strip().upper()

    if "F" == unit:
        output = cal_cels(value)
        print(f"Your value in Celsius is: {output:.2f} °C\n")

    elif "C" == unit:
        output = cal_fahr(value)
        print(f"Your value in Fahrenheit is: {output:.2f} °F\n")
    
    else:
        print("Enter units carefully (C or F)\n")
    
    k = k + 1
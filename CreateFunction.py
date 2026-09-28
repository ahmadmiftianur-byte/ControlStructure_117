#1Create a function that converts temperature from Celsius to Fahrenheit and vice versa. The function accepts two parameters, namely the temperature value and the temperature unit ('C' for Celsius, 'F' for Fahrenheit).

def convert_temperature (value, unit):
    if (unit == 'c'):
        return (value * 9 / 5) + 32
    elif (unit == 'f'):
        return (value - 32) * 5 / 9
    else:
        return None

input_value = float(input("masukkan value: "))
input_unit = input("masukkan unit (c/f): ")

konversi = convert_temperature(input_value, input_unit)
if (input_unit == 'c'):
    print(input_value, "derajat Celsius = ",konversi, "derajat Fahrenheit")
elif (input_unit == 'f'):
    print("derajat Fahrenheit = ", input_value, "derajat Celsius = ", konversi)


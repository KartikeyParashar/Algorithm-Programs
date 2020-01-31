# given the temperature
# in fahrenheit as input outputs the temperature in Celsius or viceversa using the
# formula
# Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
# Fahrenheit to Celsius: (°F − 32) x 5/9 = °C

def temperature_conversion_to_f(degreeC):
    return degreeC*(9/5) + 32

def temperature_conversion_to_c(degreeF):
    return (degreeF - 32) * (5/9)

temperature = input("For converting temperature from Celcius to Fahrenheit, type F and for converting temperature from Fahrenheit to Celcius, type C: ")

if temperature == 'F':
    degreeC = float(input("Enter a temperature in Celsius for Fahrenheit conversion: "))
    print(f"{temperature_conversion_to_f(degreeC)} degree Fahrenheit")

elif temperature == 'C':
    degreeF = float(input("Enter a temperature in Fahrenheit for Celsius conversion: "))
    print(f"{temperature_conversion_to_c(degreeF)} degree Celsius")


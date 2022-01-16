# Create a program that accepts an integer as input, lets call it celsius. This value will represent a temperature on the celsius scale. Next you program should print the corresponding value on the Fahrenheit scale.The formula for converting celsius to Fahrenheit is as follows:  (degrees in celsius) * 9/5 + 32

celsius = int(input("What is the current temperature in celsius: "))

fahren = celsius * 9/5 + 32
print(celsius, "degrees celsius is equal to", fahren, "fahrenheit")

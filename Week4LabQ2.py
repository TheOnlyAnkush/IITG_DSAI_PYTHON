def temperature_covert():
    #input from user
    temperature = float (input("Enter the Temperature Value: "))
    unit = input("Enter the unit (C for Celciums or F for Fahrenheit): ").strip().upper()

    # Check if the input unit is valid
    if unit == "C":
        # Convert from Celcius to Fahrenheit
        fahrenheit = (temperature * 9/5) + 32
        print (temperature,"°C is equals to", fahrenheit, "°F")
    elif unit == "F":
        # Convert from Fahrenheit to Celcius
        celcius = (temperature - 32) * 5/9
        print (temperature,"°F is equals to", celcius, "°C")
    else:
        print ("Invalid unit.")
temperature_covert()
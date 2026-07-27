def c_to_f(celsius):
    fahrenheit = float(celsius) * 1.8 + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = (float(fahrenheit) - 32.0) / 1.8
    return celsius

def kg_to_lbs(kg):
    lbs = float(kg) * 2.2
    return lbs

def lbs_to_kg(lbs):
    kg = float(lbs) / 2.2
    return kg

def km_to_miles(km):
    miles = float(km) * 0.62
    return miles

def miles_to_km(miles):
    km = float(miles) / 0.62
    return km

while True:
    type = input(f"What do you want to convert?\n 1. C to F,\n 2. F to C,\n 3. kg to lbs,\n 4. lbs to kg,\n 5. km to miles,\n 6. miles to km\nPlease enter (1, 2, 3, 4, 5, 6): ")
    if (type == "1"):
        celsius = input(f"Please enter the value: ")
        fahrenheit = c_to_f(celsius)
        print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit.")
    elif (type == "2"):
        fahrenheit = input(f"Please enter the value: ")
        celsius = f_to_c(fahrenheit)
        print(f"{fahrenheit} degree Fahrenheit is equal to {celsius} degree Celsius.")
    elif (type == "3"):
        kg = input(f"Please enter the value: ")
        lbs = kg_to_lbs(kg)
        print(f"{kg} kg is equal to {lbs} pounds.")
    elif (type == "4"):
        lbs = input(f"Please enter the value: ")
        kg = lbs_to_kg(lbs)
        print(f"{lbs} pounds is equal to {kg} kg.")
    elif (type == "5"):
        km = input(f"Please enter the value: ")
        miles = km_to_miles(km)
        print(f"{km} km is equal to {miles} miles.")
    elif (type == "6"):
        miles = input(f"Please enter the value: ")
        km = miles_to_km(miles)
        print(f"{miles} miles is equal to {km} km.")
    else:
        print(f"Unknown conversion type!")

    status = input(f"Would you like to do another conversion? (1. yes/2. quit): ")
    if (status == "1"):
        continue
    else:
        print("Goodbye!")
        break
temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("Its hot!")
elif temp > 30 and temp <= 50:
    print("Go outside !")
else:
    print("Error!")

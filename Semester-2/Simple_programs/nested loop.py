print("---Decision to do an activity---")

temperature = input("Enter the temperature of the surrounding(warm/cold): ").strip().lower()
humidity = input("Enter the humidity of the atmosphere(dry/humid): ").strip().lower()

if temperature == "warm":
    if humidity == "dry":
        print("Play BasketBall")
    elif humidity == "humid":
        print("Play Tennis")
if temperature == "cold":
    if humidity == "dry":
        print("Play cricket")
    elif humidity == "humid":
        print("Swim")

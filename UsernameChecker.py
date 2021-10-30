from mojang import MojangAPI
import random, string
import threading

def checkIGN(length):
    ign = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    uuid = MojangAPI.get_uuid(ign)
    
    if not uuid:
        print(f"{ign} Available")
        with open("usernames.txt", "a") as file:
            file.write(f"\n{ign}")
    else:
        print(f"{ign} Not Available")
        return
        
def setInterval(length,time):
    e = threading.Event()
    while not e.wait(time):
        checkIGN(length)

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput > 3:
                if userInput < 17:
                    return userInput
                    break
                else:
                    print("Username must be 16 characters or lower")
                    continue
            else:
                print("Username must be 3 characters or higher")
                continue

length = inputNumber("How many letters of the username do you want? ")
setInterval(length, 5)

import time

isConnected = "no"




for retry in range(4):
    time.sleep(2)
    isConnected = input ('isConnected?:')
    if  isConnected == "yes":
        print("now connected")
        break
    else:
        print("request timed out")

print("processing your requenst...")
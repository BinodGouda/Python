import time

timestamp = int(time.strftime("%H"))

if (timestamp >= 4 and timestamp < 12):
    print("Good Morning")

elif(timestamp >= 12 and timestamp < 18):
    print("Good Afternoon")

elif(timestamp >= 18 and timestamp < 20):
    print("Good Evning")

elif(timestamp >= 20 and timestamp < 24):
    print("Good Night")
    
else:
    print("Invalid Time")

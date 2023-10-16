import time
print("""Welcome to the 10 second game!
Here are the rules - You have to count as close to ten seconds as you can.
When you're ready to start the clock press 'Enter'.
Press 'Enter' again when you think you've counted 10 seconds.""")
start = input()
startTime = time.time()
print("Press 'Enter' to stop the clock")
stop = input()
stopTime = time.time()
print(round(stopTime - startTime,2))

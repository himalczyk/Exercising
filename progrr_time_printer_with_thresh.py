from time import sleep
seconds = 0

while True:
    sleep(seconds)
    print("Hello")
    seconds = seconds+1
    if seconds > 3:
        print("End of loop")
        break
    
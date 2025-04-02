from datetime import datetime
time = datetime.now()
CurrentTime = time.strftime("%H:%M:%S")

name = input("Who are you?",)
print("Hello", name)
oras = print("The current time is ", CurrentTime)
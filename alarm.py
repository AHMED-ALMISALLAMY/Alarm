import datetime
from playsound import playsound


# input hour
alarmHour = int(input("Enter Hour: "))

# input minute
alarmMin = int(input("Enter Minute: "))

# input Am / PM
alarmAM = input("AM or PM? ").upper()


if alarmAM == 'PM':
    # if it PM that mean after 12 o'clock 
    alarmHour += 12

while True:
    # if your hour that you input =to hour.now in your device and minute you choose =to minute.now in your device
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:

        # it will print 'playing now'
        print("Playing Now")

        # Here playing any mp3 sound.
        print("anysound.mp3")

        # Then the loop will stop.
        break
from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        actual_time.strftime("%d/%m/%Y")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
            break


def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(alarm_set_time)


window = Tk()
window.title("Alarm Clock")
window.geometry("400x160")
window.config(bg="#922B21")
window.resizable(width=False, height=False)
Label(window, text="Remember to set time in 24 hour format!", fg="white", bg="#922B21",
      font=("Arial", 15)).place(x=20, y=120)
Label(window, text="Hour     Min     Sec", font=60, fg="white", bg="black").place(x=210)
Label(window, text="Set Time for Alarm: ", fg="white", bg="#922B21", relief="solid",
      font=("Helevetica", 15, "bold")).place(x=10, y=40)

hour = StringVar()
min = StringVar()
sec = StringVar()

Entry(window, textvariable=hour, bg="#48C9B0", width=4, font=20).place(x=210, y=40)
Entry(window, textvariable=min, bg="#48C9B0", width=4, font=20).place(x=270, y=40)
Entry(window, textvariable=sec, bg="#48C9B0", width=4, font=20).place(x=330, y=40)

Button(window, text="Set Your Alarm", fg="Black", bg="#D4AC0D", width=15, command=get_alarm_time,
       font=20).place(y=80, x=100)

window.mainloop()

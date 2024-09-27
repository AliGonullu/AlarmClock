from datetime import time, datetime
from time import sleep
from math import floor
from pygame import mixer
from os import system, name

def timeout_sound() -> None:
    print("\n***Time is out***")
    mixer.music.play()
    while mixer.music.get_busy(): sleep(1)
    mixer.quit()

def time_calculation(_hour, _minute, _second) ->list:
    hour :int = _hour + floor(_minute / 60) + floor(_second / 3600) % 24
    minute :int = _minute + floor(_second / 60) % 60
    second :int = _second % 60
    return [hour, minute, second]

def takeUserInput(text) -> int:
    ans :str = input(f"{text}")
    return (int(ans) if ans.isnumeric() else 0) if ans != None else 0

def alarm() -> None:
    raw_hour :int = takeUserInput("Set your alarm (hour) : ")
    raw_minute :int = takeUserInput("Set your alarm (minute) : ")
    raw_second :int = takeUserInput("Set your alarm (second) : ")
    calc :list = time_calculation(raw_hour, raw_minute, raw_second)
    target_time :str = time(calc[0], calc[1], calc[2]).strftime("%H:%M:%S")
    current_time :str = datetime.now().time().strftime("%H:%M:%S")
    h :int = int(current_time.split(":")[0])
    m :int = int(current_time.split(":")[1])
    s :int = int(current_time.split(":")[2])
    while f"{h:02}:{m:02}:{s:02}" != target_time:
        print("\n ***" + target_time + "***\n" + f"\n--> {h:02}:{m:02}:{s:02}")
        sleep(1.000)
        system('cls' if name == 'nt' else 'clear')
        s += 1
        if s > 59:
            m += 1
            s = 0
            if m > 59:
                h += 1
                m = 0
    del raw_hour, raw_minute, raw_second, h, m, s
    
def chronometer() -> None:
    hour :int = takeUserInput("Set your chronometer (hour) : ")
    minute :int = takeUserInput("Set your chronometer (minute) : ")
    second :int = takeUserInput("Set your chronometer (second) : ")
    calc :list = time_calculation(hour, minute, second)
    hour :int = calc[0]
    minute :int = calc[1]
    second :int = calc[2]
    
    while hour > 0 or minute > 0 or second > 0:
        print(f"\n {hour:02}:{minute:02}:{second:02}")
        sleep(1.00)
        system('cls' if name == 'nt' else 'clear')
        second -= 1
        if second < 0:
            minute -= 1
            second = 59
            if minute < 0:
                hour -= 1
                minute = 59
    del hour, minute, second

def main() -> None:
    mixer.init()
    mixer.music.load("C:/Users/egonu/OneDrive/Belgeler/VS_Code_F/Python_L/Media/alarm_sound.wav")
    system('cls' if name == 'nt' else 'clear')
    while True:
        ans :int = takeUserInput("1) Alarm\n2) Chronometer\n\n Choose your action : ")
        if ans == 1:
            system('cls' if name == 'nt' else 'clear')
            alarm()
            break
        elif ans == 2:
            system('cls' if name == 'nt' else 'clear')
            chronometer()
            break
        else:
            system('cls' if name == 'nt' else 'clear')
            print("****\nInvalid answer.\n****")
    timeout_sound()

if __name__ == "__main__":
    main()
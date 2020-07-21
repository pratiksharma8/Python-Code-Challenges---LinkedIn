from datetime import datetime

print('Enter time to set alarm : ')
set_hr = int(input("Hr(0-23): "))
set_min = int(input("M(0-59): "))

print(f'Alarm is set for {set_hr}:{set_min}')


def set_alarm():
    now = datetime.now().time()
    current_time_hr = int(now.strftime("%H"))
    current_time_min = int(now.strftime("%M"))

    print(f'Current time: {now}')

    if current_time_hr == set_hr and current_time_min == set_min:
        print("Alarm is going off.. Snooze or loose")
    else:
        print(
            f"Time remaining {abs(24 - (abs(set_hr - current_time_hr)))} hr {abs(60 - (abs(set_min - current_time_min)))} minutes")


set_alarm()

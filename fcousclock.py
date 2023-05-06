import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Remaining time: {remaining_time // 60:02d}:{remaining_time % 60:02d}", end="\r")
        time.sleep(1)
    print("\nTime is up! Take a break.")

if __name__ == "__main__":
    focus_timer(25) # 25 minutes is the standard time for a Pomodoro session

# Create a program that displays the passing of time
import time
import sched

# Create a scheduler object
s = sched.scheduler(time.time, time.sleep)

# Function to update and display the clock
def update_clock(sc):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time)
    
    # Schedule the next update after 1 second
    s.enter(1, 1, update_clock, (sc,))

# Schedule the initial update
s.enter(1, 1, update_clock, (s,))

# Run the scheduler
s.run()
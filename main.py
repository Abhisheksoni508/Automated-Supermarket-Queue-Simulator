"""
 Part C of the Supermarket Checkout Lane Queue Simulation
 is a combination of Part A and Part B. It consists of a simulation
 that runs the entire program for a certain amount of time and stops itself.

 Created on Jan 18, 2024
 @authors: Shiyon Suresh & Abhishek Soni
"""

import time
from f1 import LaneManagement  # Using class LaneManagement from f1
from f2 import CustomerLayout  # Using class CustomerLayout from f2


# generate_f3 simulates the whole program
def generate_f3():
    f1 = LaneManagement({}, {})  # First initiation for class LaneManagement
    f2 = CustomerLayout({}, {})  # First initiation for class CustomerLayout
    starting_time = time.time()  # Starting time of the program
    last_time_customer_generated = starting_time
    last_time_lane_data_generated = starting_time
    last_time_move_lane = starting_time
    cfg_simulation_duration = 600  # The duration of simulation in seconds
    cfg_customer_generation_timer = 30  # Interval to generate random number of customers
    cfg_lane_data_timer = 10  # Interval to print the lane data
    cfg_move_lane_data_timer = 30  # Interval to check moving of lane
    f1.lane_startup()
    time.sleep(3)
    f2.generate_customer()
    while time.time() - starting_time < cfg_simulation_duration:  # The loop run till the simulation timer
        current_time = time.time()

        # Calculates the last time for each function
        elapsed_time_customer_generation = current_time - last_time_customer_generated
        elapsed_time_lane_data_generation = current_time - last_time_lane_data_generated
        elapsed_time_move_lane = current_time - last_time_move_lane

        if elapsed_time_lane_data_generation >= cfg_lane_data_timer:  # Checking time to print lane data
            f2.print_lane_management()
            f2.remove_customer()
            last_time_lane_data_generated = current_time  # reset the start time

        # Checking time to generate new customers
        elif elapsed_time_customer_generation >= cfg_customer_generation_timer:
            f2.generate_customer()
            f2.print_lane_management()
            last_time_customer_generated = current_time  # reset the start time

        if elapsed_time_move_lane >= cfg_move_lane_data_timer:  # Checking time for move lane
            f2.move_lane()
            last_time_move_lane = current_time

        time.sleep(1)  # Time sleep to cooldown the whole program for CPU

    print('##### END OF SIMULATION #####')


if __name__ == "__main__":
    generate_f3()

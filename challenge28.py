#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra M, and Nick A
# Event Logging Tool Part 3 of 3

import logging
import os
import datetime
import logging.handlers as handlers
import time

target = "8.8.8.8"

# Create loggers
logger = logging.getLogger()

# Print to screen logger
Slogger = logging.StreamHandler()

# Print to file
Flogger = logging.FileHandler('Demo.log')

# Set levels
Slogger.setLevel(logging.ERROR)
Flogger.setLevel(logging.DEBUG)

# Create formatter
SFormat = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
FFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add format to handlers
Slogger.setFormatter(SFormat)
Flogger.setFormatter(FFormat)

# Add handlers to loggers

logger.addHandler(Slogger)
logger.addHandler(Flogger)

logger.info("Script started: ping_Status")
def ping_Status(target):
    try:

        # Intentionally raise an exception to simulate an error
        raise ValueError("An intentional error occurred")        
        # Evaluate the response and assign success or failure to the status variable
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "success"
            print(f"{target} is up!")
        else:
            status = "failure"
            print(f"{target} is down!")

        # Get the current timestamp and print the status and timestamp
        currenttime = datetime.datetime.now()
        print(f"{currenttime} - Status: {status}")
        return status

    except Exception as e:
        logger.exception("An error has occurred")
        raise e

while True:
    try:
        # Transmit a single ICMP ping packet to the target
        ping_Status(target)
        # Wait for 2 seconds before transmitting another ping packet
        time.sleep(2)

    except KeyboardInterrupt:
        # Stop the program if the user interrupts it
        break

    except Exception as e:
        logger.exception("An error has occurred")
logger.info("Script started: ping_Status")

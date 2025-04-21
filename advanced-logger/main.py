import logging
import sys
import time

logging.basicConfig(
    filename='output.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Script started")

try:
    # Simulate work
    for i in range(3):
        logging.info(f"Processing item {i}")
        time.sleep(1)
    
    # Simulate error (comment this line for success)
    x = 1 / 0  

except Exception as e:
    logging.error(f"CRITICAL ERROR: {str(e)}")
    sys.exit(1)  # Fail the job

logging.info("Script completed successfully")
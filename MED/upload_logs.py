import logging
import requests
import uuid
# import enums as en
import os
from datetime import datetime
# =============================================================================
# Class to upload log files on server
# =============================================================================
class C_logs:

    
    # =============================================================================
    # init function of the class where we make inital variables
    # =============================================================================
    def __init__(self):
        # log file name
        self.log_name = f'All.txt'

        # making header for the request
        self.headers = {'User-Agent': 'Mozilla/5.0 Chrome/39.0.2171.95 Safari/537.36'}

        # ur of the server
        self.url = "http://localhost:3000/upload"

        # init mac address
        self.mac = '00-00-00-00-00-00'

        # Th for file upload size
        self.sizeTH = 1000

    # =============================================================================
    # get mac address of the system
    # =============================================================================
    def get_mac(self):
        try:
            #  get the mac
            mac_num = hex(uuid.getnode()).replace('0x', '').upper()

            # converting it to format
            self.mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))

        except Exception as e:
            logging.error('Error getting MAC address: {}'.format(e))


    # =============================================================================
    # sending file to server function its main function
    # =============================================================================
    def send_log(self):
        logging.info('Sending Log')

        try:
            # getting the mac address of the computer
            self.get_mac()

            # generating the payload and files as in the provided send_file_to_server function
            file_path = self.log_name
            api_url = self.url
            mac_address = self.mac

            # Generate a timestamp for the file name
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            unique_file_name = f"All_{timestamp}.txt"
            print(unique_file_name)

            # Open the file in binary mode
            with open(file_path, 'rb') as file:
                # Create a dictionary of files to send
                files = {'file': (unique_file_name, file, 'text/plain')}
             

                # Send the POST request with the file and MAC address as data
                data = {
                    'macAddress': mac_address,
                    'botName': "Test ALi",  # Assuming this is set correctly in your enums
                    'version': 5  # Replace with your version number if needed
                }
                # Send the POST request with the file
                response = requests.post(api_url, headers=self.headers, data=data, files=files)

            if response.status_code == 200:
                logging.info("File uploaded successfully.")
            else:
                logging.error(f"Failed to upload the file. Status code: {response.status_code}")
                logging.error(response.text)

        except Exception as e:
            logging.error(f'Unable to send Log file to server: {e}')

    # =============================================================================
    # Clearing the content of file
    # =============================================================================
    def del_old_log(self):
        try:
            open(self.log_name, "w").close()
        except Exception as e:
            logging.error('Unable to clear log file: {}'.format(e))

    # =============================================================================
    # Check size if 500kb plus file then send to server
    # =============================================================================
    def check_size(self):
        b = os.path.getsize(self.log_name)
        b = int(b / 1024)
        return b > self.sizeTH

    # =============================================================================
    # Main function to Run the code
    # =============================================================================
    def Run(self):
        if self.check_size():
            self.send_log()
            self.del_old_log()
        else:
            logging.warning('Log file size is below the threshold, not sending.')

# =============================================================================

# =============================================================================
# making this general function to call form other files
# =============================================================================
def send_log():
    obj = C_logs()
    obj.Run()

# =============================================================================
# Testing
# Uncomment the line below to test the sending of the log.
send_log()
# =============================================================================


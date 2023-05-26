import socket
import time
from faker import Faker

fake = Faker()

# DISCLAIMER
# This script is for educational purposes only. Do not use it for illegal activities.
# I am not responsible for any damage done by this script.
# This script should only be used on systems you own or have permission to use it on.
# This script is not intended to harm anyone, and you are responsible for your own actions.

print("KeePassMini-Spamer.py")
print("DISCLAIMER!!!\nThis script is for educational purposes only.\nDo not use it for illegal activities.\nI am not responsible for any damage done by this script.\nThis script should only be used on systems you own or have permission to use it on.\nThis script is not intended to harm anyone, and you are responsible for your own actions.")
print("")

def sendSpam():
    # Analyse String
    anna = "!AMSG|"
    if fake.boolean():
        anna += "WIFI"
    else:
        anna += "CELL"

    anna += "|" + fake.country() + "|" + fake.language_code()
    anna += "|" + fake.timezone() + "|" + fake.word()
    anna += "|" + str(fake.random_number(digits=1)) + "." + str(fake.random_number(digits=1)) + "." + str(fake.random_number(digits=1))
    anna += "|" + fake.uuid4()
    anna += "|" + str(fake.random_number(digits=1)) + "." + str(fake.random_number(digits=1)) + "." + str(fake.random_number(digits=1))
    anna += "|"

    # Generate clipboard content over time
    clipboard_data = []
    clipboard_data.extend([fake.word() for _ in range(100)])  # Random English words

    # Generate the same email for multiple messages to make them less identifiable
    email = fake.email()
    clipboard_data.extend([email] * 5)  # Repeated email addresses

    clipboard_data.extend([fake.password() for _ in range(5)])  # Generated passwords

    for content in clipboard_data:
        anna += content + "|"
        print(anna)
        send_udp_data(anna)
        time.sleep(0.1)  # Delay between each session

    return "Data sent successfully"


def send_udp_data(data):
    address = "anna.unicomedv.de"
    port = 10548

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_socket.sendto(data.encode(), (address, port))
        print("UDP send data success")
    except socket.error as error:
        print(f"UDP send data error: {error}")
    finally:
        client_socket.close()


spam_count = int(input("How many spam messages do you want to send?: "))
for i in range(spam_count):
    sendSpam()

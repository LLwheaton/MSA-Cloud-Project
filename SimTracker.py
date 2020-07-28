import time
import random

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=iot-hub-linda.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=kCA+cSeheHD0RFgyKIPlgKTZc3JFn7na4JudO81CU70="

# Heart rate ranges from 65-100
HEART_RATE = 65 # * 35 floor

# Blood pressure - 2 types
SYSTOLIC_BP = 90 # range 90-120
DIASTOLIC_BP = 60 # range 60-80

MESSAGE = '{{"heart_rate": {heart_rate},"systolic_bp": {systolic_bp}, "diastolic_bp": {diastolic_bp}}}'

try:
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    while True:
        # The message text will be replaced with simulated values
        # for heart rate and blood pressure
        heart_rate = HEART_RATE + round(random.random() * 35, 0)
        systolic_bp = SYSTOLIC_BP + round(random.random() * 30, 0)
        diastolic_bp = DIASTOLIC_BP + round(random.random() * 20, 0)

        formatted_message = MESSAGE.format(heart_rate=heart_rate, systolic_bp=systolic_bp, diastolic_bp=diastolic_bp)
        message = Message(formatted_message)

        # Message will be send to iot hub client
        print("Sending message: {}".format(message))
        client.send_message(message)
        print("Message sent.")
        # Send message every 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

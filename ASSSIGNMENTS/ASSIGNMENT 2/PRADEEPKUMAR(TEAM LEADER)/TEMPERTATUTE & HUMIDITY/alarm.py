import random
from playsound import playsound

# Generate random temperature and humidity values
temperature = random.uniform(10, 40)
humidity = random.uniform(30, 80)

# Set thresholds for temperature and humidity
temperature_threshold = 30
humidity_threshold = 60

# Check if temperature or humidity exceeds the threshold
if temperature > temperature_threshold and humidity > humidity_threshold:
    print("Alarm: High temperature and high humidity detected!")
    playsound("alarm.wav") # replace "alarm.wav" with the file path of your alarm sound
elif temperature > temperature_threshold:
    print("Alarm: High temperature detected!")
    playsound("alarm.wav") # replace "alarm.wav" with the file path of your alarm sound
elif humidity > humidity_threshold:
    print("Alarm: High humidity detected!")
    playsound("alarm.wav") # replace "alarm.wav" with the file path of your alarm sound
else:
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
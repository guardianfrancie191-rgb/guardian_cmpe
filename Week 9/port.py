import serial
import threading
import time


PORT = "COM1"
BAUDRATE = 9600

ser =serial.Serial("COM1", 9600, timeout=1)

time.sleep(2)

def send(message):
    ser.write((message + '\n').encode())
    print (f"sent: {message}")


def receive():
  if ser.in_waiting > 0:
    data = ser.readline().decode('utf-8')
    if data:print (f"received: {data}")
    return data
  else:
      return None


def received_continuously():
  while running:
      received_data = receive()
      time.sleep(0.1)

running = True
receiver_thread = threading.Thread(target=received_continuously, daemon=True)
receiver_thread.start()

try:
 while True:

  message = input ("Enter message: ")
  if message:
     send(message)

except KeyboardInterrupt:
  print ("exit")

finally:
    running = False


# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)  # Get the Tello drone's address

# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep=6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# Functions

# First Hoop
def first_hoop():
    sendmsg('up 20')
    sendmsg('forward 200')


# Second Hoop
def second_hoop():
    sendmsg('go 240 0 60 40', 7)


# Third Hoop

def third_hoop():
    # sendmsg('ccw 90', 7)
    # sendmsg('forward 270')
    # sendmsg('up 10', 10)
    # sendmsg('ccw 90', 10)

    sendmsg('curve 50 135 0 270 0 0 40', 20)
    # sendmsg('curve 50 100 0 100 0 0 40', 20)


# Fourth Hoop
def fourth_hoop():
    sendmsg('go 300 0 -60 40', 10)


print("\nJacob Estes")
print("Program Name: Tello Drone Training School")
print("Date: 11.9.2020")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
print("\n****CHECK IF CO-PILOT IS READY****")
ready = input('\nAre you ready to take flight: ')

try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        first_hoop()

        second_hoop()

        third_hoop()

        fourth_hoop()

        sendmsg('land')

        print('\nGreat Flight!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()

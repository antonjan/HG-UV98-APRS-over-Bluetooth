import bluetooth
import threading
import binascii

def receive_data(socket):
    while True:
        try:
            #byte = ser.read(1)
            byte = socket.recv(1)
            if byte:
                if byte == b'\xC0':
                    frame = byte
                    while True:
                        byte = socket.recv(1)
                        frame += byte
                        if byte == b'\xC0':
                            parsed_frame = parse_kiss_frame(frame)
                            if parsed_frame:
                                data, port = parsed_frame
                                print(f"Port {port}: {binascii.hexlify(data).decode()}")
        except KeyboardInterrupt:
            print("Monitoring stopped.")
            break
'''
    while True:
        try:
            data = socket.recv(1024)
            if len(data) == 0:
                break
            print(f"Received: {data.decode('utf-8')}")
        except OSError:
            #print(f"Receved: {data}")
            break
'''
def parse_kiss_frame(frame):
    if frame[0] != 0xC0 or frame[-1] != 0xC0:
        return None

    frame = frame[1:-1]  # Remove start and end flags

    # KISS protocol commands
    cmd = frame[0] & 0xF0
    port = frame[0] & 0x0F

    if cmd == 0x00:  # Data frame
        return frame[1:], port
    elif cmd == 0x40:  # TX Delay
        return f"TX Delay: {frame[1]}", port
    elif cmd == 0x80:  # Persist
        return f"Persist: {frame[1]}", port
    elif cmd == 0xC0:  # Slot Time
        return f"Slot Time: {frame[1]}", port
    else:
        return None            
def parse_kiss_frame(frame):
    if frame[0] != 0xC0 or frame[-1] != 0xC0:
        return None

    frame = frame[1:-1]  # Remove start and end flags

    # KISS protocol commands
    cmd = frame[0] & 0xF0
    port = frame[0] & 0x0F

    if cmd == 0x00:  # Data frame
        return frame[1:], port
    elif cmd == 0x40:  # TX Delay
        return f"TX Delay: {frame[1]}", port
    elif cmd == 0x80:  # Persist
        return f"Persist: {frame[1]}", port
    elif cmd == 0xC0:  # Slot Time
        return f"Slot Time: {frame[1]}", port
    else:
        return None
        
def main():
    # Replace 'HG-UV98' with the name or address of your APRS radio
    target_device_name = 'ZR6AIC-7'

    # Search for nearby Bluetooth devices
    #while True:
    try:
       nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
       print( "try to connect")
    except:
       print("could not find a blutooth device on this pc")
       #time.sleep(2.4)
       #break
    # Find the target device in the list of nearby devices
    target_device_address = None
    for address, name in nearby_devices:
        if name == target_device_name:
            target_device_address = address
            print("found device =",target_device_address)
            break

    if target_device_address is None:
        print(f"Device '{target_device_name}' not found.")
        return

    # Create a Bluetooth socket and connect to the radio
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1  # RFCOMM port for most devices
    print("opening port", target_device_address)
    sock.connect((target_device_address, port))

    print(f"Connected to '{target_device_name}' over Bluetooth")

    # Start a separate thread to receive data from the radio
    receive_thread = threading.Thread(target=receive_data, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            pass  # Main program loop to keep the receiving thread alive
    except KeyboardInterrupt:
        print("Disconnected.")
        sock.close()

if __name__ == "__main__":
    main()


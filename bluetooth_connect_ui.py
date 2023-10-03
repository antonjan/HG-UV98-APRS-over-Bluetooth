import bluetooth
import threading
import binascii
import aprslib

def decode_aprs_string(str_aprs):
    try:
        parsed_string = aprslib.parse(str_aprs)
#        print("****************************************************************************************************")
#        print("packet:",str_aprs)
#        print("parsed:",parsed_string)
#        print("****************************************************************************************************")
        return parsed_string
    except Exception as e:
        print(f"Error aprs message: {e}")
        return None 
'''
****************************************************************************************************
packet: b'N0VPR-4>APNU19,WIDE2-2,qAO,AE0BB:!4127.85NS09429.35W#PHG6130/A=001525W3, IAnv1.9B MENLO, IA'
parsed: {'raw': 'N0VPR-4>APNU19,WIDE2-2,qAO,AE0BB:!4127.85NS09429.35W#PHG6130/A=001525W3, IAnv1.9B MENLO, IA', 'from': 'N0VPR-4', 'to': 'APNU19', 'path': ['WIDE2-2', 'qAO', 'AE0BB'], 'via': 'AE0BB', 'messagecapable': False, 'format': 'uncompressed', 'posambiguity': 0, 'symbol': '#', 'symbol_table': 'S', 'latitude': 41.464166666666664, 'longitude': -94.48916666666666, 'phg': '6130', 'phg_power': 36, 'phg_height': 6.096, 'phg_gain': 1.9952623149688795, 'phg_dir': 'omni', 'phg_range': 14.011864462334005, 'altitude': 464.82000000000005, 'comment': 'W3, IAnv1.9B MENLO, IA'}
****************************************************************************************************
'''



def decode_kiss_frame(hex_message):
    try:
        # Convert the hex string to bytes
        hex_bytes = bytes.fromhex(hex_message)

        # Check for KISS framing byte (0xC0)
        if hex_bytes[0] != 0xC0 or hex_bytes[-1] != 0xC0:
            raise ValueError("Invalid KISS frame")

        # Remove KISS framing bytes
        data_bytes = hex_bytes[1:-1]

        # Initialize variables
        decoded_data = bytearray()
        escape = False

        # Process the data bytes
        for byte in data_bytes:
            if escape:
                decoded_data.append(byte ^ 0x20)
                escape = False
            elif byte == 0xDB:
                escape = True
            else:
                decoded_data.append(byte)

        # Convert the decoded bytes to a string
        decoded_message = decoded_data.decode('utf-8', errors='ignore')

        return decoded_message

    except Exception as e:
        print(f"Error decoding KISS frame: {e}")
        return None


def receive_data(socket):
    while True:
        try:
            data = socket.recv(1024)
            print("data from bluetooth",data)
            #parsed_string = aprslib.parse(data)
            parsed_string = decode_aprs_string(data)
            print("parsed_string=",parsed_string)
            #packet: b'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98\r\n'
            #parsed: {'raw': 'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98', 'from': 'ZR6AIC-8', 'to': 'APUV98', 'path': ['ZR6AIC-7*', 'WIDE1*'], 'via': '', 'messagecapable': False, 'format': 'uncompressed', 'posambiguity': 0, 'symbol': '[', 'symbol_table': '/', 'latitude': 31.565, 'longitude': 120.38, 'altitude': 99.9744, 'comment': 'UV98'}
            #print(parsed_string)
            if len(data) == 0:
                break
            print("dada 0 =", data[0])
            print("type =",type(data[0]))
            if data[0] == 192:
               mystring = ""
               for digit in data:
                  mystring += chr(digit) #str(digit)
               #decoded_text = decode_kiss_frame(data)
               #print(f"Received1: {decoded_text}")
               #print("string =",mystring)
               #mynewstring = "M0XER-4>APRS64,TF3RPF,WIDE2*,qAR,TF3SUT-2:"+mystring
               #decoded_text = decode_aprs_string(mynewstring)
               #decoded_text = str(data, encoding='utf-8')
               #decoded_test = data.decode("utf-8")
               #decoded_text = decode_kiss_frame(mystring)    
            
               print(f"Received1: {decoded_text}")
            else:
               print(f"Received2: {data.decode('utf-8')}")
   
        except Exception as e:
            print(f"Error in receving message: {e}")
            #print(f"Receved: {data}")
            break
'''    while True:
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
                                print(f"\nPort {port}: {binascii.hexlify(data).decode()}")
        except KeyboardInterrupt:
            print("Monitoring stopped.")
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
'''def parse_kiss_frame(frame):
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
'''        
def main():
    # Replace 'HG-UV98' with the name or address of your APRS radio
    target_device_name = 'ZR6AIC-7'

    # Search for nearby Bluetooth devices
    #while True:
    try:
       nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True)
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


import aprslib

# Configure your APRS-IS server connection settings
aprs_server = "rotate.aprs2.net"
aprs_port = 14580
callsign = "ZR6AIC-9"
passcode = "22194"

# Connect to the APRS server
aprs = aprslib.IS(callsign, passcode, aprs_server, aprs_port)
aprs.connect()

# Create an APRS message
to_call = "ZR6AIC-5"  # Replace with the recipient's callsign
message_text = "Hello from Anton APRS!"

# Send the APRS message
aprs.sendall(message_text, to_call)

# Close the APRS connection
aprs.disconnect()

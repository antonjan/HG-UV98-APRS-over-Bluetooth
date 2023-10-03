# HG-UV98-APRS-over-Bluetooth
This repository will have my code to communicate with the HG-UV98 Transceiver.
# usage
python3 bluetooth_connect.py
try to connect
Device 'NOCALL-7' not found.
(base) anton@anton-ThinkPad-P52:~/HG-UV98_APRS$ python3 bluetooth_connect.py 
try to connect
found device = 00:0C:BF:19:70:28
opening port 00:0C:BF:19:70:2
Connected to 'NOCALL-7' over Bluetooth
Port 0: 82a0aaac727060b4a46c829286f0ae92888a62406303f021333133332e39304e2f31323032322e3830455b3030302f3030302f413d30303033323855563938
Port 0: 82a0aaac727060b4a46c829286f0ae92888a62406303f021333133332e39304e2f31323032322e3830455b3030302f3030302f413d30303033323855563938c0

# Message decoding if Bluetooth is set to UI for a (using bluetooth_connect_ui.py)
      data from bluetooth b'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98\r\n'
      parsed_string= {'raw': 'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98', 'from': 'ZR6AIC-8', 'to': 'APUV98', 'path': ['ZR6AIC-7*', 'WIDE1*'], 'via': '', 'messagecapable': False, 'format': 'uncompressed', 'posambiguity': 0, 'symbol': '[', 'symbol_table': '/', 'latitude': 31.565, 'longitude': 120.38, 'altitude': 99.9744, 'comment': 'UV98'}
      


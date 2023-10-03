import re
import aprslib

# Input APRS UI message
aprs_message = 'ZR6AIC-8>APUV98,WIDE1-1:!3133.90N/12022.80E[000/000/A=000328UV98\r\n'
#packet: b'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98\r\n'
#parsed: {'raw': 'ZR6AIC-8>APUV98,ZR6AIC-7*,WIDE1*:!3133.90N/12022.80E[000/000/A=000328UV98', 'from': 'ZR6AIC-8', 'to': 'APUV98', 'path': ['ZR6AIC-7*', 'WIDE1*'], 'via': '', 'messagecapable': False, 'format': 'uncompressed', 'posambiguity': 0, 'symbol': '[', 'symbol_table': '/', 'latitude': 31.565, 'longitude': 120.38, 'altitude': 99.9744, 'comment': 'UV98'}

parsed_string = aprslib.parse(aprs_message)
print(type(parsed_string))
print("from",parsed_string['from'])
print("to",parsed_string['to'])
print("path",parsed_string['path'])
print("via",parsed_string['via'])
print("messagecapable",parsed_string['messagecapable'])
print("format",parsed_string['format'])
print("posambiguity:",parsed_string['posambiguity'])
print("symbol:",parsed_string['symbol'])
print("symbol_table:",parsed_string['symbol_table'])
print("latitude:",parsed_string['latitude'])
print("longitude:",parsed_string['longitude'])
print("altitude:",parsed_string['altitude'])
print("comment:",parsed_string['comment'])
print("parsed string",parsed_string)

# Define a regular expression pattern to match the call sign
#call_sign_pattern = rb'([A-Z0-9\-]+)>'

# Use re.search to find the call sign in the message
#match = re.search(call_sign_pattern, aprs_message)
'''
if match:
    call_sign = match.group(1).decode('utf-8')  # Decode the bytes to a string
    print("Call Sign:", call_sign)
else:
    print("Call sign not found in the APRS message.")
'''

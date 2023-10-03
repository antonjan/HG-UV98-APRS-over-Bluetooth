import aprslib

def callback(packet):
    parsed_string = aprslib.parse(packet)
    print("****************************************************************************************************")
    print("packet:",packet)
    print("parsed:",parsed_string)
    print("****************************************************************************************************")

AIS = aprslib.IS("ZR6AIC-5")
AIS.connect()
# by default `raw` is False, then each line is ran through aprslib.parse()
AIS.consumer(callback, raw=True)


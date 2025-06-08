import serial,time

def tryOpenSerial(com,baund=460800,parity='N',stopbits=1,maxReryCount=3,delay=0.5):
    debug_list = []
    serials = False
    emsg = ''
    for i in range(maxReryCount):
        try:serials = serial.Serial(com, baund,parity=parity,stopbits=stopbits);break
        except Exception as e:time.sleep(delay);emsg = e 
    if not serials:
        debug_list.append(emsg)
        debug_list.append('{} in {}?'.format(com,list(serial.tools.list_ports.comports())))
    return serials,debug_list
def trySendSerial( serials,delay:float=0.5,msgList:list = [],msgType='hex' ):
    debug_list = []
    pass
    
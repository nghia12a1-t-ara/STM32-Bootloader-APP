from ParseHexFile import ParseFileHex
import re
import serial
import serial.tools.list_ports

class SerialDataTransfer():
    def __init__(self, SerialOBJ, DataList, mySerial):
        self.DataList = DataList
        self.mySerial = mySerial
        
    def ConvertRawDataToWord(self):
        listLen = len(self.DataList)
        
        ### Get First Address to Transfer Only
        firstAddr = list(self.DataList[0].keys())[0]
        
        for i in range(listLen):
            tempDict = self.DataList[i]
            Address = list(tempDict.keys())[0]
            rawData = tempDict[Address]
            tempLen = len(rawData)

            ### Slice Data each Words to Transfer into Serial Port
            while tempLen > 0:
                WordTransfer = str(rawData[0:8])
                ByteDataTransfer = WordTransfer.encode('UTF-8')
                print(ByteDataTransfer)
                
                # Call Transfer func() to transfer Data into Serial Port
                #SerialConnect.TransferDataWord(self.SerialOBJ, self.mySerial, ByteDataTransfer)
                self.mySerial.write(ByteDataTransfer)

                # Slice First Word of Data
                rawData = rawData[8:]
                tempLen = len(rawData)

class SerialConnect():
    def __init__(self, port, baudrate, bytesize, timeout, stopbits):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.timeout = timeout
        self.stopbits = stopbits

    '''--------- List all Device connect with COM Port --------'''
    def listDevice(self):
        list_ports = serial.tools.list_ports.comports()
        print(list_ports)
        return list_ports
        
    '''-------------- Get data from STM32-UART ---------------'''
    def USBtoCOMPort(self):     
        commPort = 'ABC'
        
        lst = self.listDevice()
        numConnection = len(lst)
        for i in range(0,numConnection):
            port = lst[i]
            strPort = str(port)

            if 'CP210x' in strPort:
                splitPort = strPort.split(' ')
                commPort = (splitPort[0])
        return commPort        

    def ConnectPort(self):
        ser1 = serial.Serial(self.port, baudrate = self.baudrate, timeout = self.timeout)
        return ser1

    def TransferDataWord(self, mySerial, WordData):
        # Wait until there is data waiting in the serial buffer
        if(mySerial.in_waiting > 0):
            mySerial.write(WordData)

### Example ###
### temp = ParseFileHex("D:\\myFPT\\Bootloader\\NUCLEO\\Blink_led - Cam\\MDK-ARM\\Blink_led\\Blink_led.hex")
'''SerialOBJ = SerialConnect("COM3", 9600, 8, 2, serial.STOPBITS_ONE)
ser1 = SerialOBJ.ConnectPort()

a = '0123AFEC'
b = a.encode('UTF-8')

ser1.write(b)
'''

'''
Object1 = SerialDataTransfer(SerialOBJ, temp.ParseRawData(), ser1)
Object1.ConvertRawDataToWord()
'''



import re

class ParseFileHex():
    def __init__(self, path):
        self.path = path

    ### Get Data from a Line
    def ParseData(self, lineContent, byteCountDec):
        if int(byteCountDec) > 0:
            EndDataField = 8 + (byteCountDec * 2)
            Data = lineContent[8:EndDataField]
        return Data        

    ### Return  :   List of Dictionaries contain Address
    ###             and Raw Data of Hex File
    def ParseRawData(self):
        with open(self.path, 'r') as HexFile:
            HexText = HexFile.read()
        ListLine = re.findall(r':(\w+)', HexText)
        numLine = len(ListLine)

        BASE_ADDRESS_DEC = 0
        DataList = []
        
        for line in range(numLine):
            tempDict = {}
            
            lineContent = ListLine[line]

            # Get byte Count from Hex Line - 2 characters
            byteCountHex = lineContent[0:2]
            byteCountDec = int(byteCountHex, 16)

            # Get Address - 4 characters
            offsetAddr = lineContent[2:6]
            
            # Get Record Types - 2 characters
            RecordTypeHex = lineContent[6:8]
            RecordTypeDec = int(RecordTypeHex, 16)

            if RecordTypeDec == 0:
                # Data
                tempData = self.ParseData(lineContent, byteCountDec)

                # Calculate Address
                tempAddress = BASE_ADDRESS + offsetAddr

                ### Save Address and Data
                tempDict = ({tempAddress: tempData})
                DataList.append(tempDict)
                
            elif RecordTypeDec == 1:
                # End of File
                break
            elif RecordTypeDec == 4:
                # Base Address
                BASE_ADDRESS = self.ParseData(lineContent, byteCountDec)
        
        return DataList

            

### Example ### 
# Object1 = ParseHexFile("D:/myFPT/Bootloader/NUCLEO/Blink_led - Cam/MDK-ARM/Blink_led/Blink_led.hex")
# DataList = Object1.ParseRawData()
# print(DataList)

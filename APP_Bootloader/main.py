import sys
import time, os, re
import serial
from serial import Serial
import serial.tools.list_ports

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QCheckBox, QTableWidget
)
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from BOOT_GUI import Ui_MainWindow

from DataTransfer import SerialConnect, SerialDataTransfer
from ParseHexFile import ParseFileHex

path = []
DataList = []

#################################################################
################## Main WINDOW for Show Config ##################
#################################################################
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.status = 0
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
	
    def connectSignalsSlots(self):
        self.BootButton.clicked.connect(self.BootFirmware)
        self.BrowseHexFile.clicked.connect(self.FindFiles)
        ### Serial Parameters
        self.comboComPort.activated[str].connect(self.SelectCOMPORT)
        self.comboDataSize.activated[str].connect(self.SelectDataSize)
        self.comboBaud.activated[str].connect(self.SelectBaudrate)
        self.comboStopBits.activated[str].connect(self.SelectStopbits)
        self.comboParity.activated[str].connect(self.SelectParity)
        ### Config Frame
        self.checkStartAddrEn.stateChanged.connect(self.checkStartAddr)
        self.checkFrameEn.stateChanged.connect(self.checkFrame)
        
        self.SetConfigBTN.clicked.connect(self.SetConfig)

    #############################################################
    ##################### Get Serial Parameters #################
    def SelectCOMPORT(self):
        comPort = self.comboComPort.currentText()
        return comPort

    def SelectDataSize(self):
        DataSize = self.comboDataSize.currentText()
        return DataSize
    
    def SelectBaudrate(self):
        Baudrate = self.comboBaud.currentText()
        return Baudrate
    
    def SelectStopbits(self):
        Stopbit = self.comboStopBits.currentText()
        return Stopbit

    def SelectParity(self):
        parity = self.comboParity.currentText()
        return parity

    #############################################################
    ################## Config Frame/Start Address ###############
    def checkStartAddr(self):
        if self.checkStartAddrEn.isChecked():
            return True
        else:
            return False

    def checkFrame(self):
        if self.checkFrameEn.isChecked():
            return True
        else:
            return False

    def SetConfig(self):
        SectorAvai = 0
        
        ### Get Serial Port Parameters ###
        comPort = str(self.SelectCOMPORT())
        baudrate = int(self.SelectBaudrate())
        dataSize = int(self.SelectDataSize())
        timeOut = int(self.TimeoutText.toPlainText())
        if self.SelectStopbits() == '1 bit':
            Stopbits = serial.STOPBITS_ONE
        else:
            Stopbits = serial.STOPBITS_TWO        

        ### Get Config Parameters ###
        if (self.checkStartAddr() == True):
            StartAddr = self.StartAddress.toPlainText()
        if (self.checkFrame() == True):
            StartFrame = self.StartFrame.toPlainText()
            EndFrame = self.EndFrame.toPlainText()
        
        ### Get Sector Number ###    
        SectorOBJ = self.SectorList.currentItem()
        if SectorOBJ == None:
            SectorAvai = 0
            QMessageBox.about(self, "Error", "Please Choose Sector to Boot Firmware!!!")
        else:
            SectorAvai = 1
            Sector = SectorOBJ.text()
        
        ### Check if COM Port Available ###
        listAvailablePort = [comport.device for comport in serial.tools.list_ports.comports()]
        
        ### Connect the COM Port if Available ###
        if (comPort not in listAvailablePort):
            self.status = 0
            QMessageBox.about(self, "Error", "This Com Port is not Available!!!")
            
        if (comPort in listAvailablePort) and (SectorAvai == 1):
            ### Get File Hex & Parse File ###
            if len(path) == 0:
                self.status = 0
                QMessageBox.about(self, "Error", "Please Choose File Hex!!!")
            else:
                print('ok')
                self.status = 1
                temp = ParseFileHex(str(path[0]))
                self.DataList = temp.ParseRawData()

            print('ok')
            self.SerialOBJ = SerialConnect(comPort, baudrate, dataSize, timeOut, Stopbits)
            self.ser = self.SerialOBJ.ConnectPort()
            print('Done')
                
    
    #############################################################
    ##################### Generate - Boot Start #################
    def FindFiles(self):
        ConfigPath = QFileDialog.getOpenFileName(self, "Open Hex File", "~", "Hex Files (*.hex)")
        self.textEdit.setText(ConfigPath[0])
        path.append(ConfigPath[0])

    def BootFirmware(self):
        # Start Transfer Firmware
        ### Handler and Transfer Data ###
        if self.status == 1:
            print('boot')
            DataOBJ = SerialDataTransfer(self.SerialOBJ, self.DataList, self.ser)
            print('ok')
            DataOBJ.ConvertRawDataToWord()
            print('Done')
        
        TIME_LIMIT = 100
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.001)
            self.GenProcess.setValue(count)


#################################################################
########################## MAIN FUNCTION ########################
#################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

#################################################################
#################################################################


import serial
import time

enab1 = [" 0x01 0x02 0x04 0x08 0x18 0x24",
         " 0x42 0x81 0x81 0x42 0x24 0x18",
         " 0x08 0x04 0x02 0x01 0x00 0x00",
         " 0x00 0x00 0x00 0x00 0x00 0x00",
         " 0xFE 0x10 0x10 0x10 0xFE 0x00",
         " 0xFE 0x92 0x92 0x92 0x92 0x00",
         " 0xFE 0x02 0x02 0x02 0x02 0x00",
         " 0xFE 0x02 0x02 0x02 0x02 0x00",
         " 0x7C 0x82 0x82 0x82 0x7C 0x00",
         " 0x00 0x00 0x00 0x00 0x00 0x00",
         " 0xFE 0x90 0x90 0x90 0x90 0x00",
         " 0xFE 0x90 0x90 0x90 0x6E 0x00",
         " 0x7C 0x82 0x82 0x82 0x7C 0x00",
         " 0xFE 0x40 0x20 0x40 0xFE 0x00"]

enab2 = [" 0x80 0x40 0x20 0x10 0x18 0x3C",
         " 0x7E 0xFF 0xFF 0x7E 0x3C 0x18",
         " 0x10 0x20 0x40 0x80 0x00 0x00",
         " 0x00 0x00 0x00 0x00 0x00 0x00",
         " 0x00 0x00 0x00 0x00 0x00 0x00",
         " 0x80 0x80 0xFE 0x80 0x80 0x00",
         " 0xFE 0x90 0x90 0x90 0x6E 0x00",
         " 0x7C 0x82 0x82 0x82 0x7C 0x00",
         " 0x80 0x60 0x1E 0x60 0x80 0x00",
         " 0x00 0x00 0x00 0x00 0x00 0x00",
         " 0xFE 0x40 0x38 0x04 0xFE 0x00",
         " 0x80 0x60 0x1E 0x60 0x80 0x00",
         " 0x00 0x00 0xFA 0x00 0x00 0x00"]  

pirate = serial.Serial("/dev/ttyUSB0", 115200)

def initializeBusPirate():
  pirate.write(bytes("m\n", 'UTF-8'))
  time.sleep(0.05)
  pirate.write(bytes("4\n", 'UTF-8'))
  time.sleep(0.05)
  pirate.write(bytes("4\n", 'UTF-8'))
  time.sleep(0.05)
  pirate.write(bytes("W\n", 'UTF-8'))
  time.sleep(0.05)
  pirate.write(bytes("P\n", 'UTF-8'))
  time.sleep(0.05)

def initializeSSD1306 ():
  pirate.write(bytes("a\nA\n", 'UTF-8'))
  time.sleep(0.05)
  pirate.write(bytes("[0x78 0x00 0x10 0x40 0x81 0x7f 0xa1 0xa6 0xa8 0x0f 0xd3 0x00 0xd5 0xf0 0xd9 0x22 0xda 0x02 0xdb 0x49 0x8d 0x14 0xaf]\n", 'UTF-8'))
  time.sleep(0.05)

  for x in range(0, 127):
    pirate.write(bytes("[0x78 0x40 0x00]\n", 'UTF-8'))
    time.sleep(0.01)

  selectLine(0)

  for x in range(0, 127):
    pirate.write(bytes("[0x78 0x40 0x00]\n", 'UTF-8'))
    time.sleep(0.01)

def writeBlock (inp):
  for row in inp:
    pirate.write(bytes("[0x78 0x40" + row + "]\n", 'UTF-8'))
    time.sleep(0.05)

def selectLine (lineNumber):
  lineCodes = [ "0xB1", "0xB0" ]
  pirate.write(bytes("[0x78 0x00 0x00 0x10 " + lineCodes[lineNumber] + "]\n", 'UTF-8'))
  time.sleep(0.02)
  
initializeBusPirate()
initializeSSD1306()

selectLine(0)
writeBlock(enab1)
selectLine(1)
writeBlock(enab2)

pirate.close()



    def open_power(self):
        serial_com = self.combox_power_com.currentText()
        serials = serial.Serial(serial_com, 9600)
        serials.write('{\"A01\":110000}'.encode())
        serials.close()
            
    def close_power(self):
        serial_com = self.combox_power_com.currentText()
        serials = serial.Serial(serial_com, 9600)
        serials.write('{\"A01\":100000}'.encode())
        serials.close()   

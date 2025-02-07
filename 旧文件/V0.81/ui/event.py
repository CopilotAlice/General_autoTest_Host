# 各类点击事件
class MainWindowEvent:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow
        self.mw = mainWindow
        # self.mainWindow.pushButton_debug_2.clicked.connect(self.clkEvent_pushbutton2)
        # self.event_clk_count = 0


# ------------------接收转发/卫导数据接收&转发--------------
    


    # def clkEvent_pushbutton2(self):
    #     self.event_clk_count+=1
    #     self.mainWindow.textBrowser_debug_4.append('{} {} click enent'.format( self.mainWindow.normal_time ,'clkEvent_pushbutton2' ))
    #     self.mainWindow.clk_couts+=1
    #     self.mainWindow.new_constants.append(self .event_clk_count)
    #     print('{} {}'.format( self.mainWindow.clk_couts,self.mainWindow.new_constants ))




# ------------------接收转发/卫导数据接收&转发--------------
    def clkEvent_recforward_all(self):
        checked = self.mainWindow.checkBox_recforward_all.isChecked()
        for checkbox in self.mainWindow.init_ui.recforward_check_list:
            checkbox.setChecked(checked)

    def changeEvent_recforward(self):
        recforward_text = self.mainWindow.textEdit_recforward_msg.toPlainText()
        print(recforward_text)
        rf_list = recforward_text.split(',')


# ---------------卫导接收事件-----------------
    def changeEvent_auxsate_com(self):
        self.mw.combox_set_com_13.setCurrentText(self.mw.comboBox_ascii_com.currentText())
    def changeEvent_auxsate_baund(self):
        self.mw.combox_set_baund_13.setCurrentText(self.mw.comboBox_ascii_baund.currentText())
    def changeEvent_auxsate_check(self):
        self.mw.comboBox_set_check_13.setCurrentText(self.mw.comboBox_ascii_check.currentText())
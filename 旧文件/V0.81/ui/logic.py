# �����߼��¼�
class MainWindowLogic:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow
        self.mw = mainWindow
        
        self.logic_recforward()
        # �������������¼��߼�
        self.logic_auxsate()

    
    def logic_recforward(self):
        self.mainWindow.textEdit_recforward_msg.textChanged.connect(self.mainWindow.events.changeEvent_recforward)
        self.mainWindow.checkBox_recforward_all.clicked.connect(self.mainWindow.events.clkEvent_recforward_all)

    def logic_auxsate(self):
        self.mw.comboBox_ascii_com.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_com)
        self.mw.comboBox_ascii_baund.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_baund)
        self.mw.comboBox_ascii_check.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_check)
    
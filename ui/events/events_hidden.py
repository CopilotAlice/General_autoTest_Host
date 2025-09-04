from PyQt5.QtWidgets import QApplication,QWidget
class MainWindowEventHidden:
    def __init__(self, mainWindow):
        self.mw = mainWindow
        self.logic_clickHidden()
        self.logic_changeHidden()
    
    # groupbox点击隐藏其下的所有模块
    def logic_clickHidden(self):
        self.mw.groupBox_sate_config.toggled.connect(self.clickEvent_childHidden)
        self.mw.groupBox_sate_show.toggled.connect(self.clickEvent_childHidden)
        self.mw.groupBox_turntable.toggled.connect(self.clickEvent_childHidden)
        self.mw.groupBox_turntable3x.toggled.connect(self.clickEvent_childHidden)
        self.mw.groupBox_module_ascii.toggled.connect(self.clickEvent_childHidden)
    def clickEvent_childHidden(self,checked):
        sender = self.mw.sender()
        for child in sender.findChildren(QWidget):
            if child is not sender:
                child.setVisible(checked)
    
    # 当通用装订未选择内容时，自动隐藏首页内容
    def logic_changeHidden(self):
        self.mw.comboBox_general_rule.currentTextChanged.connect(self.changeEvent_buttonHidden)
    def changeEvent_buttonHidden(self):
        text = self.mw.comboBox_general_rule.currentText()
        if text in [
            '选择协议','None',''
        ]:
            self.mw.widget_quickButton.setVisible(False)
        else:
            self.mw.widget_quickButton.setVisible(True)
            
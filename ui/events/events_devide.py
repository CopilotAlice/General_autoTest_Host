# 逻辑及事件
from funs.fun_serial import *
class MainWindowEventDevide:
    def __init__(self, mainWindow):
        self.mw = mainWindow
        self.logic_tempBox()
        self.logic_turntable3x()

    # 点击温箱控制按钮
    def logic_tempBox(self):
        self.mw.pushButton_tempbox_set.clicked.connect(self.clickEvent_tempbox_set)
    # 温箱控制逻辑事件
    def clickEvent_tempbox_set(self):
        temp_com = self.mw.comboBox_tempbox_com.currentText()
        temp_set = self.mw.lineEdit_tempbox_set.text()
        try:
            temp_int = int(temp_set)
        except ValueError:
            self.mw.showMsgList_devide.append('温度设置错误:{}℃'.format(temp_set))
            return
        send_msg_list = [
            'TEMP,S{}'.format(temp_int),
            'POWER,ON'
        ]
        result,msg_list,emsg = tryOpenAndSend(temp_com,baund=9600,msgList=send_msg_list,msgType='ascii')
        if isinstance(msg_list, str):
            msg_list = [msg_list]
        if len(msg_list) == 0:
            msg_list = ['温箱无返回信息']
        self.mw.showMsgList_devide+= msg_list
        if not result:
            self.mw.debugMsgList_devide.append('温箱控制失败:{}'.format(emsg))
            
    # 三轴转台逻辑事件
    def logic_turntable3x(self):
        self.mw.pushButton_turntable3x_set.clicked.connect(self.clickEvent_turntable3x_set)
        
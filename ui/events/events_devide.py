# 逻辑及事件
from funs.fun_serial import *
class MainWindowEventDevide:
    def __init__(self, mainWindow):
        self.mw = mainWindow
        self.logic_tempBox()
        self.logic_turntable3x()


    '''
    温箱控制相关
    点击[定值启动]按钮
    尝试开启串口，发送设定温度及启动命令
    将返回信息显示在显示信息列表中
    '''
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
            msg_list = ['温箱无回读信息']
        self.mw.showMsgList_devide+= msg_list
        if not result:
            self.mw.debugMsgList_devide.append('温箱控制失败:{}'.format(emsg))
            
            
    '''
    三轴转台相关
    点击[打开串口]按钮 尝试使用结构体中的串口参数开启串口
    点击[关闭串口]按钮 关闭串口
    点击[发送命令]按钮 发送命令
    点击[转台转动]按钮 发送转动命令
    '''
    # 三轴转台逻辑事件
    def logic_turntable3x(self):
        self.mw.pushButton_turntable3x_open.clicked.connect(self.clickEvent_turntable3x_open)
        self.mw.pushButton_turntable3x_close.clicked.connect(self.clickEvent_turntable3x_close)
        self.mw.pushButton_turntable3x_command.clicked.connect(self.clickEvent_turntable3x_command)
        self.mw.pushButton_turntable3x_turn.clicked.connect(self.clickEvent_turntable3x_turn)
    # 点击三轴转台打开串口
    def clickEvent_turntable3x_open(self):
        com = self.mw.comboBox_turntable3x_com.currentText()
        if self.mw.struct_turntable3x.serial_com == com:
            self.mw.debugMsgList_devide.append('三轴转台串口未改变')
        self.mw.struct_turntable3x.serial_com = com
        result,emsg = self.mw.struct_turntable3x.serial_open()
        if not result:
            self.mw.debugMsgList_devide.append('三轴转台串口打开失败:{}'.format(emsg))
        while len(self.mw.struct_turntable3x.list_debugMsg) > 0:
            self.mw.debugMsgList_devide.append(self.mw.struct_turntable3x.list_debugMsg.pop(0))
    # 点击三轴转台关闭串口
    def clickEvent_turntable3x_close(self):
        result,emsg = self.mw.struct_turntable3x.serial_close()
        if not result:
            self.mw.debugMsgList_devide.append('三轴转台串口打开失败:{}'.format(emsg))
            self.mw.debugMsgList_devide.append(self.mw.struct_turntable3x.list_debugMsg.pop(0))
    # 点击三轴转台发送命令
    def clickEvent_turntable3x_command(self):
        if self.mw.struct_turntable3x.serial is None:
            self.clickEvent_turntable3x_open()
        command = self.mw.comboBox_turntable3x_command.currentText()
        
        if command=='转台急停':
            result = self.mw.struct_turntable3x.sendMsg_stp()
        elif command=='通讯检查':
            result = self.mw.struct_turntable3x.sendMsg_chk()
        elif command=='进入远控':
            result = self.mw.struct_turntable3x.sendMsg_rem()
        elif command=='返回本控':
            result = self.mw.struct_turntable3x.sendMsg_loc()
        elif command=='开启使能':
            result = self.mw.struct_turntable3x.sendMsg_enb()
        elif command=='断开使能':
            result = self.mw.struct_turntable3x.sendMsg_dis()
        elif command=='转台寻零':
            result = self.mw.struct_turntable3x.sendMsg_hmz()
        elif command=='运行模式':
            list_input = self.turntable3x_get_input()
            result = self.mw.struct_turntable3x.sendMsg_mod(*list_input[-3:])
        elif command=='位置设置':
            list_input = self.turntable3x_get_input()
            result = self.mw.struct_turntable3x.sendMsg_pos(*list_input[:3])
        elif command=='速度设置':
            list_input = self.turntable3x_get_input()
            result = self.mw.struct_turntable3x.sendMsg_vel(*list_input[3:6])
        elif command=='转台运行':
            result = self.mw.struct_turntable3x.sendMsg_run()
        elif command=='转台停止':
            result = self.mw.struct_turntable3x.sendMsg_stp()
        elif command=='状态查询':
            result = self.mw.struct_turntable3x.sendMsg_sts()
        else:
            self.mw.debugMsgList_devide.append('未知命令:{}'.format(command))
            return
        while len(self.mw.struct_turntable3x.list_showMsg) > 0:
            msg = self.mw.struct_turntable3x.list_showMsg.pop(0)
            self.mw.lineEdit_turntable3x_returnMsg.setText(msg)
        while len(self.mw.struct_turntable3x.list_debugMsg) > 0:
            msg = self.mw.struct_turntable3x.list_debugMsg.pop(0)
            self.mw.debugMsgList_devide.append(msg)
            
    # 点击三轴转台转动
    def clickEvent_turntable3x_turn(self):
        list_input = self.turntable3x_get_input()
        self.mw.struct_turntable3x.sendMsg_mod(*list_input[-3:])
        self.mw.struct_turntable3x.sendMsg_pos(*list_input[:3])
        self.mw.struct_turntable3x.sendMsg_vel(*list_input[3:6])
        self.mw.struct_turntable3x.sendMsg_run()
        
        while len(self.mw.struct_turntable3x.list_showMsg) > 0:
            msg = self.mw.struct_turntable3x.list_showMsg.pop(0)
            self.mw.lineEdit_turntable3x_returnMsg.setText(msg)
        while len(self.mw.struct_turntable3x.list_debugMsg) > 0:
            msg = self.mw.struct_turntable3x.list_debugMsg.pop(0)
            self.mw.debugMsgList_devide.append(msg)
        
            
    def turntable3x_get_input(self):
        list_result_input = []
        for lineEdit in self.mw.list_turntable3x_input:
            if lineEdit.text() == '':
                list_result_input.append(0)
            else:
                try:
                    list_result_input.append(int(lineEdit.text()))
                except ValueError:
                    list_result_input.append(0)
                    self.mw.debugMsgList_devide.append('三轴输入错误:{}'.format(lineEdit.text()))
        return list_result_input
        
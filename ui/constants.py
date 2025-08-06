# 全局变量/结构体控制模块
# 全局变量/结构体控制模块
import os
import serial
import time
from ui.structs import *
from funs.fun_locals import *
class MainWindowConstants:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        # 待完成 载入配置文件
        self.init_load_path()

        # 初始化结构体 12路设置内容
        self.structList_12tab = []
        self.init_12tab_setting()

        # 初始化结构体 通用装订规则 
        self.struct_general_bind = None
        self.init_general_bind()
        
        # 初始化结构体 发送卫导数据
        self.init_send_struct()
        # 初始化结构体 发送卫导数据
        self.init_send_struct()
        
        # # 初始化结构体 装订信息缓存
        # self.init_send_cache()
        
    # 初始化载入文件全局变量
    def init_load_path(self):
        self.load_filepath = os.getcwd()
        
    # 初始化结构体 12路设置内容
    def init_12tab_setting(self):
        self.structList_12tab = []
        self.structList_12tab.append(struct_tab_setting(self.mw,'all'))
        for i in range(14):
            self.structList_12tab.append(struct_tab_setting(self.mw,i+1))
        self.cache_sendHexList = []
        for i in range(12):
            self.cache_sendHexList.append('')
        self.cache_sendAsciiList = []
        for i in range(12):
            self.cache_sendAsciiList.append('')
        
    def init_general_bind(self):
        self.mw.class_general_bind = struct_general_bind()
    
    # 初始化结构体 发送卫导数据
    def init_send_struct(self):
        lists = [
            self.mw.settings.sate_append_sate,
            self.mw.settings.sate_save_sate,
            self.mw.settings.sate_save_GNGGA,
            self.mw.settings.sate_save_GPGGA,
            self.mw.settings.sate_save_BDGGA,
            self.mw.settings.sate_save_GPVTG,
            self.mw.settings.sate_save_HEADINGA,
            self.mw.settings.sate_save_KSXT
        ]
        self.struct_sate = struct_sate()
        self.struct_sate.init_sate_save(lists)


class turnTable3x:
    def __init__(self):
        self.list_debugMsg = []
        self.list_showMsg = []
        self.list_mode = [0, 0, 0]  # 运行模式
        self.list_commandLocation = [0, 0, 0]
        self.list_commandSpeed = [0, 0, 0]
        self.list_commandAcceleration = [10, 10, 10]
        self.flag_theading = False
        self.serial = None
        self.serial_com = 'COM1'
        self.serial_check = False

    def append_debugMsg(self, msg):
        if isinstance(msg, list):
            msg = ', '.join([str(i) for i in msg])
        self.list_debugMsg.append(str(msg))
        while len(self.list_debugMsg) > 10:
            self.list_debugMsg.pop(0)

    def append_showMsg(self, msg):
        if isinstance(msg, list):
            msg = ', '.join([str(i) for i in msg])
        self.list_showMsg.append(str(msg))
        while len(self.list_showMsg) > 100:
            self.list_showMsg.pop(0)
    def serial_open(self):
        if self.serial is None:
            try:
                self.serial = serial.Serial(self.serial_com, 115200)
            except Exception as e:
                self.append_debugMsg('开启串口异常: {}'.format(e))
                self.serial = None
        else:
            try:
                self.serial.close()
                self.serial = None
                self.serial = serial.Serial(self.serial_com, 115200)
            except Exception as e:
                self.append_debugMsg('重启串口异常: {}'.format(e))
                self.serial = None

    def serial_close(self):
        if self.serial is None:
            return True
        else:
            try:
                self.serial.close()
                self.serial = None
            except Exception as e:
                self.append_debugMsg('重启串口异常: {}'.format(e))
    # 尝试读取串口数据
    def serial_tryRec(self, tryCount=10, waitTime=0.02):
        count = 0
        while count < tryCount:
            count += 1
            try:
                wait = self.serial.in_waiting
                if wait > 0:
                    recdata = self.serial.read(wait)
                    return recdata
            except Exception as e:
                self.append_debugMsg('获取数据错误: {}'.format(e))
                time.sleep(waitTime)
        return False
    # 尝试发送和读取校验
    def sendAndRec(self, sendMsg='', recMsg=''):
        if len(sendMsg) > 0:
            # print('sendMsg: {}'.format(sendMsg))
            try:
                self.serial.write(sendMsg.encode())
            except Exception as e:
                self.append_debugMsg('tt_chk send error: {}'.format(e))
                return False
        try:
            rec = self.serial_tryRec()
            if not rec:
                self.append_debugMsg('未接收到转台指令')
                return False
            if len(recMsg) > 0:
                if recMsg in rec.decode():
                    return True
                else:
                    self.append_showMsg('回读校验失败: {}'.format(recMsg))
                    self.append_debugMsg(
                        '回读校验失败: send:<{}> check:<{}> rec:<{}>'.format(sendMsg, recMsg, rec.decode())
                    )
                    return False
            else:
                return rec.decode()
        except Exception as e:
            self.append_debugMsg('tt_chk rec error: {}'.format(e))
            return False
        return False

    # 通讯校验和
    def sumCheckAscii(self, string):
        return sum(ord(c) for c in string) & 0xFF

    # 通讯检查
    def sendMsg_chk(self):
        return self.sendAndRec('$MNCHK,1*CE\r\n', '$ASCHK,OK*30')
    # 进入远控
    def sendMsg_rem(self):
        return self.sendAndRec('$MNREM,1*DC\r\n', '$ASREM,OK*3E')
    # 返回本控
    def sendMsg_loc(self):
        return self.sendAndRec('$MNLOC,1*D6\r\n', '$ASLOC,OK*38')
    # 使能
    def sendMsg_enb(self):
        return self.sendAndRec('$MNENB,1*CD\r\n', '$ASENB,OK*2F')
    # 断开使能
    def sendMsg_dis(self):
        return self.sendAndRec('$MNDIS,1*D8\r\n', '$ASDIS,OK*3A')
    # 转台寻零
    def sendMsg_hmz(self):
        return self.sendAndRec('$MNHMZ,1*E7\r\n', '$ASHMZ,OK*49')
    # 运行模式
    def sendMsg_mod(self, a, b, c):
        msg_list = [a, b, c]
        for i in msg_list:
            if str(i) not in ['0', '1', '2']:
                self.append_showMsg('转台运行模式设置错误: {}'.format([a, b, c]))
                return False
        sendMsg = 'MNMOD,{},{},{}'.format(a, b, c)
        recMsg = 'ASMOD,{},{},{},OK'.format(a, b, c)
        return self.sendAndRec(
            '${}*{:02X}\r\n'.format(sendMsg, self.sumCheckAscii(sendMsg)),
            '${}*{:02X}'.format(recMsg, self.sumCheckAscii(recMsg))
            )
    # 位置设置
    def sendMsg_pos(self, a, b, c):
        msg_list = [a, b, c]
        for i in msg_list:
            try:float(i)
            except:
                self.append_showMsg('转台位置设置错误: {}'.format([a, b, c]))
                return False
        sendMsg = 'MNPOS,{},{},{}'.format(a, b, c)
        recMsg = 'ASPOS,{},{},{},OK'.format(a, b, c)
        return self.sendAndRec(
            '${}*{:02X}\r\n'.format(sendMsg, self.sumCheckAscii(sendMsg)),
            '${}*{:02X}'.format(recMsg, self.sumCheckAscii(recMsg))
            )
    # 速度设置
    def sendMsg_vel(self, a, b, c):
        msg_list = [a, b, c]
        send_list = []
        for i in msg_list:
            try:send_list.append(float(i))
            except:
                self.append_showMsg('转台速度设置错误: {}'.format([a, b, c]))
                return False
        sendMsg = 'MNVEL,{},{},{}'.format(a, b, c)
        recMsg = 'ASVEL,{},{},{},OK'.format(a, b, c)
        return self.sendAndRec(
            '${}*{:02X}\r\n'.format(sendMsg, self.sumCheckAscii(sendMsg)),
            '${}*{:02X}'.format(recMsg, self.sumCheckAscii(recMsg))
            )
    # 加速度设置
    def sendMsg_acc(self, a, b, c):
        msg_list = [a, b, c]
        for i in msg_list:
            try:float(i)
            except:
                self.append_showMsg('转台加速度设置错误: {}'.format([a, b, c]))
                return False
        sendMsg = 'MNACC,{},{},{}'.format(a, b, c)
        recMsg = 'ASACC,{},{},{},OK'.format(a, b, c)
        return self.sendAndRec(
            '${}*{:02X}\r\n'.format(sendMsg, self.sumCheckAscii(sendMsg)),
            '${}*{:02X}'.format(recMsg, self.sumCheckAscii(recMsg))
            )
    # 运行
    def sendMsg_run(self):
        return self.sendAndRec('$MNRUN,1*ED\r\n', '$ASRUN,OK*4F')
    # 停止
    def sendMsg_stp(self):
        return self.sendAndRec('$MNSTP,1*EF\r\n', '$ASSTP,OK*51')
    # 状态查询
    def sendMsg_sts(self):
        return self.sendAndRec('$MNSTS,1*F2\r\n', '')
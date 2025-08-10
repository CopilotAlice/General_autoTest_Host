import struct 
import ctypes
import time
import numpy as np
import pandas as pd
from funs.fun_chy2 import *
from funs.fun_sate import *
from PyQt5 import QtWidgets, QtGui, QtCore







# 结构体 通用装订规则
class struct_general_bind:
    def __init__(self):
        self.struct_path = './'
        self.struct_name = 'general_bind'
        self.struct_decode = 'xcbB?hHiIlLqQfdspPtyY'
        self.struct_format = '<'
        self.struct_packRule = ''
        self.struct_len = 0
        self.struct_sendHz = 1
        self.struct_packList = []
        self.struct_paraList = []
        self.struct_titlList = []
        self.struct_dataList = []
        self.struct_buttonList = []
        self.struct_default = ''
        self.struct_typeCheck = 'None'
        self.struct_ruleCheck = False
        self.struct_debugList = []
        self.struct_debugFlag = False
        
    def read_struct_file(self,struct_file):
        self.init_structList()
        if len(struct_file)==0:
            return 
        for line in struct_file.split('\n'):
            split_data = line.split()
            if len(split_data)<3:
                continue
            if line.startswith('#'):
                tar = split_data[1].lower()
                val = split_data[2]
                if 'default' in tar:
                    self.struct_default = ''.join(split_data[2:])
                if ('rulehead' in tar)|('format' in tar):
                    self.struct_format = try_return_format(val)
                if ('send_hz' in tar)|('autohz' in tar):
                    self.struct_sendHz = try_return_int(val,1)
                if 'sum' in tar.lower():
                    self.struct_typeCheck = 'sum'
                    self.struct_ruleCheck = try_return_checkRule(val)
                if 'crc' == tar.lower():
                    self.struct_typeCheck = 'crc'
                    self.struct_ruleCheck = try_return_checkRule(val)
                if 'crc16' == tar.lower():
                    self.struct_typeCheck = 'crc16'
                    self.struct_ruleCheck = try_return_checkRule(val)
                if 'crc32' == tar.lower():
                    self.struct_typeCheck = 'crc32'
                    self.struct_ruleCheck = try_return_checkRule(val)
                if 'crc_mcrf4' == tar.lower():
                    self.struct_typeCheck = 'crc_mcrf4'
                    self.struct_ruleCheck = try_return_checkRule(val)
                if 'button' in tar.lower():
                    self.struct_buttonList.append([val,''.join(split_data[3:])])
                    
            elif len(split_data)<4:
                self.struct_debugList.append('未知规则行:{}'.format(line))
            elif split_data[0] in self.struct_decode:
                self.struct_packList.append(split_data[0])
                self.struct_paraList.append(try_return_num(split_data[1]))
                self.struct_titlList.append(split_data[2])
                self.struct_dataList.append(split_data[3])
            else:
                self.struct_debugList.append('未知规则行:{}'.format(line))
                continue
        self.get_struct_len()
    def init_structList(self):
        self.struct_ruleCheck = False
        self.struct_typeCheck = 'None'
        self.struct_packList = []
        self.struct_paraList = []
        self.struct_titlList = []
        self.struct_dataList = []
        self.struct_buttonList = []
        self.struct_debugList = []
    def get_struct_len(self):
        self.struct_len = 0
        self.struct_packRule = self.struct_format+''.join(self.struct_packList)
        self.struct_len = struct.calcsize(self.struct_packRule)
        return self.struct_len,self.struct_packRule 
      
      
        
class struct_tab_setting:
    def __init__(self,mw,tab=1):
        self.tab = tab  
        self.com = mw.findChild( QtWidgets.QComboBox,'combox_set_com_{}'.format(tab) )
        self.baund = mw.findChild( QtWidgets.QComboBox,'combox_set_baund_{}'.format(tab) )
        self.check = mw.findChild( QtWidgets.QComboBox,'comboBox_set_check_{}'.format(tab) )
        self.stop = mw.findChild( QtWidgets.QComboBox,'comboBox_stopbit_{}'.format(tab) )
        self.open = mw.findChild( QtWidgets.QPushButton,'pushButton_com_open_{}'.format(tab) )
        self.name = mw.findChild( QtWidgets.QLineEdit,'lineEdit_file_names_{}'.format(tab) )
        self.plan = mw.findChild( QtWidgets.QLineEdit,'lineEdit_plan_names_{}'.format(tab) )
        self.rule = None
        
        self.flag_open = (self.open.text()=='开启')
    
    def set_com(self,com='COM1'):
        self.com.setCurrentText(str(com))
    def set_baund(self,baund=115200):
        self.baund.setCurrentText(str(baund))
    def set_check(self,check='无校验'):
        self.check.setCurrentText(str(check))
    def set_stop(self,stop='Stop1'):
        
        self.stop.setCurrentText(str(stop))
    def set_open(self,open='开启'):
        self.open.setText(str(open))
        self.flag_open = (open=='开启')
    def switch_open(self):
        self.open.setText('关闭' if self.get_open_flag() else '开启') 
    def set_name(self,name='autosave'):
        self.name.setText('{}_{}'.format(name,self.tab))
    def set_plan(self,plan=''):
        self.plan.setText(str(plan))
        
    def get_com(self):
        return self.com.currentText()
    def get_baund(self):
        return self.baund.currentText()
    def get_check(self):
        return self.check.currentText()
    def get_stop(self):
        return self.stop.currentText()
    def get_open(self):
        return self.open.text()
    def get_open_flag(self):
        return self.open.text()=='开启'
    def get_name(self):
        return self.name.text()
    def get_plan(self):
        return self.plan.text()

class struct_sate:
    def __init__(self):
        self.flag_sate_receive = False
        self.threading_flag_sate = False
        # 卫导串口
        self.serials = None
        # 发送缓存
        self.list_sate_send = []
        # 接收缓存
        self.list_sate_receive = []     
        # 分类接收缓存
        self.list_sate_ascii_msg = []
        for i in range(8):
            self.list_sate_ascii_msg.append([])
        # 分类保存缓存
        self.list_sate_flag = []
        for i in range(8):
            self.list_sate_flag.append(False)
        # 分类保存文件名
        self.list_sate_name = []
        for i in range(8):
            self.list_sate_name.append('')
        # 添加卫导标题
        self.list_sate_titl = []
        for i in range(8):
            self.list_sate_titl.append([])
        # 添加卫导长度
        self.list_sate_leng = []
        for i in range(8):
            self.list_sate_leng.append(0)
        # 处理后保存卫导数据
        self.list_sate_msg = []
        for i in range(8):
            self.list_sate_msg.append([])

        
        self.init_sate_name()
        self.init_sate_titl()
        self.init_sate_leng()
        self.init_sate_zero()
        self.init_sate_shap()

    
    def init_sate_name(self):
        self.list_sate_name[0] = '发送'
        self.list_sate_name[1] = '反馈'
        self.list_sate_name[2] = '$GNGGA'
        self.list_sate_name[3] = '$GPGGA'
        self.list_sate_name[4] = '$BDGGA'
        self.list_sate_name[5] = '$GNVTG'
        self.list_sate_name[6] = '#HEADINGA'
        self.list_sate_name[7] = '$KSXT'
    
    def init_sate_save(self,lists):
        for i in range(8):
            self.list_sate_flag[i] = lists[i]
    def init_sate_titl(self):
        for i in range(3):
            shift = 2
            self.list_sate_titl[i+shift].append('纬度')
            self.list_sate_titl[i+shift].append('经度')
            self.list_sate_titl[i+shift].append('卫星')
            self.list_sate_titl[i+shift].append('精度')
            self.list_sate_titl[i+shift].append('高度')
        for i in range(1):
            shift = 5
            self.list_sate_titl[i+shift].append('真北航向')
            self.list_sate_titl[i+shift].append('磁北航向')
            self.list_sate_titl[i+shift].append('水平速度')
            self.list_sate_titl[i+shift].append('水平速度')
            self.list_sate_titl[i+shift].append('模式指示')
        for i in range(1):
            shift = 6
            self.list_sate_titl[i+shift].append('航向')
            self.list_sate_titl[i+shift].append('俯仰')
            self.list_sate_titl[i+shift].append('航向偏差')
            self.list_sate_titl[i+shift].append('俯仰偏差')
            self.list_sate_titl[i+shift].append('跟踪卫星')
            self.list_sate_titl[i+shift].append('使用卫星')
        for i in range(1):
            shift = 7
            self.list_sate_titl[i+shift].append('utc时间')
            self.list_sate_titl[i+shift].append('经度')
            self.list_sate_titl[i+shift].append('纬度')
            self.list_sate_titl[i+shift].append('海拔高')
            self.list_sate_titl[i+shift].append('东速')
            self.list_sate_titl[i+shift].append('北速')
            self.list_sate_titl[i+shift].append('天速')
    def init_sate_leng(self):
        for i in range(8):
            self.list_sate_leng[i] = len(self.list_sate_titl[i])
    def init_sate_zero(self):
        for i in range(8):
            pass
    def init_sate_shap(self):
        self.list_sate_msg = []
        for i in range(8):
            self.list_sate_msg.append([])
            for j in range(self.list_sate_leng[i]):
                self.list_sate_msg[i].append(0.0)



        
    def append_sare_send(self,send_data):
        self.list_sate_send.append('{}\r\n'.format(send_data).encode('ascii'))
        
    def append_sate_receive(self,receive_data):
        self.list_sate_receive.append(receive_data)
        self.replace_sate_receive()
    
    def replace_sate_receive(self):
        while len(self.list_sate_receive)>0:
            sate_data = self.list_sate_receive.pop(0)
            on_rule = False
            for i in range(6):
                if self.list_sate_name[i+2] in sate_data:
                    self.list_sate_ascii_msg[i+2].append(sate_data)
                    # print('{} :{}'.format(i,sate_data))
                    on_rule = True
                    if i<3:
                        self.list_sate_msg[i+2] = GPGGA2loc(sate_data)
                        # print(GPGGA2loc(sate_data))
                    elif i==3:
                        self.list_sate_msg[i+2] = GNVTG2loc(sate_data)
                    elif i==4:
                        self.list_sate_msg[i+2] = HEADINGA2loc(sate_data)
                    elif i==5:
                        self.list_sate_msg[i+2] = KSXT2loc(sate_data)
                    break
            if not on_rule:
                self.list_sate_ascii_msg[1].append(sate_data)
    def clear_sate_list(self,num):
        self.list_sate_msg[num] = [0]*len(self.list_sate_msg[num])

class clickEventThread_decodeShow(QtCore.QThread):
    update_signal = QtCore.pyqtSignal(str)
    def run(self):
        for i in range(10):
            time.sleep(1)
            self.update_signal.emit('事件更新:{}s'.format(i+1))
            

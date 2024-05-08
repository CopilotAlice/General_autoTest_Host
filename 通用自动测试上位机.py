from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from Automated_testing import Ui_MainWindow
from pyqtgraph.Qt import QtCore
import binascii
import datetime
import os
import serial
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import pandas as pd
import numpy as np
import serial
import serial.tools.list_ports as sports
import threading
import time
import os
import struct

# 设置pandas显示 多列显示和输出对齐
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
# pd.set_option('display.colheader_justify', 'left')
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("通用自动测试上位机_蔡_2404_V0.1")
        self.show_message_length = 30   # 显示的最大行数
        self.show_message_count = 0     # 显示提示次数
        
        # 初始化界面元素
        self.inside_location = 0.0
        self.inside_speed = 0.0
        self.outside_location = 0.0
        self.outside_speed = 0.0
        self.automatic_time = 0          # 自动测试时间  
        self.power_flag = False
        
        # 初始化使用元素
        self.short_time = '000000'
        self.normal_time = '00:00:00'
        self.show_message_automatic = None
        self.show_message_singletest = None
        
        # 初始化多线程标志位
        self.test_mode = None
        self.threading_test_flag = False        # 测试标志
        
        # debug调试状态
        self.debug_flag = False
        self.debug_read_rules = False
        self.bebug_binding = False
        self.debug_begin_test = False
        self.debug_threading = True
        
        # 初始化解算规则列表-新
        self.decode_rule_list = []    # 解算规则
        self.decode_save_list = []    # 是否保存
        self.decode_para_list = []    # 系数
        self.decode_titl_list = []    # 标题
        self.decode_cout_list = []    # 排序序号
        self.decode_sort_list = []    # 排序后列表
        self.decode_header_list = []    # 大小端
        
        
        # 配置文件路径
        self.para_com_filename = './配置文件/para_com.txt'
        self.para_config_filename = './配置文件/para_config.txt'
        self.model_list = [
            ['通讯','转台','电源','温箱','装订','自动'],
            ['protocal','turntable','power','tempbox','binding','automatic'],
            ['解算规则','标定规则','none','none','装订规则','自动规则']
        ]
        
        # 配置文件默认设置
        self.config_hold_time = 5           # 转台稳定后等待时间
        self.config_save_ms = 0             # 是否保存毫秒值 1True/0False
        self.config_save_BD_average = 1     # 是否将标定过程各点取均值存放
        self.config_save_BD_bin = 1         # 是否保存标定过程中16进制原始数
        self.config_save_BD_1file = 1       # 将标定过程各点存储到一个文件/多个文件
        self.config_power_model = 1         # 电源型号：1程控电源，2继电器
        self.config_special_flag = None     # 特殊标志位
        self.config_decode_header_type = 1  # 0:使用帧头模式/1:使用2帧头中间模式/2:使用帧头帧尾模式
        
        # 解算规则配置
        self.rules_lists_format = 'xcbB?hHiIlLqQfdspPtyY'   # 解算规则可用范围
        
        # 总控-刷新comboBox串口
        self.comboBox_update_com_flag = True
        self.comboBox_update_rules_flag = True
        self.comboBox_com_list = [self.comboBox_protocal_com, 
                                self.comboBox_turntable_com, 
                                self.comboBox_power_com,
                                self.comboBox_tempbox_com,
                                self.comboBox_binding_com,
                                self.combox_set_com_all]
        self.combox_com_list = [self.combox_set_com_1,
                                self.combox_set_com_2,
                                self.combox_set_com_3,
                                self.combox_set_com_4,
                                self.combox_set_com_5,
                                self.combox_set_com_6,
                                self.combox_set_com_7,
                                self.combox_set_com_8,
                                self.combox_set_com_9,
                                self.combox_set_com_10,
                                self.combox_set_com_11,
                                self.combox_set_com_12]
        self.combox_com_open_list = [self.pushButton_com_open_1,
                                    self.pushButton_com_open_2,
                                    self.pushButton_com_open_3,
                                    self.pushButton_com_open_4,
                                    self.pushButton_com_open_5,
                                    self.pushButton_com_open_6,
                                    self.pushButton_com_open_7,
                                    self.pushButton_com_open_8,
                                    self.pushButton_com_open_9,
                                    self.pushButton_com_open_10,
                                    self.pushButton_com_open_11,
                                    self.pushButton_com_open_12]
        self.comboBox_binding_list = [self.lineEdit_binding_latitude,
                                      self.lineEdit_binding_longitude,
                                      self.lineEdit_binding_height,
                                      self.lineEdit_binding_time]
        # 十二路开关切换
        for i in range(12):
            self.combox_com_open_list[i].clicked.connect(self.change_button)
        for binding in self.comboBox_binding_list:
            binding.textChanged.connect(self.binding_change)
        for combox in self.comboBox_com_list+self.combox_com_list:
            combox.view().setMinimumWidth(85)
            
        # 总控开关切换
        self.pushButton_com_open_all.clicked.connect(self.change_button_all)
        # 单路通讯协议同步多路更新
        self.comboBox_protocal_com.currentTextChanged.connect(self.protocal_com_change)
        self.comboBox_protocal_baund.currentTextChanged.connect(self.protocal_com_change)
        self.comboBox_protocal_check.currentTextChanged.connect(self.protocal_com_change)
        self.combox_set_com_1.currentTextChanged.connect(self.comboBox_com_change)
        self.combox_set_baund_1.currentTextChanged.connect(self.comboBox_com_change)
        self.comboBox_set_check_1.currentTextChanged.connect(self.comboBox_com_change)
        # 多路文件名同步更新
        self.lineEdit_file_names_all.textChanged.connect(self.filenames_change)
        # 规则更新同步
        # self.comboBox_protocal_rule.currentIndexChanged.connect(self.read_rules)
        self.pushButton_begin_test.clicked.connect(self.begin_test)
        self.pushButton_stop_test.clicked.connect(self.stop_test)
        
        
        self.show_timer_count0 = 0
        self.show_timer_count1 = 0
        self.show_timer_count2 = 0
        self.show_timer_count3 = 0
        
        # 打开软件自动更新一次所有状态
        self.show_message_01s()
        self.show_message_05s()
        self.show_message_1s()
        self.show_message_5s()
        
        
        # 读取默认配置文件
        self.read_default_para_com()
        self.read_default_para_config()
        
        # 事件0.5s更新
        self.show_timer0 = QTimer(self)
        self.show_timer0.timeout.connect(self.show_message_01s)
        self.show_timer0.start(100)
        # 事件0.5s更新
        self.show_timer1 = QTimer(self)
        self.show_timer1.timeout.connect(self.show_message_05s)
        self.show_timer1.start(500)
        # 事件1s更新
        self.show_timer2 = QTimer(self)
        self.show_timer2.timeout.connect(self.show_message_1s)
        self.show_timer2.start(1000)
        # 事件3s更新
        self.show_timer3 = QTimer(self)
        self.show_timer3.timeout.connect(self.show_message_5s)
        self.show_timer3.start(5000)
    
    # 事件更新0.1s线程，用于更新数据输出和绘图
    def show_message_01s(self):
        if self.show_message_automatic is not None:
            self.textBrowser_automatic_ruleline.append(self.show_message_automatic)
            self.show_message_automatic = None
            self.textBrowser_automatic_ruleline().setValue(self.textBrowser_automatic_ruleline().maximum())
        if self.show_message_singletest is not None:
            self.textBrowser_single_test.append(self.show_message_singletest)
            self.show_message_singletest = None
            self.textBrowser_single_test().setValue(self.textBrowser_single_test().maximum())
            
            
    # 事件更新0.5s线程，用于更新数据输出和绘图
    def show_message_05s(self):
        self.show_timer_count1 += 1
    # 事件更新1s线程，用于按秒更新界面元素
    def show_message_1s(self):
        self.show_timer_count2 += 1
        self.lcdNumber_inside_location.display('{:.2f}'.format(self.inside_location))
        self.lcdNumber_inside_speed.display('{:.2f}'.format(self.inside_speed))
        self.lcdNumber_outside_location.display('{:.2f}'.format(self.outside_location))
        self.lcdNumber_outside_speed.display('{:.2f}'.format(self.outside_speed))
        self.lcdNumber_automatic_time.display(int(self.automatic_time))
        self.radioButton_power_flag.setChecked(self.power_flag)
        # 转换时分秒
        self.test_time = datetime.datetime.now().strftime('%H%M%S')
        self.normal_time = datetime.datetime.now().strftime('%H:%M:%S')
    # 事件更新5s线程，用于更新串口等对时间不敏感内容
    def show_message_5s(self):
        self.show_timer_count3 += 1
        # 更新串口  #串口   #更新
        if self.comboBox_update_com_flag:
            plist = list(serial.tools.list_ports.comports())
            com_lists = []
            for com in plist:
                com_lists.append(str(list(com)[0]))
            # com_lists.sort()
            com_lists = sorted(com_lists,key=lambda x:int(x[3:]))
            for comboBox in self.comboBox_com_list+self.combox_com_list:
                select_combo = comboBox.currentText()
                comboBox.clear()
                comboBox.addItem('None')
                for com in com_lists:
                    comboBox.addItem(com)
                if select_combo in com_lists:
                    comboBox.setCurrentText(select_combo)
                else:
                    comboBox.setCurrentIndex(0)
        # 更新规则文件 #协议    #更新
        if self.comboBox_update_rules_flag:
            model_list = self.model_list
            for i in range(len(model_list[0])):
                file_path = model_list[2][i]
                if file_path.lower()=='none':
                    continue
                file_list = []
                for file_name in os.listdir('./'+file_path):
                    file_name = file_name.split('.txt')[0]
                    file_list.append(file_name)
                file_list.sort()
                comboBox = self.findChild(QtWidgets.QComboBox,'comboBox_%s_rule'%(model_list[1][i]))
                if comboBox is None:
                    if self.show_message_count<3:
                        self.show_message_count+=1
                        print('未找到对应控件：comboBox_%s_rule'%(model_list[1][i]))
                    continue
                select_combo = comboBox.currentText()
                comboBox.clear()
                comboBox.addItem('选择协议')
                for rule in file_list:
                    comboBox.addItem(rule)
                if select_combo in file_list:
                    comboBox.setCurrentText(select_combo)
                else:
                    comboBox.setCurrentIndex(0)
            
    # 多路开关按钮切换 20240425
    def change_button(self):
        sender = self.sender()
        sender.setText('开启') if sender.text()=='关闭' else sender.setText('关闭')
    # 多路开关总控 20240425
    def change_button_all(self):
        sender = self.sender()
        set_text = '开启' if sender.text()=='关闭' else '关闭'
        sender.setText(set_text)
        for i in range(12):
            button = self.findChild(QtWidgets.QPushButton,'pushButton_com_open_%s'%(i+1))
            if button is not None:
                button.setText(set_text)
            else:
                print('未找到对应控件：pushButton_com_open_%s'%(i+1))
    # 单路多路同步更新 20240425
    def protocal_com_change(self):
        protocal_com = self.comboBox_protocal_com.currentText()
        protocal_baund = self.comboBox_protocal_baund.currentText()
        protocal_check = self.comboBox_protocal_check.currentText()
        self.combox_set_com_1.setCurrentText(protocal_com)
        self.combox_set_baund_1.setCurrentText(protocal_baund)
        self.comboBox_set_check_1.setCurrentText(protocal_check)
    def comboBox_com_change(self):
        protocal_com = self.combox_set_com_1.currentText()
        protocal_baund = self.combox_set_baund_1.currentText()
        protocal_check = self.comboBox_set_check_1.currentText()
        self.comboBox_protocal_com.setCurrentText(protocal_com)
        self.comboBox_protocal_baund.setCurrentText(protocal_baund)
        self.comboBox_protocal_check.setCurrentText(protocal_check)
    # 多路文件名同步更新 20240425
    def filenames_change(self):
        filenames = self.lineEdit_file_names_all.text()
        for i in range(12):
            lineEdit = self.findChild(QtWidgets.QLineEdit,'lineEdit_file_names_%s'%(i+1))
            if lineEdit is not None:
                lineEdit.setText(filenames+'_'+str(i+1))
            else:
                print('未找到对应控件：lineEdit_file_names_%s'%(i+1))
    # 读取默认配置文件-全局串口 20240427
    def read_default_para_com(self):
        # 串口默认配置
        para_name = self.para_com_filename
        if not os.path.exists(para_name):
            self.textBrowser_automatic_ruleline.append('未读取到默认配置文件({})'.format(para_name))
        else:
            with open(para_name,'r',encoding='gb2312',errors='replace') as f:
                for line in f:
                    para_rule_list = line.split()
                    if line.startswith('#'):
                        continue
                    elif len(para_rule_list)<3:
                        continue
                    elif para_rule_list[1]=='protocal':
                        self.comboBox_protocal_com.setCurrentText(para_rule_list[2])
                        self.comboBox_protocal_baund.setCurrentText(para_rule_list[3])
                        self.comboBox_protocal_check.setCurrentText(para_rule_list[4])
                    elif para_rule_list[1]=='turntable':
                        self.comboBox_turntable_com.setCurrentText(para_rule_list[2])
                    elif para_rule_list[1]=='power':
                        self.comboBox_power_com.setCurrentText(para_rule_list[2])
                    elif para_rule_list[1]=='temp':
                        self.comboBox_tempbox_com.setCurrentText(para_rule_list[2])
                    elif para_rule_list[1]=='binding':
                        self.comboBox_binding_com.setCurrentText(para_rule_list[2])
                    elif 'tab_' in para_rule_list[1]:
                        self.findChild(QtWidgets.QComboBox,'combox_set_com_%s'%(para_rule_list[1][4:])).setCurrentText(para_rule_list[2])
                        self.findChild(QtWidgets.QComboBox,'combox_set_baund_%s'%(para_rule_list[1][4:])).setCurrentText(para_rule_list[3])
                        self.findChild(QtWidgets.QComboBox,'comboBox_set_check_%s'%(para_rule_list[1][4:])).setCurrentText(para_rule_list[4])
                        self.findChild(QtWidgets.QComboBox,'comboBox_stopbit_%s'%(para_rule_list[1][4:])).setCurrentText(para_rule_list[5])
                        self.findChild(QtWidgets.QPushButton,'pushButton_com_open_%s'%(para_rule_list[1][4:])).setText(para_rule_list[6])
                    else:
                        self.textBrowser_automatic_ruleline.append('未知配置项：%s'%(para_rule_list))
    # 读取默认配置文件-全局设置 20240507
    def read_default_para_config(self):
        para_name = self.para_config_filename
        if not os.path.exists(para_name):
            self.textBrowser_automatic_ruleline.append('未读取到默认配置文件({})'.format(para_name))
        else:
            with open(para_name,'r',encoding='gb2312',errors='replace') as f:
                for line in f:
                    para_rule_list = line.split()
                    if line.startswith('#'):
                        continue
                    elif len(para_rule_list)<3:
                        continue
                    # 默认转台速度设置
                    elif para_rule_list[1]=='in_spd':
                        self.lineEdit_inside_speed.setText(para_rule_list[2])
                    elif para_rule_list[1]=='in_acc':
                        self.lineEdit_inside_acceleration.setText(para_rule_list[2])
                    elif para_rule_list[1]=='out_spd':
                        self.lineEdit_outside_speed.setText(para_rule_list[2])
                    elif para_rule_list[1]=='out_acc':
                        self.lineEdit_outside_acceleration.setText(para_rule_list[2])
                    # 默认转台稳定后等待时间
                    elif para_rule_list[1]=='hold_time':
                        self.config_hold_time = int(para_rule_list[2])
                    # 是否保存毫秒值
                    elif para_rule_list[1]=='save_ms':
                        self.config_save_ms = int(para_rule_list[2])
                    # 是否保存标定各位置均值
                    elif para_rule_list[1]=='save_BD_average':
                        self.config_save_BD_average = int(para_rule_list[2])
                    # 是否将数据保存到一个文件中
                    elif para_rule_list[1]=='save_BD_1file':
                        self.config_save_BD_1file = int(para_rule_list[2])
                    # 是否保存标定16进制原始数
                    elif para_rule_list[1]=='save_BD_bin':
                        self.config_save_BD_bin = int(para_rule_list[2])
                    # 程控电源模式/继电器模式
                    elif para_rule_list[1]=='power_model':
                        self.config_power_model = int(para_rule_list[2])
                    # 默认使用对应规则列表中的对应序号
                    elif para_rule_list[1]=='default_protocal':
                        self.comboBox_protocal_rule.setCurrentIndex(int(para_rule_list[2]))
                    elif para_rule_list[1]=='default_turntable':
                        self.comboBox_turntable_rule.setCurrentIndex(int(para_rule_list[2]))
                    elif para_rule_list[1]=='default_binding':
                        self.comboBox_binding_rule.setCurrentIndex(int(para_rule_list[2]))
                    elif para_rule_list[1]=='default_automatic':
                        self.comboBox_automatic_rule.setCurrentIndex(int(para_rule_list[2]))
                    # 默认使用寻找帧头模式
                    elif para_rule_list[1]=='decode_header_type':
                        self.config_decode_header_type = int(para_rule_list[2])
                    else:
                        self.textBrowser_automatic_ruleline.append('未知配置项：%s'%(para_rule_list))
    # 读取载入解算规则文件  20240508
    # 读取规则文件并更新全局变量
    def read_rules(self):
        if self.debug_flag:
            print('def_read_rules')
        # 打开规则文件
        try:
            rule_name = self.comboBox_protocal_rule.currentText()
            if len(rule_name)==0:
                print('没有选择规则文件')
                return
            with open('./解算规则/{}.txt'.format(rule_name), 'r',encoding='gb2312') as file:
                rules = file.read()
        except Exception as e:
            self.textBrowser_automatic_ruleline.append('读取规则文件失败:'+str(e))
            return False
        # 规则初始化
        rules_lists_format = self.rules_lists_format
        decode_rule_list = []    # 解算规则
        decode_save_list = []    # 是否保存
        decode_para_list = []    # 系数
        decode_titl_list = []    # 标题
        decode_cout_list = []    # 排序序号
        decode_sort_list = []    # 排序后列表
        decode_header_list = []    # 大小端

        default_header = '>'     # 默认大小端

        decode_rule = []
        decode_save = []
        decode_para = []
        decode_titl = []
        decode_cout = []
        
        # 帧头帧尾
        self.decode_rule_header = b'' 
        self.decode_rule_ender = b'' 
        
        # 逐行读取规则文件
        for lines in rules.split('\n'):
            # 规则文件配置项
            if lines.startswith('#'):
                if len(lines.split())<3:
                    print('规则文件长度过少:{}'.format(lines))
                    continue
                # 波特率
                elif lines.split()[1].lower() == 'baund':
                    self.comboBox_protocal_baund.setCurrentText(lines.split()[2])
                    self.combox_set_baund_all.setCurrentText(lines.split()[2])
                # 校验位
                elif lines.split()[1].lower() == 'check':   
                    self.comboBox_protocal_check.setCurrentText(check2chinese(lines.split()[2]))
                    self.comboBox_set_check_all.setCurrentText(check2chinese(lines.split()[2]))
                # 帧头
                elif lines.split()[1].lower() == 'header':
                    self.decode_rule_header = bytes.fromhex(''.join(lines.split()[2:]))
                # 帧尾
                elif lines.split()[1].lower() == 'ender':
                    self.decode_rule_ender = bytes.fromhex(''.join(lines.split()[2:]))
                # 帧率
                elif lines.split()[1].lower() == 'comm_hz':
                    self.comm_hz = try_set_text(lines.split()[2],int,200)
                # 经度
                elif lines.split()[1].lower() == 'longitude':
                    self.lineEdit_binding_longitude.setText(lines.split()[2])
                # 纬度
                elif lines.split()[1].lower() == 'dimensions':
                    self.lineEdit_binding_latitude.setText(lines.split()[2])
                # 高度
                elif lines.split()[1].lower() == 'height':
                    self.lineEdit_binding_height.setText(lines.split()[2])
                # 对准时间
                elif lines.split()[1].lower() == 'alignment_time':
                    self.lineEdit_binding_time.setText(lines.split()[2])
                # 特殊标志位
                elif lines.split()[1].lower() == 'special_flag':
                    self.config_special_flag = lines.split()[2]
                    
                elif lines.split()[1].lower() == 'rulelist':
                    continue
                # 读取规则文件-新
                elif lines.split()[1].lower()=='rulehead':
                    if len(decode_rule)==0:
                        continue
                    else:
                        decode_rule_list.append(decode_rule)
                        decode_save_list.append(decode_save)
                        decode_para_list.append(decode_para)
                        decode_titl_list.append(decode_titl)
                        decode_cout_list.append(decode_cout)
                        decode_header_list.append(default_header)
                        
                        decode_rule = []
                        decode_save = []
                        decode_para = []
                        decode_titl = []
                        decode_cout = []
                    default_header = lines.split()[2]
                else:
                    if self.debug_flag | self.debug_read_rules:
                        print('未知规则:<{}>split:<{}>'.format(lines,lines.split()))
                    continue
            # 判断不合法规则
            elif len(lines)==0 | len(lines.split())==0:
                continue
            elif len(lines.split())<5:
                self.textBrowser_fileCsv.append('错误长度<{}>'.format(lines))
                continue
            elif lines.split()[0] not in rules_lists_format:
                self.textBrowser_fileCsv.append('不在解算规则范围内<{}>'.format(lines))
                continue
            # 读取合法规则文件
            else:
                # 读取规则文件-新
                lines_split = lines.split()
                decode_rule.append(lines_split[0])
                decode_save.append(lines_split[1])
                decode_para.append(lines_split[2])
                decode_titl.append(lines_split[3])
                decode_cout.append(lines_split[4])
        # 
        if len(decode_rule)!=0:
            decode_rule_list.append(decode_rule)
            decode_save_list.append(decode_save)
            decode_para_list.append(decode_para)
            decode_titl_list.append(decode_titl)
            decode_cout_list.append(decode_cout)
            decode_header_list.append(default_header)
    
        decode_sort_list = []
        for test_order in decode_cout_list:
            max_count = 0
            sorted_list = []
            for i in range(len(test_order)):
                if str(i) in test_order:
                    continue
                else:
                    max_count = i
                    break
            for i in range(len(test_order)):
                if test_order[i]=='N':
                    sorted_list.append(str(max_count))
                    max_count +=1
                else:
                    sorted_list.append(test_order[i])
            decode_sort_list.append(sorted_list)
        if self.debug_flag | self.debug_read_rules:
            print('读取规则文件')
            print('decode_rule_list:{}'.format(decode_rule_list))
            print('decode_save_list:{}'.format(decode_save_list))
            print('decode_para_list:{}'.format(decode_para_list))
            print('decode_titl_list:{}'.format(decode_titl_list))
            print('decode_cout_list:{}'.format(decode_cout_list))
            print('decode_sort_list:{}'.format(decode_sort_list))
            print('decode_header_list:{}'.format(decode_header_list))

        self.decode_rule_list = decode_rule_list    # 解算规则
        self.decode_save_list = decode_save_list    # 是否保存
        self.decode_para_list = decode_para_list    # 系数
        self.decode_titl_list = decode_titl_list    # 标题
        self.decode_cout_list = decode_cout_list    # 排序序号
        self.decode_sort_list = decode_sort_list    # 排序后列表
        self.decode_header_list = decode_header_list    # 大小端
        
        # self.comboBox_begin_axis.clear()
        # for i in range(len(title_sort)):
        #     self.comboBox_begin_axis.addItem('{} {}'.format(i,self.title_sorted[i]))
        # self.comboBox_begin_axis.setCurrentIndex(1)
                                                
        # self.textBrowser_fileCsv.append('主机规则载入完成')      
        # self.fileCsv_append_flag = True
    def binding_change(self):
        if self.bebug_binding:
            print('binding_change')
        binding_latitude = try_get_text(self.lineEdit_binding_latitude,float,0)
        binding_longitude = try_get_text(self.lineEdit_binding_longitude,float,0)
        binding_height = try_get_text(self.lineEdit_binding_height,float,0)
        binding_time = try_get_text(self.lineEdit_binding_time,float,0)
        binding_latitude = int(binding_latitude*1e7)
        binding_longitude = int(binding_longitude*1e7)
        binding_height = int(binding_height)
        binding_time = int(binding_time/5)

        command_list1 = ['55','AA']
        command_list = []
        command_list.append('FF')
        command_list.append('66')
        command_list+=hexcut2list(struct.pack('>i', binding_longitude).hex().upper())
        command_list+=hexcut2list(struct.pack('>i', binding_latitude).hex().upper())
        command_list+=hexcut2list(struct.pack('>i', binding_height).hex().upper())[-2:]
        command_list+=hexcut2list(struct.pack('>i', binding_time).hex().upper())[-1:]
        checks = struct.pack('B',calculate_checksum(bytes.fromhex(''.join(command_list)))).hex().upper()
        command_list.append(checks)
        if self.bebug_binding:
            print(' '.join(command_list1+command_list))
        self.lineEdit_binding_command.setText(' '.join(command_list1+command_list))
        
    def stop_test(self):
        if self.debug_flag:
            print('停止测试')
        self.threading_test_flag = False
    # 点击开始测试事件，判断测试模式
    def begin_test(self):
        if self.debug_flag:
            print('开启测试')
        self.read_rules()
        protocal_rule = self.comboBox_protocal_rule.currentText()
        protocal_com = self.comboBox_protocal_com.currentText()
        protocal_baund = self.comboBox_protocal_baund.currentText()
        protocal_check = self.comboBox_protocal_check.currentText()
        turntable_rule = self.comboBox_turntable_rule.currentText()
        turntable_com = self.comboBox_turntable_com.currentText()
        power_com = self.comboBox_power_com.currentText()
        binding_rule = self.comboBox_binding_rule.currentText()
        tempbox_com = self.comboBox_tempbox_com.currentText()
        automatic_rule = self.comboBox_automatic_rule.currentText()
        if self.debug_flag | self.debug_begin_test:
            print('protocal::rule:{}\tcom:{}\tbaund:{}\tcheck:{}'.format(protocal_rule,protocal_com,protocal_baund,protocal_check))
            print('turntable:rule:{}\tcom:{}'.format(turntable_rule,turntable_com))
            print('power_com:rule:{}'.format(power_com))
            print('binding_rule:rule:{}'.format(binding_rule))
            print('tempbox_com:rule:{}'.format(tempbox_com))
            print('automatic_rule:rule:{}'.format(automatic_rule))
        
        begin_test_mode = 'only_test'
        if not ((turntable_rule.lower()=='none')|(turntable_rule.lower()=='选择协议')):
            begin_test_mode = 'turntable_test'
        if not ((automatic_rule.lower()=='none')|(automatic_rule.lower()=='选择协议')):
            begin_test_mode = 'automatic_test'
        self.test_mode = begin_test_mode
        self.textBrowser_automatic_ruleline.append('{} 当前模式：{}'.format(self.normal_time,testmode2chinese(begin_test_mode)))
        # self.show_message_automatic = '{} 当前模式：{}'.format(self.normal_time,testmode2chinese(begin_test_mode))
        
        self.only_test()
        
        
    # 单独测试模式、通用惯导采集
    def only_test(self):
        protocal_rule = self.comboBox_protocal_rule.currentText()
        protocal_com = self.comboBox_protocal_com.currentText()
        protocal_baund = self.comboBox_protocal_baund.currentText()
        protocal_check = self.comboBox_protocal_check.currentText()
        
        # self.threading_test_flag = False
        # time.sleep(0.1)
        # self.threading_test_flag = True
        
        # threading_receive = threading.Thread(target=self.receive_data_threading)
        # threading_receive.setDaemon(True)
        # threading_receive.start()
        # threading_decode = threading.Thread(target=self.decode_data_threading)
        # threading_decode.setDaemon(True)
        # threading_decode.start()
        # print('尝试创建')
        thread_receive_list = []
        thread_decode_list = []
        for i in range(12):
            if self.combox_com_open_list[i].text() == '开启':
                thread = threading.Thread(target=self.receive_data_threading,args=(i,))
                thread.setDaemon(True)
                thread_receive_list.append(thread)
                thread.start()
        
        
        
        

    def receive_data_threading(self,thread_num):
        # com = self.findChild()
        com = self.combox_com_list[thread_num].currentText()
        if self.debug_flag | self.debug_threading:
            print('thread_num:{}  com:{}'.format(thread_num,com))
            
        while self.threading_test_flag:
            time.sleep(0.1)

            
         


# 根据规则解算数据
def decode_hex_frame(frame,rules_format,rules_head,rules_saveck,rules_paras):
    bit_data = []
    for i in range(len(rules_format)):
        if str(rules_saveck[i])=='1':
            bit_frame_length = struct.calcsize(rules_head[i]+rules_format[i])
            before_frame_length = struct.calcsize('>'+''.join(rules_format[:i]))
            frame_data = frame[before_frame_length:before_frame_length+bit_frame_length]
            if str(rules_paras[i])=='1':
                decode_frame_data = struct.unpack(rules_head[i]+rules_format[i],frame_data)[0]
            else:
                decode_frame_data = struct.unpack(rules_head[i]+rules_format[i],frame_data)[0] *float(rules_paras[i])
                
            bit_data.append(decode_frame_data)
        else:
            continue
    return bit_data

def try_set_text(obj,types,default=1):
    try: return types(obj)
    except: return types(default)
def try_get_text(obj,types,default=1):
    try: return types(obj.text())
    except: return types(default)
def int2str(string,rjust=2,strjust='0'):
    return str(string).rjust(rjust,strjust)
def hex2int(strings):
    return int(strings,16) if bin(int(strings,16))[2:].rjust(len(strings)*4,'0')[0]=='0' else int(strings,16)-int(len(strings)*'F',16)-1
def int2hex(string,rjust=2):
    return hex(string)[2:].rjust(rjust,'0')[-rjust:].upper() if int(string)>0 else int2hex(int('F'*rjust,16)+int(string)+1,rjust)
def reverse(string):
    return ''.join([string[len(string)-i*2-2:len(string)-i*2] for i in range(len(string)//2)])
def hexcut2list(string):
    return [string[i*2:i*2+2] for i in range(len(string)//2)]
def struct_unpack_int3(string):
    return int(struct.unpack('<i',b'\x00'+string)[0]/256)
# 校验位中英转换
def check2chinese(data):
    try: return ['无校验','偶校验','奇校验'][['none','even','odd'].index(str(data).lower())]
    except: return '无校验'
def chinese2check(data):
    try: return [serial.PARITY_NONE,serial.PARITY_EVEN,serial.PARITY_ODD][['无校验','偶校验','奇校验'].index(str(data).lower())]
    except: return serial.PARITY_NONE
# 规则文件中英转换
def rulename2chinese(data):
    try: return ['解算规则','标定规则','装订规则','自动规则'][['protocal','turntable','binding','automatic'].index(str(data).lower())]
    except: return '错误名称'
# 测试模式中英转换
def testmode2chinese(data):
    try: return ['惯导测试','转台标定','自动测试'][['only_test','turntable_test','automatic_test'].index(str(data).lower())]
    except: return '错误名称'
def calculate_checksum(data):
    checksum = 0
    for byte in data:
        checksum += byte
    return checksum & 0xFF 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

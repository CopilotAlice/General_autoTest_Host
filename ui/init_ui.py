# 初始化界面
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
class MainWindowInit:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        
        
        self.init_ui_setting()
        # 初始化时间
        self.init_ui_time()
        
        


# ------------------接收转发/卫导数据接收&转发--------------
        # 初始化  卫导数据列表
        self.init_recforward_data()
        # 初始化  卫导数据列表
        self.init_recforward_check()
        # 设置 时间
        self.init_ui_recforward()
        # 初始化  卫导数据列表
        self.init_sate_textBrowser_ascii()




# ------------------初始化界面----------------
    def init_ui_setting(self):
        self.mw.tableWidget_general_show.setColumnWidth(0, 10)
        self.mw.tabWidget.setCurrentIndex(0)
        self.mw.tabWidget_2.setCurrentIndex(0)
        

# ---------------初始化事件相关内容----------------
    def init_ui_time(self):
        now = datetime.now()
        self.year = now.year
        self.month = now.month
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second
        self.microsecond = now.microsecond/1000
        self.date_time_list = [
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second,
            now.microsecond/1000
        ]
        # 转换时分秒
        self.test_time = now.strftime('%H%M%S')
        self.normal_time = now.strftime('%H:%M:%S')
        self.long_time = now.strftime('%Y%m%d_%H%M%S')
        self.update_time()
        
    def update_time(self):
        now = datetime.now()
        # 转换时分秒
        self.test_time = now.strftime('%H%M%S')
        self.normal_time = now.strftime('%H:%M:%S')
        self.long_time = now.strftime('%Y%m%d_%H%M%S')
        
    def get_time_list(self):
        self.update_time()
        return [self.test_time,self.normal_time,self.long_time]
        
    def get_normal_time(self):
        self.update_time()
        return self.normal_time



        
            

# ------------------接收转发/卫导数据接收&转发--------------
    def init_ui_recforward(self):
        for i in range(7):
            self.recforward_data_list[i].setText(
                str(self.date_time_list[i])
            )
    def init_recforward_check(self):
        self.recforward_check_list = []
        for i in range(16):
            self.recforward_check_list.append(
                self.mw.findChild(QtWidgets.QCheckBox, 'checkBox_recforward_{}'.format(i+1))
            )
    def init_recforward_data(self):
        self.recforward_data_list = []
        for i in range(16):
            self.recforward_data_list.append(
                self.mw.findChild(QtWidgets.QLineEdit, 'lineEdit_recforward_{}'.format(i+1))
            )
    def init_recforward_shift(self):
        self.recforward_shift_list = []
        for i in range(16):
            self.recforward_check_list.append(
                self.mw.findChild(QtWidgets.QLineEdit, 'lineEdit_rf_flycontrol_{}'.format(i+1))
            )
    def init_sate_textBrowser_ascii(self):
        self.textBrowser_ascii_list = []
        for i in range(8):
            self.textBrowser_ascii_list.append(
                self.mw.findChild(QtWidgets.QTextBrowser, 'textBrowser_ascii_{}'.format(i))
            )
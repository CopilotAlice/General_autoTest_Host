# ��ʼ������
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
class MainWindowInit:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow
        
        

        # ��ʼ��ʱ��
        self.init_ui_time()
        
        


# ------------------����ת��/�������ݽ���&ת��--------------
        # ��ʼ��  ���������б�
        self.init_recforward_data()
        # ��ʼ��  ���������б�
        self.init_recforward_check()
        # ���� ʱ��
        self.init_ui_recforward()
        







# ---------------��ʼ���¼��������----------------
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



        
            

# ------------------����ת��/�������ݽ���&ת��--------------
    def init_ui_recforward(self):
        for i in range(7):
            self.recforward_data_list[i].setText(
                str(self.date_time_list[i])
            )
    def init_recforward_check(self):
        self.recforward_check_list = []
        for i in range(16):
            self.recforward_check_list.append(
                self.mainWindow.findChild(QtWidgets.QCheckBox, 'checkBox_recforward_{}'.format(i+1))
            )
    def init_recforward_data(self):
        self.recforward_data_list = []
        for i in range(16):
            self.recforward_data_list.append(
                self.mainWindow.findChild(QtWidgets.QLineEdit, 'lineEdit_recforward_{}'.format(i+1))
            )
    def init_recforward_shift(self):
        self.recforward_shift_list = []
        for i in range(16):
            self.recforward_check_list.append(
                self.mainWindow.findChild(QtWidgets.QLineEdit, 'lineEdit_rf_flycontrol_{}'.format(i+1))
            )
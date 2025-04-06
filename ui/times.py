import os
from PyQt5 import QtWidgets, QtGui, QtCore
from funs.fun_locals import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer


# 周期消息更新、事件处理
class MainWindowTimes:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        # 规则文件更新 【名称】 【ui名称】 【文件夹名称】
        self.test_count = 0
        self.update_test_time()
        
    def update_test_time(self):
        self.test_time = QTimer(self.mw)
        self.test_time.timeout.connect(self.timeEvent_test)
        # self.test_time.start(1000)
        
        
        
    def timeEvent_test(self):
        self.test_count+=1
        # print('test:{}'.format(self.test_count))
        pass
    
    # 更新事件-扫描文件夹路径 更新规则文件
    def timeEvent_update_combobox(self):
        for counts in range(len(self.mw.init_ui.list_comboBox_localNames)):
            comboBox_paths = self.mw.init_ui.list_comboBox_localPaths[counts]
            comboBox_names = self.mw.init_ui.list_comboBox_localNames[counts]
            if comboBox_names is None:
                continue
            
            
        for i in range(len(model_list[0])):
            file_path = model_list[2][i]
            if file_path.lower()=='none':
                continue
            path_list = []
            file_list = []
            
            comboBox = self.findChild(QtWidgets.QComboBox,'comboBox_%s_rule'%(model_list[1][i]))
            if comboBox is None:
                if self.debug_update_5s_file:
                    print('未找到对应控件：comboBox_%s_rule'%(model_list[1][i]))
                continue
            comboBox_path = self.findChild(QtWidgets.QComboBox,'comboBox_%s_path'%(model_list[1][i]))
            if comboBox_path is None:
                if self.debug_update_5s_file:
                    print('未找到对应控件：comboBox_%s_path'%(model_list[1][i]))
                continue
            
            for file_name in os.listdir('./'+file_path):
                if os.path.isdir(file_path+'/'+file_name):
                    path_list.append(file_name)
            if len(path_list)==0:
                comboBox_path.clear()
                comboBox_path.addItem('')
            else:
                comboBox_file_list = []
                for count in range(comboBox_path.count()):
                    comboBox_file_list.append(comboBox.itemText(count))
                if '选择路径' in comboBox_file_list:
                    comboBox_file_list.remove('选择路径')
                if '' in comboBox_file_list:
                    comboBox_file_list.remove('')
                if not (comboBox_file_list==path_list):
                    select_combo = comboBox_path.currentText()
                    comboBox_path.clear()
                    comboBox_path.addItem('选择路径')
                    for path in path_list:
                        comboBox_path.addItem(path)
                    if select_combo in path_list:
                        comboBox_path.setCurrentText(select_combo)
                    else:
                        comboBox_path.setCurrentIndex(0)
            select_path_name = comboBox_path.currentText()
            if not (select_path_name=='选择路径')|(select_path_name==''):
                file_path = file_path+'/'+select_path_name
                
            
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            
            for file_name in os.listdir('./'+file_path):
                file_name = file_name.split('.txt')[0]
                file_list.append(file_name)
            file_list.sort()
            if self.debug_update_5s_file:
                print('file_list:{}\ncomboBox_file_list:{}'.format(file_list,comboBox_file_list))
            
            
            
            comboBox_file_list = []
            for count in range(comboBox.count()):
                comboBox_file_list.append(comboBox.itemText(count))
            try:    
                comboBox_file_list.remove('选择协议')
            except:
                if self.debug_update_5s_file:
                    print('comboBox_file_list中没有选择协议项:{}'.format(comboBox_file_list))
            if comboBox_file_list==file_list:
                if self.debug_update_5s_file:
                    print('没有新的协议')
                continue
            else:
                if self.debug_update_5s_file:
                    print('comboBox_file_list:{}\nfile_list:{}'.format(comboBox_file_list,file_list))
            if comboBox is None:
                if self.debug_update_5s_file:
                    print('未找到对应控件：comboBox_%s_rule'%(model_list[1][i]))
                continue
            select_combo = comboBox.currentText()
            comboBox.clear()
            comboBox.addItem('选择协议')
            for rule in file_list:
                comboBox.addItem(rule)
            # comboBox.setCurrentText(select_combo)
            if select_combo in file_list:
                comboBox.setCurrentText(select_combo)
            else:
                comboBox.setCurrentIndex(0)
        
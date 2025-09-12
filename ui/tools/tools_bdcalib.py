# 工具栏下属
# 处理标定数据
import os,re
from PyQt5.QtWidgets import QWidget, QFileDialog,QLineEdit

class MainWindowToolBdcalib:
    def __init__(self, mainWindow):
        self.mw = mainWindow
        self.list_input_para = []
        self.list_input_data = []
        # 正则表达式
        self.list_pathrule_and = []
        self.list_pathrule_nor = []
        self.show_path = self.mw.lineEdit_tools_bd3x_showPath
        self.show_file = self.mw.listWidget_tools_bd3x_pathShow
        self.mw.pushButton_tools_bd3x_loadPath.clicked.connect(self.load_path)
        self.mw.pushButton_test1.clicked.connect(self.test1)
        self.init_list()
        self.init_data()
        
    # 初始化所有输入框
    def init_list(self):
        lineEdit_length = 8
        for i in range(lineEdit_length):
            self.list_input_para.append(self.mw.findChild(QLineEdit,'lineEdit_tools_bd3x_{}'.format(i)))
            
    # 初始化输入框所有变量
    def init_data(self):
        for count,lineedit in enumerate(self.list_input_para):
            app_data = lineedit.text() if lineedit.text() else ''
            if len(self.list_input_data)<=count:
                self.list_input_data.append(app_data)
            else:
                self.list_input_data[count] = app_data
        decode_rule_and = self.list_input_data[0]
        decode_rule_nor = self.list_input_data[1]
        self.list_pathrule_and = []
        self.list_pathrule_nor = []
        for count, rule in enumerate(decode_rule_and.split('|')):
            self.list_pathrule_and.append([])
            for r in re.split(r'[\s,，]+', rule):
                self.list_pathrule_and[count].append(r) if r else None
        for count, rule in enumerate(decode_rule_nor.split('|')):
            self.list_pathrule_nor.append([])
            for r in re.split(r'[\s,，]+', rule):
                self.list_pathrule_nor[count].append(r) if r else None
            
    # 打开文件夹载入路径
    def load_path(self):
        folder = QFileDialog.getExistingDirectory(self.mw, "选择文件夹", "")
        if folder:
            self.show_path.setText(folder)
            self.show_all_files(folder)
            
    # 在listWidget_tools_bd3x_pathShow中显示所有正则规则中的文件
    def show_all_files(self,folder):
        self.show_file.clear()
        
        try:
            files = os.listdir(folder)
            for file in files:
                if file.endswith('.txt') or file.endswith('.csv'):
                    self.show_file.addItem(file)
        except Exception as e:
            self.show_file.addItem('Error: {}'.format(e))
    def test1(self):
        self.init_data()
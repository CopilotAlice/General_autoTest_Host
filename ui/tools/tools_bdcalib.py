# 工具栏下属
# 处理标定数据
import os,re,datetime,shutil,threading
import pandas as pd
from PyQt5.QtWidgets import QWidget, QFileDialog,QLineEdit, QListWidgetItem, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize,Qt,QTimer,QThread    

class MainWindowToolBdcalib:
    def __init__(self, mainWindow):
        self.mw = mainWindow
        # 系数列表
        self.list_input_lineEdit = []
        self.list_input_data = []
        # 正则表达式
        self.list_pathrule_and = []
        self.list_pathrule_nor = []
        self.pixmap = None
        # 快捷路径
        self.show_path = self.mw.lineEdit_tools_bd3x_showPath
        self.show_file = self.mw.listWidget_tools_bd3x_pathShow
        # 逻辑事件
        self.mw.pushButton_tools_bd3x_loadPath.clicked.connect(self.load_path)
        self.mw.listWidget_tools_bd3x_pathShow.itemClicked.connect(self.item_click_showMsg)
        self.mw.listWidget_tools_bd3x_pathShow.itemDoubleClicked.connect(self.item_click_changeFolder)
        self.mw.label_tools_imgShow.resizeEvent = self.label_resizeEvent
        self.mw.pushButton_tools_bd3x_uppath.clicked.connect(self.click_uppath)
        self.mw.checkBox_tools_bd3x_regexFolder.clicked.connect(self.show_all_files)
        self.mw.pushButton_tools_bd3x_avePath.clicked.connect(self.click_avePath)
        # 初始化
        self.init_list()
        self.init_data()
        self.mw.task_done = self.task_done
        
    # 初始化所有输入框
    def init_list(self):
        lineEdit_length = 10
        for i in range(lineEdit_length):
            self.list_input_lineEdit.append(self.mw.findChild(QLineEdit,'lineEdit_tools_bd3x_{}'.format(i)))
            
            
    # 初始化输入框所有变量
    def init_data(self):
        for count,lineedit in enumerate(self.list_input_lineEdit):
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
        folder = QFileDialog.getExistingDirectory(self.mw, "选择文件夹_载入预览路径", "")
        if folder:
            self.show_path.setText(folder)
            self.mw.lineEdit_tools_bd3x_loadPath.setText(folder)
            self.show_all_files(folder)
            
    # 在listWidget_tools_bd3x_pathShow中显示所有正则规则中的文件
    def show_all_files(self,folder):
        if self.mw.sender() == self.mw.checkBox_tools_bd3x_regexFolder:
            folder = self.show_path.text()
        self.init_data()
        self.show_file.clear()
        try:
            files = os.listdir(folder)
            for file in files:
                if os.path.isdir(os.path.join(folder, file)):
                    self.show_file.addItem('[{}]'.format(file))
                else:
                    if self.mw.checkBox_tools_bd3x_regexFolder.isChecked():
                        and_rule = any([all([re.search(r, file) for r in rule]) for rule in self.list_pathrule_and]) if self.list_pathrule_and else True
                        nor_rule = any([any([re.search(r, file) for r in rule]) for rule in self.list_pathrule_nor]) if self.list_pathrule_nor else True
                    else:
                        and_rule = True
                        nor_rule = False
                    if and_rule and (not nor_rule):
                        self.show_file.addItem(file)
        except Exception as e:
            self.show_file.addItem('Error: {}'.format(e))
        
    def append_degugMsg(self,msg):
        now = datetime.datetime.now()
        try: self.mw.textBrowser_tools_bd3x_msglast.setText('{} {}'.format(now.strftime('%H:%M:%S'), msg))
        except Exception as e: print('Error:append_degugMsg: {}'.format(e))
    
    # 根据类型预览文件
    def preview_file(self, mode=0):
        set_list = [
            self.mw.tableWidget_tools_bd3x_fileShow,
            self.mw.textEdit_tools_bd3x_fileShow,
            self.mw.label_tools_imgShow
        ]
        if mode==0:
            set_mode = [True, False, False]
        elif mode==1:
            set_mode = [False, True, False]
        elif mode==2:
            set_mode = [False, False, True]
        elif mode==-1:
            set_mode = [False, False, False]
        for i in range(len(set_list)):
            # set_list[i].setVisible(set_mode[i])
            set_list[i].hide() if not set_mode[i] else set_list[i].show()
    # 点击返回上级目录
    def click_uppath(self):
        current_path = self.show_path.text()
        parent_path = os.path.dirname(current_path)
        if os.path.isdir(parent_path) and parent_path != current_path:
            self.show_path.setText(parent_path)
            self.show_all_files(parent_path)
            self.append_degugMsg('进入上级目录:\n {}'.format(parent_path))
    # 双击进入文件夹
    def item_click_changeFolder(self,item):
        if item.text().startswith('[') and item.text().endswith(']'):
            folder_name = item.text()[1:-1]
            new_path = os.path.join(self.show_path.text(), folder_name)
            if os.path.isdir(new_path):
                self.show_path.setText(new_path)
                self.show_all_files(new_path)
                self.append_degugMsg('进入文件夹:\n [{}]'.format(folder_name))
    # 单击预览文件
    def item_click_showMsg(self,item):
        img_list = ['png','jpg','jpeg','bmp','tif','tiff']
        txt_list = ['txt','csv','log','ini','json','xml']
        if item.text().startswith('[') and item.text().endswith(']'):
            # 如果是双击，则进入列表中
            self.preview_file(mode=-1)
        elif any([item.text().lower().endswith('.'+ext) for ext in img_list]):
            self.preview_file(mode=2)
            self.append_degugMsg('载入图片:\n {}'.format(item.text()))
            item_path = os.path.join(self.show_path.text(), item.text())    
            self.pixmap = QPixmap(item_path)
            self.update_imgShow_pixmap()
            self.mw.label_tools_imgShow.setScaledContents(False)
        elif any([item.text().lower().endswith('.'+ext) for ext in txt_list]):
            # 尝试使用pd.read_csv读取前10行
            try:
                import pandas as pd
                # 尝试使用gb2312和utf-8打开文件
                df = pd.read_csv(os.path.join(self.show_path.text(), item.text()), encoding='gb2312',sep='\\s+', nrows=10,encoding_errors="replace")
                self.preview_file(mode=0)
                table = self.mw.tableWidget_tools_bd3x_fileShow
                table.clear()
                table.setRowCount(len(df))
                table.setColumnCount(len(df.columns))
                table.setHorizontalHeaderLabels(df.columns.tolist())
                for i in range(len(df)):
                    for j in range(len(df.columns)):
                        table.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
                table.resizeColumnsToContents()
                self.append_degugMsg('载入表格:\n {}'.format(item.text()))
            #否则使用普通文本读取前10行
            except Exception as e:
                print('读取为表格失败:', e)
                try:
                    with open(os.path.join(self.show_path.text(), item.text()), 'r', encoding='gb2312', errors='replace') as f:
                        content = ''.join([f.readline() for _ in range(10)])
                    self.preview_file(mode=1)
                    textedit = self.mw.textEdit_tools_bd3x_fileShow
                    textedit.setPlainText(content)
                    self.append_degugMsg('载入文本:\n {}'.format(item.text()))
                except Exception as e2:
                    self.preview_file(mode=-1)
                    self.append_degugMsg('无法载入文件\n {}: {}, {}'.format(item.text(), e, e2)) 
        else:
            self.preview_file(mode=-1)
            self.append_degugMsg('不支持预览该文件:\n {}'.format(item.text()))

    def update_imgShow_pixmap(self):
        if self.pixmap :
            self.mw.label_tools_imgShow.setPixmap(
                self.pixmap.scaled(
                    QSize(
                        int(self.mw.label_tools_imgShow.size().width()-20),
                        int(self.mw.label_tools_imgShow.size().height()-40)
                    ),
                    # self.mw.label_tools_imgShow.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
    def label_resizeEvent(self, event):
        self.update_imgShow_pixmap()
        QWidget.resizeEvent(self.mw.label_tools_imgShow, event)
        
    def click_avePath(self):
        # 打开文件夹
        folder_path = QFileDialog.getExistingDirectory(self.mw, '选择文件夹_预处理标定数据')
        if folder_path:
            self.show_path.setText(folder_path)
            self.mw.lineEdit_tools_bd3x_avePath.setText(folder_path)
            self.init_data()
            self.show_all_files(folder_path)
            self.append_degugMsg('预处理标定数据中...')
            threadings = threading.Thread(
                target=self.thread_ave_all_files,
                args=(folder_path,)
                )
            threadings.start()
            
    def thread_ave_all_files(self, path):
        self.ave_all_files(path)
    def ave_all_files(self, path):
        # 初始化变量
        ave_length_split = self.list_input_lineEdit[8].text()
        drop_row_footer = self.list_input_lineEdit[9].text()    
        try:ave_length_split = int(ave_length_split)
        except:ave_length_split = 10
        try:drop_row_footer = [int(r) for r in re.split(r'[\s,，]+',drop_row_footer)]
        except:drop_row_footer = []
        if len(drop_row_footer)!=2: drop_row_footer = [0, 0]
        list_all_input = []
        for i in range(6):
            input_data = self.list_input_lineEdit[i+2].text()
            input_list = []
            for j in range(3):
                try:input_list.append( int( re.split(r'[\s,，]+',input_data)[j] ) )
                except Exception as e:
                    try: input_list.append(input_list[j-1])
                    except: input_list.append(1)

            list_all_input.append(input_list)

        
        # 创建ave和std文件夹
        save_ave_path = os.path.join(path, 'all_ave')
        save_std_path = os.path.join(path, 'all_std')
        if os.path.exists(save_ave_path):
            shutil.rmtree(save_ave_path)
        os.makedirs(save_ave_path)
        if os.path.exists(save_std_path):
            shutil.rmtree(save_std_path)
        os.makedirs(save_std_path)
           
        # 遍历文件夹
        load_paths = path
        for plan_name in os.listdir(load_paths):
            if not os.path.isdir(os.path.join(load_paths, plan_name)):
                continue
            if plan_name.startswith('all_'):
                continue    
            list_all_file = [f for f in os.listdir(os.path.join(load_paths, plan_name)) if re.search(r'BD(\d+)#',f)]
            list_regex_name = []
            for file in list_all_file:
                and_rule = any([all([re.search(r, file) for r in rule]) for rule in self.list_pathrule_and]) if self.list_pathrule_and else True
                nor_rule = any([any([re.search(r, file) for r in rule]) for rule in self.list_pathrule_nor]) if self.list_pathrule_nor else True
                if and_rule and not nor_rule:
                    list_regex_name.append(file)    
                    df = pd.read_csv(os.path.join(load_paths, plan_name, list_regex_name[0]), encoding='gb2312', sep='\\s+',skiprows=drop_row_footer[0], skipfooter=drop_row_footer[1])
                    if len(df) < ave_length_split:
                        ave_length = len(df)
                    else:
                        ave_length = (len(df)//ave_length_split)*ave_length_split
                    df_ave = df.iloc[:,-ave_length:].mean()
                    and_rule_list = [all([re.search(r, file) for r in rule]) for rule in self.list_pathrule_and]
                    try: save_rule_name = '_'.join(self.list_pathrule_and[and_rule_list.index(True)])
                    except: save_rule_name = 'other'
                    save_name = '{}_{}.txt'.format(plan_name,save_rule_name)
                    save_ave_file = os.path.join(save_ave_path, save_name)
                    save_std_file = os.path.join(save_std_path, save_name)
                    if not os.path.exists(save_ave_file):
                        self.init_save_file(save_ave_file)
        print('QTimer1 数据处理完成')
        QTimer.singleShot(0,lambda r='预处理标定数据结束。':self.tools_bd3x_taskDone(r))
        print('QTimer2 数据处理完成')
        QTimer.singleShot(0,lambda r='预处理标定数据结束。':self.mw.tools_bd3x_taskDone(r))
        print('QTimer3 数据处理完成')
        QTimer.singleShot(0,lambda r='预处理标定数据结束。':self.tools_bd3x_taskDone()) 
    def task_done(self,result):
        print('\nappend_degugMsg\n')
        self.append_degugMsg('预处理标定数据结束。\n{}'.format(result) )
    def init_save_file(self,save_file_path):
        # Turntable	Gx(deg/h)	Gy(deg/h)	Gz(deg/h)	Ax(m/s2)	Ay(m/s2)	Az(m/s2)	GxTemp	GyTemp	GzTemp	AxTemp	AyTemp	AzTemp	Length
        save_title_list = [
            'Turntable', 'Gx(deg/h)', 'Gy(deg/h)', 'Gz(deg/h)', 'Ax(m/s2)', 'Ay(m/s2)',
            'GxTemp', 'GyTemp', 'GzTemp', 'AxTemp', 'AyTemp', 'AzTemp', 'Length'
        ]
        try:
            with open(save_file_path, 'w+', newline='', encoding='gb2312') as f:
                f.write('{}\n'.format('\t'.join(save_title_list)))
        except Exception as e:
            self.append_degugMsg('初始化保存文件失败:\n {}'.format(e))
        

        
                        
                    
                    
                    
                    

        
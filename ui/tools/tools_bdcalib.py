# 工具栏下属
# 处理标定数据
import os,re,datetime,shutil,threading#,debugpy
import pandas as pd
from PyQt5.QtWidgets import QWidget, QFileDialog,QLineEdit, QListWidgetItem, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize,Qt,QTimer,QThread,pyqtSignal

def extract_number(filename):
    match = re.search(r'BD(\d+)#',filename)
    return int(match.group(1)) if match else float('inf')

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
        self.work_processData = None
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
        self.mw.pushButton_tools_bd3x_modTransform.clicked.connect(self.click_formatConversion)
        self.mw.comboBoxt_tools_bd3x_preset.currentTextChanged.connect(self.change_preset)
        self.mw.pushButton_tools_bd3x_createBin.clicked.connect(self.click_createBin)
        self.mw.pushButton_tools_bd3x_autoRun.clicked.connect(self.click_autoRun)
        self.mw.pushButton_tools_bd3x_calPara.clicked.connect(self.click_calPara)
        # 初始化
        self.init_list()
        self.init_data()
        
    # 初始化所有输入框
    def init_list(self):
        lineEdit_length = 16
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
                df = pd.read_csv(
                    os.path.join(self.show_path.text(), item.text()), 
                    encoding='gb2312',
                    delim_whitespace=True, 
                    nrows=100,
                    dtype='str',
                    encoding_errors="replace",
                    index_col=False
                )
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
                        content = ''.join([f.readline() for _ in range(100)])
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
            self.work_processData = class_Worker(folder_path, self.list_input_data, self.list_pathrule_and, self.list_pathrule_nor,self.mw.root_mode)
            self.work_processData.finished.connect(self.task_done)
            self.work_processData.mode = 1
            self.work_processData.start()
    def click_formatConversion(self):
        # 打开文件夹
        folder_path = QFileDialog.getExistingDirectory(self.mw, '选择文件夹_格式转换_通用')
        if folder_path:
            self.show_path.setText(folder_path)
            self.mw.lineEdit_tools_bd3x_formatPath.setText(folder_path)
            self.init_data()
            self.show_all_files(folder_path)
            self.append_degugMsg('格式转换中...')
            self.work_processData = class_Worker(folder_path, self.list_input_data, self.list_pathrule_and, self.list_pathrule_nor,self.mw.root_mode)
            self.work_processData.finished.connect(self.task_done)
            self.work_processData.mode = 2
            self.work_processData.start()
    def click_calPara(self):
        # 打开文件夹
        folder_path = QFileDialog.getExistingDirectory(self.mw, '选择文件夹_参数计算_通用')
        if folder_path:
            self.show_path.setText(folder_path)
            self.mw.lineEdit_tools_bd3x_calPath.setText(folder_path)
            self.init_data()
            self.show_all_files(folder_path)
            self.append_degugMsg('参数计算中...')
            self.work_processData = class_Worker(folder_path, self.list_input_data, self.list_pathrule_and, self.list_pathrule_nor,self.mw.root_mode)
            self.work_processData.finished.connect(self.task_done)
            self.work_processData.mode = 3
            self.work_processData.start()
    def task_done(self):
        try:debug_info = self.work_processData.debug_info;self.work_processData.debug_info = ''
        except Exception as e: debug_info = '未读取到信息'
        if len(debug_info)>0: self.append_degugMsg(f'处理数据完成：\n{debug_info}')
        else: self.append_degugMsg('处理数据完成\n未读取到信息')
        self.show_all_files(self.show_path.text())
    def change_preset(self):
        self.append_degugMsg('未读取到预设文件')
    def click_createBin(self):
        self.append_degugMsg('未读取到pyc文件')
    def click_autoRun(self):
        self.append_degugMsg('未实现的功能')
    
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class class_Worker(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, folder_path,list_input_data,list_pathrule_and, list_pathrule_nor,root_mode):
        super().__init__()
        self.root_mode = root_mode
        self.folder_path = folder_path
        self.list_input_data = list_input_data
        self.folder_path = folder_path
        self.list_pathrule_and = list_pathrule_and
        self.list_pathrule_nor = list_pathrule_nor
        self.debug_info = ''
        self.mode = 0
        self.G = 9.801538877
        

    def run(self):
        if self.root_mode:
            try:
                import debugpy
                debugpy.debug_this_thread()
            except Exception as e:
                self.debug_info = '无法开启调试: {}'.format(e)
        if self.mode==0:
            self.debug_info = '未设置处理模式'
        elif self.mode==1:
            self.ave_all_data()
        elif self.mode==2:
            self.format_all_data()
        elif self.mode==3:
            self.cal_all_para()
            
        else:
            self.debug_info = '未知的处理模式'
        self.finished.emit('线程work_processData结束')
        
        
        
    def ave_all_data(self):
        # 初始化变量
        ave_length_split = self.list_input_data[10]
        drop_row_footer = self.list_input_data[11]
        rollings = self.list_input_data[12]
        save_data_accuracy = self.list_input_data[14]
        
        try:ave_length_split = int(ave_length_split)
        except:ave_length_split = 1
        try:rollings = int(rollings)
        except:rollings = 1
        try:save_data_accuracy = int(save_data_accuracy)
        except:save_data_accuracy = 6
        drop_row_footer = []
        try:drop_row_footer = [int(r) for r in re.split(r'[\s,，]+',drop_row_footer)]
        except:drop_row_footer = []
        if len(drop_row_footer)!=2: drop_row_footer = [0, 0]
        list_all_input = []
        
        # 读取原始数据并分隔list
        for i in range(8):
            input_data = self.list_input_data[i+2]
            input_list = []
            for j in range(3):
                try:
                    if i<4: input_list.append( int( re.split(r'[\s,，]+',input_data)[j] ) )
                    else: input_list.append( float( re.split(r'[\s,，]+',input_data)[j] ) )
                except Exception as e:
                    try: input_list.append(input_list[j-1])
                    except: input_list.append(1)

            list_all_input.append(input_list)

        # 保存轴系重排
        save_list_axis = []
        save_list_para = []
        for i in range(4):
            save_list_axis+=list_all_input[i]
        for i in range(4):  
            save_list_para+=list_all_input[i+4]
            
            
        path = self.folder_path
        # 创建ave和std文件夹
        save_ave_path = os.path.join(path, 'all_ave')
        save_std_path = os.path.join(path, 'all_std')
        if os.path.exists(save_ave_path):
            shutil.rmtree(save_ave_path)
        os.makedirs(save_ave_path)
        if os.path.exists(save_std_path):
            shutil.rmtree(save_std_path)
        os.makedirs(save_std_path)
        

            
        
        total_folder = 0
        total_file = 0
        total_error = 0
        # 遍历文件夹
        load_paths = path
        for plan_name in os.listdir(load_paths):
            if not os.path.isdir(os.path.join(load_paths, plan_name)):
                continue
            if plan_name.startswith('all_'):
                continue    
            total_folder += 1
            list_all_file = [f for f in os.listdir(os.path.join(load_paths, plan_name)) if re.search(r'BD(\d+)#',f)]
            sorted_list_files = sorted(list_all_file,key=extract_number)
            
            list_regex_name = []
            for file_name in sorted_list_files:
                and_rule = any([all([re.search(r, file_name) for r in rule]) for rule in self.list_pathrule_and]) if self.list_pathrule_and else True
                nor_rule = any([any([re.search(r, file_name) for r in rule]) for rule in self.list_pathrule_nor]) if self.list_pathrule_nor else True
                if and_rule and not nor_rule:
                    total_file+=1
                    total_error+=1
                    list_regex_name.append(file_name)    
                    df = pd.read_csv(
                        os.path.join(load_paths, plan_name, file_name),
                        encoding='gb2312',
                        delim_whitespace=True,skiprows=drop_row_footer[0], skipfooter=drop_row_footer[1],
                        index_col=False
                    )
                    if len(df) < ave_length_split:
                        ave_length = len(df)
                    else:
                        ave_length = (len(df)//ave_length_split)*ave_length_split
                    df_ave = df.iloc[-ave_length:,:].mean()
                    and_rule_list = [all([re.search(r, file_name) for r in rule]) for rule in self.list_pathrule_and]
                    try: save_rule_name = '_'.join(self.list_pathrule_and[and_rule_list.index(True)])
                    except: save_rule_name = 'other'
                    try:turntable = re.search(r'(?:loc|spd)\[([^\]]+)\]', file_name).group(1)
                    except: turntable = 'None'
                    save_name = '{}_{}.txt'.format(plan_name,save_rule_name)
                    save_ave_file = os.path.join(save_ave_path, save_name)
                    save_name = '{}_{}_roll{}s.txt'.format(plan_name,save_rule_name,rollings)
                    save_std_file = os.path.join(save_std_path, save_name)
                    # 均值
                    if not os.path.exists(save_ave_file):
                        self.init_save_aveFile(save_ave_file)
                    save_file_data = []
                    save_file_data.append('[{}]'.format(turntable))
                    for count,axis in enumerate(save_list_axis):
                        save_data = df_ave[axis]*save_list_para[count]
                        save_file_data.append(f"{save_data:.{save_data_accuracy}f}")
                    save_file_data.append(str(ave_length))
                    with open(save_ave_file, 'a+', newline='', encoding='gb2312') as f:
                        f.write('\t'.join(save_file_data)+'\n')
                    # 标准差
                    if not os.path.exists(save_std_file):
                        self.init_save_aveFile(save_std_file)
                    save_file_data = []
                    save_file_data.append('[{}]'.format(turntable))
                    for count,axis in enumerate(save_list_axis):
                        if count<6:
                            save_data = df.iloc[-ave_length:,axis].rolling(rollings).mean().std()*save_list_para[count]
                        else:
                            save_data = df.iloc[-ave_length:,axis].mean()*save_list_para[count]
                        save_file_data.append(f"{save_data:.{save_data_accuracy}f}")
                    save_file_data.append(str(ave_length))
                    with open(save_std_file, 'a+', newline='', encoding='gb2312') as f:
                        f.write('\t'.join(save_file_data)+'\n')
                        
                    total_error-=1
                    
                    
        self.debug_info = f'文件夹：{total_folder}，文件：{total_file}，错误：{total_error}'
        
    def init_save_aveFile(self,save_file_path):
        # Turntable	Gx(deg/h)	Gy(deg/h)	Gz(deg/h)	Ax(m/s2)	Ay(m/s2)	Az(m/s2)	GxTemp	GyTemp	GzTemp	AxTemp	AyTemp	AzTemp	Length
        save_title_list = [
            'Turntable', 'Gx(deg/h)', 'Gy(deg/h)', 'Gz(deg/h)', 'Ax(m/s2)', 'Ay(m/s2)','Az(m/s2)',
            'GxTemp', 'GyTemp', 'GzTemp', 'AxTemp', 'AyTemp', 'AzTemp', 'Length'
        ]
        try:
            with open(save_file_path, 'w+', newline='', encoding='gb2312') as f:
                f.write('{}\n'.format('\t'.join(save_title_list)))
        except Exception as e:
            self.append_degugMsg('初始化保存文件失败:\n {}'.format(e))
        

    def format_all_data(self):
        format_count = self.list_input_data[13]
        save_data_accuracy = self.list_input_data[14]
        try: format_count = int(format_count)
        except: format_count = 10
        try: save_data_accuracy = int(save_data_accuracy)
        except: save_data_accuracy = 6
        path = self.folder_path
        if os.path.isdir(os.path.join(path, 'all_ave')):
            pass
        elif os.path.basename(path) == 'all_ave':
            path = os.path.dirname(path)
        else:
            self.debug_info = '未找到all_ave文件夹'
            return
        ave_path = os.path.join(path, 'all_ave')
        format_path = os.path.join(path, 'all_format')
        if os.path.exists(format_path):
            shutil.rmtree(format_path)
        os.makedirs(format_path)
        total_folder = 1
        total_file = 0
        total_error = 0
        # 遍历文件夹
        for filename in os.listdir(ave_path):
            if not filename.endswith('.txt'):
                continue
            total_file += 1
            total_error+=1
            try:
                df = pd.read_csv(os.path.join(ave_path, filename), encoding='gb2312', delim_whitespace=True)
            except Exception as e:
                print('读取文件{}失败:\n {}'.format(filename, e))
                continue
            sdf = pd.concat([
                df.iloc[:, 1:7],  # 6 列
                pd.DataFrame(0, index=df.index, columns=[f"zero{i}" for i in range(3)]),  # 3 列 0
                df.iloc[:, 7:13], # 6 列
                pd.DataFrame(0, index=df.index, columns=[f"zero{i}" for i in range(4)])   # 4 列 0
            ], axis=1)
            save_name = filename.split('.txt')[0] + '_format.txt'
            save_data = sdf.values.tolist()
            f = open(os.path.join(format_path, filename),'w+')
            count = 0
            for line in save_data:
                # save_line = '\t'.join([ '{:.6f}'.format(data) for data in line ])
                save_line = '\t'.join([f"{data:.{save_data_accuracy}f}" for data in line ])
                for i in range(format_count):
                    count+=1
                    if i==(format_count-1): end = 's\n'
                    else: end = '\n'
                    f.write('{}\t'.format(count)+save_line+end)
            f.close()
            total_error-=1
            
        self.debug_info = f'文件夹：{total_folder}，文件：{total_file}，错误：{total_error}'

    def init_save_paraFile(self,save_file_path):
        save_title_list = [
            'filename','Gx0(°h)','Gy0(°h)','Gz0(°h)','Ax0(m/s²)','Ay0(m/s²)','Az0(m/s²)',
             'GxSF','GySF','GzSF','AxSF','AySF','AzSF',
             'GKxy','GKxz','GKyx','GKyz','GKzx','GKzy',
             'AKxy','AKxz','AKyx','AKyz','AKzx','AKzy',
             
        ]
        try:
            with open(save_file_path, 'w+', newline='', encoding='gb2312') as f:
                f.write('{}\n'.format('\t'.join(save_title_list)))
        except Exception as e:
            self.append_degugMsg('初始化保存文件失败:\n {}'.format(e))
        
    def cal_all_para(self):
        # 初始化文件夹
        if os.path.isdir(os.path.join(path, 'all_ave')):
            pass
        elif os.path.basename(path) == 'all_ave':
            path = os.path.dirname(path)
        else:
            self.debug_info = '未找到all_ave文件夹'
            return
        ave_path = os.path.join(path, 'all_ave')
        para_path = os.path.join(path, 'all_para')
        if os.path.exists(para_path):
            shutil.rmtree(para_path)
        os.makedirs(para_path)
        
        # 初始化文件
        list_columns = [
            "G0", "G+", "G-", 
            "ScaleFactor+", "ScaleFactor-", 
            "NonLinear+", "NonLinear-", 
            "K*x", "K*y", "K*z", 
            "Temp"
        ]
        list_rows = ["Gx", "Gy", "Gz", "Ax", "Ay", "Az"]
        # df = pd.DataFrame(index=rows, columns=columns)
        # 遍历文件生成参数表和总参数表
        total_folder = 1
        total_file = 0
        total_error = 0
        for filename in os.listdir(ave_path):
            if not filename.endswith('.txt'):
                continue
            total_file+=1
            total_error+=1
            try:
                df = pd.read_csv(os.path.join(ave_path, filename), encoding='gb2312', delim_whitespace=True)
                if (df.shape[0] < 19) or (df.shape[1] < 13):
                    print('文件{}尺寸不正确{}'.format(filename, df.shape))
                    continue
            except Exception as e:
                print('读取文件{}失败:\n {}'.format(filename, e))
                continue
            para_name = filename.split('.txt')[0] + '_para.txt'
            save_data = []
            save_data.append('[{}]\n'.format(para_name))
            save_data.append('Turntable\tLength\tAverage\tStandard Deviation\tMax\tMin\n')
            for i in range(len(df)):
                row = df.iloc[i]
                turntable = row['Turntable']
                length = row['Length']
                average = row[1:7].mean()
                
                
                
                
            total_error-=1
        self.debug_info = f'文件夹：{total_folder}，文件：{total_file}，错误：{total_error}'
        
                    
                    
                    
                    

        
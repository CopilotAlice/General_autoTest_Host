import os
import struct 
import time
import pandas as pd 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from funs.fun_chy2 import *
# 各类点击事件
class MainWindowEvent:
    def __init__(self,mainWindow):
        self.debug_flag_event = False
        self.debug_flag_event = False
        self.mw = mainWindow


# ------------------接收转发/卫导数据接收&转发 202502 废弃中--------------
    # def clkEvent_recforward_all(self):
    #     checked = self.mw.checkBox_recforward_all.isChecked()
    #     for checkbox in self.mw.init_ui.recforward_check_list:
    #         checkbox.setChecked(checked)

    # def changeEvent_recforward(self):
    #     recforward_text = self.mw.textEdit_recforward_msg.toPlainText()
    #     print(recforward_text)
    #     rf_list = recforward_text.split(',')



# ------------------通用装订逻辑事件--------------
    # 更新装订规则事件
    def changeEvent_general_rule(self):
        load_path = './装订规则'
        comboxpath = self.mw.comboBox_general_path.currentText()
        if comboxpath not in self.mw.list_notpath:
            load_path+= '/{}'.format(comboxpath)
        load_name = self.mw.comboBox_general_rule.currentText()
        if (len(load_name)==0)|(load_name=='选择协议'):
            return False
        try:
            filename = '{}/{}.txt'.format(load_path,load_name)
            if os.path.exists(filename):
                with open(filename,'r+',encoding='gb2312') as f:
                    bind_rule_file = f.read()
                self.mw.class_general_bind.read_struct_file(bind_rule_file)
                self.mw.lineEdit_general_sendHz.setText(str(self.mw.class_general_bind.struct_sendHz))
                self.funcEvent_general_changeButton()
                self.funcEvent_general_changeTable()
                self.changeEvent_general_bind_table()
                return True
            else:
                return False
        except Exception as e:
            print('装订规则文件读取失败:{}'.format(e))
            return False
    def funcEvent_general_clearButton(self):
        for i in range(9):
            self.mw.init_ui.list_general_button[i].setText('预设指令')
            self.mw.init_ui.list_general_mainWindowButton[i].setText('预设指令')
    # 设定装订规则事件按钮
    def funcEvent_general_changeButton(self):
        count = 0
        for lists in self.mw.class_general_bind.struct_buttonList:
            self.mw.init_ui.list_general_button[count].setText(lists[0])
            self.mw.init_ui.list_general_mainWindowButton[count].setText(lists[0])
            count += 1
    def funcEvent_general_changeTable(self):
        self.mw.init_ui.flag_general_tableReady = False
        table = self.mw.tableWidget_general_show
        table.clearContents()
        len_pack = len(self.mw.class_general_bind.struct_packList)
        table.setRowCount(len_pack)
        table.setColumnCount(4)
        table_title = ['类型','系数','标题','输入']
        for i in range(4):
            table.setHorizontalHeaderItem(i,QtWidgets.QTableWidgetItem(table_title[i]))
        table.setColumnWidth(0,35)
        table.setColumnWidth(1,35)
        table.setColumnWidth(2,60)
        table.setColumnWidth(3,100)
        try:
            for i in range(len_pack):
                table.setItem(i,0,QtWidgets.QTableWidgetItem(str(self.mw.class_general_bind.struct_packList[i])))
                table.setItem(i,1,QtWidgets.QTableWidgetItem(str(self.mw.class_general_bind.struct_paraList[i])))
                table.setItem(i,2,QtWidgets.QTableWidgetItem(str(self.mw.class_general_bind.struct_titlList[i])))
                table.setItem(i,3,QtWidgets.QTableWidgetItem(str(self.mw.class_general_bind.struct_dataList[i])))
            self.mw.init_ui.flag_general_tableReady = True
        except Exception as e:
            print('更新装订规则表格失败:{}'.format(e))
            pass
    def changeEvent_general_bind_table(self):
        if not self.mw.init_ui.flag_general_tableReady:
            return
        table_widget = self.mw.tableWidget_general_show
        rows = table_widget.rowCount()
        cols = table_widget.columnCount()
        struct_head = self.mw.class_general_bind.struct_format
        data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = table_widget.item(row, col)
                text = item.text() if item is not None else ""
                row_data.append(text)
            data.append(row_data)
        send_command = b''
        send_command_list = []
        
        for i in range(len(data)):
            send_rule = data[i]
            try:
                pack_rule = struct_head+send_rule[0]
                if ('f' in send_rule[0].lower())|('d' in send_rule[0].lower()):
                    pack_data = try_return_bdx(send_rule[3])/float(send_rule[1])
                else:
                    pack_data = int( try_return_bdx(send_rule[3])/float(send_rule[1]) )
                # print(pack_data)
                send_byte = struct.pack(
                    pack_rule,try_return_check(pack_data,send_rule[0])
                )
                # if ('f' in send_rule[0].lower())|('d' in send_rule[0].lower()):
                #     send_byte = struct.pack(
                #         struct_head+send_rule[0],
                #         try_return_bdx(send_rule[3])/float(send_rule[1])
                #         )
                # else:
                #     send_byte = struct.pack(
                #         struct_head+send_rule[0],
                #         int( try_return_bdx(send_rule[3])/float(send_rule[1]) )
                #         )
                # print(send_byte)
            except Exception as e:
                send_byte = struct.calcsize(struct_head+send_rule[0])*b'\xFF'
            # send_command += send_byte
            send_command_list.append(send_byte)
        try:
            ruleCheck = self.mw.class_general_bind.struct_ruleCheck
            if ruleCheck:
                check_type = self.mw.class_general_bind.struct_typeCheck
                if check_type=='sum':
                    check_string = b''.join(send_command_list[ruleCheck[1]:ruleCheck[2]])
                    check_sum = try_return_check(sum(check_string),data[ruleCheck[0]][0])
                    send_command_list[ruleCheck[0]] = struct.pack(
                        struct_head+data[ruleCheck[0]][0],check_sum
                    )
        except Exception as e:
            print('更新装订规则校验位失败:{}'.format(e))
        send_command = b''.join(send_command_list)
        send_hex = ' '.join(f'{byte:02X}' for byte in send_command)
            
        self.mw.textEdit_general_msg.setPlainText(send_hex)
        self.mw.lineEdit_binding_command.setText(send_hex)
    # 点击事件触发
    def clickEvent_general_send(self):
        send_text = self.mw.textEdit_general_msg.toPlainText()
        send_tab = self.mw.comboBox_general_com.currentText()
        # print('time:{} 发送装订:{}'.format(1,send_text)) 
        send_time = time.strftime('%H:%M:%S',time.localtime())
        self.mw.lineEdit_general_log.setText('{} 发送装订:[{}]...'.format(send_time,send_text[:15]))
        send_text = send_text.replace(' ','')
        if len(send_text)%2==1:
            send_text += '0'
        try:
            send_index = int(send_tab.spplit(' ')[0])
        except:
            send_index = False
        if send_index:
            self.mw.constants.cache_sendHexList[send_index-1] = send_text
        else:
            for i in range(12):
                self.mw.constants.cache_sendHexList[i] = send_text
        
    # 装订规则事件按钮触发
    def clickEvent_general_bind(self):
        sender = self.mw.sender()
        button_name = sender.objectName()
        # print('clickEvent_general_bind事件：{}'.format(button_name))
        button_index = int(button_name.split('_')[2])
        button_index = (button_index-1)%9
        try:
            send_command = self.mw.class_general_bind.struct_buttonList[button_index][1]
        except:
            send_command = ''
        send_command = send_command.replace(' ','')
        if len(send_command)%2==1:
            send_command += '0'
        send_command = ' '.join([send_command[i:i+2] for i in range(0, len(send_command), 2)])
        self.mw.textEdit_general_msg.setPlainText(send_command)
        self.mw.lineEdit_binding_command.setText(send_command)
        self.clickEvent_general_send()
        # send_tab = self.mw.comboBox_general_com.currentText()
        # try:
        #     send_index = int(send_tab.spplit(' ')[0])
        # except:
        #     send_index = False
        # if send_index:
        #     self.mw.constants.cache_sendHexList[send_index-1] = send_command
        # else:
        #     for i in range(12):
        #         self.mw.constants.cache_sendHexList[i] = send_command
    def changeEvent_general_autoSend(self):
        checked = self.mw.checkBox_general_autoSend.isChecked()
        try: times = 1000//int(self.mw.lineEdit_general_sendHz.text())
        except: times = 1000
        if checked:
            # self.mw.textEdit_general_msg.textChanged.connect(self.clickEvent_general_send)
            self.mw.times.time_autoSend.timeout.connect(self.clickEvent_general_send)
            self.mw.times.time_autoSend.start(times)
        else:
            self.mw.times.time_autoSend.timeout.disconnect(self.clickEvent_general_send)
            self.mw.times.time_autoSend.stop()
        

# -----------------12路设置模块事件-----------------
    # com口更新逻辑 涉及com定时更新逻辑 若加入同步，逻辑不清晰 废弃中
    def changeEvent_com_update_all(self):
        pass
        # setting = self.mw.constants.structList_12tab[0].com.currentIndex()
        # for i in range(12):
        #     self.mw.constants.structList_12tab[i+1].set_baund(setting)
    def changeEvent_baund_update_all(self):
        setting = self.mw.constants.structList_12tab[0].baund.currentText()
        for i in range(12):
            self.mw.constants.structList_12tab[i+1].set_baund(setting)
    def changeEvent_check_update_all(self):
        setting = self.mw.constants.structList_12tab[0].check.currentText()
        for i in range(12):
            self.mw.constants.structList_12tab[i+1].set_check(setting)
    def changeEvent_stop_update_all(self):
        setting = self.mw.constants.structList_12tab[0].stop.currentText()
        for i in range(12):
            self.mw.constants.structList_12tab[i+1].set_stop(setting)
    def changeEvent_open_update_all(self):
        setting = self.mw.constants.structList_12tab[0].open.text()
        for i in range(12):
            self.mw.constants.structList_12tab[i+1].set_open(setting)
    def changeEvent_plan_update_all(self):
        setting = self.mw.constants.structList_12tab[0].plan.text()
        for i in range(12):
            self.mw.constants.structList_12tab[i+1].set_plan(setting)
    def changeEvent_open_switch(self,tab):
        self.mw.constants.structList_12tab[tab].switch_open()
    # 主控串口设定同步更新总控
    def changeEvent_baund_update_main(self):
        self.mw.constants.structList_12tab[0].set_baund(self.mw.comboBox_protocal_baund.currentText())
    def changeEvent_check_update_main(self):
        self.mw.constants.structList_12tab[0].set_check(self.mw.comboBox_protocal_check.currentText())
            
            
# ---------------卫导接收事件集-----------------
    # 同步更新事件
# ---------------卫导接收事件集-----------------
    # 同步更新事件
    def changeEvent_auxsate_com(self):
        self.mw.combox_set_com_13.setCurrentText(self.mw.comboBox_ascii_com.currentText())
    def changeEvent_auxsate_baund(self):
        self.mw.combox_set_baund_13.setCurrentText(self.mw.comboBox_ascii_baund.currentText())
    def changeEvent_auxsate_check(self):
        self.mw.comboBox_set_check_13.setCurrentText(self.mw.comboBox_ascii_check.currentText())
    # 发送事件
    def clickEvent_auxsate_send(self):
        send_text = self.mw.comboBox_sate_smsg.toPlainText()
        self.mw.constants.struct_sate.append_sare_send(send_text)
        self.mw.textBrowser_ascii_0.append('{} 载入:{}'.format(self.mw.init_ui.short_time,send_text))
        
# ---------------处理标定事件集-----------------
    def clickEvent_para_loadPath(self):
        oldMode = self.mw.sender().objectName() == 'pushButton_para_loadOld'
        list_para_input = []
        for i in range(5):
            list_para_input.append(self.mw.init_ui.list_para_input[i].text())
            # print(list_para_input)
        for i in range(5):
            try: list_para_input[i] = int(list_para_input[i])
            except: list_para_input[i] = 1
        if list_para_input[2]==0:
            list_para_input[2]=None
        if list_para_input[3]==0:
            list_para_input[3]=None
        # print(list_para_input)
        flag_move_dir = True
        flag_del_empty = self.mw.checkBox_para_delEmptyFolder.isChecked()
            # dir = QtWidgets.QFileDialog.getExistingDirectory(self,'选择文件夹')
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        
        if oldMode:
            if dir:
                # print(dir)
                self.mw.lineEdit_para_loadOld.setText(dir)
            else:
                self.mw.lineEdit_para_loadOld.setText('按提示选择文件路径')
                return
            list_msg = move_dir_para_old(dir)
            self.mw.textBrowser_para_show.append('打开文件夹，准备重新排序...')
            for msg in list_msg:
                self.mw.textBrowser_para_show.append(msg)
            for msg in list_msg:
                if '失败' in msg:
                    flag_move_dir = False
                    self.mw.textBrowser_para_show.append('重新排序过程中有报错，建议检查数据重新处理...')
                    break
            if flag_move_dir:
                self.mw.textBrowser_para_show.append('排序完成，尝试处理中...')
        else:
            if dir:
                # print(dir)
                self.mw.lineEdit_para_loadNew.setText(dir)
            else:
                self.mw.lineEdit_para_loadNew.setText('按提示选择文件路径')
                return
            
        load_paths = Path(dir)
            
        # 删除空文件夹
        if flag_del_empty:
            del_empty_folder(dir)
            self.mw.textBrowser_para_show.append('删除空文件夹')
        save_path = load_paths/'all_ave'
        if os.path.exists(save_path):
            shutil.rmtree(save_path)
        # 遍历惯导名称
        for fog_name in os.listdir(load_paths):
            if not os.path.isdir(load_paths/fog_name):
                continue
            if 'all_' in fog_name:
                continue
            # 遍历测试项目
            for plan_name in os.listdir(load_paths/fog_name):
                if not os.path.isdir(load_paths/fog_name/plan_name):
                    continue
                # 遍历测试文件
                list_ave_file = [
                    f for f in os.listdir(load_paths/fog_name/plan_name) 
                    if (( 'BD' in f )&( '#' in f ))
                    ]
                if len(list_ave_file)==0:
                    continue
                self.mw.textBrowser_para_show.append('处理文件夹:{}/{}'.format(fog_name,plan_name))
                sort_save_path = save_path/fog_name
                if not os.path.exists(sort_save_path):
                    os.makedirs(sort_save_path)
                flag_hztxt = any('hz.txt' in i for i in list_ave_file)
                flag_stxt = any('s.txt' in i for i in list_ave_file)
                # print(list_ave_file)
                save_file_hz = sort_save_path/'{}_ave_hz.txt'.format(plan_name)
                save_file_s = sort_save_path/'{}_ave_s.txt'.format(plan_name)
                if flag_hztxt:
                    lists = [fn for fn in list_ave_file if 'hz.txt' in fn]
                    for filename in sorted( 
                        lists, key= lambda itemname:int(itemname.split('BD')[1].split('#')[0]) 
                        ):
                        try:
                            files = pd.read_csv(load_paths/fog_name/plan_name/filename,sep='\\s+',header=None,skiprows=1, encoding='gb2312')
                        except:
                            continue
                        
                        if ('spd[' in filename):
                            turn_table = filename.split('spd[')[1].split(']')[0]
                            fbegin = list_para_input[0]
                            fend = -list_para_input[2]
                        elif ('loc[' in filename):
                            turn_table = filename.split('loc[')[1].split(']')[0]
                            fbegin = list_para_input[1]
                            fend = -list_para_input[3]
                        else:
                            turn_table = 'None'
                        files = files.iloc[fbegin:fend,:]
                        mean_data = files.mean()
                        len_data = len(files)
                        save_data = '{}\t{}\t{}\n'.format(
                            turn_table,
                            '\t'.join(['{:.6f}'.format(i) for i in mean_data]),
                            len_data
                        )
                        with open(save_file_hz,encoding='gb2312',mode='a+') as f:
                            f.write(save_data)
                    
                    
                if flag_stxt:
                    lists = [fn for fn in list_ave_file if 's.txt' in fn]
                    for filename in sorted( 
                        lists, key= lambda itemname:int(itemname.split('BD')[1].split('#')[0]) 
                        ):
                        try:
                            files = pd.read_csv(load_paths/fog_name/plan_name/filename,sep='\\s+',header=None,skiprows=1, encoding='gb2312')
                        except:
                            continue
                        
                        if ('spd[' in filename):
                            turn_table = filename.split('spd[')[1].split(']')[0]
                            fbegin = list_para_input[0]
                            fend = -list_para_input[2]
                        elif ('loc[' in filename):
                            turn_table = filename.split('loc[')[1].split(']')[0]
                            fbegin = list_para_input[1]
                            fend = -list_para_input[3]
                        else:
                            turn_table = 'None'
                        files = files.iloc[fbegin:fend,:]
                        mean_data = files.mean()
                        len_data = len(files)
                        save_data = '{}\t{}\t{}\n'.format(
                            turn_table,
                            '\t'.join(['{:.6f}'.format(i) for i in mean_data]),
                            len_data
                        )
                        with open(save_file_s,encoding='gb2312',mode='a+') as f:
                            f.write(save_data)

                    
                    
                    
                
                    
    # 实时更新规则文件并更新至表格
    def changeEvent_deocdeRuleToTableWidget(self):
        rules_lists_format = 'xcbB?hHiIlLqQfdspPtyY'
        baund = 460800
        check = 'none'
        heade = '55AA'
        decodeList = []
        decodeLine = ''
        headList = ['标志','格式','保存','系数','标题','排序','接收']
        showTable = self.mw.tableWidget_decode_show
        path_name = self.mw.comboBox_protocal_path.currentText()
        rule_name = self.mw.comboBox_protocal_rule.currentText()
        if path_name not in ['选择路径','',None,'none','None']:
            filename = './解算规则/{}/{}.txt'.format(path_name,rule_name)
        else:
            filename = './解算规则/{}.txt'.format(rule_name)
        if not os.path.exists(filename):
            return False
        try:
            with open(filename, 'r',encoding='gb2312',errors='ignore') as files:
                rules = files.read()
        except Exception as e:
            self.mw.lineEdit_decodeShow_MSG.setText('规则文件读取失败: {}'.format(e))
        showTable.clear()
        showTable.setRowCount(0)
        showTable.setColumnCount(len(headList))
        showTable.setHorizontalHeaderLabels(headList)
        flag_list = ['√','×']
        for line in rules.split('\n'):
            row_position = showTable.rowCount()
            showTable.insertRow(row_position)
            split_data  = line.split()
            if line.startswith('#'): shift=0
            else:shift = 1
            flags = 1
            for index,value in enumerate(split_data):
                if index>4:
                    continue    
                showTable.setItem(row_position,index+shift,QTableWidgetItem(value))
                if (shift==0)&(index==1)&(value=='check'):
                    check = split_data[index+1]
                if (shift==0)&(index==1)&(value=='baund'):
                    baund = split_data[index+1]
                if (shift==0)&(index==1)&(value=='header'):
                    heade = ''.join(split_data[index+1:])
                if (shift==0)&(index==1)&(value=='rulehead'):
                    decodeList.append('')
                    decodeList[-1]+=split_data[index+1]
                if (index==0)&(value in rules_lists_format):
                    flags = 0
                    decodeList[-1]+=value
                    decodeLine+=value
            showTable.setItem(row_position,0,QTableWidgetItem(flag_list[flags]))
        showTable.setColumnWidth(0, 40)
        showTable.setColumnWidth(1, 40)
        showTable.setColumnWidth(5, 40)
        decodeLength = struct.calcsize('>'+decodeLine)
        self.mw.lineEdit_decodeShow_ruleLength.setText(str(decodeLength))
        self.mw.lineEdit_decodeShow_rules.setText(' '.join(decodeList))
        self.mw.lineEdit_decodeShow_MSG.setText('规则文件读取完毕: {}.txt'.format(rule_name))
                
        # time.sleep(10)
        
                    
        
        
        
        
    def clickEvent_para_createPara(self):
        self.mw.textBrowser_para_show.append('未找到规则文件，无法生成参数文件')
        return
    def clickEvent_para_savePara(self):
        self.mw.textBrowser_para_show.append('未找到规则文件，无法保存参数文件')
        return
    
# ---------------通讯协议路径更新事件集-----------------def logic_comboBoxPath_update(self):
    def changeEvent_protocal_path(self):
        sender = self.mw.sender()
        mode = sender.objectName().split('_')[1]
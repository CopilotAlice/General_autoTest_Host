import os
from PyQt5 import QtWidgets
from ui.fun_chy2 import *
import pandas as pd 
# 各类点击事件
class MainWindowEvent:
    def __init__(self,mainWindow):
        self.debug_flag_event = False
        self.mw = mainWindow


# ------------------接收转发/卫导数据接收&转发 开发中--------------
    def clkEvent_recforward_all(self):
        checked = self.mw.checkBox_recforward_all.isChecked()
        for checkbox in self.mw.init_ui.recforward_check_list:
            checkbox.setChecked(checked)

    def changeEvent_recforward(self):
        recforward_text = self.mw.textEdit_recforward_msg.toPlainText()
        print(recforward_text)
        rf_list = recforward_text.split(',')



# ------------------通用装订逻辑事件 开发中--------------
    # 更新装订规则事件
    def changeEvent_general_rule(self):
        load_path = './装订规则'
        comboxpath = self.mw.comboBox_general_path.currentText()
        if comboxpath not in self.mw.list_notpath:
            load_path+= '/{}'.format(comboxpath)
        load_name = self.mw.comboBox_general_rule.currentText()
        # print('changeEvent_general_rule事件：{}'.format(self.mw.comboBox_general_rule.currentText()))
        try:
            filename = '{}/{}.txt'.format(load_path,load_name)
            if os.path.exists(filename):
                with open(filename,'r+',encoding='gb2312') as f:
                    bind_rule_file = f.read()
                self.mw.struct_general_bind.read_struct_file(bind_rule_file)
                return True
            else:
                return False
        except Exception as e:
            # print('更新装订规则失败:{}'.format(e))
            return False
        # self.mainWindow.read_binding()
        

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
        for i in range(10):
            list_para_input.append(self.mw.init_ui.list_para_input[i].text())
            # print(list_para_input)
        for i in range(3):
            try: list_para_input[i] = int(list_para_input[i])
            except: list_para_input[i] = 1
        if list_para_input[1]==0:
            list_para_input[1]=None
        # print(list_para_input)
        self.auto_plot_always = True
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
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                flag_hztxt = any('hz.txt' in i for i in list_ave_file)
                flag_stxt = any('s.txt' in i for i in list_ave_file)
                # print(list_ave_file)
                save_file_hz = save_path/'{}_ave_hz.txt'.format(plan_name)
                save_file_s = save_path/'{}_ave_s.txt'.format(plan_name)
                if flag_hztxt:
                    lists = [fn for fn in list_ave_file if 'hz.txt' in fn]
                elif flag_stxt:
                    lists = [fn for fn in list_ave_file if 's.txt' in fn]
                else:
                    continue
                for filename in sorted( 
                        lists, key= lambda itemname:int(itemname.split('BD')[1].split('#')[0]) 
                        ):
                    # print(filename)
                    mod_list = ['spd[','loc[']
                    turn_table = 'None'
                    for mod in mod_list:
                        if mod in filename:
                            turn_table = filename.split(mod)[1].split(']')[0]
                            break
                        else:
                            turn_table = 'None'
                    try:
                        files = pd.read_csv(load_paths/fog_name/plan_name/filename,sep='\\s+',header=None,skiprows=1, encoding='gb2312')
                    except:
                        # print('pd打开文件失败:{}'.format(filename))
                        continue
                    # if 'loc' not in filename:
                    #     print(load_paths/fog_name/plan_name/filename)
                    #     print(files.head)
                    if flag_hztxt:
                        files = files.iloc[
                            list_para_input[0]*list_para_input[2]:-list_para_input[1]*list_para_input[2],
                            0:12
                            ]
                    else:
                        files = files.iloc[
                            list_para_input[0]:-list_para_input[1],
                            0:12
                            ]
                    # if 'loc' not in filename:
                    #     print(files.head())
                    #     return 
                    mean_data = files.mean()
                    len_data = len(files)
                    save_data = '{}\t{}\t{}\n'.format(
                        turn_table,
                        '\t'.join(['{:.6f}'.format(i) for i in mean_data]),
                        len_data
                    )
                    if save_file_hz:
                        save_name = save_file_hz
                    else:
                        save_name = save_file_s
                    # print('plan:{} save:{}'.format(plan_name,save_name))
                    with open(save_name,encoding='gb2312',mode='a+') as f:
                        f.write(save_data)
                        
                        

                    
                    
                    
                
                    
                
                
                
                    
        
        
        
        
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
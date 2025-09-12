import os
from funs.fun_chy2 import *
import uuid,hashlib
class MainWindowSetting:
    def __init__(self,mainWindow):
        self.mw = mainWindow
                
        # 初始化    para_config 基础内容
        self.init_default_config()
        # 初始化    para_config 卫导相关设定
        self.init_config_sate()
        self.test1 = 1

        # 读取para_config默认配置----------最后执行-------------
        self.init_read_para()
        self.init_read_root()
        self.init_load_setting()


    def init_default_config(self):
        self.para_config_filename = './配置文件/para_config.txt'
        self.root_config_filename = './配置文件/root_config.txt'
        self.flag_read_para   = False # 读取到配置文件
        self.flag_read_root   = False # 读取到配置文件
        self.flag_read_all  = False     # 配置文件全部正常
        self.list_read_error    = []    # 读取配置文件错误记录
        self.list_read_wrong    = []    # 读取配置文件警告记录
        self.flag_save_error_info = True    # 保存

    
    def init_config_sate(self):
        self.sate_append_sate = 1
        self.sate_save_sate = 1
        self.sate_clear_msg = 1
        self.sate_save_1file = 1
        self.sate_save_GNGGA = 1
        self.sate_save_GPGGA = 1
        self.sate_save_BDGGA = 1
        self.sate_save_GPVTG = 1
        self.sate_save_HEADINGA = 1
        self.sate_save_KSXT = 1
        





    def init_read_para(self):
        para_name = self.para_config_filename
        if not os.path.exists(para_name):
            self.flag_read_para   = False
            self.list_read_error.append('init_read_para 没有默认配置文件<{}>'.format(para_name))
        else:
            try:
                files = open(para_name,'r',encoding='gb2312',errors='replace') 
                self.flag_read_para = True
            except Exception as e:
                self.flag_read_para = False
                self.list_read_error.append('init_read_para 读取默认配置文件错误:{}'.format(e))
                return False
            for line in files:
                para_rule_list = line.split()
                if line.startswith('#'):
                    continue
                elif len(para_rule_list)<3:
                    continue
                # 尝试获取配置文件中的变量及赋值，限定符合要求
                try:
                    config_name = para_rule_list[1]
                    config_value = try_int(float(para_rule_list[2]))
                except:
                    self.list_read_wrong.append('init_read_para 未知配置-值:<{}>'.format(para_rule_list))
                    continue
                try:
                    self.__dict__[config_name] = config_value
                except Exception as e:
                    self.list_read_error.append('init_read_para 配置赋值错误:<{}>'.format(e))
                    continue
        
    def init_read_root(self):
        para_name = self.root_config_filename
        if not os.path.exists(para_name):
            self.flag_read_config   = False
            self.list_read_error.append('init_read_root 没有默认配置文件<{}>'.format(para_name))
        else:
            try:
                files = open(para_name,'r',encoding='gb2312',errors='replace') 
                self.flag_read_para = True
            except Exception as e:
                self.flag_read_para = False
                self.list_read_error.append('init_read_root 读取默认配置文件错误:{}'.format(e))
                return False
            for line in files:
                para_rule_list = line.split()
                if line.startswith('#'):
                    continue
                elif len(para_rule_list)<3:
                    continue
                try:
                    config_name = para_rule_list[1]
                    config_value = try_int(float(para_rule_list[2]))
                except:
                    self.list_read_wrong.append('init_read_root 未知配置-值:<{}>'.format(para_rule_list))
                    continue
                try:
                    self.__dict__[config_name] = config_value
                except Exception as e:
                    self.list_read_error.append('init_read_root 配置赋值错误:<{}>'.format(e))
                    continue
        
    def init_load_setting(self):
        mac_uuid = get_machine_code()
        self.mw.lineEdit_debug_6.setText('UUID:{}'.format( mac_uuid ))
        tabwidget = self.mw.tabWidget
        tabwidget_show_list = [
            self.mw.tab_para,
            self.mw.tab_debug2
        ]
        flag_show_tab = mac_uuid not in [
            'AE:DC:28:8F:A9:D8',
            '40:EC:99:76:18:CC',
            '40:EC:99:76:18:CF'
        ]
        if flag_show_tab:
            for tab in tabwidget_show_list:
                index = tabwidget.indexOf(tab)
                if index!=-1:
                    tabwidget.setTabVisible(index,False)

        

# 全局变量/结构体控制模块
import os
from ui.structs import *
class MainWindowConstants:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        # 待完成 载入配置文件
        self.init_load_path()

        # 初始化结构体 12路设置内容
        self.structList_12tab = []
        self.init_12tab_setting()

        # 初始化结构体 通用装订规则 
        self.struct_general_bind = None
        self.init_general_bind()
        
        # 初始化结构体 发送卫导数据
        self.init_send_struct()
        
        
    # 初始化载入文件全局变量
    def init_load_path(self):
        self.load_filepath = os.getcwd()
        
    # 初始化结构体 12路设置内容
    def init_12tab_setting(self):
        self.structList_12tab = []
        self.structList_12tab.append(struct_tab_setting(self.mw,'all'))
        for i in range(14):
            self.structList_12tab.append(struct_tab_setting(self.mw,i+1))
        
    def init_general_bind(self):
        self.struct_general_bind = struct_general_bind()
    
    # 初始化结构体 发送卫导数据
    def init_send_struct(self):
        lists = [
            self.mw.settings.sate_append_sate,
            self.mw.settings.sate_save_sate,
            self.mw.settings.sate_save_GNGGA,
            self.mw.settings.sate_save_GPGGA,
            self.mw.settings.sate_save_BDGGA,
            self.mw.settings.sate_save_GPVTG,
            self.mw.settings.sate_save_HEADINGA,
            self.mw.settings.sate_save_KSXT
        ]
        self.struct_sate = struct_sate()
        self.struct_sate.init_sate_save(lists)
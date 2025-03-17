# ȫ�ֱ�������ģ��
import os
from ui.structs import *
class MainWindowConstants:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        # ����� ���������ļ�
        self.init_load_path()

        # ��ʼ���ṹ�� 12·��������
        self.structList_12tab = []
        self.init_12tab_setting()

        # ��ʼ���ṹ�� ͨ��װ������ 
        self.struct_general_bind = None
        self.init_general_bind()
        
        
        
    # ��ʼ�������ļ�ȫ�ֱ���
    def init_load_path(self):
        self.load_filepath = os.getcwd()
        
    # ��ʼ���ṹ�� 12·��������
    def init_12tab_setting(self):
        self.structList_12tab = []
        self.structList_12tab.append(struct_tab_setting(self.mw,'all'))
        for i in range(14):
            self.structList_12tab.append(struct_tab_setting(self.mw,i+1))
        
    def init_general_bind(self):
        self.struct_general_bind = struct_general_bind()
        
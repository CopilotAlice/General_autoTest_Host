# ȫ�ֱ�������ģ��
import os
class MainWindowConstants:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow

        self.init_load_path()


        self.mainWindow.new_constants = []
        self.mainWindow.clk_couts = 0

    # ��ʼ�������ļ�ȫ�ֱ���
    def init_load_path(self):
        self.load_filepath = os.getcwd()
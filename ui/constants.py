# 全局变量控制模块
import os
class MainWindowConstants:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow

        self.init_load_path()


        self.mainWindow.new_constants = []
        self.mainWindow.clk_couts = 0

    # 初始化载入文件全局变量
    def init_load_path(self):
        self.load_filepath = os.getcwd()
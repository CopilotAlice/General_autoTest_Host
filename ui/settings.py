import os

class MainWindowSetting:
    def __init__(self,mainWindow):
        self.mw = mainWindow
                
        # 初始化    para_config 基础内容
        self.init_default_config()
        # 初始化    para_config 卫导相关设定
        self.init_config_sate()
        self.test1 = 1

        # 读取para_config默认配置----------最后执行-------------
        self.init_read_config()


    def init_default_config(self):
        self.para_config_filename = './配置文件/para_config.txt'
        self.flag_read_config   = False # 读取到配置文件
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
        




    




    def init_read_config(self):
        para_name = self.para_config_filename
        if not os.path.exists(para_name):
            self.flag_read_config   = False
            self.list_read_error.append('init_read_config 没有默认配置文件<{}>'.format(para_name))
        else:
            try:
                files = open(para_name,'r',encoding='gb2312',errors='replace') 
                self.flag_read_config = True
            except Exception as e:
                self.flag_read_config = False
                self.list_read_error.append('init_read_config 读取默认配置文件错误:{}'.format(e))
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
                    config_value = float(para_rule_list[2])
                except:
                    self.list_read_wrong.append('init_read_config 未知配置-值:<{}>'.format(para_rule_list))
                    continue
                # 若配置文件中的变量不在默认配置中，记录错误
                # if not hasattr(self,config_name):
                #     self.list_read_wrong.append('init_read_config 未知配置-项:<{}>'.format(config_name))
                #     continue
                try:
                    self.__dict__[config_name] = config_value
                    print('init_read_config 配置赋值成功:<{}:{}>'.format(config_name,config_value))
                except Exception as e:
                    self.list_read_error.append('init_read_config 配置赋值错误:<{}>'.format(e))
                    print('init_read_config 配置赋值失败:<{}:{}>'.format(config_name,config_value))
                    continue
        # print('-'*20)
        # for i in self.__dict__:
        #     print(i,self.__dict__[i])
                
                
        
    def init_try_int(self,data):
        try:
            return int(data)
        except Exception as e:
            pass
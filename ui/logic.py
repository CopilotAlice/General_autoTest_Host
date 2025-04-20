# 各类逻辑事件
class MainWindowLogic:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        
        # 卫导转发逻辑事件
        self.logic_recforward()
        # 装订规则更新事件
        self.logic_general_bind()
        # 12路设置模块 逻辑
        self.logic_12tab_setting()
        # 通讯协议选择更新事件
        self.logic_protocal_rule_change()
        self.logic_comboBoxPath_update()
        
        # 辅助卫导接收事件逻辑
        self.logic_auxsate()
        # 处理标定数据
        self.logic_cal_BD_data()

    # 卫导转发逻辑事件
    def logic_recforward(self):
        self.mw.textEdit_recforward_msg.textChanged.connect(self.mw.events.changeEvent_recforward)
        self.mw.checkBox_recforward_all.clicked.connect(self.mw.events.clkEvent_recforward_all)


    # 装订规则更新事件
    def logic_general_bind(self):
        self.mw.comboBox_general_rule.currentTextChanged.connect(self.mw.events.changeEvent_general_rule)

    
    # 12路设置模块 逻辑 12路串口更新设定
    def logic_12tab_setting(self):
        for i in range(15):
            self.mw.constants.structList_12tab[i].open.clicked.connect(self.mw.constants.structList_12tab[i].switch_open)
        self.mw.constants.structList_12tab[0].com.currentTextChanged.connect(self.mw.events.changeEvent_com_update_all)
        self.mw.constants.structList_12tab[0].baund.currentTextChanged.connect(self.mw.events.changeEvent_baund_update_all)
        self.mw.constants.structList_12tab[0].check.currentTextChanged.connect(self.mw.events.changeEvent_check_update_all)
        self.mw.constants.structList_12tab[0].stop.currentTextChanged.connect(self.mw.events.changeEvent_stop_update_all)
        self.mw.constants.structList_12tab[0].open.clicked.connect(self.mw.events.changeEvent_open_update_all)
        self.mw.constants.structList_12tab[0].plan.textChanged.connect(self.mw.events.changeEvent_plan_update_all)
        # 主串口更新逻辑 同步更新主控
        self.mw.comboBox_protocal_baund.currentTextChanged.connect(self.mw.events.changeEvent_baund_update_main)
        self.mw.comboBox_protocal_check.currentTextChanged.connect(self.mw.events.changeEvent_check_update_main)
        
    
    # 通讯协议选择更新事件
    def logic_protocal_rule_change(self):
        pass
        
    # 辅助卫导接收事件逻辑
    def logic_auxsate(self):
        # 快捷栏同步更新事件
        # 快捷栏同步更新事件
        self.mw.comboBox_ascii_com.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_com)
        self.mw.comboBox_ascii_baund.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_baund)
        self.mw.comboBox_ascii_check.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_check)
        # 辅助卫导发送事件
        self.mw.pushButton_sate_send.clicked.connect(self.mw.events.clickEvent_auxsate_send)
    
    def logic_cal_BD_data(self):
        self.mw.pushButton_para_loadOld.clicked.connect(self.mw.events.clickEvent_para_loadPath)
        self.mw.pushButton_para_loadNew.clicked.connect(self.mw.events.clickEvent_para_loadPath)
        self.mw.pushButton_para_createPara.clicked.connect(self.mw.events.clickEvent_para_createPara)
        self.mw.pushButton_para_savePara.clicked.connect(self.mw.events.clickEvent_para_savePara)
    
    def logic_comboBoxPath_update(self):
        for paths in self.mw.init_ui.list_comboBox_localPaths:
            paths.currentTextChanged.connect(self.mw.times.timeEvent_update_combobox)
                

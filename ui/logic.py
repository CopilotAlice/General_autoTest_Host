# �����߼��¼�
class MainWindowLogic:
    def __init__(self,mainWindow):
        self.mw = mainWindow
        
        # ����ת���߼��¼�
        self.logic_recforward()
        # װ����������¼�
        self.logic_general_bind()
        # 12·����ģ�� �߼�
        self.logic_12tab_setting()
        # ͨѶЭ��ѡ������¼�
        self.logic_protocal_rule_change()
        
        # �������������¼��߼�
        self.logic_auxsate()


    # ����ת���߼��¼�
    def logic_recforward(self):
        self.mw.textEdit_recforward_msg.textChanged.connect(self.mw.events.changeEvent_recforward)
        self.mw.checkBox_recforward_all.clicked.connect(self.mw.events.clkEvent_recforward_all)


    # װ����������¼�
    def logic_general_bind(self):
        self.mw.comboBox_general_rule.currentTextChanged.connect(self.mw.events.changeEvent_general_rule)

    
    # 12·����ģ�� �߼� 12·���ڸ����趨
    def logic_12tab_setting(self):
        for i in range(15):
            self.mw.constants.structList_12tab[i].open.clicked.connect(self.mw.constants.structList_12tab[i].switch_open)
        self.mw.constants.structList_12tab[0].com.currentTextChanged.connect(self.mw.events.changeEvent_com_update_all)
        self.mw.constants.structList_12tab[0].baund.currentTextChanged.connect(self.mw.events.changeEvent_baund_update_all)
        self.mw.constants.structList_12tab[0].check.currentTextChanged.connect(self.mw.events.changeEvent_check_update_all)
        self.mw.constants.structList_12tab[0].stop.currentTextChanged.connect(self.mw.events.changeEvent_stop_update_all)
        self.mw.constants.structList_12tab[0].open.clicked.connect(self.mw.events.changeEvent_open_update_all)
        self.mw.constants.structList_12tab[0].plan.textChanged.connect(self.mw.events.changeEvent_plan_update_all)
        # �����ڸ����߼� ͬ����������
        self.mw.comboBox_protocal_baund.currentTextChanged.connect(self.mw.events.changeEvent_baund_update_main)
        self.mw.comboBox_protocal_check.currentTextChanged.connect(self.mw.events.changeEvent_check_update_main)
        
    
    # ͨѶЭ��ѡ������¼�
    def logic_protocal_rule_change(self):
        pass
        
    # �������������¼��߼�
    def logic_auxsate(self):
        self.mw.comboBox_ascii_com.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_com)
        self.mw.comboBox_ascii_baund.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_baund)
        self.mw.comboBox_ascii_check.currentTextChanged.connect(self.mw.events.changeEvent_auxsate_check)
    
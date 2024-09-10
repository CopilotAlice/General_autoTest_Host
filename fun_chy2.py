import struct 

def try_int_data(data,default=1):
    try:
        return int(data),False
    except Exception as e:
        return default,e
def try_float_data(data,default=1):
    try:
        return float(data),False
    except Exception as e:
        return default,e
def try_hex_data(data,default=1):
    try:
        return bytes.fromhex(data),False
    except Exception as e:
        return bytes.fromhex(default),e

def crc_1188a(data_add):
    len_word = len(data_add) // 2  # 计算数据长度的一半
    word = [0] * len_word  # 初始化word数组
    crc_value = 0x0000  # 初始化CRC值

    for i in range(len_word):
        word[i] = (data_add[2 * i] << 8) + data_add[2 * i + 1]
        word[i] = ((word[i] >> (i % 16)) | (word[i] << (16 - (i % 16)))) & 0xFFFF
        crc_value ^= word[i]
    
    return crc_value


class class_rule:
    def __init__(self):
        self.rules_lists_format = 'xcbB?hHiIlLqQfdspPtyY'   # 解算规则可用范围
        # 通用参数
        # 规则文件名称
        self.filename = ''
        # 帧头
        self.header = b''
        # 帧尾
        self.ender = b''
        # 大小端
        self.format = '>'
        # 规则长度
        self.rule_length = 1
        # 结算规则
        self.decode_rules = ''
        # 文件标题
        self.file_title = []
        # 结算格式
        self.rule_list = []
        # 是否保存
        self.save_list = []
        # 系数
        self.para_list = []
        # 标题
        self.titl_list = []
        # 排序
        self.cout_list = []
        # 默认值/其他 - 废弃
        self.defa_list = []
        # 是否结算时输出hex原始数
        self.dhex_list = []
        
        # 1553 指定参数
        self.mode = 'normal'
        # 发送间隔
        self.send_ms = 1
        # 每秒频率
        self.send_hz = 1000
        # 子地址
        self.addr = 1

        # 调试报错信息列表
        self.debug_flag_onetime = False
        self.debug_flag_alltime = False
        self.debug_list = []
        self.debug_decode_list = []
        # 调试显示标志位
        self.debug_flag1 = False
        self.debug_flag2 = False
        self.debug_flag3 = False
        self.debug_flag4 = False
        self.debug_flag5 = False
    def reset_debug(self):
        if self.debug_flag_onetime | self.debug_flag_alltime:
            self.debug_flag_onetime = False
            self.debug_list = []
            self.debug_decode_list = []

    def read_rule_file(self,files,filename = 'None'):
        line_count = -1
        self.filename = filename.split('.')[0]
        if len(files)<=0:
            return False,'文件长度为0'
        if '\n' not in files:
            return False,'规则文件读取错误' 
        for line in files.split('\n'):
            if len(line)==0:
                break
            line_count+=1
            rules = line.split()
            if line_count==0:
                self.file_title = rules
            elif len(rules[0])>1:
                self.debug_list.append('{} 规则文件长度不符:<{}>'.format(line_count,rules[0]))
                continue
            elif '#' in rules[0]:
                # 发送频率
                if 'send_ms' in rules[1]:
                    self.send_ms = int(rules[2])
                    if self.send_ms==0:
                        self.send_hz = 0
                    else:
                        self.send_hz = int( 1000/self.send_ms )
                # 大小端
                elif 'rulehead' in rules[1]:
                    self.format = rules[2]
                elif 'send' in rules[1]:
                    self.debug_list.append('{} send-废弃参数{}'.format(line_count,rules[2]))
                    continue
                elif 'rece' in rules[1]:
                    self.debug_list.append('{} rece-废弃参数{}'.format(line_count,rules[2]))
                    continue
                # 1553专用 子地址
                elif 'addr' in rules[1]:
                    self.addr,result = try_int_data(rules[2])
                    if result != False:
                        self.debug_list.append('{} addr取整数错误<{} {}>'.format( line_count,rules[2],result ))
                # 帧头
                elif ('head' in rules[1])&('rule' not in rules[1]):
                    self.header,result = try_hex_data(''.join(rules[2:]))
                    if result != False:
                        self.debug_list.append('{} head取hex错误<{} {}>'.format( line_count,''.join(rules[2:]),result ))

            elif rules[0] in self.rules_lists_format:
                try:
                    self.rule_list.append(rules[0])
                    self.save_list.append(rules[1])
                    self.para_list.append(rules[2])
                    self.titl_list.append(rules[3])
                    self.cout_list.append(rules[4])
                    try:
                        self.defa_list.append(rules[5])
                    except Exception as e:
                        self.defa_list.append('0')
                        self.debug_list.append('{} 注释为空 ：{}'.format(line_count,e))

                except Exception as e:
                    debug_messages = '{} 严重错误：逐行读取规则文件失败:{} '.format(line_count,e)
                    self.debug_list.append(debug_messages)
                    print(debug_messages)

            else:
                self.debug_list.append('{} 未知规则<{}>'.format(line_count,' '.join(rules)))
        self.update_decode_rules()
        self.update_rule_length()
        self.float_para_list()
        return True,'解算完成'

    def update_decode_rules(self):
        self.decode_rules = self.format+''.join(self.rule_list)
    def update_rule_length(self):
        self.rule_length = struct.calcsize(self.decode_rules)
    def float_para_list(self):
        self.dhex_list = []
        for i in range(len(self.para_list)):
            # 不结算而是按照hex格式输出
            if ('h' in self.para_list[i]) | ('H' in self.para_list[i]):
                self.dhex_list.append(1)
                float_data = int(1)
            else:
                self.dhex_list.append(0)
                float_data = float(self.para_list[i])
            # int_data = int(self.para_list[i])
            if float_data.is_integer():
                self.para_list[i] = int(float_data)
            else:
                self.para_list[i] = float_data
    def decode_hex_data(self,hex_data):
        if not hex_data.startswith(self.header):
            self.debug_decode_list.append('帧头错误 {}'.format(hex_data[:len(self.header)+2]))
        if len(hex_data)>self.rule_length:
            hex_data = hex_data[:self.rule_length]
            self.debug_decode_list.append('长度过长 rule_length:{} hex_length:{}'.format(self.rule_length,len(hex_data)))
        if len(hex_data)<self.rule_length:
            hex_data = hex_data.rjust(self.rule_length,b'\x00')
        try:
            decode_data = struct.unpack(self.decode_rules,hex_data)
            decode_data = list(decode_data)
        except Exception as e:
            # decode_data = False
            self.debug_decode_list.append('解算错误 :{} {}'.format(hex_data.hex(),e))
            return False
        try:
            for i in range(len(self.para_list)):
                decode_data[i] *= self.para_list[i]
        except Exception as e :
            self.debug_decode_list.append('参数错误:{} {}'.format(e,decode_data))


        # print(decode_data)
        # return list(decode_data)
        return decode_data

        

class Turntable_class:
    def __init__(self):
        # 转台通讯协议数据帧格式
        self.header='AAAA5555'
        self.command_length = '3800'
        self.command_count = '0100'
        self.inside_command='80'
        self.inside_para1 = '00000000'
        self.inside_para2 = '00000000'
        self.inside_para3 = '00000000'
        self.outside_command='00'
        self.outside_para1 = '00000000'
        self.outside_para2 = '00000000'
        self.outside_para3 = '00000000'
        self.otherside_command='00'
        self.otherside_para1 = '00000000'
        self.otherside_para2 = '00000000'
        self.otherside_para3 = '00000000'
        self.thermostat_command = 'FF'
        self.thermostat_speed = '00'
        self.thermostat_target= '0000'
        self.spare_command = 'FFFFFFFF'
        self.check_command = '00'
        self.all_hex = ''
        self.split_hex = ''
    # 组合各数据帧 计算校验并返回总指令
    def get_command(self):
        all_hex = ''.join([self.command_length,self.command_count,self.inside_command,self.inside_para1,self.inside_para2,self.inside_para3,self.outside_command,self.outside_para1,self.outside_para2,self.outside_para3,self.otherside_command,self.otherside_para1,self.otherside_para2,self.otherside_para3,self.thermostat_command,self.thermostat_speed,self.thermostat_target,self.spare_command])
        # self.command_count = int2hex(int(reverse(self.command_count),16)+1,4)
        # print(self.command_count)
        split_hex = ''
        check = 0
        for i in range(len(all_hex)//2):
            bit = all_hex[i*2:i*2+2]
            split_hex+=bit+' '
            check+=int(bit,16)
        check = int2hex(check)
        all_hex += check
        split_hex += check
        self.check_command = check
        self.all_hex = self.header+all_hex
        self.split_hex = 'AA AA 55 55 '+split_hex
        return self.all_hex
    # 内框置零
    def reset_inside(self):
        self.inside_command='00'
        self.inside_para1 = '00000000'
        self.inside_para2 = '00000000'
        self.inside_para3 = '00000000'
        return self.get_command()
    # 外框置零
    def reset_outside(self):
        self.outside_command='00'
        self.outside_para1 = '00000000'
        self.outside_para2 = '00000000'
        self.outside_para3 = '00000000'
        return self.get_command()
    # 内框归零
    def reset_inside(self):
        self.inside_command = '81'
        self.inside_para1 = reverse(int2hex(0*10000,8))
        self.inside_para2 = reverse(int2hex(10*10000,8))
        self.inside_para3 = reverse(int2hex(10*100,8))
        return self.get_command()
    # 外框归零
    def reset_outside(self):
        self.outside_command = '81'
        self.outside_para1 = reverse(int2hex(0*10000,8))
        self.outside_para2 = reverse(int2hex(10*10000,8))
        self.outside_para3 = reverse(int2hex(10*100,8))
        return self.get_command()
    # 内框设置位置
    def inside_location(self,location=0,speed=10,acceleration=10):
        self.inside_command = '81'
        self.inside_para1 = reverse(int2hex(int(location*10000),8))
        self.inside_para2 = reverse(int2hex(int(speed*10000),8))
        self.inside_para3 = reverse(int2hex(int(acceleration*100),8))
        return self.get_command()
    # 内框设置速率
    def inside_speed(self,speed=10,acceleration=10):
        self.inside_command = '82'
        self.inside_para1 = reverse(int2hex(int(speed*10000),8))
        self.inside_para2 = reverse(int2hex(int(acceleration*100),8))
        self.inside_para3 = '00000000'
        return self.get_command()
    # 外框设置位置

    def outside_location(self,location=0,speed=10,acceleration=10):
        self.outside_command = '81'
        self.outside_para1 = reverse(int2hex(int(location*10000),8))
        self.outside_para2 = reverse(int2hex(int(speed*10000),8))
        self.outside_para3 = reverse(int2hex(int(acceleration*100),8))
        return self.get_command()
    # 外框设置速率
    def outside_speed(self,speed=10,acceleration=10):
        self.outside_command = '82'
        self.outside_para1 = reverse(int2hex(int(speed*10000),8))
        self.outside_para2 = reverse(int2hex(int(acceleration*100),8))
        self.outside_para3 = '00000000'
        return self.get_command()

        
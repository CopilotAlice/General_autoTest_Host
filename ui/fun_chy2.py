import struct, os, shutil
from pathlib import Path
crc_table =[
	0x00000000,0x77073096,0xee0e612c,0x990951ba,0x076dc419,0x706af48f,0xe963a535,0x9e6495a3,
	0x0edb8832,0x79dcb8a4,0xe0d5e91e,0x97d2d988,0x09b64c2b,0x7eb17cbd,0xe7b82d07,0x90bf1d91,
	0x1db71064,0x6ab020f2,0xf3b97148,0x84be41de,0x1adad47d,0x6ddde4eb,0xf4d4b551,0x83d385c7,
	0x136c9856,0x646ba8c0,0xfd62f97a,0x8a65c9ec,0x14015c4f,0x63066cd9,0xfa0f3d63,0x8d080df5,
	0x3b6e20c8,0x4c69105e,0xd56041e4,0xa2677172,0x3c03e4d1,0x4b04d447,0xd20d85fd,0xa50ab56b,
	0x35b5a8fa,0x42b2986c,0xdbbbc9d6,0xacbcf940,0x32d86ce3,0x45df5c75,0xdcd60dcf,0xabd13d59,
	0x26d930ac,0x51de003a,0xc8d75180,0xbfd06116,0x21b4f4b5,0x56b3c423,0xcfba9599,0xb8bda50f,
	0x2802b89e,0x5f058808,0xc60cd9b2,0xb10be924,0x2f6f7c87,0x58684c11,0xc1611dab,0xb6662d3d,
	0x76dc4190,0x01db7106,0x98d220bc,0xefd5102a,0x71b18589,0x06b6b51f,0x9fbfe4a5,0xe8b8d433,
	0x7807c9a2,0x0f00f934,0x9609a88e,0xe10e9818,0x7f6a0dbb,0x086d3d2d,0x91646c97,0xe6635c01,
	0x6b6b51f4,0x1c6c6162,0x856530d8,0xf262004e,0x6c0695ed,0x1b01a57b,0x8208f4c1,0xf50fc457,
	0x65b0d9c6,0x12b7e950,0x8bbeb8ea,0xfcb9887c,0x62dd1ddf,0x15da2d49,0x8cd37cf3,0xfbd44c65,
	0x4db26158,0x3ab551ce,0xa3bc0074,0xd4bb30e2,0x4adfa541,0x3dd895d7,0xa4d1c46d,0xd3d6f4fb,
	0x4369e96a,0x346ed9fc,0xad678846,0xda60b8d0,0x44042d73,0x33031de5,0xaa0a4c5f,0xdd0d7cc9,
	0x5005713c,0x270241aa,0xbe0b1010,0xc90c2086,0x5768b525,0x206f85b3,0xb966d409,0xce61e49f,
	0x5edef90e,0x29d9c998,0xb0d09822,0xc7d7a8b4,0x59b33d17,0x2eb40d81,0xb7bd5c3b,0xc0ba6cad,
	0xedb88320,0x9abfb3b6,0x03b6e20c,0x74b1d29a,0xead54739,0x9dd277af,0x04db2615,0x73dc1683,
	0xe3630b12,0x94643b84,0x0d6d6a3e,0x7a6a5aa8,0xe40ecf0b,0x9309ff9d,0x0a00ae27,0x7d079eb1,
	0xf00f9344,0x8708a3d2,0x1e01f268,0x6906c2fe,0xf762575d,0x806567cb,0x196c3671,0x6e6b06e7,
	0xfed41b76,0x89d32be0,0x10da7a5a,0x67dd4acc,0xf9b9df6f,0x8ebeeff9,0x17b7be43,0x60b08ed5,
	0xd6d6a3e8,0xa1d1937e,0x38d8c2c4,0x4fdff252,0xd1bb67f1,0xa6bc5767,0x3fb506dd,0x48b2364b,
	0xd80d2bda,0xaf0a1b4c,0x36034af6,0x41047a60,0xdf60efc3,0xa867df55,0x316e8eef,0x4669be79,
	0xcb61b38c,0xbc66831a,0x256fd2a0,0x5268e236,0xcc0c7795,0xbb0b4703,0x220216b9,0x5505262f,
	0xc5ba3bbe,0xb2bd0b28,0x2bb45a92,0x5cb36a04,0xc2d7ffa7,0xb5d0cf31,0x2cd99e8b,0x5bdeae1d,
	0x9b64c2b0,0xec63f226,0x756aa39c,0x026d930a,0x9c0906a9,0xeb0e363f,0x72076785,0x05005713,
	0x95bf4a82,0xe2b87a14,0x7bb12bae,0x0cb61b38,0x92d28e9b,0xe5d5be0d,0x7cdcefb7,0x0bdbdf21,
	0x86d3d2d4,0xf1d4e242,0x68ddb3f8,0x1fda836e,0x81be16cd,0xf6b9265b,0x6fb077e1,0x18b74777,
	0x88085ae6,0xff0f6a70,0x66063bca,0x11010b5c,0x8f659eff,0xf862ae69,0x616bffd3,0x166ccf45,
	0xa00ae278,0xd70dd2ee,0x4e048354,0x3903b3c2,0xa7672661,0xd06016f7,0x4969474d,0x3e6e77db,
	0xaed16a4a,0xd9d65adc,0x40df0b66,0x37d83bf0,0xa9bcae53,0xdebb9ec5,0x47b2cf7f,0x30b5ffe9,
	0xbdbdf21c,0xcabac28a,0x53b39330,0x24b4a3a6,0xbad03605,0xcdd70693,0x54de5729,0x23d967bf,
	0xb3667a2e,0xc4614ab8,0x5d681b02,0x2a6f2b94,0xb40bbe37,0xc30c8ea1,0x5a05df1b,0x2d02ef8d
]

def calculate_td_hex(data_list):
    struct_string = 'BbhhhhhhiiihBBBBBBBbhHhhHbBBb'
    struct_list = [i for i in struct_string]
    struct_endian = '<'
    struct_para = [
        1,1,0.0054931640625,0.0054931640625,0.0054931640625,
        0.02,0.02,0.02,0.0003017485/3600,0.0003017485/3600,0.01,
        1,1,1,1,1,1,10,0.1,1,
        0.5,0.0054931640625,0.0054931640625,0.0054931640625,0.0054931640625,
        1,5,1,1
    ]
    struct_return_list = []
    for i in range(len(struct_string)):
        try: pack_data = struct.pack(struct_endian+struct_list[i],int(data_list[i]/struct_para[i]))
        except: pack_data = struct.pack(struct_endian+struct_list[i],0)
        struct_return_list.append(pack_data)
    return struct_return_list
    
def calculate_fz_hex(data_list):
    struct_string = 'BbiiiiiiB'
    struct_list = [i for i in struct_string]
    struct_endian = '<'
    struct_para = [
        1,1,
        0.000001,0.000001,0.000001,0.000001,0.000001,0.000001,
        1
    ]
    struct_return_list = []
    for i in range(len(struct_string)):
        try: pack_data = struct.pack(struct_endian+struct_list[i],int(data_list[i]/struct_para[i]))
        except: pack_data = struct.pack(struct_endian+struct_list[i],0)
        struct_return_list.append(pack_data)
    return struct_return_list
    
def calculate_gnss_hex(data_list):
    struct_string = 'BBBhhh'+ 'iiii'+ 'HBBBBBB'+ 'BBBHBBHB'+ 'HhBBBBB'+'BBBB'
    struct_list = [i for i in struct_string]
    struct_endian = '<'
    struct_para = [
        1,1,0.1,0.02,0.02,0.02,
        0.0003017485/3600,0.0003017485/3600,0.01,0.01,
        1,1,1,1,1,1,0.1,
        1,1,1,1,1,1,1,1,
        0.0054931640625,0.0054931640625,0.1,0.1,0.1,1,1
    ]
    struct_return_list = []
    for i in range(len(struct_string)):
        try: pack_data = struct.pack(struct_endian+struct_list[i],int(data_list[i]/struct_para[i]))
        except: pack_data = struct.pack(struct_endian+struct_list[i],0)
        struct_return_list.append(pack_data)
    return struct_return_list

def calculate_crc32(buffer: bytearray) -> int:
    """
    计算给定二进制缓冲区的 CRC32 值
    :param buffer: 二进制缓冲区（bytearray）
    :return: 计算得到的 CRC32 值
    """
    ul_crc = 0
    for byte in buffer:
        ul_crc = crc_table[(ul_crc ^ byte) & 0xff] ^ (ul_crc >> 8)
    return ul_crc

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
    crc_value = (crc_value<<len_word%16) | (crc_value>>(16-(len_word%16)))
    return crc_value&0xffff
    # return crc_value

def move_dir(src,dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    shutil.move(src,dest)
def split_pro(data):
    split_symbol = [' ',',','，']
    for symbol in split_symbol:
        data = '#*#'.join(data.split(symbol))
    return [item for item in data.split('#*#') if item]
def move_dir_para_old(from_path,skip_name = ['all_ave']):
    from_path = Path(from_path)
    to_path = from_path
    list_msg = []
    for test_name in os.listdir(from_path):
        if test_name in skip_name:
            continue
        for fog_name in os.listdir(from_path/test_name):
            if fog_name in skip_name:
                continue
            fog_path = from_path/test_name/fog_name
            to_fog_path = to_path/fog_name/test_name
            try:
                for data_name in os.listdir(fog_path):
                    move_dir(fog_path/data_name,to_fog_path)
                list_msg.append('移动文件夹: {} -> {}'.format(
                    str(fog_path).replace(str(from_path),''),str(to_fog_path).replace(str(from_path),'')
                    ))
            except Exception as e:
                list_msg.append('移动文件夹失败: {} {}'.format(fog_path,e))
    return list_msg
def del_empty_folder(path):
    for folder in os.listdir(path):
        folder_path = os.path.join(path,folder)
        if os.path.isdir(folder_path):
            del_empty_folder(folder_path)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                
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

decode_rule_01 = '''#	大小端	是否保存	系数	标题	排序	注释
#	baund	115200				
#	check	none	(none/odd/even			
#	header	99	66			
#	latitude	39.73675				
#	longitude	116.50984				
#	height	20				
#	alignment_time	100				
#	receive_hz	50		
#	drop0data    None   [1]					
#	rulehead	<				
B	0	1	0x99	N		
B	0	1	0x66	N		
B	0	1	帧数据长度	N		
I	1	1	导航时间	0		
i	1	8.381903175442434e-08	纬度	1		
i	1	7.628928873515189e-06	高度	2		
i	1	8.381903175442434e-08	经度	3		
h	1	0.007812738425855281	X轴速度	N		
h	1	0.007812738425855281	Y轴速度	N		
h	1	0.007812738425855281	Z轴速度	N		
h	1	0.005493331705679495	横滚角	N		
h	1	0.005493331705679495	航向角	N		
h	1	0.005493331705679495	俯仰角	N		
h	1	0.009155552842799158	X轴角速率	N		
h	1	0.009155552842799158	Y轴角速率	N		
h	1	0.009155552842799158	Z轴角速率	N		
h	1	0.0030518509475997192	X轴加速度	N		
h	1	0.0030518509475997192	Y轴加速度	N		
h	1	0.0030518509475997192	Z轴加速度	N		
I	1	1	状态字低32位	N		
I	1	1	状态字高32位	N		
I	1	1	算法状态字低32位	N		
B	1	1	导航方式状态字	N						
#	rulehead	<	
B	1	1	GPS状态	N		
B	1	1	接收机定位星数	N		
B	1	1	备份	N		
i	1	8.381903175442434e-08	接收机纬度	N		
i	1	7.628928873515189e-06	接收机高度	N		
i	1	8.381903175442434e-08	接收机经度	N		
h	1	0.005493331705679495	接收机航向	N		
h	1	0.028125878933716678	接收机前向速度	N		
h	1	0.007812738425855281	接收机PDOP值	N					
#	rulehead	<		
h	1	1	导航软件版本号	N		
I	1	1	惯导产品编号	N		
h	1	1	惯导滚动角误差估计值	N		
h	1	1	惯导俯仰角误差估计值	N		
h	1	1	X加表零位估计值	N		
h	1	1	Y加表零位估计值	N		
h	1	1	Z加表零位估计值	N		
h	1	0	备份	N		
h	1	0	备份	N		
B	1	0	备份	N		
B	1	0	异或校验	N		
B	1	0	和校验	N		'''
decode_rule_02 = '''#	是否保存	系数	标题	排序	注释
#	baund	460800			
#	check	none	(none/odd/even		
#	header	55	AA		
#	ender	C0	FF		
#	latitude	39.73675			
#	longitude	116.50984			
#	height	20			
#	alignment_time	200			
#	receive_hz	200			
#	special_flag	gd1s_wd			
#	sum_check	None	[2,3:61]
#	drop0data    [1]			
#	rulehead	>			
B	0	1	0x55	N	
B	0	1	0xAA	N	
B	0	1	校验和	N	（3~61字节的和）
B	0	1	PPS到来时间差	N	（4us/LSB
H	0	1	状态字	N	（0x07:标识PPS到来；）
h	1	0.0625	z加表温度	12	（输出值/16为加表温度℃）
I	1	0.005	5ms计数	0	
f	1	41256000	Gx	1	（5ms的角度增量，单位为弧度）
f	1	41256000	Gy	2	（5ms的角度增量，单位为弧度）
f	1	41256000	Gz	3	（5ms的角度增量，单位为弧度）
f	1	200	Ax	4	（5ms的速度增量，m/s）
f	1	200	Ay	5	（5ms的速度增量，m/s）
f	1	200	Az	6	（5ms的速度增量，m/s）
h	1	0.0625	x陀螺温度	7	（输出值为陀螺温度℃）
h	1	0.0625	y陀螺温度	8	（输出值为陀螺温度℃）
h	1	0.0625	z陀螺温度	9	（输出值为陀螺温度℃）
h	1	0.0625	x加表温度	10	（输出值/16为加表温度℃）
h	1	0.0625	y加表温度	11	（输出值/16为加表温度℃）
B	1	1	校正使能	N	
B	1	1	无线电有效标志	N	
B	1	1	气压高度标志	N	
B	1	1	卫导模式	N	
B	1	1	保留	N	
B	1	1	系统工作状态	N	
B	1	1	卫导1更新标志	N	
B	1	1	卫导2更新标志	N	
B	1	1	5ms标志	N	
x	0	1	状态0	N	
x	0	1	状态1	N	
x	0	1	状态2	N	
x	0	1	保留	N	
x	0	1	保留	N	
x	0	1	保留	N	
x	0	1	保留	N	
x	0	1	0xC0	N	
x	0	1	0xFF	N	
#	rulehead	<			
B	0	1	0x66	N	
B	0	1	0x99	N	
B	0	1	校验和	N	（3~61字节的和）
H	1	1	GPS周	N	
I	1	1.00E-03	GPS秒	N	
i	1	1.00E-07	卫导1纬度	N	
i	1	1.00E-07	卫导1经度	N	
i	1	1.00E-03	卫导1高度	N	
H	1	1.00E-03	卫导1PDOP	N	
B	1	1.00E+00	卫导1定位状态	N	
B	1	1.00E+00	卫导1卫星数	N	
i	1	1.00E-03	真北航向角	N	
i	1	1.00E-03	地面速度	N	
B	1	1.00E+00	模式指示	N	
B	1	1.00E+00	卫导选择使能	N	
B	1	1.00E+00	卫导通道标志	N	
B	1	1.00E+00	卫导模式	N	
i	1	1.00E-07	卫导2纬度	N	
i	1	1.00E-07	卫导2经度	N	
i	1	1.00E-03	卫导2高度	N	
H	1	1.00E-03	卫导2PDOP	N	
B	1	1.00E+00	卫导2定位状态	N	
B	1	1.00E+00	卫导2卫星数	N	
i	1	1.00E-03	卫导2真北航向角	N	
i	1	1.00E-03	卫导2地面速度	N	
B	1	1.00E+00	卫导2模式指示	N	
B	0	1	0xC0	N	
B	0	1	0xFF	N	
#	rulehead	<			
B	0	1	0xAA	N	
B	0	1	0xBB	N	
B	0	1	校验和	N	（3~61字节的和）
H	1	1	周	N	（低字节在前）
I	1	0.001	秒	N	（低字节在前），量纲：1e-3
i	1	1.00E-07	纬度	N	（4字节，低字节在前，单位：度）
i	1	1.00E-07	经度	N	（4字节，低字节在前，单位：度）
i	1	1.00E-03	高度	N	（4字节，低字节在前，单位：米）
i	1	1.00E-04	东向速度x	N	（低字节在前），量纲：1e-4，单位：m/s
i	1	1.00E-04	北向速度y	N	（低字节在前），量纲：1e-4，单位：m/s
i	1	1.00E-04	天向速度z	N	（低字节在前），量纲：1e-4，单位：m/s
i	1	1.00E-06	俯仰角x	N	（低字节在前），量纲：1e-6，单位：度
i	1	1.00E-06	滚转角y	N	（低字节在前），量纲：1e-6，单位：度
i	1	1.00E-06	偏航角z	N	（低字节在前），量纲：1e-6，单位：度
B	1	1	状态字	N	（0x01：初始对准；0x02：纯惯性；0x03：纯惯性
H	1	1	耗时	N	
h	1	1	加表X零位	N	（低字节在前，单位：ug）
h	1	1	加表Y零位	N	（低字节在前，单位：ug）
h	1	1	加表Z零位	N	（低字节在前，单位：ug）
b	1	1.00E-03	陀螺X零位	N	（低字节在前，单位：度）
b	1	1.00E-03	陀螺Y零位	N	（低字节在前，单位：度）
b	1	1.00E-03	陀螺Z零位	N	（低字节在前，单位：度）
B	0	1	保留	N	
H	0	1	保留	N	
H	0	1	保留	N	
B	0	1	0xC0	N	
B	0	1	0xFF	N	'''
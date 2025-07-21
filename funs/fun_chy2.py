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
crc16_table = [
    0x0000,0x1021,0x2042,0x3063,0x4084,0x50A5,0x60C6,0x70E7,
    0x8108,0x9129,0xA14A,0xB16B,0xC18C,0xD1AD,0xE1CE,0xF1EF,
    0x1231,0x0210,0x3273,0x2252,0x52B5,0x4294,0x72F7,0x62D6,
    0x9339,0x8318,0xB37B,0xA35A,0xD3BD,0xC39C,0xF3FF,0xE3DE,
    0x2462,0x3443,0x0420,0x1401,0x64E6,0x74C7,0x44A4,0x5485,
    0xA56A,0xB54B,0x8528,0x9509,0xE5EE,0xF5CF,0xC5AC,0xD58D,
    0x3653,0x2672,0x1611,0x0630,0x76D7,0x66F6,0x5695,0x46B4,
    0xB75B,0xA77A,0x9719,0x8738,0xF7DF,0xE7FE,0xD79D,0xC7BC,
    0x48C4,0x58E5,0x6886,0x78A7,0x0840,0x1861,0x2802,0x3823,
    0xC9CC,0xD9ED,0xE98E,0xF9AF,0x8948,0x9969,0xA90A,0xB92B,
    0x5AF5,0x4AD4,0x7AB7,0x6A96,0x1A71,0x0A50,0x3A33,0x2A12,
    0xDBFD,0xCBDC,0xFBBF,0xEB9E,0x9B79,0x8B58,0xBB3B,0xAB1A,
    0x6CA6,0x7C87,0x4CE4,0x5CC5,0x2C22,0x3C03,0x0C60,0x1C41,
    0xEDAE,0xFD8F,0xCDEC,0xDDCD,0xAD2A,0xBD0B,0x8D68,0x9D49,
    0x7E97,0x6EB6,0x5ED5,0x4EF4,0x3E13,0x2E32,0x1E51,0x0E70,
    0xFF9F,0xEFBE,0xDFDD,0xCFFC,0xBF1B,0xAF3A,0x9F59,0x8F78,
    0x9188,0x81A9,0xB1CA,0xA1EB,0xD10C,0xC12D,0xF14E,0xE16F,
    0x1080,0x00A1,0x30C2,0x20E3,0x5004,0x4025,0x7046,0x6067,
    0x83B9,0x9398,0xA3FB,0xB3DA,0xC33D,0xD31C,0xE37F,0xF35E,
    0x02B1,0x1290,0x22F3,0x32D2,0x4235,0x5214,0x6277,0x7256,
    0xB5EA,0xA5CB,0x95A8,0x8589,0xF56E,0xE54F,0xD52C,0xC50D,
    0x34E2,0x24C3,0x14A0,0x0481,0x7466,0x6447,0x5424,0x4405,
    0xA7DB,0xB7FA,0x8799,0x97B8,0xE75F,0xF77E,0xC71D,0xD73C,
    0x26D3,0x36F2,0x0691,0x16B0,0x6657,0x7676,0x4615,0x5634,
    0xD94C,0xC96D,0xF90E,0xE92F,0x99C8,0x89E9,0xB98A,0xA9AB,
    0x5844,0x4865,0x7806,0x6827,0x18C0,0x08E1,0x3882,0x28A3,
    0xCB7D,0xDB5C,0xEB3F,0xFB1E,0x8BF9,0x9BD8,0xABBB,0xBB9A,
    0x4A75,0x5A54,0x6A37,0x7A16,0x0AF1,0x1AD0,0x2AB3,0x3A92,
    0xFD2E,0xED0F,0xDD6C,0xCD4D,0xBDAA,0xAD8B,0x9DE8,0x8DC9,
    0x7C26,0x6C07,0x5C64,0x4C45,0x3CA2,0x2C83,0x1CE0,0x0CC1,
    0xEF1F,0xFF3E,0xCF5D,0xDF7C,0xAF9B,0xBFBA,0x8FD9,0x9FF8,
    0x6E17,0x7E36,0x4E55,0x5E74,0x2E93,0x3EB2,0x0ED1,0x1EF0
]
def general_crc16Table():
    table = []
    poly = 0x1021
    for byte in range(256):
        crc = byte<<8
        for _ in range(8):
            if crc&0x8000:
                crc = ((crc<<1)^poly)&0xffff
            else:
                crc = (crc<<1)&0xffff
        table.append(crc)
    return table
def calculate_crc16(data):
    crc = 0xffff
    for byte in data:
        tbl_idx = ((crc>>8)^byte)&0xff
        crc = ((crc<<8)^crc16_table[tbl_idx])&0xffff
    return crc
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
    shutil.move(str(src),str(dest))
def split_pro(data):
    split_symbol = [' ',',','，']
    for symbol in split_symbol:
        data = '#*#'.join(data.split(symbol))
    return [item for item in data.split('#*#') if item]
def split_plus(data):
    split_list = data.replace('[','').replace(']','')
    for flag in [',','，',':','：']:
        split_list = split_list.replace(flag,' ')
    return split_list.split()
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

# 尝试返回格式
def try_return_format(format):
    format = str(format)
    if '>' in format:
        return '>'
    else:
        return '<'
def try_return_int(data,default=1):
    try:return int(data)
    except:return default
def try_return_num(data,default=1):
    try:
        data = float(data)
        return int(data) if data.is_integer() else data
    except:
        return default
def try_return_checkRule(data,default=False):
    # 77,2:76
    try:
        for i in [' ',',','，',':','：']:
            data = data.replace(i,' ')
        check_tar = int(data.split()[0])
        check_beg = int(data.split()[1])
        check_end = int(data.split()[2])
        return [check_tar,check_beg,check_end]
    except:
        return default
def try_return_bdx(data,default=1):
    if '0x' in data:
        try: return int(data,16)
        except: return default
    elif '0b' in data:
        try: return int(data,2)
        except:return default
    else:
        return try_return_num(data,default)
def try_return_check(data,type):
    limits = {
        'b': 256,
        'B': 256,
        'h': 65536,
        'H': 65536,
        'i': 2**32,
        'I': 2**32,
        'q': 2**64,
        'Q': 2**64
    }
    try:
        return int(data) % limits[type]
    except:
        return data
def try_int(data):
    if isinstance(data,float) and data.is_integer():
        return int(data)
    return data
def check2serial(data):
    import serial
    try: return [serial.PARITY_NONE,serial.PARITY_EVEN,serial.PARITY_ODD][['无校验','偶校验','奇校验'].index(str(data).lower())]
    except: return serial.PARITY_NONE
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

        

# class Turntable_class:
#     def __init__(self):
#         # 转台通讯协议数据帧格式
#         self.header='AAAA5555'
#         self.command_length = '3800'
#         self.command_count = '0100'
#         self.inside_command='80'
#         self.inside_para1 = '00000000'
#         self.inside_para2 = '00000000'
#         self.inside_para3 = '00000000'
#         self.outside_command='00'
#         self.outside_para1 = '00000000'
#         self.outside_para2 = '00000000'
#         self.outside_para3 = '00000000'
#         self.otherside_command='00'
#         self.otherside_para1 = '00000000'
#         self.otherside_para2 = '00000000'
#         self.otherside_para3 = '00000000'
#         self.thermostat_command = 'FF'
#         self.thermostat_speed = '00'
#         self.thermostat_target= '0000'
#         self.spare_command = 'FFFFFFFF'
#         self.check_command = '00'
#         self.all_hex = ''
#         self.split_hex = ''
#     # 组合各数据帧 计算校验并返回总指令
#     def get_command(self):
#         all_hex = ''.join([self.command_length,self.command_count,self.inside_command,self.inside_para1,self.inside_para2,self.inside_para3,self.outside_command,self.outside_para1,self.outside_para2,self.outside_para3,self.otherside_command,self.otherside_para1,self.otherside_para2,self.otherside_para3,self.thermostat_command,self.thermostat_speed,self.thermostat_target,self.spare_command])
#         # self.command_count = int2hex(int(reverse(self.command_count),16)+1,4)
#         # print(self.command_count)
#         split_hex = ''
#         check = 0
#         for i in range(len(all_hex)//2):
#             bit = all_hex[i*2:i*2+2]
#             split_hex+=bit+' '
#             check+=int(bit,16)
#         check = int2hex(check)
#         all_hex += check
#         split_hex += check
#         self.check_command = check
#         self.all_hex = self.header+all_hex
#         self.split_hex = 'AA AA 55 55 '+split_hex
#         return self.all_hex
#     # 内框置零
#     def reset_inside(self):
#         self.inside_command='00'
#         self.inside_para1 = '00000000'
#         self.inside_para2 = '00000000'
#         self.inside_para3 = '00000000'
#         return self.get_command()
#     # 外框置零
#     def reset_outside(self):
#         self.outside_command='00'
#         self.outside_para1 = '00000000'
#         self.outside_para2 = '00000000'
#         self.outside_para3 = '00000000'
#         return self.get_command()
#     # 内框归零
#     def reset_inside(self):
#         self.inside_command = '81'
#         self.inside_para1 = reverse(int2hex(0*10000,8))
#         self.inside_para2 = reverse(int2hex(10*10000,8))
#         self.inside_para3 = reverse(int2hex(10*100,8))
#         return self.get_command()
#     # 外框归零
#     def reset_outside(self):
#         self.outside_command = '81'
#         self.outside_para1 = reverse(int2hex(0*10000,8))
#         self.outside_para2 = reverse(int2hex(10*10000,8))
#         self.outside_para3 = reverse(int2hex(10*100,8))
#         return self.get_command()
#     # 内框设置位置
#     def inside_location(self,location=0,speed=10,acceleration=10):
#         self.inside_command = '81'
#         self.inside_para1 = reverse(int2hex(int(location*10000),8))
#         self.inside_para2 = reverse(int2hex(int(speed*10000),8))
#         self.inside_para3 = reverse(int2hex(int(acceleration*100),8))
#         return self.get_command()
#     # 内框设置速率
#     def inside_speed(self,speed=10,acceleration=10):
#         self.inside_command = '82'
#         self.inside_para1 = reverse(int2hex(int(speed*10000),8))
#         self.inside_para2 = reverse(int2hex(int(acceleration*100),8))
#         self.inside_para3 = '00000000'
#         return self.get_command()
#     # 外框设置位置

#     def outside_location(self,location=0,speed=10,acceleration=10):
#         self.outside_command = '81'
#         self.outside_para1 = reverse(int2hex(int(location*10000),8))
#         self.outside_para2 = reverse(int2hex(int(speed*10000),8))
#         self.outside_para3 = reverse(int2hex(int(acceleration*100),8))
#         return self.get_command()
#     # 外框设置速率
#     def outside_speed(self,speed=10,acceleration=10):
#         self.outside_command = '82'
#         self.outside_para1 = reverse(int2hex(int(speed*10000),8))
#         self.outside_para2 = reverse(int2hex(int(acceleration*100),8))
#         self.outside_para3 = '00000000'
#         return self.get_command()

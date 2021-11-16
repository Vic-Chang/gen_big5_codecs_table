def gen_big5_hex() -> tuple[hex, hex]:
    """
    產出 Big5 內碼 Table
    :return: 回傳 Tuple[ 現行 Hex , 低位 Hex ]
    """
    # BIG5 為雙位元組字元集
    # 高位元數列為: 0x81-0xFE
    high_bytes_from = 0x81
    high_bytes_to = 0xFE

    # 低位元數列為: 0x40-0x7E 、 及0xA1-0xFE 兩組
    low_bytes_from = 0x40
    low_bytes_to = 0xFE
    # 排除掉以下 (位於 0x7E 至 0xA1 數列)
    low_bytes_exclude_from = 0x7F
    low_bytes_exclude_to = 0xA0
    for high in range(high_bytes_from, high_bytes_to + 1):
        for low in range(low_bytes_from, low_bytes_to + 1):
            if low not in range(low_bytes_exclude_from, low_bytes_exclude_to + 1):
                yield hex((high << 8) + low), hex(low)


def gen_big5_table(codecs_name):
    """
    依照編碼, 產出一張內碼Table
    :param codecs_name: Big5 類
    :return: Print 出 Table
    """
    # Print Header
    print('　　｜　+0　+1　+2　+3　+4　+5　+6　+7　+8　+9　+A　+B　+c　+D　+E　+F')

    current_hex_head = ''
    msg = ''
    for big5_hex, low_hex in gen_big5_hex():
        hex_str = big5_hex[2:]
        low_hex_str = low_hex[2:]
        hex_head = hex_str[:3]
        if current_hex_head == hex_head:
            char = get_decoded_char(codecs_name, hex_str)
            if char is not None:
                msg += f'　{char}'
            else:
                msg += f'　None'

            # 若低位元為 '7e' or 'fe', 則下一個肯定不存在 (ff, 7f), 原因為低位元只到 0x7E 以及 0xFE
            if low_hex_str.lower() in ['7e', 'fe']:
                msg += f'　Undefined'
        else:
            # 印出累積的資料行
            if msg != '':
                print(msg)
            msg = ''

            current_hex_head = hex_head
            msg += f'{current_hex_head}　｜　'

            # 若低位元為 'a1', 則上一個肯定不存在 (a0), 原因為 0xA0 位於低位排除名單內
            if low_hex_str.lower() == 'a1':
                msg += f'　Undefined'
            char = get_decoded_char(codecs_name, hex_str)
            if char is not None:
                msg += f'　{char}'
            else:
                msg += f'　None'


def gen_big5_markdown_table(codecs_name):
    """
    依照編碼, 產出一張 Markdown 語法內碼Table
    :param codecs_name: Big5 類
    :return: Print 出 Table
    """
    # Print Header
    print(f'{codecs_name}| +0| +1| +2| +3| +4| +5| +6| +7| +8| +9| +A| +B| +c| +D| +E| +F|')
    print(f'---------| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:| :-:|')

    current_hex_head = ''
    msg = ''
    for big5_hex, low_hex in gen_big5_hex():
        hex_str = big5_hex[2:]
        low_hex_str = low_hex[2:]
        hex_head = hex_str[:3]
        if current_hex_head == hex_head:
            char = get_decoded_char(codecs_name, hex_str)
            if char is not None:
                msg += f'{char}|'
            else:
                msg += f'None|'

            # 若低位元為 '7e' or 'fe', 則下一個肯定不存在 (ff, 7f), 原因為低位元只到 0x7E 以及 0xFE
            if low_hex_str.lower() in ['7e', 'fe']:
                msg += f'Undefined|'
        else:
            # 印出累積的資料行
            if msg != '':
                print(msg)
            msg = ''

            current_hex_head = hex_head
            msg += f'{current_hex_head}|'

            # 若低位元為 'a1', 則上一個肯定不存在 (a0), 原因為 0xA0 位於低位排除名單內
            if low_hex_str.lower() == 'a1':
                msg += f'Undefined|'
            char = get_decoded_char(codecs_name, hex_str)
            if char is not None:
                msg += f'{char}|'
            else:
                msg += f'None|'


def get_decoded_char(codecs_name, hex_str):
    try:
        char = bytes.fromhex(hex_str).decode(codecs_name)
        return char
    except UnicodeDecodeError as e:
        return None


if __name__ == '__main__':
    gen_big5_markdown_table('big5')

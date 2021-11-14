def gen_big5_hex():
    # BIG5 為雙位元組字元集
    high_bytes_from = 0x81
    high_bytes_to = 0xFE

    low_bytes_from = 0x40
    low_bytes_to = 0xFF
    for high in range(high_bytes_from, high_bytes_to):
        for low in range(low_bytes_from, low_bytes_to):
            # print(f'{hex(high << 8)} + {hex(low)} = {hex((high << 8) + low)} = {bytes.fromhex(hex((high << 8) + low)).decode("big5")}')
            yield hex((high << 8) + low)


def gen_big5_table(codecs_name):
    last_char_list = [i for i in range(15)]
    # last_char_list.extend(['A', 'B', 'C', 'D', 'E', 'F'])
    # for i in last_char_list:
    #     print(i)

    from_code = 0xA440
    to_code = 0xC67E
    for code in range(from_code, to_code):
        for i in last_char_list:
            if code + i > to_code:
                break
            try:
                # print(f'code: {code}, int: {code + i}, words: {bytes.fromhex(hex(code + i)[2:]).decode("big5")}')
                bytes.fromhex(hex(code + i)[2:]).decode(codecs_name)
            except:
                print(hex(code + i))


if __name__ == '__main__':
    # gen_big5_table('cp950')
    for i in gen_big5_hex():
        try:
            print(bytes.fromhex(i[2:]).decode("big5"))
        except:
            pass
            # print('None')

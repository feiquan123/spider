def read_file(file):
    buff_size = 1024
    with open(file, 'r',encoding='utf-8') as f:
        while True:
            block = f.read(buff_size)
            if block:
                yield block
            else:
                return


if __name__ == '__main__':
    for row in read_file('../out/douban.csv'):
        print(row)
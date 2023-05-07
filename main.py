#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

# 文件路径
FILE_PATH = "FOME.txt"
# 分割数量
SPLIT_NUMBER = 3


if __name__ == '__main__':
    file_name, file_suffix = os.path.splitext(FILE_PATH)

    # 读取文件
    with open(FILE_PATH, "r") as f:
        content = f.readlines()

    # 按行解析文件
    data = list()
    item = list()
    for line in reversed(content):
        item.insert(0, line)
        if line.startswith(">"):
            data.insert(0, item)
            item = list()

    # 拆分并保存文件
    dir_name = str(int(time.time()))
    os.mkdir(dir_name)
    for index, data_item in enumerate(data):
        file_path = os.path.join(dir_name, f"{file_name}{int(index / SPLIT_NUMBER)}{file_suffix}")
        with open(file_path, "a") as f:
            f.writelines(data_item)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time       : 2021/3/9 23:28
@Author     : Andy
@Email      : zd18zd@163.com
"""


import pandas as pd


csv_file = "phone-book.csv"
vcf_file = "phone-book2.vcf"


def get_csv(f):
    df = pd.read_csv(f, index_col=None)
    # print(df)
    return df


def main():
    df = get_csv(csv_file)

    name_list = df["name"].tolist()
    number_list = df["number"].tolist()
    if len(name_list) != len(number_list):
        raise ValueError("CSV file is wrong .")

    with open(vcf_file, "w+", encoding="utf-8") as f:
        content = ["BEGIN:VCARD", "VERSION:3.0", "", "", "", "END:VCARD\n", ]
        for i in range(len(name_list)):
            content[2] = "N;CHARSET=UTF-8:" + str(name_list[i])
            content[3] = "FN;CHARSET=UTF-8:" + str(name_list[i])
            content[4] = "TEL;TYPE=CELL:" + str(number_list[1])
            line = "\n".join(content)
            f.write(line)
            content = ["BEGIN:VCARD", "VERSION:3.0", "", "", "", "END:VCARD\n", ]
    print("Writing is  Done !!!")


if __name__ == '__main__':
    main()

from winreg import *
import pandas as pd
import json, re


# from collections import OrderedDict


class Read:
    # key_string = ''
    # path = 'A:\\!Series'

    def __init__(self):
        self.key_string = r'Software\MPC-HC\MPC-HC\Recent File List'
        self.files_dict = dict()
        self.path = r'A:\!Series'

    def read(self):
        with OpenKey(HKEY_CURRENT_USER, self.key_string) as key:
            order = list()
            for i in range(0, 25):
                try:
                    name, value, index = EnumValue(key, i)
                except WindowsError:
                    break

                ind = value.find(self.path)
                if ind == -1: continue
                series_name = ''

                for i in range(ind + len(self.path) + 1, 100):
                    if value[i] == '\\':  break
                    series_name = series_name + value[i]

                print(series_name)
                if series_name in self.files_dict.keys(): continue
                self.files_dict[series_name] = value

        print(order)
        print(pd.Series(self.files_dict))
        print(self.files_dict)

    def store_as_json(self):

        with open('file_data.json', 'w') as fp:
            json.dump(self.files_dict, fp)


obj = Read()
obj.read()
obj.store_as_json()

from winreg import *
import pandas as pd
import json
# from collections import OrderedDict


class Read:
    # key_string = ''
    path = 'A:\\!Series'

    def __init__(self):
        self.key_string = r'Software\MPC-HC\MPC-HC\Recent File List'
        self.files_dict = dict()

    def read(self):
        with OpenKey(HKEY_CURRENT_USER, self.key_string) as key:
            try:
                for i in range(0, 25):
                    name, value, index = EnumValue(key, i)
                    self.files_dict[name] = [value, i + 1]

            except WindowsError:
                pass
        print(pd.Series(self.files_dict))
        # print(self.files)

    def store_as_json(self):
        # ...

        with open('file_data.json', 'w') as fp:
            json.dump(self.files_dict, fp)




obj = Read()
obj.read()

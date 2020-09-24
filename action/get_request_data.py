# encoding = 'utf-8'
# author = 'jessica'
import os
import json
from util.parse_excel import *
from config.config import *


class GetRequestData(object):
    def __init__(self):
        pass

    @classmethod
    def get_request_data(cls, rely_rule):
        pe = ParseExcel()
        pe.load_workbook(test_data_path)
        request_data = {}
        inter_dict = {
            "Login": "Login",
            "NewAccount": "NewAccount",
            "GetAccount": "GetAccount",
            "EditAccount": "EditAccount",
            "QueryAccount": "QueryAccount",
            "DeleteAccount": "DeleteAccount"
        }
        data_type_col_dict = {
            "request": idx_request_data,
            "response": idx_response_data
        }
        for key, value in rely_rule.items():
            print('key,value==>', key, ':', value)
            rlist = value.split('->')
            print('len(rlist): ', len(rlist))
            if len(rlist) == 4:
                api_type, case_no, data_type, data_key = rlist
                inter_sheet_obj = pe.get_sheet_by_name(inter_dict[api_type])
                rely_content = json.loads(pe.get_value_in_cell(inter_sheet_obj, row_no=int(case_no)+1, col_no=data_type_col_dict[data_type]))
                command = "%s%s['%s']" % (rely_content, data_key, key)
                request_data[key] = eval(command)
            elif len(rlist) == 3:
                api_type, case_no, data_type = rlist
                print("api_type, case_no, data_type: ", api_type, ', ', case_no, ', ', data_type)
                inter_sheet_obj = pe.get_sheet_by_name(inter_dict[api_type])
                content_str = "%s" % pe.get_value_in_cell(inter_sheet_obj, row_no=int(case_no)+1, col_no=data_type_col_dict[data_type]+1)
                print('content_str: ', content_str)
                rely_content = json.loads(content_str)
                command = "%s['%s']" % (rely_content, key)
                print('command: ', command)
                request_data[key] = eval(command)
                print('request_data[key]: ', request_data[key])
            else:
                request_data[key] = value
                print('request_data[key]: ', request_data[key])
        print('request_data: ', request_data)
        return request_data


# if __name__ == '__main__':
#     rely_rule = {
#
#     }
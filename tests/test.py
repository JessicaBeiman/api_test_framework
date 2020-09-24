# encoding = 'utf-8'
# author = 'jessica'
import requests
import json
from util.parse_excel import *
from util.http_client import *
from config.config import *
from action.write_test_result import *


def test_api():
    pe = ParseExcel()
    pe.load_workbook(test_data_path)

    # 先读API sheet
    api_sheet_obj = pe.get_sheet_by_name('API')
    if_execute_list = pe.get_single_column(sheet=api_sheet_obj, col_no=idx_api_if_execute+1)  # 找到IfExecute列判断是否执行
    for idx, cell in enumerate(if_execute_list[1:], 2):  # 第一行标题去掉，idx从2开始，即第2行开始
        if cell.value.upper() == 'Y':
            row_obj = pe.get_single_row(sheet=api_sheet_obj, row_no=idx)
            api_name = row_obj[idx_api_name].value
            request_url = row_obj[idx_request_url].value
            request_method = row_obj[idx_request_method].value
            params_type = row_obj[idx_params_type].value
            api_case_sheet_name = row_obj[idx_api_case_sheet_name].value
            # print(api_name, request_url, request_method, params_type, api_case_sheet_name)
            print('api_case_sheet_name: ', api_case_sheet_name)

            # 下一步读具体的接口用例sheet
            case_sheet_obj = pe.get_sheet_by_name(api_case_sheet_name)
            case_if_execute_list = pe.get_single_column(case_sheet_obj, idx_case_if_execute+1)
            # print(case_if_execute_list)
            for case_idx, case_cell in enumerate(case_if_execute_list[1:], 2):
                if case_cell.value.upper() == 'Y':
                    case_row_obj = pe.get_single_row(case_sheet_obj, case_idx)
                    rely_rule = case_row_obj[idx_rely_rule].value
                    print('rely_rule: ', rely_rule)
                    # response_code = case_row_obj[idx_response_code].value
                    # data_store = case_row_obj[idx_data_store].value
                    check_point = case_row_obj[idx_check_point].value
                    # result = case_row_obj[idx_result].value
                    # error_info = case_row_obj[idx_error_info].value
                    if rely_rule:
                        request_data = json.dumps(GetRequestData.get_request_data(eval(rely_rule)))
                    else:
                        request_data = case_row_obj[idx_request_data].value
                    hc = HttpClient()
                    response = hc.request(method=request_method,
                                          url=request_url,
                                          params_type=params_type,
                                          request_data=request_data)
                    print('response.status_code: ', response.status_code)
                    if response.status_code == check_point:
                        response_data = response.text
                        print('response_data: ', response_data)
                        write_result(pe, case_sheet_obj, case_idx, request_data=request_data, response_data=response_data)


if __name__ == '__main__':
    test_api()


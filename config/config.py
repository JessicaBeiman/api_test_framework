# encoding = 'utf-8'
# author = 'jessica'
import os

# 项目的绝对路径
project_dir = os.path.dirname(os.path.dirname(__file__))

# 数据文件的绝对路径
test_data_path = project_dir + '\\test_data\\inter_test_data.xlsx'

# API sheet中所需列号
idx_api_name = 1
idx_request_url = 2
idx_request_method = 3
idx_params_type = 4
idx_api_case_sheet_name = 5
idx_api_if_execute = 6

# 接口用例sheet中所需列号
idx_request_data = 1
idx_rely_rule = 2
idx_response_code = 3
idx_response_data = 4
idx_data_store = 5
idx_check_point = 6
idx_case_if_execute = 7
idx_result = 8
idx_error_info = 9

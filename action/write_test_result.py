# encoding = 'utf-8'
# author = 'jessica'
from config.config import *
from util.parse_excel import *
from action.get_request_data import *
import json


def write_result(wb_obj, sheet_obj, row_num, request_data=None, response_data=None, error_key=None):
    try:
        if request_data:
            wb_obj.write_cell(sheet=sheet_obj, content=request_data, row_no=row_num, col_no=idx_request_data+1)
        if response_data:
            wb_obj.write_cell(sheet=sheet_obj, content=response_data, row_no=row_num, col_no=idx_response_data+1)
        if error_key:
            wb_obj.write_cell(sheet=sheet_obj, content='Fail', row_no=row_num, col_no=idx_result+1)
            wb_obj.write_cell(sheet=sheet_obj, content="%s" % error_key, row_no=row_num, col_no=idx_error_info+1)
        else:
            wb_obj.write_cell(sheet=sheet_obj, content='Pass', row_no=row_num, col_no=idx_result+1)
    except Exception as e:
        raise e

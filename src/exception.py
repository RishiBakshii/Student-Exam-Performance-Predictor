import sys
from logger import logging

"""
this will take 2 parameters first is error which we will pass and second parameter will be 
given by the sys library
"""

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # this will return 3 things but we are only interest in the last one 
    #  exc_tb will be having all the information about exception in what file and which line it has occured

    # getting the filename from exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename

    # getting the line number
    line_number=exc_tb.tb_lineno

    error_message=f'Error occured in python script name {file_name} line number {line_number} error message {str(error)}'

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)


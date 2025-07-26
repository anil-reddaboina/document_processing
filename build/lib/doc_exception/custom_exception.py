
import sys
import traceback
from doc_logging.custom_logger import CustomerLogger

logger = CustomerLogger().get_logger()
class DocumentPortalException(Exception):
    def __init__(self, error_msg, error_details:sys):
        _,_,exec_tb=error_details.exc_info()
        self.current_exec_file_name = exec_tb.tb_frame.f_code.co_filename
        self.line_no = exec_tb.tb_lineno
        self.error_message = str(error_msg)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))
    
    def __str__(self):
                return f"{self.error_message} (File: {self.current_exec_file_name}, Line: {self.line_no})\nTraceback: {self.traceback_str}"
        
if __name__== "__main__":
    try:
        a = 1/0
        print(a)
    except Exception as e:
        app_exc=DocumentPortalException(e,sys)
        logger.error(app_exc)
        raise app_exc
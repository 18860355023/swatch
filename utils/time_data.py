from datetime import datetime

# 时间转换类
class TimeConvert():
    def __init__(self):
        pass

    def str2datetime(self, str_time):
        return datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    
    def datetime2str(self, datetime_time):
        return datetime_time.strftime("%Y-%m-%d %H:%M:%S")
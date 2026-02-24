from math import floor
from time import time
from datetime import datetime
from pathlib import Path
from io_csv import TOP_PATH

class CEGASLogger:
    def __init__(self):
        """Initializes the log file (and parent directories if uninitialized)"""
        # start date/time variables
        self.start = datetime.now()
        self.start_time = time()

        # logfile format: <cegas directory>/logs/YYYY/Month/dd-hh.mm.ss.log
        logfile_path = f"{TOP_PATH}/logs/{self.start.strftime("%Y/%B")}"
        Path(logfile_path).mkdir(parents=True, exist_ok=True)
        
        logfile = f"{logfile_path}/{self.start.strftime("%d-%H.%M.%S.log")}"

        # file name: <cegas directory>/logs/YYYY/Month/dd-hh.mm.ss.log    
        self.__logfile = open(logfile, "w")
        self.tee(f"Now logging to {logfile}.")

    def __s2hms_format(self, num, suffix=":"):
        """Returns an empty string if a number is 0, 
        else return the number as string with a suffix"""

        if num == 0:
            return 
        else:
            return str(num) + suffix
        
    def hm(self):
        """Uses datetime to return a timestamp formatted as hh:mm"""
        return datetime.now().strftime("%H:%S")
        
    def s2hms(self, seconds: float, delim=None):
        """Converts `seconds` into a `str` with hours, minutes, and seconds"""
        hours = floor(seconds/3600)
        seconds = seconds % 3600

        minutes = floor(seconds/60)
        seconds = round(seconds % 60, 2)

        if delim:
            hours = self.__s2hms_format(hours, delim)
            minutes = self.__s2hms_format(minutes, delim)
            seconds = self.__s2hms_format(seconds, delim)
        else:
            hours = self.__s2hms_format(hours, "h ")
            minutes = self.__s2hms_format(minutes, "m ")
            seconds = self.__s2hms_format(seconds, "s")

        return hours + minutes + seconds

    def tee(self, text: str, *args, **kwargs):
        """Similar to the Linux `tee` command. Prints to stdout as well as
        the class's log file. Params are identical to `print()`"""

        print(text, *args, **kwargs)
        
        # convert `text` to `print()` equivalent before logging
        for arg in args:
            if "sep" in kwargs:
                text = kwargs["sep"].join(arg)
        if "end" in kwargs:
            text += kwargs["end"]
        
        self.log(f"<{self.hm()}>[STDOUT] {text}")

    def log(self, text):
        """Log any text to the logfile."""
        self.__logfile.write(f"<{self.hm()}> {text}\n")

    def close(self):
        """Records total logging runtime, and safely closes the logfile"""
        total_runtime = self.s2hms(self.start_time - time())
        self.tee(f"Logged for {total_runtime}.")

        self.__logfile.close()
        print("Log file closed successfully.")

logger = CEGASLogger()
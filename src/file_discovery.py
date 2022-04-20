#!/bin/python
from configparser import ConfigParser
from python_tracer.Logger import VerboseLevel,Logger

from os import listdir
from os.path import isdir

config = ConfigParser()
config.read("hitomu.ini")
log_level       = int(config.get("log", "prod_env"))
log_path        = config.get("log", "path")
log_extension   = config.get("log", "extension")

log = Logger(log_path,log_level,service_name="hitomu", log_extension=log_extension)

_EXTENSION = ["avi", "divx", "mkv","mp4"]

def get_all_files(input_dir,is_recursive):
    revelant_files = []
    potential_folder = listdir(input_dir)
    length = len(potential_folder)
    for f_id in range(length):
        log.avancement((100 * (f_id+1) / length), after= str(f_id+1)+'/'+str(length) )
        files = potential_folder[f_id]
        path = input_dir + files if input_dir[-1] == '/' else input_dir + '/'+ files
        if isdir(path):
            if is_recursive:
                potential_folder.extend(listdir(path))
        else:
            if is_intersting_file(path):
                revelant_files.append(path)
    print()
    return revelant_files

def is_intersting_file(path):
    extension = str(path).split(".")[-1]
    return extension in _EXTENSION

#    log.debug(extension)
#    pass
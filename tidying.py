#!/bin/python
from configparser import ConfigParser
from python_tracer.Logger import VerboseLevel,Logger

from sys import platform
from argparse import ArgumentParser

from src.file_discovery import get_all_files

config = ConfigParser()
config.read("hitomu.ini")
log_level       = int(config.get("log", "prod_env"))
log_path        = config.get("log", "path")
log_extension   = config.get("log", "extension")

log = Logger(log_path,log_level,service_name="hitomu", log_extension=log_extension)

print()
log.info("This program is use for tidying up all video file fount in the user personnal system files")



if __name__ == '__main__':
    #Parsing all important arguments
    parser = ArgumentParser(description="Description heres")
    parser.add_argument('-i', '--input', required=True,type=str, help="the path for the 'To tidying' folder")
    parser.add_argument('-o', '--output', required=True,type=str, help="the path for the folder where you want to store the tidying thing")
    parser.add_argument('-r', '--recursive',action='store_true', required=False, help="Do you want the programme to recursively inspect folder")
    
    arguments = parser.parse_args()

    if platform == "linux" or platform == "linux2":
        input_dir = arguments.input
        output_dir = arguments.output
        is_recursive = arguments.recursive

        log.info("The input path is : %s" % input_dir)
        log.info("The output path is : %s" % output_dir)
        log.info("Does the program is recursive : %s" % is_recursive)
        
        all_intersting_files = get_all_files(input_dir,is_recursive)
        log.info("There are %s vidéo files" % len(all_intersting_files))
    elif platform == "darwin":
        log.fatal("MacOS is not supported yet")
    elif platform == "win32":
        log.fatal("Windows is not supported yet")

print()
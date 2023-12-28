import argparse
from datetime import datetime
import glob
import logging
import markdown
import os
from time import time

from exit_codes import ExitCodes

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', dest='debug_flag')
args = parser.parse_args()

if not args.debug_flag:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.DEBUG)

def get_last_run_time() -> str:
    try:
        with open('.tiny', 'r+') as tiny_file:
            return tiny_file.read()
    except FileNotFoundError:
        logging.info('No tiniest website history found. Creating a new one...')
        with open('.tiny', 'w+') as tiny_file:
            return f'Last run time: -1'

def update_last_run_time() -> None:
     with open('.tiny', 'w+') as tiny_file:
            run_time_message = f'Last run time: {time()}'
            tiny_file.write(run_time_message)
            logging.debug(f'Created the file .tiny with content {run_time_message}')

def get_files_to_compile(last_run_time: str) -> list:
    logging.debug(f'Current last_run_time value >>> {last_run_time}')
    files_to_compile = []
    for item in glob.glob('**/*.md', recursive=True):
        file_stats = os.stat(item)
        if last_run_time < file_stats.st_mtime:
            logging.debug(f'File: {item}, Last Run: {last_run_time}, Last Modified: {file_stats.st_mtime}')
            files_to_compile.append(item)
    return files_to_compile

def parse_tiny_header(file: str) -> str:
    return '<head><title>Static Title</title></head>\n\n<body>'

def parse_md_to_html(file: str) -> str:
    md_input = open(file, 'r').read()
    html_output = markdown.markdown(md_input)
    return html_output

def parse_footer() -> str:
    return f'Created using <a href="https://github.com/CanburakTumer/tiniest_static_website"> Tiniest Static Website </a> on {datetime.fromtimestamp(time())}\n</body>'

def create_html_file(files: list) -> None:
    for item in files:
        logging.info(f'Creating HTML from {item}')
        header = parse_tiny_header(item)
        body = parse_md_to_html(item)
        logging.debug(body)
        footer = parse_footer()

        with open(item[:-2]+'.html', 'w') as output_file:
            output_file.write(header + '\n\n' + body + '\n\n' + footer)

if __name__ == '__main__':
    logging.debug(f'current working directory >>> {os.getcwd()}')
    last_run_time = float(get_last_run_time()[15:])
    files_to_compile = get_files_to_compile(last_run_time)
    
    if not files_to_compile:
        logging.info('There is no changes since last tiny run.')
        exit(ExitCodes.NO_CHANGE)
    else:
        create_html_file(files_to_compile)

    update_last_run_time()

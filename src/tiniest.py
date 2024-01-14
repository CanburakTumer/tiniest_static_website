import argparse
from datetime import datetime
import glob
import logging
import markdown
from markdown.extensions.tables import TableExtension
import os
from time import time

from exit_codes import ExitCodes
from tiniest_header import parse_tiny_header

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', dest='debug_flag')
parser.add_argument('--dry-run', action='store_true', dest='dry_run_flag')
parser.add_argument('-a', '--all', action='store_true', dest='all_flag')
args = parser.parse_args()

def get_last_run_time() -> str:
    try:
        with open('.tiny', 'r+') as tiny_file:
            return tiny_file.read()
    except FileNotFoundError:
        logging.info('No tiniest website history found. Creating a new one...')
        if not args.dry_run_flag:
            with open('.tiny', 'w+') as tiny_file:
                return f'Last run time: -1'
        else:
            logging.info('Last run time: -1')

def update_last_run_time() -> None:
    run_time_message = f'Last run time: {time()}'
    if not args.dry_run_flag:
        with open('.tiny', 'w+') as tiny_file:
            tiny_file.write(run_time_message)
            logging.debug(f'Updated the file .tiny with content {run_time_message}')
    else:
        logging.info(f'would update the file .tiny with content {run_time_message}')

def get_files_to_compile(last_run_time: str) -> list:
    logging.debug(f'Current last_run_time value >>> {last_run_time}')
    files_to_compile = []
    for item in glob.glob('**/*.md', recursive=True):
        file_stats = os.stat(item)
        if last_run_time < file_stats.st_mtime:
            logging.debug(f'File: {item}, Last Run: {last_run_time}, Last Modified: {file_stats.st_mtime}')
            files_to_compile.append(item)
    return files_to_compile

def parse_md_to_html(file: str, close_metadata_tag_index: int) -> str:
    md_input = open(file, 'r').read()
    html_output = markdown.markdown(md_input[close_metadata_tag_index:], extensions=[TableExtension(use_align_attribute=True)])
    return html_output

def parse_footer() -> str:
    return f'<hr /><center>\nCreated using <a href="https://github.com/CanburakTumer/tiniest_static_website"> Tiniest Static Website </a> on {datetime.fromtimestamp(time())}\n</center>\n</body>'

def create_html_file(files: list) -> None:
    for item in files:
        if not args.dry_run_flag:
            logging.info(f'Creating HTML from {item}')
        else:
            logging.info(f'would create HTML from {item}')
        header, close_metadata_tag_index = parse_tiny_header(item)
        body = parse_md_to_html(item, close_metadata_tag_index)
        logging.debug(body)
        footer = parse_footer()

        if not args.dry_run_flag:
            with open(item[:-2]+'html', 'w') as output_file:
                output_file.write(header + '\n\n' + body + '\n\n' + footer)
        else:
            logging.info(f'would have written changes into {item[:-2]}html')

if __name__ == '__main__':
    if not args.debug_flag:
        logging.basicConfig(level= logging.INFO)
    else:
        logging.basicConfig(level= logging.DEBUG)
    logging.debug(f'current working directory >>> {os.getcwd()}')

    last_run_time = float(get_last_run_time()[15:]) if not args.all_flag else -1
    files_to_compile = get_files_to_compile(last_run_time)
    
    if not files_to_compile:
        logging.info('There is no changes since last tiny run.')
        exit(ExitCodes.NO_CHANGE)
    else:
        create_html_file(files_to_compile)

    update_last_run_time()

import logging

from exit_codes import ExitCodes

START_TAG = '<<<tiny'
END_TAG = 'tiny>>>'

def find_tiniest_meta_start_tag(md_text: str):
    start_index = md_text.find(START_TAG)
    meta_count = md_text.count(START_TAG)

    if meta_count > 1:
        logging.error(f'There are more than one tiny meta open tags.')
        exit(ExitCodes.MORE_THAN_ONE_META)

    return start_index, meta_count

def find_tiniest_meta_close_tag(md_text: str):
    end_index = md_text.find(END_TAG)
    meta_count = md_text.count(END_TAG)

    if meta_count > 1:
        logging.error(f'There are more than one tiny meta close tags.')
        exit(ExitCodes.MORE_THAN_ONE_META)

    return end_index, meta_count

def parse_metadata(meta_text: str) -> str:
    title_start = meta_text.find('title:') + 6
    title_end = meta_text.find('\n', title_start)
    logging.debug(f'Title start index {title_start}')

    if title_start > 5:
        title_text =  f'<title>{meta_text[title_start:title_end].strip()}</title>\n'
    else:
        title_text = '<title> Made with Tiniest Static Website Generator </title>'

    style_start = meta_text.find('style:') + 6
    style_end = meta_text.find('\n', style_start)
    logging.debug(f'Style start index {style_start}')

    if style_start > 5:
        style_text = f'<link rel="stylesheet" href="{meta_text[style_start:style_end].strip()}">\n'
    else:
        style_text = ""

    return title_text + style_text



def parse_tiny_header(file: str) -> str:
    with open(file, 'r') as markdown:
        md_text = markdown.read()
        start_tag_index, start_tag_count = find_tiniest_meta_start_tag(md_text)
        close_tag_index, close_tag_count = find_tiniest_meta_close_tag(md_text)

        if start_tag_count != close_tag_count:
            logging.error('Open and close tags does not match.')
            exit(ExitCodes.META_DID_NOT_MATCH)
        
        if start_tag_index > close_tag_index:
            logging.error('Open and close tags does not match.')
            exit(ExitCodes.META_DID_NOT_MATCH)

        if start_tag_index > -1:
            html_output = '<head>' + parse_metadata(md_text[start_tag_index:close_tag_index]) + '</head>\n\n<body>'
        else:
            html_output = '<head><title> Made with Tiniest Static Website Generator </title></head>\n\n<body>'

    return html_output, close_tag_index + len(END_TAG)
        
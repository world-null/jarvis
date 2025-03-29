import re


def extract_yt_term(command):
    # define a regular expression pattern to capture the song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    # use re.search to to find the match in the command
    match=re.search(pattern,command,re.IGNORECASE)
    # if any match is found return the extract song; otherwise return none
    return match.group(1) if match else None
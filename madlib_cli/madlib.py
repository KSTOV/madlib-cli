import re

def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except:
        raise FileNotFoundError

def parse_template(string):
    regex = "{([^{}]*)}"
    stripped = re.sub(regex, '{}', string)
    parts = tuple(re.findall(regex, string))
    return (stripped, parts)

def merge(text, words):
    return text.format(*words)

import re

def trim(test_string, removal_string):
    return re.sub(r'^(.*?)('+ removal_string + ')(.*)$', r'\1' + r'\2', test_string)

example = "I want to remove everything after quips, this for instance is useless"
print trim(example, 'quips')


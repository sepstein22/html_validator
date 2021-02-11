#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version
    of html validation by checking whether
    opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    balanced = True
    try:
        sorted_tags = _extract_tags(html)
    except Exception as e:
        return False
    for index in range(len(sorted_tags)):
        sym = sorted_tags[index]
        if sym[1] != '/':
            stack.append(sym)
        else:
            if stack == []:
                balanced = False
            else:
                top = stack.pop()
                if sym[2:] != top[1:]:
                    balanced = False
    if balanced and stack == []:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used
    directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    output = []
    leng = len(html) - 1
    for i in range(leng):
        if html[i] == '<':
            string = ''
            x = i

            while html[x] != '>' and x < leng:
                string += html[x]
                x += 1
            string += '>'
            output.append(string)
    return output

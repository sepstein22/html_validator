#!/bin/python3


def validate_html(html):
    '''
    This function performs
    a limited version
    of html validation by checking whether
    opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    try:
        sorted_tags = _extract_tags(html)
    except Exception as e:
        print(e)
        return False

    stack = []
    balanced = True
    for tag in sorted_tags:
        if '/' not in tag:
            stack.append(tag)
        else:
            if stack == []:
                balanced = False
            else:
                top = stack.pop()
                if tag[2:] != top[1:]:
                    balanced = False
    if balanced and (stack == []):
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
    leng = len(html)-1
    if ('<' in html) & ('>' in html):
        for i in range(leng):
            string = ''
            if html[i] == '<':
                string += html[i]
                i += 1

                while html[i] != '>' and i < leng:
                    string += html[i]
                    i += 1
                string += '>'
                output.append(string)
        return output
    elif ('<' in html):
        raise ValueError('found < without an >')
    else:
        return []
# string += html[x]
# x += 1
# string += '>'
# output.append(strin)
# return output

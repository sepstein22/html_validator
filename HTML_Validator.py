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
    sorted_tags = _extract_tags(html)
    for index, tag in enumerate(sorted_tags):
        if "/" not in tag:
            stack.append(tag)
        else:
            if stack == []:
                balanced = False
            else:
                top = stack.pop()
                if top[1:] != tag[2:]:
                    return False
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

    for i in range(len(html)):
        if html[i] == '<':
            string = ''
            x = i

            while html[x] != '>':
                string += html[x]
            string += '>'
            output.append(string)
    return output

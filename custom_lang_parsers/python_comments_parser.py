def get_sequences_from_list(multi_line_comments):
    '''

    :param multi_line_comments: Multi line comments from Python file
    :return: Length of sequences present in the multi-line comment list
    '''
    result = [[]]
    for i1, i2 in zip(multi_line_comments, multi_line_comments[1:]):
        if i2 - i1 == 1:
            # Extend list or append based on the presence/absence of last item in the list of list
            if not result[-1]:
                result[-1].extend((i1, i2))
            else:
                result[-1].append(i2)
        elif result[-1]:
            # to add the new sequence
            result.append([])

    # Remove last item in the list if we dont see sequences
    if not result[-1]:
        del result[-1]

    return len(result)


def report_python_comments_stats(all_lines):

    single_line_comments = 0
    multi_line_comments = 0
    all_comments = 0
    inline_comments = []
    all_comments_list = []
    multi_line_comments_lines = []
    todos = 0

    for line_no, line in enumerate(all_lines):
        if '#' in line:
            all_comments += 1
            all_comments_list.append(line)
            possible_inline_comments = line.strip().split('#')
            # all comments with some text before '#' considered as inline comment
            if len(possible_inline_comments[0]) > 0:
                inline_comments.append(line_no)
        # check if the previous or next line has '#' and also make sure the prev or current line is not an inline comment
        if '#' in line and ('#' in all_lines[line_no - 1] or '#' in all_lines[line_no + 1]) and \
                                line_no - 1 not in inline_comments and line_no not in inline_comments:
            multi_line_comments_lines.append(line_no)
            multi_line_comments += 1
        # check if previous and next line is not a comment
        if '#' in line and ('#' not in all_lines[line_no - 1] and '#' not in all_lines[line_no + 1]):
            single_line_comments += 1
        if 'TODO' in line:
            todos += 1
            # obtain length of sequences from muli-line comment lines to get the total # of block line comments
    block_line_comments = get_sequences_from_list(multi_line_comments_lines)
    print "Total number of comment lines:", all_comments
    print "Total number of single line comments:", single_line_comments + len(inline_comments)
    print "Total number of comment lines within block comments:", multi_line_comments
    print "Total number of block line comments:", block_line_comments
    print "Total number of TODOs:", todos
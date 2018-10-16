import re
def get_sequences_from_list(multi_line_comment_lines):
    '''

    :param multi_line_comments: Multi line comments from Python file
    :return: Length of sequences present in the multi-line comment list
    '''
    result = [[]]
    for i1, i2 in zip(multi_line_comment_lines, multi_line_comment_lines[1:]):
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

    multi_line_comments = 0
    for sublist in result:
        partial_sum = sublist[-1] - sublist[0] + 1
        multi_line_comments += partial_sum
    # print result
    return len(result), multi_line_comments


def report_python_comments_stats(all_lines):

    single_line_comments = 0
    multi_line_comments = 0
    all_comments = 0
    inline_comments = []
    all_comments_list = []
    multi_line_comments_lines = []
    todos = 0

    for line_no, line in enumerate(all_lines):
        line = line.strip()
        single_line_with_quotes = line.split('#')
        #single and double quotes
        quotes = ["\'", '\"']
        if line.startswith('#'):
            all_comments +=1
        elif '#' in line:
            # get all strings with quotes
            list_with_double_quotes_in_line = re.findall('"([^"]*)"', line)
            list_with_single_quotes_in_line = re.findall("'([^']*)'", line)

            list_with_quotes_in_line = list_with_double_quotes_in_line + list_with_single_quotes_in_line

            # no quotes in line
            # print list_with_quotes_in_line
            if len(list_with_quotes_in_line) == 0:
                print line
                all_comments += 1
            else:
                for str in list_with_quotes_in_line:
                    # ignore if // present within a quote
                    # print str
                    if '#' not in str and len(list_with_quotes_in_line) == 1:
                        print line
                        all_comments += 1
                    if '#' not in str:
                        # print line
                        pass
                    else:
                        count_of_slash_within_quotes = str.count('#')
                        count_of_comment_syntax = line.count('#')
                        # case where both comment and // within quotes exists
                        if count_of_comment_syntax - count_of_slash_within_quotes > 0:
                            print line
                            all_comments += 1
        # if '#' in line and single_line_with_quotes[0] not in quotes:
        #     if len(single_line_with_quotes[0]) > 1 and any(quote in quotes for quote in single_line_with_quotes[0]):
        #         pass
        #     else:
        #         # print line
        #         all_comments += 1
        #         all_comments_list.append(line)
        #         possible_inline_comments = line.strip().split('#')
        #         # all comments with some text before '#' considered as inline comment
        #         if len(possible_inline_comments[0]) > 0:
        #             inline_comments.append(line_no)
        # check if the previous or next line has '#' and also make sure the prev or current line is not an inline comment
        if '#' in line and single_line_with_quotes[0] not in quotes and ('#' in all_lines[line_no - 1] or '#' in all_lines[line_no + 1]) and \
                                line_no - 1 not in inline_comments and line_no not in inline_comments and (all_lines[line_no - 1].split('#')[0] not in quotes or all_lines[line_no + 1].split('#')[0] not in quotes):
            if len(single_line_with_quotes[0]) > 1 and any(quote in quotes for quote in single_line_with_quotes[0]):
                pass
            else:
                # print line
                multi_line_comments_lines.append(line_no)
                    # print line
            # multi_line_comments += 1
        # check if previous and next line is not a comment
        # if '#' in line and single_line_with_quotes[0] not in quotes and (all_lines[line_no - 1].split('#')[0] not in quotes and all_lines[line_no + 1].split('#')[0] not in quotes):
        #     single_line_comments += 1
        #     print line
        if 'TODO' in line:
            todos += 1
            # obtain length of sequences from muli-line comment lines to get the total # of block line comments
    block_line_comments, multi_line_comments = get_sequences_from_list(multi_line_comments_lines)
    print "Total number of comment lines:", all_comments
    print "Total number of single line comments:", all_comments - multi_line_comments
    print "Total number of comment lines within block comments:", multi_line_comments
    print "Total number of block line comments:", block_line_comments
    print "Total number of TODOs:", todos
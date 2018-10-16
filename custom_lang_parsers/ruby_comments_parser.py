import re

def report_ruby_comments_stats(all_lines):
    single_line_comments = 0
    inline_comments = []
    block_line_start = []
    single_line_comments_line_nos = []
    block_line_end = []
    todos = 0
    multi_line_comts = 0

    for line_no, line in enumerate(all_lines):
        single_line_with_quotes = line.split('#')
        # single and double quotes
        quotes = ["\'", '\"']
        if line.startswith('#'):
            single_line_comments +=1
            single_line_comments_line_nos.append(line_no)
            # print line
        elif '#' in line:
            # get all strings with quotes
            list_with_double_quotes_in_line = re.findall('"([^"]*)"', line)
            list_with_single_quotes_in_line = re.findall("'([^']*)'", line)

            list_with_quotes_in_line = list_with_double_quotes_in_line + list_with_single_quotes_in_line

            # no quotes in line
            # print list_with_quotes_in_line
            if len(list_with_quotes_in_line) == 0:
                # print line
                single_line_comments += 1
                single_line_comments_line_nos.append(line_no)
                # print line
            else:
                for str in list_with_quotes_in_line:
                    # ignore if // present within a quote
                    # print str
                    if '#' not in str and len(list_with_quotes_in_line) == 1:
                        # print line
                        single_line_comments += 1
                        single_line_comments_line_nos.append(line_no)
                    elif '#' not in str and len(list_with_quotes_in_line) > 1:
                        # print list_with_single_quotes_in_line
                        list_with_quotes_in_line = list_with_quotes_in_line[1:]
                        # print list_with_single_quotes_in_line
                        pass
                    else:
                        count_of_slash_within_quotes = str.count('#')
                        count_of_comment_syntax = line.count('#')
                        # case where both comment and // within quotes exists
                        if count_of_comment_syntax - count_of_slash_within_quotes > 0:
                            # print line
                            single_line_comments += 1
                            single_line_comments_line_nos.append(line_no)
                            # print line
        if line.startswith('=begin'):
            block_line_start.append(line_no)
        if line.startswith('=end'):
            block_line_end.append(line_no)
        if 'TODO' in line:
            todos += 1
    # print multi_line_comts, "multi_line_comts"
    # print "start", block_line_start
    # print "end", block_line_end
    start_end = zip(block_line_start, block_line_end)
    result = []
    # Get the number of line nos. in the multi line comment block
    for x, y in start_end:
        result += range(x, y + 1)
    # check if any single line comment appears in the multi line comment block
    single_line_comment_in_multi_line_block = [i for i in single_line_comments_line_nos if i in result]
    for i, j in start_end:
        multi_line_comts += (j - i)
    print "Total number of comment lines:", single_line_comments - len(block_line_end) + multi_line_comts - len(single_line_comment_in_multi_line_block)
    print "Total number of single line comments:", single_line_comments - len(single_line_comment_in_multi_line_block)
    print "Total number of comment lines within block comments:", multi_line_comts - len(block_line_end)
    print "Total number of block line comments:", len(block_line_end)
    print "Total number of TODOs:", todos
import re
def report_java_comments_stats(all_lines):
    single_line_comments = 0
    block_line_start = []
    block_line_end = []
    inline_comments = []
    todos = 0
    multi_line_comts = 0
    no_of_lines = 0
    # Note: xml doc comments are considered as single line comments in C#
    for line_no, line in enumerate(all_lines):
        line = line.strip()
        # add another check to make sure that we dont count // present within a string
        quotes = ["\'", '\"']
        if line.startswith('//'):
            single_line_comments +=1
        elif '//' in line:
            # get all strings with quotes
            list_with_double_quotes_in_line = re.findall('"([^"]*)"', line)
            list_with_single_quotes_in_line = re.findall("'([^']*)'", line)

            list_with_quotes_in_line = list_with_double_quotes_in_line + list_with_single_quotes_in_line

            # no quotes in line
            # print list_with_quotes_in_line
            if len(list_with_quotes_in_line) == 0:
                # print line
                single_line_comments += 1
            else:
                for str in list_with_quotes_in_line:
                    # ignore if // present within a quote
                    # print str
                    if '//' not in str and len(list_with_quotes_in_line) == 1:
                        # print line
                        single_line_comments += 1
                    if '//' not in str:
                        # print line
                        pass
                    else:
                        count_of_slash_within_quotes = str.count('//')
                        count_of_comment_syntax = line.count('//')
                        # case where both comment and // within quotes exists
                        if count_of_comment_syntax - count_of_slash_within_quotes > 0:
                            # print line
                            single_line_comments += 1
        if 'TODO' in line:
            todos += 1
        multi_line_with_quotes_1 = line.split('/*')
        if '/*' in line and multi_line_with_quotes_1[0] not in quotes:
            if len(multi_line_with_quotes_1[0]) > 1 and any(quote in quotes for quote in multi_line_with_quotes_1[0]):
                pass
            else:
                # print line
                block_line_start.append(line_no)
                if len(line) > 3:
                    multi_line_comts += 1
        multi_line_with_quotes_2 = line.split('*/')
        if '*/' in line and multi_line_with_quotes_2[0] not in quotes:
            if len(multi_line_with_quotes_2[0]) > 1 and any(quote in quotes for quote in multi_line_with_quotes_2[0]):
                pass
            # print line
            else:
                block_line_end.append(line_no)
                #to avoid cases where block line comments are empty
                if len(line) > 3 and line_no not in block_line_start:
                    multi_line_comts += 1
    # print multi_line_comts, "multi_line_comts"
    # print "start", block_line_start
    # print "end", block_line_end
    start_end = zip(block_line_start, block_line_end)
        # multi_line_comts -= len(block_line_end)
    for i, j in start_end:
        multi_line_comts += (j - i)
    # print multi_line_comts
    multi_line_comts -= len(block_line_end)
    all_comments = single_line_comments + multi_line_comts
    # print "no", no_of_lines
    # print len(inline_comments)
    print "Total number of comment lines:", all_comments
    print "Total number of single line comments:", single_line_comments
    print "Total number of comment lines within block comments:", multi_line_comts
    print "Total number of block line comments:", len(block_line_end)
    print "Total number of TODOs:", todos
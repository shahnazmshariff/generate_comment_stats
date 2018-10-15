def report_php_comments_stats(all_lines):
    single_line_comments = 0
    block_line_start = []
    block_line_end = []
    todos = 0
    multi_line_comts = 0

    for line_no, line in enumerate(all_lines):
        line = line.strip()
        # if line.startswith('/*') or line.startswith('*') or '//' in line:
        #     all_comments += 1
        quotes = ["\'", '\"']
        single_line_with_quotes_1 = line.split('//')
        single_line_with_quotes_2 = line.split('#')
        if '//' in line and single_line_with_quotes_1[0] not in quotes:
            count_single_quotes = 0
            # in order to distinguish inline comments and strings which have // or #
            # I count the number of quotes in the line before the start of comment (// or #)
            # based on the heuristics that inline comments will have more than one quote symbol before the start of the comment
            for str in single_line_with_quotes_1[0]:
                if str == "\'" or str == '\"':
                    count_single_quotes +=1
            # print count_single_quotes
            if len(single_line_with_quotes_1[0]) > 1 and count_single_quotes >= 1:
                pass
            else:
                single_line_comments += 1
        if '#' in line and single_line_with_quotes_2[0] not in quotes:
            count_single_quotes = 0
            for str in single_line_with_quotes_2[0]:
                if str == "\'" or str == '\"':
                    count_single_quotes += 1
            # print count_single_quotes
            if len(single_line_with_quotes_2[0]) > 1 and count_single_quotes >= 1:
                pass
            else:
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
                # to avoid cases where block line comments are empty
                if len(line) > 3 and line_no not in block_line_start:
                    multi_line_comts += 1
    # print multi_line_comts, "multi_line_comts"
    # print "start", block_line_start
    # print "end", block_line_end
    start_end = zip(block_line_start, block_line_end)
    for i, j in start_end:
        multi_line_comts += (j - i)
    multi_line_comts -= len(block_line_end)
    all_comments = single_line_comments + multi_line_comts
    print "Total number of comment lines:", all_comments
    print "Total number of single line comments:", single_line_comments
    print "Total number of comment lines within block comments:", multi_line_comts
    print "Total number of block line comments:", len(block_line_end)
    print "Total number of TODOs:", todos
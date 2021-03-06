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
        # although a comment can have strings with quotes - so check if the string preceding // contains a quote
        single_line_with_quotes = line.split('//')
        # if '//' in line:
        #     print single_line_with_quotes[-2]
        # print single_line_with_quotes
        quotes = ["\'", '\"']
        # for i in range(len(single_line_with_quotes)):
        #     print single_line_with_quotes[i]
        if '//' in line and single_line_with_quotes[0] not in quotes:
            # print single_line_with_quotes[-1]
            no_of_lines += 1
            count_single_quotes = 0
            # in order to distinguish inline comments and strings which have // or #
            # I count the number of quotes in the line before the start of comment (// or #)
            # based on the heuristics that inline comments will have more than one quote symbol before the start of the comment
            for str in single_line_with_quotes[0]:
                if str == "\'" or str == '\"':
                    count_single_quotes += 1
            print count_single_quotes
            if count_single_quotes > 1:
                # print single_line_with_quotes[0]
                # print line
                pass
            else:
                print line
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
def report_java_comments_stats(all_lines):
    single_line_comments = 0
    block_line_start = []
    block_line_end = []
    todos = 0
    multi_line_comts = 0
    # Note: xml doc comments are considered as single line comments in C#
    for line_no, line in enumerate(all_lines):
        line = line.strip()
        if '//' in line:
            single_line_comments += 1
        if 'TODO' in line:
            todos += 1
        if '/*' in line:
            block_line_start.append(line_no)
            if len(line) > 3:
                multi_line_comts += 1
        if line.endswith('*/'):
            # print line
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
    print "Total number of comment lines:", all_comments
    print "Total number of single line comments:", single_line_comments
    print "Total number of comment lines within block comments:", multi_line_comts
    print "Total number of block line comments:", len(block_line_end)
    print "Total number of TODOs:", todos
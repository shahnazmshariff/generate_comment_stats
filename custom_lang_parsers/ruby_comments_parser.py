def report_ruby_comments_stats(all_lines):
    single_line_comments = 0
    inline_comments = []
    block_line_start = []
    block_line_end = []
    todos = 0
    multi_line_comts = 0

    for line_no, line in enumerate(all_lines):
        single_line_with_quotes = line.split('#')
        # single and double quotes
        quotes = ["\'", '\"']
        if '#' in line and single_line_with_quotes[0] not in quotes:
            count_single_quotes = 0
            for str in single_line_with_quotes[0]:
                if str == "\'" or str == '\"':
                    count_single_quotes += 1
            # print count_single_quotes
            if len(single_line_with_quotes[0]) > 1 and count_single_quotes >= 1:
                pass
            else:
                single_line_comments += 1
                # single_line_comments.append(line)
                possible_inline_comments = line.strip().split('#')
                # all comments with some text before '#' considered as inline comment
                if len(possible_inline_comments[0]) > 0:
                    inline_comments.append(line_no)
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
    for i, j in start_end:
        multi_line_comts += (j - i)
    print "Total number of comment lines:", single_line_comments + multi_line_comts
    print "Total number of single line comments:", single_line_comments
    print "Total number of comment lines within block comments:", multi_line_comts - 1
    print "Total number of block line comments:", len(block_line_end)
    print "Total number of TODOs:", todos
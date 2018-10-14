'''
Currently support Java, Python, C#, Ruby, PHP, C++, C, Javascript
Pass filename as command line parameter
Note: Please ensure that the file exists in the same directory as this script
'''

import sys
def open_file(file):
    '''

    :param file: Input file
    :return: file object
    '''
    extension = file.split('.')
    # To omit files with no extensions or files that start with '.' as per requirement
    if file.startswith('.') or len(extension) == 1:
        print "File is invalid"
        return 0
    else:
        try:
            f = open(file, 'r')
            return f
        except IOError:
            print "Recheck filename/path (Error opening file)"
            return 0

def type_of_language(file):
    '''

    :param file: Input file
    :return: Programming Language used in the file
    '''
    file = file.lower()
    extension = file.split('.')
    ext_name_map = {'java': 'java', 'py':'python', 'cs':'c#', 'js':'javascript', 'c':'c', 'c++':'c++', 'php': 'php', 'rb': 'ruby'}
    if extension[1] in ext_name_map:
        return ext_name_map[extension[1]]
    else:
        print "language not supported"
        return 'unknown'

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

def file_parser(file, language):
    '''

    :param file: Input file
    :param language: Programming language used in input file
    :return: print required values (eg: Total # of comment lines)
    '''
    single_line_comments = 0
    multi_line_comments = 0
    block_line_comments = 0
    all_comments = 0
    inline_comments = []
    all_comments_list = []
    multi_line_comments_lines = []
    block_line_start = []
    block_line_end = []
    todos = 0
    multi_line_comts = 0

    all_lines = file.readlines()
    print "Total number of lines:", len(all_lines)
    if language == 'java' or language == 'c#' or language == 'javascript' or language=='c' or language=='c++':
        # Note: xml doc comments are considered as single line comments in C#
        for line_no, line in enumerate(all_lines):
            line = line.strip()
            # if line.startswith('/*') or line.startswith('*') or '//' in line:
            #     all_comments += 1
            if '//' in line:
                single_line_comments += 1
            if 'TODO' in line:
                todos += 1
            if line.startswith('/*'):
                block_line_start.append(line_no)
                # print len(line)
                if len(line)>3:
                    multi_line_comts+=1
            if line.endswith('*/'):
                block_line_end.append(line_no)
                if len(line)>3:
                    multi_line_comts+=1
        # print multi_line_comts, "multi_line_comts"
        # print "start", block_line_start
        # print "end", block_line_end
        start_end = zip(block_line_start, block_line_end)
        for i,j in start_end:
            multi_line_comts += (j-i)
        all_comments = single_line_comments + multi_line_comts
        print "Total number of comment lines:", all_comments
        print "Total number of single line comments:", single_line_comments
        print "Total number of comment lines within block comments:", multi_line_comts
        print "Total number of block line comments:", len(block_line_end)
        print "Total number of TODOs:", todos
    elif language == 'python':
        for line_no, line in enumerate(all_lines):
            if '#' in line:
                all_comments += 1
                all_comments_list.append(line)
                possible_inline_comments = line.strip().split('#')
                # all comments with some text before '#' considered as inline comment
                if len(possible_inline_comments[0]) > 0:
                    inline_comments.append(line_no)
            #check if the previous or next line has '#' and also make sure the prev or current line is not an inline comment
            if '#' in line and ('#' in all_lines[line_no-1] or '#' in all_lines[line_no+1]) and \
                                    line_no-1 not in inline_comments and line_no not in inline_comments:
                multi_line_comments_lines.append(line_no)
                multi_line_comments += 1
            #check if previous and next line is not a comment
            if '#' in line and ('#' not in all_lines[line_no-1] and '#' not in all_lines[line_no+1]):
                single_line_comments += 1
            if 'TODO' in line:
                todos += 1
        #obtain length of sequences from muli-line comment lines to get the total # of block line comments
        block_line_comments = get_sequences_from_list(multi_line_comments_lines)
        print "Total number of comment lines:", all_comments
        print "Total number of single line comments:", single_line_comments + len(inline_comments)
        print "Total number of comment lines within block comments:", multi_line_comments
        print "Total number of block line comments:", block_line_comments
        print "Total number of TODOs:", todos
    elif language == 'php':
        for line_no, line in enumerate(all_lines):
            line = line.strip()
            # if line.startswith('/*') or line.startswith('*') or '//' in line:
            #     all_comments += 1
            if '//' in line or '#' in line:
                single_line_comments += 1
            if 'TODO' in line:
                todos += 1
            if line.startswith('/*'):
                block_line_start.append(line_no)
                # print len(line)
                if len(line)>3:
                    multi_line_comts+=1
            if line.endswith('*/'):
                block_line_end.append(line_no)
                if len(line)>3:
                    multi_line_comts+=1
        # print multi_line_comts, "multi_line_comts"
        # print "start", block_line_start
        # print "end", block_line_end
        start_end = zip(block_line_start, block_line_end)
        for i,j in start_end:
            multi_line_comts += (j-i)
        all_comments = single_line_comments + multi_line_comts
        print "Total number of comment lines:", all_comments
        print "Total number of single line comments:", single_line_comments
        print "Total number of comment lines within block comments:", multi_line_comts
        print "Total number of block line comments:", len(block_line_end)
        print "Total number of TODOs:", todos
    elif language == 'ruby':
        for line_no, line in enumerate(all_lines):
            if '#' in line:
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
        print multi_line_comts, "multi_line_comts"
        print "start", block_line_start
        print "end", block_line_end
        start_end = zip(block_line_start, block_line_end)
        for i, j in start_end:
            multi_line_comts += (j - i)
        print "Total number of comment lines:", single_line_comments + multi_line_comts
        print "Total number of single line comments:", single_line_comments
        print "Total number of comment lines within block comments:", multi_line_comts-1
        print "Total number of block line comments:", len(block_line_end)
        print "Total number of TODOs:", todos

if __name__ == '__main__':
    # Pass filename as command line arg
    file = sys.argv[1]
    f = open_file(file)
    if f!=0:
        prog_language = type_of_language(file)
        if prog_language != 'unknown':
            file_parser(f, prog_language)
    else:
        print 'Exiting application..'
        sys.exit()

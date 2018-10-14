'''
Currently support Java, Python, C#, Ruby, PHP, C++, C, Javascript
Pass filename as command line parameter
Note: Please ensure that the file exists in the same directory as this script
'''

import sys
from custom_lang_parsers import java_comments_parser
from custom_lang_parsers import python_comments_parser
from custom_lang_parsers import php_comments_parser
from custom_lang_parsers import ruby_comments_parser
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



def file_parser(file, language):
    '''

    :param file: Input file
    :param language: Programming language used in input file
    :return: print required values (eg: Total # of comment lines)
    '''

    all_lines = file.readlines()
    print "Total number of lines:", len(all_lines)
    if language == 'java' or language == 'c#' or language == 'javascript' or language=='c' or language=='c++':
       java_comments_parser.report_java_comments_stats(all_lines)
    elif language == 'python':
       python_comments_parser.report_python_comments_stats(all_lines)
    elif language == 'php':
       php_comments_parser.report_php_comments_stats(all_lines)
    elif language == 'ruby':
        ruby_comments_parser.report_ruby_comments_stats(all_lines)


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

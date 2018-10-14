# generate_comment_stats
Generate the total number of lines, comments and the number of single, multi-line and TODO comments. Currently support 8 programming languages (Python, Java, JavaScript, C#, Ruby, C++, C, PHP)

c#:

single: //
multi-line: /*  .. */
xml-doc comments: ///

java:

single: //
multi-line: /*  .. */

javascript:

single: //
multi-line: /*  .. */

c, c++:

single: //
multi-line: /*  .. */


php:

single: // or #
multi-line: /* ... */

ruby:

single: #
multi-line: =begin, =end

python:

single: #
multi-line: # followed by #

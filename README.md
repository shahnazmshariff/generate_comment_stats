Generate Comment Stats 

Input: Source Code 

Output: The total number of lines, comments and the number of single, multi-line and TODO comments 

Usage:

	cd generate_comment_stats
	python comment_stats.py /path/to/file

Example:

	python comment_stats.py sample1.java

Currently supports 8 programming languages (Python, Java, JavaScript, C#, Ruby, C++, C, PHP)

Syntax for comments in popular programming languages:

C#:

	single line: //
	multi-line: /*  .. */
	xml-doc comments: ///

Java:

	single line: //
	multi-line: /*  .. */

Javascript:

	single line: //
	multi-line: /*  .. */

C, C++:

	single line: //
	multi-line: /*  .. */


PHP:

	single line: // or #
	multi-line: /* ... */

Ruby:

	single line: #
	multi-line: =begin, =end

Python:

	single line: #
	multi-line: # followed by #

Note

	In java, c#, javascript, C, C++

		1. /*comment 1*/ will be considered as a block line comment but the number of lines within the block will be 0 (as the block starts and closes in the same line)

		2. /* comment 1 starting on line 1
      		   *
      		   *
     		   */

	'Total # of comment lines within block comment' will be 4 as the comment starts on the first line

	In Python

		1. print "Hello world!" # printing hello world ---- (1)
     	        #comment explaining the next line          ---- (2)

	In this case, (1) will be considered as an inline comment and (2) as a single line comment. ie. (1) and (2) together will not be considered as a multi-line   block

		2. '#' within docstring comments will be considered as a comment  

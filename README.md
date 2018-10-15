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

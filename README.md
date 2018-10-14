# generate_comment_stats
Generate the total number of lines, comments and the number of single, multi-line and TODO comments. Currently support 8 programming languages (Python, Java, JavaScript, C#, Ruby, C++, C, PHP)

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

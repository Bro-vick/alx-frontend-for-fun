if __name__ == '__main__':
'''This line checks whether the script is being run as the main program (as opposed to being imported as a module). If it is being run as the main program, the code inside the if block will be executed.'''
if len(sys.argv[1:]) != 2:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    sys.exit(1)
'''sys.argv is a list in Python that contains the command-line arguments passed to the script. sys.argv[1:] slices the list to exclude the first element (the name of the script itself), so it contains only the arguments passed to the script. The length of this list is checked to ensure that exactly two arguments are passed (the input and output file names). If not, an error message is printed to the standard error stream (sys.stderr) and the script exits with a non-zero status code.'''
input_file = sys.argv[1]
output_file = sys.argv[2]
'''
These lines assign the first and second arguments passed to the script (the input and output file names, respectively) to the variables input_file and output_file.
'''
if not (os.path.exists(input_file) and os.path.isfile(input_file)):
    print(f'Missing {input_file}', file=sys.stderr)
    sys.exit(1)
'''
os.path.exists() checks whether the specified file or directory exists, and os.path.isfile() checks whether it's a file (as opposed to a directory, for example). If the input file does not exist or is not a file, an error message is printed to the standard error stream and the script exits with a non-zero status code.
'''
with open(input_file, encoding='utf-8') as file_1:
    html_content = []
    md_content = [line[:-1] for line in file_1.readlines()]
    for line in md_content:
        heading = re.split(r'#{1,6} ', line)
        if len(heading) > 1:
            h_level = len(line[:line.find(heading[1])-1])
            html_content.append(f'<h{h_level}>{heading[1]}</h{h_level}>\n')
        else:
            html_content.append(line)
'''
This block of code opens the input file using the open() function and reads its contents using the readlines() method. Each line is stripped of its newline character (\n) using slice notation ([:-1]) and added to a list called md_content.

Then, for each line in md_content, the regular expression r'#{1,6} ' is used to split the line at the first occurrence of one or more hash characters (#) followed by a space character. If the line is a heading (i.e., it contains one or more hash characters), the heading level is determined by counting the number of hash characters, and an HTML heading tag (<h1>, <h2>, etc.) is constructed using string formatting and appended to a list called html_content. Otherwise, the original line is appended to html_content
'''
'''
more detailed explanation of the block above...
This block of code is responsible for processing the markdown content of the input file and converting it to HTML format.

md_content = [line[:-1] for line in file_1.readlines()]: This line reads the content of the input file line by line and stores it in the md_content list. The [:-1] slice is used to remove the newline character at the end of each line.

for line in md_content:: This line starts a loop that iterates over each line of the md_content list.

heading = re.split(r'#{1,6} ', line): This line uses a regular expression to split the current line at the first occurrence of one to six hash symbols followed by a space. This is the markdown syntax for creating headings.

if len(heading) > 1:: This line checks if the line contains a heading by testing if the heading list has more than one element. If there is only one element, it means that the line is not a heading.

h_level = len(line[:line.find(heading[1])-1]): This line calculates the level of the heading by counting the number of hash symbols at the beginning of the line. The heading[1] element contains the heading text, and line[:line.find(heading[1])-1] is used to get the substring of the line before the heading text. The -1 is used to remove the space between the hash symbols and the heading text.

html_content.append(f'<h{h_level}>{heading[1]}</h{h_level}>\n'): This line generates the HTML equivalent of the heading and appends it to the html_content list. The f-string is used to insert the h_level variable into the HTML tags.

else: html_content.append(line): If the current line is not a heading, it is added to the html_content list as is.
'''
with open(output_file, 'w', encoding='utf-8') as file_2:
    file_2.writelines(html_content)
'''
Finally, the html_content list is written to the output file using the writelines() method. The file is opened in write mode ('w') and encoded in UTF-8 to handle non-ASCII characters.
'''

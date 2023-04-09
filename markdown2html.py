import sys
import os
import markdown

# Check if the number of arguments is correct
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Convert Markdown to HTML
with open(input_file, 'r') as f:
    md_content = f.read()
    html_content = markdown.markdown(md_content)

# Write HTML output to file
with open(output_file, 'w') as f:
    f.write(html_content)

sys.exit(0)


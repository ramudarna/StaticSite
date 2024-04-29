import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception('No h1 header found in the markdown')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    #Read markdown content
    with open(from_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    
    #Read template content
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read

    #Convert markdown to html
    html_content = markdown_to_html_node(markdown_content).to_html()

    #Extract title from markdown
    title = extract_title(markdown_content)

    #Replace placeholders in template with HTML and title
    html_output = template_content.replace("{{Title}}", title).replace("{{Content}}", html_content)

    #Write html to destination file 
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(html_output)
#Path to markdown file, template file, and destination file
from_path = "content/index.md"
template_path = "template.html"
dest_path="public/index.html"

#Generate the path
generate_page(from_path, template_path, dest_path)
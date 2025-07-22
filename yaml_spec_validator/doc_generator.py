# ---------------------------
# File: doc_generator.py
from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def generate_html(spec, output_path="docs/spec_doc.html"):
    if not os.path.exists("docs"):
        os.makedirs("docs")
    
    template = env.get_template("spec_template.html")
    rendered = template.render(spec=spec)

    with open(output_path, "w") as f:
        f.write(rendered)
    print(f" HTML documentation generated at {output_path}")
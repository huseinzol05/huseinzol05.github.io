from glob import glob
from nbconvert import HTMLExporter
from tqdm import tqdm
import nbformat
import os

template = """
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="description" content="{{description}}" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@huseinzol05" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="keywords" content="Husein Zolkepli" />

    <style>
      body {
        line-height: 1.4;
        font-size: 16px;
        padding: 0 10px;
        margin: 50px auto;
        max-width: 1500px;
      }

      #maincontent {
        max-width: 1200px;
        margin: 15 auto;
      }

      pre {
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
      }
    </style>

    <title>{{title}}</title>
  </head>

  <body>
    <div id="maincontent" style="margin-top: 70px">
    {{body}}
    </div>
  </body>
</html>
"""

index = """
<h2>Husein Zolkepli</h2>

<p>
I'm a software engineer with experience in distributed Large Model training, efficient LLM serving, big data systems and processing, and infrastructure engineering.
I open source Malaysian multimodality models at <a href="https://github.com/mesolitica">https://github.com/mesolitica</a>
and <a href="https://huggingface.co/mesolitica">https://huggingface.co/mesolitica</a>
</p>
"""

def replace(description, title, body):
    t = template.replace('{{description}}', description)
    t = t.replace('{{title}}', title)
    return t.replace('{{body}}', body)

with open('index.html', 'w') as fopen:
    
    index = replace(description = 'A few things from Husein Zolkepli', title = 'Husein Zolkepli', body = index)
    fopen.write(index)

files = glob('*/*.ipynb')
for f in tqdm(files):
  title = os.path.split(f)[1].split('.')[0]
  notebook = nbformat.read(open(f), as_version=4)
  html_exporter = HTMLExporter(template_file = 'base')
  (html, resources) = html_exporter.from_notebook_node(notebook)
  html = html.replace('<img alt', '<img width="100%" alt')
  with open(f.replace('.ipynb', '.html'), "w", encoding="utf-8") as f:
    f.write(replace(title, title, html))
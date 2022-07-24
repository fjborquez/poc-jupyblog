from pathlib import Path

import jupytext
import nbclient

print(Path('post.md').read_text())
print(Path('jupyblog.yaml').read_text())

markdown = jupytext.read('post.md')
rendered = nbclient.execute(markdown, None, None, allow_errors=True)
jupytext.write(rendered, 'post.ipynb')

print(Path('post.ipynb').read_text())

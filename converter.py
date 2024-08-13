import requests
from markdownify import markdownify as md
from collections.abc import MutableMapping
# URL da página que você quer converter
url = "https://medium.com/@habbema/python-apis-862ff2fd324e"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
html_content = response.text

# Convertendo o HTML para Markdown
markdown_content = md(html_content)

# Salvando o conteúdo em um arquivo Markdown
with open("output.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Conversão concluída! O conteúdo foi salvo em 'output.md'.")

#!/usr/bin/env python3
"""*** Hello World para várias línguas ***

O programa vai exibir `Hello, world!` na língua em que o sistema opracional estiver configurado.

Como usar:
 
É necessário que a variável `LANG` esteja configurada, por exemplo:
    LANG=es_SP

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__autor__ = "Symon"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

if current_language == "pt_BR":
  msg = "Olá, mundo!"
elif current_language == "es_SP":
  msg = "Hola, mundo!"
elif current_language == "it_IT":
  msg = "Ciao, mundo!"
elif current_language == "fr_FR":
  msg = "Bonjour, monde!"

print(msg)

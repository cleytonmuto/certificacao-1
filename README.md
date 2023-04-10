---
# MISSÃO CERTIFICAÇÃO
---
# OBJETIVOS

---

# BIBLIOTECAS UTILIZADAS

Linux: sudo apt install python3.10-tk
Linux: python3.10 -m pip install customtkinter pandas openpyxl bcrypt
Linux: sudo apt-get install python3-pil python3-pil.imagetk

Windows: python -m pip install customtkinter pandas openpyxl bcrypt

---

# TABELAS

SISTEMAS(id[pk], nome)

PERFIS(id[pk], nome, descricao)

MATRIZSOD(id_sistemas[fk], nome_sistemas[fk], id_perfis[fk], nome_perfis[fk])

USUARIOS(cpf[pk], id_sistemas[fk], id_perfis[fk])

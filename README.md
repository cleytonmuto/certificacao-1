---

# MISSÃO CERTIFICAÇÃO

---

# OBJETIVOS

---

# BIBLIOTECAS UTILIZADAS

Fonte:https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

<b>Installing virtualenv
Linux: python3.10 -m pip install --user virtualenv
Windows: python -m pip install --user virtualenv

<b>Creating a virtual environment
Linux: python3.10 -m venv env
Windows: python -m venv env

<b>Activating a virtual environment
Linux: source env/bin/activate
Windows: env\Scripts\activate

<b>Check the Python interpreter location
Linux: which python
Windows: where python

<b>Leaving the virtual environment
Linux: deactivate
Windows: deactivate

Linux: sudo apt install python3.10-tk
Linux: python3.10 -m pip install pysimplegui pandas openpyxl bcrypt
Windows: python -m pip install pysimplegui pandas openpyxl bcrypt

---

# TABELAS

SISTEMAS(id[pk], nome)
PERFIS(id[pk], nome, descricao)
MATRIZSOD(id_sistemas[fk], nome_sistemas[fk], id_perfis[fk], nome_perfis[fk])
USUARIOS(cpf[pk], id_sistemas[fk], id_perfis[fk])






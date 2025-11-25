import random
import string

def gerar_id_unico():
    """Gera um ID único para as ocorrências."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def validar_data(data):
    """Valida a data no formato dd/mm/aaaa."""
    try:
        dia, mes, ano = map(int, data.split('/'))
        return dia <= 31 and mes <= 12 and ano > 0
    except ValueError:
        return False
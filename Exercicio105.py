# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*notas, situacao=False):
    """
    Função para calcular estatísticas das notas dos alunos.

    Parâmetros:
    *notas (float): Lista de notas dos alunos.
    situacao (bool, opcional): Se True, inclui a situação do aluno (aprovado/reprovado) no resultado. Padrão é False.

    Retorna:
    dict: Dicionário contendo as seguintes informações:
        - 'quantidade': Quantidade de notas recebidas.
        - 'maior': A maior nota.
        - 'menor': A menor nota.
        - 'media': A média das notas.
        - 'situacao' (opcional): Situação da turma (apenas se situacao=True).

    Exemplo de uso:
    >>> notas(7.5, 8.0, 6.5, 9.0, 5.0)
    {'quantidade': 5, 'maior': 9.0, 'menor': 5.0, 'media': 7.0}

    >>> notas(7.5, 8.0, 6.5, 9.0, 5.0, situacao=True)
    {'quantidade': 5, 'maior': 9.0, 'menor': 5.0, 'media': 7.0, 'situacao': 'Aprovado'}
    """
    if not notas:
        return {'quantidade': 0, 'maior': None, 'menor': None, 'media': None}

    quantidade = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / quantidade

    resultado = {'quantidade': quantidade, 'maior': maior, 'menor': menor, 'media': media}

    if situacao:
        if media >= 7:
            resultado['situacao'] = 'Aprovado'
        else:
            resultado['situacao'] = 'Reprovado'

    return resultado


# Exemplos de uso:
print(notas(7.5, 8.0, 6.5, 9.0, 5.0))
print(notas(7.5, 8.0, 6.5, 9.0, 5.0, situacao=True))

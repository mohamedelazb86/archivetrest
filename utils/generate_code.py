import random

def genearte_code(length=8):
    data='0123456789ABCDEFGHIJKLMNOPQSRTXYZ'
    code=''.join(random.choice(data) for _ in range(length))
    return code
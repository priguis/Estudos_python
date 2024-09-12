def converter(comprimento, valor, unidade_origem, unidade_destino):
    unidades_comprimento = {
        'm': 1,      # metros
        'km': 1000,  # quilômetros
    }
    
    unidades_massa = {
        'g': 1,      # gramas
        'kg': 1000,  # quilogramas
    }
    
    if comprimento:
        fator = unidades_comprimento[unidade_destino] / unidades_comprimento[unidade_origem]
    else:
        fator = unidades_massa[unidade_destino] / unidades_massa[unidade_origem]
    
    return valor * fator

if __name__ == "__main__":
    tipo = input("Converter comprimento ou massa? (c/m): ").strip().lower()
    comprimento = tipo == 'c'
    valor = float(input("Valor a ser convertido: "))
    unidade_origem = input("Unidade de origem (m/km para comprimento ou g/kg para massa): ").strip().lower()
    unidade_destino = input("Unidade de destino (m/km para comprimento ou g/kg para massa): ").strip().lower()
    
    resultado = converter(comprimento, valor, unidade_origem, unidade_destino)
    print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")
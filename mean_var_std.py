import numpy as np  # Importa a biblioteca NumPy para facilitar operações matemáticas e manipulação de arrays

# Define a função calculate
def calculate(numbers):
    # Verifica se a lista contém exatamente 9 números, caso contrário, levanta um erro
    if len(numbers) != 9:
        raise ValueError("A lista deve conter nove números")
     
    # Converte a lista de números em um array NumPy e o remodela para uma matriz 3x3
    array = np.array(numbers).reshape(3, 3)

    # Calcula várias estatísticas para a matriz
    calculations = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    }

    # Retorna um dicionário contendo todas as estatísticas calculadas
    return calculations

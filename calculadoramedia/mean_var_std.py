import numpy as np

def calculate(matrix):
    values_dictionary = {
        'mean' : np.array([]),
        'variance' : np.array([]),
        'standard deviation' : np.array([]),
        'max' : np.array([]),
        'min' : np.array([]),
        'sum' : np.array([])
    }
    for i in range(2):
        media = np.mean(matrix, axis=i)
        values_dictionary['mean'] = np.append(values_dictionary['mean'], media)
    media = np.mean(matrix)
    values_dictionary['mean'] = np.append(values_dictionary['mean'], media)
    for i in range(2):
        varianza = np.var(matrix, axis=i)
        values_dictionary['variance'] =  np.append(values_dictionary['variance'], varianza)
    varianza = np.var(matrix)
    values_dictionary['variance'] = np.append(values_dictionary['variance'], varianza)
    for i in range(2):
        desviation = np.std(matrix, axis=i)
        values_dictionary['standard deviation'] = np.append(values_dictionary['standard deviation'], desviation)
    desviation = np.std(matrix)
    values_dictionary['standard deviation'] = np.append(values_dictionary['standard deviation'], desviation)
    for i in range(2):
        max_value = np.max(matrix, axis = i)
        values_dictionary['max'] = np.append(values_dictionary['max'], max_value)
    max_value = np.max(matrix)
    values_dictionary['max'] = np.append(values_dictionary['max'], max_value)
    for i in range(2):
        min_value = np.min(matrix, axis = i)
        values_dictionary['min'] = np .append(values_dictionary['min'], min_value)
    min_value = np.min(matrix)
    values_dictionary['min'] = np.append(values_dictionary['min'], min_value)
    for i in range(2):
        sum_value = np.sum(matrix, axis = i)
        values_dictionary['sum'] = np.append(values_dictionary['sum'], sum_value)
    sum_value = np.sum(matrix)
    values_dictionary['sum'] = np.append(values_dictionary['sum'], sum_value)
    ##Imprimir resultados

    nombres = {
        'mean': 'Medias',
        'variance': 'Varianzas',
        'standard deviation': 'Desviaciones estandar',
        'max': 'Maximos',
        'min': 'Minimos',
        'sum': 'Sumas'
    }

    for key in nombres:
        arr = np.array(values_dictionary[key])
        part1 = arr[:3].tolist()
        part2 = arr[3:6].tolist()
        part3 = arr[6:].item()#
        resultado = [part1, part2, part3]
        print(f"{nombres[key]}: \n", resultado)

def main():
    numbers = np.array([])
    for i in range(9):
        while True:
            try:
                number = float(input(f'Ingrese un numero: '))
                numbers = np.append(numbers, number)
                break
            except ValueError:
                print("El valor inresado debe ser un número. ")
    matrix = np.array(numbers).reshape(3,3)
    print('la matriz obtenida es: \n\n', matrix)
    calculate(matrix)

main() 
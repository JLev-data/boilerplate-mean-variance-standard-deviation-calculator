import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    lst_array = np.reshape(lst,(3,3))

    calculations = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
    }

    for ax in [0,1,None]:
        calculations['mean'].append(lst_array.mean(axis=ax).tolist())
        calculations['variance'].append(lst_array.var(axis=ax).tolist())
        calculations['standard deviation'].append(lst_array.std(axis=ax).tolist())
        calculations['max'].append(lst_array.max(axis=ax).tolist())
        calculations['min'].append(lst_array.min(axis=ax).tolist())
        calculations['sum'].append(lst_array.sum(axis=ax).tolist())

    return calculations

def delete(list_, index=-1):
    if index != -1:
        a = list_[:index]
        b = list_[index+1:]
        sum_ = a+b
        return sum_
    else:
        return list_[:-1]
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
str_diсt_ = {}
def get_count_char(str_) :
     str_ = "".join(str_.lower().split())
     for letter_ in str_:
         if letter_.isalpha() and letter_ not in str_diсt_:
          str_diсt_[letter_] = 1
         else:
             if letter_.isalpha() and letter_ in str_diсt_:
                str_diсt_[letter_] += 1
     return str_diсt_
def new_diсt_(str_diсt_):
    sum_ = sum(str_diсt_.values())
    for i in str_diсt_:
        str_diсt_[i] = round((str_diсt_[i]/sum_) * 100, 3)
    print(sum(str_diсt_.values()))
    return str_diсt_
print(get_count_char(main_str))

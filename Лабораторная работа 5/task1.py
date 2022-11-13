from pprint import pprint

digits_ = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]
pprint(digits_)
# TODO решить с помощью list comprehension и распечатать его

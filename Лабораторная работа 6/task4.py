import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms',
                'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000',
     '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000',
     '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000',
     '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000',
     '49.000000', '11.000000', '6.135900', '330000.000000'],
]


def csv_to_list_dict(filename=str, delimiter: str = ",") -> list[dict]:
    """
    :param filename: Название файла
    :param delimiter: Разделитель
    :return:
    """
    with open(filename, 'r') as f:
        headers = f.readline()[:-1].split(delimiter)
        rows = [line[:-1].split(delimiter) for line in f.readlines()]
        return [dict(zip(headers, line)) for line in rows]


def to_json_file(filename: str, headers: [str], rows: list[list],
                 delimiter: str = ",", new_line: str = "\n"):
    """
    :param filename: название файла для записи json
    :param headers: заголовок
    :param rows: список значений
    :param delimiter: знак между значениями
    :param new_line: переход на новую строку
    :return:
    """
    with open(OUTPUT_FILE, 'w') as outfile:
        outfile.write(delimiter.join(headers) + new_line)
        for elem in rows:
            outfile.write(delimiter.join(elem) + new_line)


to_json_file(OUTPUT_FILE, headers_list, data)

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


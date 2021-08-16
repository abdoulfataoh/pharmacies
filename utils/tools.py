import pandas
import json

def excel_sheet_to_json(path: str, sheetname: str) -> list:
    """convert excel sheet to json objects list
       suported file format are: .xlsx,.xlsm,.xltx,.xltm

    Args:
        path (str): iput excel file path
        sheetname (str): sheet name

    Returns:
        list: json objects list
    """
    data = pandas.read_excel(path, sheetname).fillna('')
    return json.loads(data.to_json(orient='records'))


def split_values(list_json_obj: list, fields_name:list) -> list: 
    """split values ​​contained in fields of a list of json objects
        example:
            d = [{'last_name': 'Abdoul Fataoh'}, {'last_name': ' Djami Farida'} ]
            field = [{'key': 'last_name', 'separator':' '}]
            split_values(d, field)
            --> [{'last_name': ['Abdoul', 'Fataoh']}, {'last_name': ['Djami', 'Farida']}]

    Args:
        list_json_obj (list): list of json objects. objects must have the same keys
        fields_name (list): list of selected fields to split

    Returns:
        list: output list
    """
    for i in range(len(list_json_obj)):
        for p in range(len(fields_name)):
            list_json_obj[i][fields_name[p]['key']] = list_json_obj[i][fields_name[p]['key']].split(fields_name[p]['separator'])
    return list_json_obj

def strip_and_lowercase_values(list_json_obj: list) -> list:
    for json_obj in list_json_obj:
        for k in json_obj.keys():
            if type(json_obj[k]) is str:
                json_obj[k] = json_obj[k].strip().lower()
    return list_json_obj








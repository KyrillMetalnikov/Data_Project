"""Find the average order cost."""


import excel2json
import json

NUMBER_OF_ROWS = 5000  # number of rows in excel file


def get_excel_data(name: str):
    """
    Convert Excel file to JSON files.

    The excel file is converted into separate JSON files based on the spreadsheet names.
    :param name: Type string, the name of the file including .xlsx
    """
    excel2json.convert_from_file(name)


def remove_row_by_total_items(max_items: int, json_file: dict) -> dict:
    """
    Removes row from a dictionary if total_items key has a higher value than inputted max_items
    :param max_items: type int, maximum amount of items allowed
    :param json_file: type dict, the json object being parsed
    :return: A filtered dictionary.
    """
    json_file_copy = json_file.copy()
    max_iterations = len(json_file)
    iterator = 0
    while max_iterations > iterator:
        if json_file_copy[iterator]["total_items"] >= max_items:
            del json_file_copy[iterator]
            max_iterations -= 1
        iterator += 1
    return json_file_copy


def main():
    get_excel_data("2019 Winter Data Science Intern Challenge Data Set.xlsx")  # data sheet is named Sheet1.json
    with open("Sheet1.json") as file:
        spreadsheet = json.load(file)
    once_filtered_spreadsheet = remove_row_by_total_items(10, spreadsheet)


if __name__ == '__main__':
    main()

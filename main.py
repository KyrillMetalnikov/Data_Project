import excel2json
import json


def get_excel_data(name):
    """
    Convert Excel file to JSON files.

    The excel file is converted into separate JSON files based on the spreadsheet names.
    :param name: Type string, the name of the file including .xlsx
    """
    excel2json.convert_from_file(name)


def main():
    get_excel_data("2019 Winter Data Science Intern Challenge Data Set.xlsx")  # data sheet is named Sheet1.json
    with open("Sheet1.json") as file:
        spreadsheet = json.load(file)


if __name__ == '__main__':
    main()

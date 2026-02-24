import csv, os, io

TOP_PATH = os.path.abspath(__file__ + '/../../..')

class DuplicatePrimaryKeyError(Exception): 
    def __init__(self, *args):
        super().__init__(*args)

def __row_str_to_none(row):
    """Prevents csv.QUOTE_STRINGS from quoting empty fields\n
    only used in `io_csv.py`"""
    row = list(row)

    for i in range(len(row)):
        if row[i] == "":
            row[i] = None

    return tuple(row)

def __row_to_string(row: tuple):
    """Converts a row tuple into a valid csv row string"""

    row = __row_str_to_none(row)
    csv_string = io.StringIO() # csvwriter writes here
    csv.writer(csv_string, quoting=csv.QUOTE_STRINGS).writerow(row)
    
    print(csv_string.getvalue())
    return csv_string.getvalue() + '\n'

def create_row(table_name: str, row: tuple):
    """Adds a row to a table's respective .csv file.\n
    Note: If sorting is needed, use cache.py"""
    row = __row_str_to_none(row)

    with open(TOP_PATH + f"/db/csv/{table_name}.csv", "a") as f:
        csv.writer(f, quoting=csv.QUOTE_STRINGS).writerow(row)
                    
def edit_row(table_name: str, row_PK_str: str, new_row: tuple):
    """WARNING: SUB-OPTIMAL\n
    This function, like `create_row()`, rewrites the file line-by-line.\n\n
    Replaces a line in a table's respective .csv file via PK"""

    csv_string = __row_to_string(new_row)
    file = TOP_PATH + f"/db/csv/{table_name}.csv"
    new_lines = []

    with open(file) as f:
        for line in f.readlines():
            if line.split(",")[0] == row_PK_str:
                new_lines.append(csv_string)
            else:
                new_lines.append(line)

    with open(file, "w") as f:
        f.writelines(new_lines)
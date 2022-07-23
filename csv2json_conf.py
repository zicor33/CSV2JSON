import pandas as pd

# Replace the Path for the file as appropriate
csv_file = pd.DataFrame(pd.read_csv("/Users/itoma/GitHub/CSV2JSON/WHO-COVID-19-global-data.csv", sep = ",", header = 0, index_col = False))

csv_file.to_json("/Users/itoma/GitHub/CSV2JSON/WHO-COVID-19-global-data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)


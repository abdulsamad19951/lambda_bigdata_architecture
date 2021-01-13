import pandas as pd
csv_file = pd.DataFrame(pd.read_csv("2019-Oct.csv", sep = ",", header = 0, index_col = False))
csv_file.to_json("./my.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
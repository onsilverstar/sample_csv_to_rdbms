import pandas as pd
my_dataframe = pd.read_csv("./sample_data.csv")
my_dataframe["c"] = my_dataframe["a"].apply(lambda x: x+5)
print(my_dataframe)
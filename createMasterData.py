import pandas as pd

df = pd.read_csv('trees.csv')
df = df.to_dict(orient='records')

master_data = []

for row in df:
    row["type"] = "tree"
    master_data.append(row)

df = pd.read_csv('bus_stops.csv')
df = df.to_dict(orient='records')

for row in df:
    row["type"] = "bus_stop"
    master_data.append(row)

master_data_df = pd.DataFrame(master_data)
master_data_df.to_csv('master_data.csv', index=False)

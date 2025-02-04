import pandas as pd

data = pd.read_csv("a0-first-repo-adrianleeperiod3/data.csv")
x = data[["customer_id", "transaction_id","contract_id"]]

import pandas as pd

rent = pd.read_csv("s3://dash-apps-open/itertoolsv1/majordf.csv")

rent["GarageType"] = rent["GarageType"].fillna("Unknown/NA")
rent["MasVnrType"] = rent["MasVnrType"].fillna("Unknown/NA")
rent["Price >= 200k"] = rent["Price >= 200k"].map({0: "Under 200k", 1: "Over 200k"})


res_df = pd.read_csv("s3://dash-apps-open/itertoolsv1/res_220525.csv")

res_df = res_df.drop(["Unnamed: 0"], axis=1)
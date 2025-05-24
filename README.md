The basis for this dashboard miniapp is a program that iteratres through a number of feature-attribute pairs, to the order of between several thousand and several million, to come up with drilled-down subsegments that have the most purity with the target variable.

This dataset used was the Ames Housing dataset [https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview], with a new feature as the target variable: "Over 200k", boolean. This references the price of the house.

In this context, program looks into several features of a house, such as "House Zoning", "Masonry Veneer Type", "Garage Type", etc. and finds the combinations of these variables that have the highest % of results with houses over 200k. While the variables in question must be researched and input manually to the program (to avoid long compute times), this example uses the features just mentioned as a baseline to come up with the following result:
- purity of overall datasat: 28.4%
- sample size of overall data: 2580
- mask: (( rent["ZngCdPr"] == "FS-RL" ) | ( rent["ZngCdPr"] == "F-VR" )) & (( rent["ClassSc_S"] == "1-STORY 1946 & NEWER ALL STYLES" ) | ( rent["ClassSc_S"] == "2-STORY 1946 & NEWER" )) & ( rent["MasVnrType"] == "BrkFace" ) & ( rent["GarageType"] == "Attchd" )
- purity of subsample: 98.3%
- sample size of subsample: 59 (2.28% of data)

This dashboard visualizes these results.

https://itertools-v1.ue.r.appspot.com/

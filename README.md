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

Some sample visuals to help illustrate the goal:

![newplot (94)](https://github.com/user-attachments/assets/e4160ac8-0fe7-4118-b10c-c3ede8abb633)
![newplot (95)](https://github.com/user-attachments/assets/887758b7-f19c-4a41-912b-4b48728e51ac)
![newplot (97)](https://github.com/user-attachments/assets/974c17f6-9da0-4ad3-836e-ce1bfa265d10)
![newplot (96)](https://github.com/user-attachments/assets/13b6ed27-b7c3-436d-a1ff-509568ef752a)

![newplot (98)](https://github.com/user-attachments/assets/675993d0-884e-4330-bc13-75068d735b7f)



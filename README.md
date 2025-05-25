The basis for this dashboard miniapp is a program that iteratres through a number of feature-attribute pairs, to the order of between several thousand and several million, to come up with drilled-down subsegments that have the most purity with the target variable.

This dataset used was the Ames Housing dataset [https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview], with a new feature as the target variable: "Over 200k", boolean. This references the price of the house.

There are several ways to use the above program to analyze a set of data. In this example, the features were manually analyzed from a theoretical perspective - ie, logically deducing what factors may be present in the segmentation of houses, like "Zoning", "Style", "Garage", etc. By iterating throught the program with various features trying to pinpoint the same general subsegment with 3-5 layers of depth (all under 2 minutes of compute time), it is possible to quickly ideate and uncover where subsegments of purity exist.

The following is a resulting subsegment that achieved 98% purity with the target variable:
- purity of overall datasat: 28.4%
- sample size of overall data: 2580
- mask:
  -   rent["ZngCdPr"] == "FS-RL" ) | rent["ZngCdPr"] == "F-VR"
  -   rent["ClassSc_S"] == "1-STORY 1946 & NEWER ALL STYLES" 
  -   rent["MasVnrType"] == "BrkFace"
  -   rent["GarageType"] == "Attchd"
- purity of subsample: 100.00%
- sample size of subsample: 51 (1.98% of data)

This dashboard visualizes these results. https://itertools-v1.ue.r.appspot.com/

Some sample visuals to help illustrate the goal of this program:

![newplot (98)](https://github.com/user-attachments/assets/675993d0-884e-4330-bc13-75068d735b7f)

![newplot (94)](https://github.com/user-attachments/assets/e4160ac8-0fe7-4118-b10c-c3ede8abb633)
![newplot (95)](https://github.com/user-attachments/assets/887758b7-f19c-4a41-912b-4b48728e51ac)
![newplot (97)](https://github.com/user-attachments/assets/974c17f6-9da0-4ad3-836e-ce1bfa265d10)
![newplot (96)](https://github.com/user-attachments/assets/13b6ed27-b7c3-436d-a1ff-509568ef752a)




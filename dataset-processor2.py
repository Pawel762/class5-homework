import pandas as pd

import matplotlib.pyplot as plt

wine_df = pd.read_csv(filepath_or_buffer='~/class5-homework/wine.data',
                sep=',',
                header=None)
wine_df.columns = ['Class','Alcohol','Malic_Acid','Ash','Alcalinity_of_Ash','Magnesium',
                'Total_Phenols','Flavanoids','Nonflavanoid_Phenols','Proanthocyanins',
                'Color_Intensity','Hue','OD280_OD315_of_Diluted_Wines','Proline']


pd.set_option('display.max_columns', None)

#Display dataset in table format

#print(wine_df.to_string())

#Display stats of dataset without the Class column
wine_B = wine_df.drop(['Class'], axis = 1)
print(wine_B.describe())


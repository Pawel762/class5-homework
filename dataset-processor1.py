

import pandas as pd

wine_df = pd.read_csv(filepath_or_buffer='~/class5-homework/wine.data',
                sep=',',
                header=None)
wine_df.columns = ['Class','Alcohol','Malic_Acid','Ash','Alcalinity_of_Ash','Magnesium',
                'Total_Phenols','Flavanoids','Nonflavanoid_Phenols','Proanthocyanins',
                'Color_Intensity','Hue','OD280_OD315_of_Diluted_Wines','Proline']

#Possibility to limit columns
pd.set_option('display.max_columns',None)

print(wine_df)

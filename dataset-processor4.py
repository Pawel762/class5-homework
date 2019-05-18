import os
import pandas as pd
import matplotlib.pyplot as plt

wine_df = pd.read_csv(filepath_or_buffer='~/class5-homework/wine.data',
                sep=',',
                header=None)
wine_df.columns = ['Class','Alcohol','Malic_Acid','Ash','Alcalinity_of_Ash','Magnesium',
                'Total_Phenols','Flavanoids','Nonflavanoid_Phenols','Proanthocyanins',
                'Color_Intensity','Hue','OD280_OD315_of_Diluted_Wines','Proline']

wine_B = wine_df.drop(['Class'], axis = 1)

os.makedirs('graphs2', exist_ok=True)

# Plotting scatterplot for Total Phenols and Alcohol
plt.scatter(wine_B['Total_Phenols'], wine_B['Alcohol'], color='r')
plt.title('Total Phenols to Alcohol')
plt.xlabel('Total_Phenols')
plt.ylabel('Alcohole')
plt.savefig(f'graphs2/Tot_Phnls_Alchl.png', format='png')

# Plotting scatterplot for Alcohol and Malic Acid
plt.scatter(wine_B['Alcohol'], wine_B['Malic_Acid'], color='r')
plt.title('Alcohol to Malic Acid')
plt.xlabel('Alcohol')
plt.ylabel('Malic_Acid')
plt.savefig(f'graphs2/Alchl_Malic_Acid.png', format='png')

# Plotting scatterplot for Alcohol and Ash
plt.scatter(wine_B['Alcohol'], wine_B['Ash'], color='r')
plt.title('Alcohol to Ash')
plt.xlabel('Alcohol')
plt.ylabel('Ash')
plt.savefig(f'graphs2/Alchl_Ash.png', format='png')

# Plotting scatterplot for Alcohol and Magnesium
plt.scatter(wine_B['Alcohol'], wine_B['Magnesium'], color='r')
plt.title('Alcohol to Magnesium')
plt.xlabel('Alcohol')
plt.ylabel('Magnesium')
plt.savefig(f'graphs2/Alchl_Magn.png', format='png')

# Plotting scatterplot for Alcohol and Flavanoids
plt.scatter(wine_B['Alcohol'], wine_B['Flavanoids'], color='r')
plt.title('Alcohol to Flavanoids')
plt.xlabel('Alcohol')
plt.ylabel('Flavanoids')
plt.savefig(f'graphs2/Alchl_Flavanoids.png', format='png')

# Plotting scatterplot for Alcohol and Proline
plt.scatter(wine_B['Alcohol'], wine_B['Proline'], color='r')
plt.title('Alcohol to Proline')
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.savefig(f'graphs2/Alchl_Proline.png', format='png')


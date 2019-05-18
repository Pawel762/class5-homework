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

os.makedirs('graphs', exist_ok=True)

#Ploting line for alcohol
plt.plot(wine_B['Alcohol'], color='g')
plt.title('Alcohol by Index')
plt.xlabel('Index')
plt.ylabel('Alcohol')
plt.savefig(f'graphs/Alcohol_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Malic_Acid
plt.plot(wine_B['Malic_Acid'], color='g')
plt.title('Malic_Acid by Index')
plt.xlabel('Index')
plt.ylabel('Malic_Acid')
plt.savefig(f'graphs/Malic_Acid_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Ash
plt.plot(wine_B['Ash'], color='g')
plt.title('Ash by Index')
plt.xlabel('Index')
plt.ylabel('Ash')
plt.savefig(f'graphs/Ash_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Alcalinity_of_Ash
plt.plot(wine_B['Alcalinity_of_Ash'], color='g')
plt.title('Alcalinity_of_Ash by Index')
plt.xlabel('Index')
plt.ylabel('Alcalinity_of_Ash')
plt.savefig(f'graphs/Alcalinity_of_Ash_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Magnesium
plt.plot(wine_B['Magnesium'], color='g')
plt.title('Magnesium by Index')
plt.xlabel('Index')
plt.ylabel('Magnesium')
plt.savefig(f'graphs/Magnesium_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Total_Phenols
plt.plot(wine_B['Total_Phenols'], color='g')
plt.title('Total_Phenols by Index')
plt.xlabel('Index')
plt.ylabel('Total_Phenols')
plt.savefig(f'graphs/Total_Phenols_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Flavanoids
plt.plot(wine_B['Flavanoids'], color='g')
plt.title('Flavanoids by Index')
plt.xlabel('Index')
plt.ylabel('Flavanoids')
plt.savefig(f'graphs/Flavanoids_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Nonflavanoid_Phenols
plt.plot(wine_B['Nonflavanoid_Phenols'], color='g')
plt.title('Nonflavanoid_Phenols by Index')
plt.xlabel('Index')
plt.ylabel('Nonflavanoid_Phenols')
plt.savefig(f'graphs/Nonflavanoid_Phenols_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Proanthocyanins
plt.plot(wine_B['Proanthocyanins'], color='g')
plt.title('Proanthocyanins by Index')
plt.xlabel('Index')
plt.ylabel('Proanthocyanins')
plt.savefig(f'graphs/Proanthocyanins_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Color_Intensity
plt.plot(wine_B['Color_Intensity'], color='g')
plt.title('Color_Intensity by Index')
plt.xlabel('Index')
plt.ylabel('Color_Intensity')
plt.savefig(f'graphs/Color_Intensity_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Hue
plt.plot(wine_B['Hue'], color='g')
plt.title('Hue by Index')
plt.xlabel('Index')
plt.ylabel('Hue')
plt.savefig(f'graphs/Hue_by_index_plot.png', format='png')
plt.clf()

#Ploting line for OD280_OD315_of_Diluted_Wines
plt.plot(wine_B['OD280_OD315_of_Diluted_Wines'], color='g')
plt.title('OD280_OD315_of_Diluted_Wines by Index')
plt.xlabel('Index')
plt.ylabel('OD280_OD315_of_Diluted_Wines')
plt.savefig(f'graphs/OD280_OD315_of_Diluted_Wines_by_index_plot.png', format='png')
plt.clf()

#Ploting line for Proline
plt.plot(wine_B['Proline'], color='g')
plt.title('Proline by Index')
plt.xlabel('Index')
plt.ylabel('Proline')
plt.savefig(f'graphs/Proline_by_index_plot.png', format='png')
plt.clf()

#plt.plot(wine_B[i], color='green')
#plt.title(str(i)+' by Index')
#plt.xlabel('Index')
#plt.ylabel(i)
#plt.savefig(f'graphs/'+str(i)+'_by_index_plot.png', format='png')
#plt.clf()


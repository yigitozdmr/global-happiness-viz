import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
file_path = "WHR26_Data_Figure_2.1.xlsx"
df = pd.read_excel(file_path)

# Clean column names: lowercase and strip spaces
df.columns = df.columns.str.strip().str.lower()

# EXACT column names from the dataset
col_ladder = 'life evaluation (3-year average)'
col_gdp = 'explained by: log gdp per capita'
col_year = 'year'

# Clean missing values
df_cleaned = df.dropna(subset=[col_ladder, col_gdp])

# Find the most recent year and filter
latest_year = int(df_cleaned[col_year].max())
df_latest = df_cleaned[df_cleaned[col_year] == latest_year]

# 2. Visualization
plt.figure(figsize=(12, 8), dpi=300)
sns.set_theme(style="whitegrid")

# Scatter Plot
scatter = sns.scatterplot(
    data=df_latest,
    x=col_gdp,
    y=col_ladder,
    size=col_ladder,
    sizes=(50, 400),
    alpha=0.7,
    color='#2ecc71', 
    edgecolor='black'
)

# Title and Axis Labels
plt.title(f'Relationship Between Economic Power and Happiness ({latest_year})', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Log GDP per capita', fontsize=14, labelpad=10)
plt.ylabel('Happiness Score (Life Evaluation)', fontsize=14, labelpad=10)

# Remove top and right borders
sns.despine()

# Adjust the Legend
handles, labels = scatter.get_legend_handles_labels()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Happiness Score")

# 3. Save as a high-resolution static file
output_filename = 'gdp_vs_happiness_scatter.png'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

print(f"Visualization successfully completed and saved as '{output_filename}'.")
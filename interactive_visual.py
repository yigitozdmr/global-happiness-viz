import pandas as pd
import plotly.express as px

# 1. Load Data
file_path = "WHR26_Data_Figure_2.1.xlsx"
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip().str.lower()

# Column names based on the dataset
col_ladder = 'life evaluation (3-year average)'
col_year = 'year'
col_country = 'country name'

# Selecting a diverse and broad group of 15 countries to avoid "chart junk" while showing a rich comparison
countries = [
    'Turkey', 'Finland', 'United States', 'Germany', 
    'India', 'China','Afghanistan', 'Japan']
df_filtered = df[df[col_country].isin(countries)]

# 2. Interactive Visualization (Plotly)
fig = px.line(
    df_filtered,
    x=col_year,
    y=col_ladder,
    color=col_country,
    markers=True,
    title="Happiness Trend of Selected Countries (2011-2025)",
    labels={col_year: "Year", col_ladder: "Happiness Score", col_country: "Country"}
)

# Clean layout design (Design & Ethics rubric requirement)
fig.update_layout(template="plotly_white", title_x=0.5, font=dict(size=14))

# 3. Save as HTML (Part A submission file)
output_filename = 'interactive_happiness_trend.html'
fig.write_html(output_filename)

print(f"Interactive visualization successfully completed and saved as '{output_filename}'.")
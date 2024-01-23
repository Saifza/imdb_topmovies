import pandas as pd
import plotly.express as px

# Load the data
titles_df = pd.read_csv('titles.csv')
years_df = pd.read_csv('years.csv')
ratings_df = pd.read_csv('ratings.csv')

# Clean the data
ratings_df['Rating'] = ratings_df['Rating'].str.extract(r'(\d+\.\d+)').astype(float)

#print(ratings_df, years_df)




# Merge the dataframes
merged_df = pd.concat([years_df, ratings_df, titles_df], axis=1)

# Sort the dataframe by 'Year'
#merged_df = merged_df.sort_values(by='Year')






# Select top 25 movies
top_25_df = merged_df.head(25)

top_20_df=top_25_df.sort_values(by='Year')


#print(top_15_df)

hue_order = top_25_df['Title'].unique()



#print(top_15_df_filtered)
# Plotting


# Create an interactive scatter plot with tooltips using plotly express
fig = px.scatter(
    top_25_df, x='Year', y='Rating', color='Title',
    hover_data=['Title'],
    title='Top 15 IMDb Ratings Over Years',
    labels={'Year': 'Year', 'Rating': 'Rating'},
)

# Show the plot
fig.show()

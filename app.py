import pandas as pd
import os
import plotly.express as px

df = pd.read_csv('./data/mart_forecast_day_202404171547.csv')
df

df_berlin = df[df['city'] == 'Berlin']
df_berlin

fig_berlin = px.bar(df_berlin, x='month_of_year', y='avg_temp_c', 
                       title='Average Monthly Temperature in Berlin',
                       labels={'Temperature': 'Temperature (°C)'})

fig_berlin.show()

df_berlin = df[df['city'] == 'Berlin']

# Filter data for Ottawa
df_ottawa = df[df['city'] == 'Ottawa']

# Filter data for Canberra
df_canberra = df[df['city'] == 'Canberra']

# Concatenate the dataframes for all cities
df_combined = pd.concat([df_berlin, df_ottawa, df_canberra])

# Plotting
fig2 = px.bar(df_combined, x='month_of_year', y='avg_temp_c', color='city',
             title='Average Monthly Temperature Comparison',
             labels={'avg_temp_c': 'Temperature (°C)', 'month_of_year': 'Month'})

fig2.show()

# Filter data for Germany
df_germany = df[df['country'] == 'Germany']

# Filter data for Australia
df_australia = df[df['country'] == 'Australia']

# Filter data for Canada
df_canada = df[df['country'] == 'Canada']

# Concatenate the dataframes for all countries
df_combined = pd.concat([df_germany, df_australia, df_canada])

# Plotting
fig2 = px.bar(df_combined, x='month_of_year', y='avg_temp_c', color='country',
             title='Average Monthly Temperature Comparison',
             labels={'avg_temp_c': 'Temperature (°C)', 'month_of_year': 'Month'})

fig2.show()

import plotly.express as px

df_countries = df[df['country'].isin(['Germany', 'Australia', 'Canada'])]

df_countries

df_countries = df_countries[['month_of_year', 'min_temp_c', 'max_temp_c',
'avg_temp_c', 'city', 'country'
 ]]
df_countries

fig = px.choropleth(df_countries, 
                    locations="country", 
                    locationmode="country names", 
                    color="avg_temp_c",
                    hover_name="country", 
                    animation_frame="month_of_year",
                    title="Average Temperature Variation Over Time",
                    color_continuous_scale=px.colors.sequential.Plasma)

# Customize the map layout
fig.update_geos(showcountries=True, countrycolor="Black")
fig.update_layout(geo=dict(showframe=False, 
                            showcoastlines=False))

# Show the map
fig.show()

table = dash_table.DataTable(df_berlin.to_dict('records'),
                                  [{"name": i, "id": i} for i in df_berlin.columns],
                               style_data={'color': 'white','backgroundColor': "#222222"},
                              style_header={
                                  'backgroundColor': 'rgb(210, 210, 210)',
                                  'color': 'black','fontWeight': 'bold'}, 
                                     style_table={ 
                                         'minHeight': '400px', 'height': '400px', 'maxHeight': '400px',
                                         'minWidth': '900px', 'width': '900px', 'maxWidth': '900px',
                                         'marginLeft': 'auto', 'marginRight': 'auto',
                                         'marginTop': 0, 'marginBottom': "30"}
                                     )

app = dash.Dash(__name__)
server = app.server

# Filter data for Berlin
df_berlin = df[df['city'] == 'Berlin']

# Filter data for Ottawa
df_ottawa = df[df['city'] == 'Ottawa']

# Filter data for Canberra
df_canberra = df[df['city'] == 'Canberra']

# Concatenate the dataframes for all cities
df_combined = pd.concat([df_berlin, df_ottawa, df_canberra])

# Plotting the bar chart
fig1 = px.bar(df_combined, 
              x='month_of_year', 
              y='avg_temp_c', 
              color='city',
              title='Average Monthly Temperature Comparison',
              labels={'avg_temp_c': 'Temperature (°C)', 'month_of_year': 'Month'})

# Plotting the choropleth map
fig2 = px.choropleth(df_countries, 
                     locations="country", 
                     locationmode="country names", 
                     color="avg_temp_c",
                     hover_name="country", 
                     animation_frame="month_of_year",
                     title="Average Temperature Variation Over Time",
                     color_continuous_scale=px.colors.sequential.Plasma)

# Customize the map layout
fig2.update_geos(showcountries=True, countrycolor="Black")
fig2.update_layout(geo=dict(showframe=False, showcoastlines=False))

# Define the layout of the app
app.layout = html.Div([
    html.H1("Temperature Analysis"),
    
    html.Div([
        html.H2("Average Monthly Temperature Comparison"),
        dcc.Graph(figure=fig1)
    ]),
    
    html.Div([
        html.H2("Average Temperature Variation Over Time"),
        dcc.Graph(figure=fig2)
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server()


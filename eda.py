# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # The African COVID-19 Dashboard Project

# %%
import pandas as pd
import numpy as np
import re
import glob
import io
import requests
from datetime import date, timedelta

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import iplot, init_notebook_mode

init_notebook_mode(connected=True)

# %% [markdown]
# # Load Data from the John Hopkins Data Project

# %%
# Load files from the web
file_date = date(2020, 1, 22)
dates = []

while file_date <= date.today():
    dates.append(file_date)
    file_date += timedelta(days=1)

files = []
for file in dates:
    file = file.strftime("%m-%d-%Y")
    print(file)
    url = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'.format(
        file)
    raw_string = requests.get(url).content
    df = pd.read_csv(io.StringIO(raw_string.decode('utf-8')))
    df['date'] = pd.to_datetime(file)
    df.rename(columns={'Country_Region': 'Country/Region'}, inplace=True)
    files.append(df)

df = pd.concat(files, axis=0, ignore_index=True, sort=False)


# %%
global_data = df.to_csv('global_data.csv', index=False)

# %% [markdown]
# # Data Exploration

# %%
df.head()


# %%
df.describe()


# %%
df.date.unique()


# %%
df.info()


# %%
df.sample(5)


# %%
# Drop the non-essential fields
df.drop(['FIPS', 'Admin2', 'Combined_Key',
         '404: Not Found'], axis=1, inplace=True)

# %% [markdown]
# ## List of African countries that are the focus of this dashboard

# %%
africa = ['Algeria',
          'Angola',
          'Benin',
          'Botswana',
          'Burkina Faso',
          'Burundi',
          'Cabo Verde',
          'Cameroon',
          'Central African Republic',
          'Chad',
          'Comoros',
          'Côte d’Ivoire',
          'Congo',
          'Djibouti',
          'Egypt',
          'Equatorial Guinea',
          'Eritrea',
          'Eswatini',
          'Ethiopia',
          'Gabon',
          'Gambia',
          'Ghana',
          'Guinea',
          'Guinea-Bissau',
          'Kenya',
          'Lesotho',
          'Liberia',
          'Libya',
          'Madagascar',
          'Malawi',
          'Mali',
          'Mauritania',
          'Mauritius',
          'Morocco',
          'Mozambique',
          'Namibia',
          'Niger',
          'Nigeria',
          'Rwanda',
          'Sao Tome and Principe',
          'Senegal',
          'Seychelles',
          'Sierra Leone',
          'Somalia',
          'South Africa',
          'South Sudan',
          'Sudan',
          'Tanzania',
          'Togo',
          'Tunisia',
          'Uganda',
          'Zambia',
          'Zimbabwe',
          'Congo (Brazzaville)',
          'Ivory Coast',
          'Congo (Kinshasa)',
          'Republic of the Congo',
          'Gambia, The',
          ]

# %% [markdown]
# ## Subset the african data from the overall data

# %%
df_africa = df[df['Country/Region'].isin(africa)]


# %%
df_africa.sample(4)


# %%
# Continue dropping non-required fields
df_africa.drop(['Province/State', 'Province_State',
                'Last Update', 'Last_Update'], axis=1, inplace=True)


# %%
df_africa.head()


# %%
df_africa.info()


# %%
df_africa.describe()


# %%
# Re-order the columns for readability
df_africa = df_africa[['date',
                       'Country/Region',
                       'Confirmed',
                       'Deaths',
                       'Recovered',
                       'Lat',
                       'Latitude', 'Long_', 'Longitude']]

# Fill missing values as 0; create Active cases column
df_africa['Confirmed'] = df_africa['Confirmed'].fillna(0).astype(int)
df_africa['Deaths'] = df_africa['Deaths'].fillna(0).astype(int)
df_africa['Recovered'] = df_africa['Recovered'].fillna(0).astype(int)
df_africa['Active'] = df_africa['Confirmed'] - \
    df_africa['Deaths'] - df_africa['Recovered']


# %%
df_africa.sample(5)


# %%
# Replace missing values for latitude
df_africa['Lat'] = df_africa.apply(
    lambda row: row['Latitude']if np.isnan(row['Lat']) else row['Lat'],
    axis=1
)


# %%
# Replace missing values for longitude
df_africa['Long_'] = df_africa.apply(
    lambda row: row['Longitude']if np.isnan(row['Long_']) else row['Long_'],
    axis=1
)


# %%
df_africa[df_africa['Long_'].isna()]
# Here we find that mainly Egypt,Algeria and Nigeria have missing latitude and longitude coordinates


# %%
df_africa.drop(['Latitude', 'Longitude'], axis=1, inplace=True)
df_africa.rename(columns={'Lat': 'Latitude',
                          'Long_': 'Longitude'}, inplace=True)


# %%
# Replace missing values for latitude and longitude
#df_africa['Lat'] = df_africa['Lat'].fillna(df.groupby('Country/Region')['Lat'].transform('mean'))
#df_africa['Long_'] = df_africa['Long_'].fillna(df.groupby('Country/Region')['Long_'].transform('mean'))


# %%
# Save the African Processed data to a csv file
african_data = df_africa.to_csv('africa_data.csv', index=False)


# %%
df_africa['Country/Region'].nunique()


# %%
# Deaths
df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Deaths'].sum()


# %%
# active cases
df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Confirmed'].sum() - df_africa[df_africa['date'] ==
                                                                                          df_africa['date'].iloc[-1]]['Deaths'].sum() - df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Recovered'].sum()


# %%
# confirmed
df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Confirmed'].sum()


# %%
# recovered
df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Recovered'].sum()


# %%
# deaths
df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Deaths'].sum()


# %%
# World fatality rate
'{:.2f}%'.format(100 *
                 df[df['date'] == df['date'].iloc[-1]]['Deaths'].sum() /
                 df[df['date'] == df['date'].iloc[-1]]['Confirmed'].sum())


# %%
# African fatality rate
'{:.2f}%'.format(100 *
                 df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Deaths'].sum() /
                 df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Confirmed'].sum())


# %%
# Outline the specific regions of the African continent
east = ['Burundi',
        'Comoros',
        'Djibouti',
        'Eritrea',
        'Ethiopia',
        'Kenya',
        'Madagascar',
        'Malawi',
        'Mauritius',
        'Mozambique',
        'Rwanda',
        'Seychelles',
        'Somalia',
        'South Sudan',
        'Tanzania',
        'Uganda',
        'Zambia',
        'Zimbabwe']
north = ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia', 'Sudan']
west = [
    'Benin',
    'Burkina Faso',
    'Cabo Verde',
    '''Côte d'Ivoire''',
    'Gambia',
    'Ghana',
    'Guinea',
    'Guinea-Bissau',
    'Liberia',
    'Mali',
    'Mauritania',
    'Niger',
    'Nigeria',
    'Senegal',
    'Sierra Leone',
    'Togo'
]
central = ['Cameroon',
           'Central African Republic',
           'Chad',
           'Congo (Brazzaville)',
           'Angola',
           'Equatorial Guinea',
           'Gabon',
           'Sao Tome and Príncipe',
           'Congo (Kinshasa)',
           'Republic of the Congo', ]
south = ['Botswana',
         'Eswatini',
         'Lesotho',
         'Namibia',
         'South Africa']

# %% [markdown]
# # Region Specific EDA - EAST AFRICA

# %%


def ea(df_africa):
    df_ea = df_africa[df_africa['Country/Region'].isin(east)]
    return df_ea


# %%
ea(df_africa)


# %%
region = 'Uganda'

print('Fatality rate: {:.2f}%'.format(100 *
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Deaths'].sum() /
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Confirmed'].sum()))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Active'].sum(),
    name="Active cases"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Confirmed'].sum(),
    name="Total Confirmed"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Deaths'].sum(),
    name="Deaths"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Recovered'].sum(),
    name="Recovered"))

fig.update_layout(title="COVID-19 infections in {}".format(region),
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
region = 'Kenya'

print('Fatality rate: {:.2f}%'.format(100 *
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Deaths'].sum() /
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Confirmed'].sum()))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Active'].sum(),
    name="Active cases"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Confirmed'].sum(),
    name="Total Confirmed"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Deaths'].sum(),
    name="Deaths"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Recovered'].sum(),
    name="Recovered"))

fig.update_layout(title="COVID-19 infections in {}".format(region),
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
region = 'Rwanda'

print('Fatality rate: {:.2f}%'.format(100 *
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Deaths'].sum() /
                                      df[(df['Country/Region'] == region) &
                                         (df['date'] == df['date'].iloc[-1])]['Confirmed'].sum()))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Active'].sum(),
    name="Active cases"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Confirmed'].sum(),
    name="Total Confirmed"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Deaths'].sum(),
    name="Deaths"))

fig.add_trace(go.Scatter(
    x=df[df['Country/Region'] == region].groupby('date')['date'].first(),
    y=df[df['Country/Region'] == region].groupby('date')['Recovered'].sum(),
    name="Recovered"))

fig.update_layout(title="COVID-19 infections in {}".format(region),
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
print('Fatality rate: {:.2f}%'.format(100 *
                                      df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Deaths'].sum() /
                                      df_africa[df_africa['date'] == df_africa['date'].iloc[-1]]['Confirmed'].sum()))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Confirmed'].sum(),
    name="Total Confirmed"))


fig.add_trace(go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Active'].sum(),
    name="Active cases"))

fig.add_trace(go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Recovered'].sum(),
    name="Recovered"))

fig.add_trace(go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Deaths'].sum(),
    name="Deaths"))

fig.update_layout(title="COVID-19 infections in all of Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for country in east:
    fig.add_trace(go.Scatter(
        x=df[df['Country/Region'] == country].groupby('date')['date'].first(),
        y=df[df['Country/Region'] == country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

fig.update_layout(title="Active COVID-19 cases in East Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()

# %% [markdown]
# # West Africa

# %%
fig = go.Figure()
for country in west:
    fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

fig.update_layout(title="Active COVID-19 cases in West Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for country in west:
    fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

fig.update_layout(title="Confirmed COVID-19 cases in West Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for country in west:
    fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

fig.update_layout(title="Recovered COVID-19 cases in West Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for country in west:
    fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

fig.update_layout(title="Death COVID-19 cases in West Africa",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
df3 = df[df['Country/Region'].isin(africa)]

data = df3[df3['date'] == df3['date'].iloc[-1]].groupby('Country/Region').agg({'Active': 'sum',
                                                                               'Long_': 'mean',
                                                                               'Lat': 'mean',
                                                                               'Country/Region': 'first'
                                                                               })

fig = go.Figure(data=go.Scattergeo(
    lon=data['Long_'],
    lat=data['Lat'],
    text=data['Country/Region'] + ', ' +
    data['Country/Region'] + ': ' + data['Active'].astype(str),
    mode='markers',
    marker_size=(100 * data['Active'] / data['Active'].max()),
    marker=dict(reversescale=False,
                autocolorscale=False,
                symbol='circle',
                line=dict(width=1, color='rgba(102, 102, 102)'),
                colorscale='Reds',
                cmin=0,
                color=data['Active'],
                cmax=data['Active'].max(),
                colorbar_title="Active Cases")))

fig.update_layout(title='Number of active cases by African countries',
                  geo=dict(scope='africa',

                           showland=True,
                           landcolor="rgb(100, 125, 100)",
                           showcountries=True,
                           showsubunits=True,
                           showlakes=False,))
fig.show()


# %%

fig = go.Figure()
for region in df_africa['Country/Region'].unique():
    if df_africa[(df_africa['date'] == df_africa['date'].iloc[-1]) & (df_africa['Country/Region'] == region)]['Confirmed'].sum() > 100:
        fig.add_trace(go.Scatter(
            x=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['date'].first(),
            y=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['Confirmed'].sum(),
            name=region,
            hoverinfo='x+y+z+text+name',
        ))

fig.update_layout(title="COVID-19 Confirmed Cases in Africa (Countries with greater than 100 confirmed cases)",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%

fig = go.Figure()
for region in df_africa['Country/Region'].unique():
    if df_africa[(df_africa['date'] == df_africa['date'].iloc[-1]) & (df_africa['Country/Region'] == region)]['Confirmed'].sum() > 50:
        fig.add_trace(go.Scatter(
            x=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['date'].first(),
            y=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['Deaths'].sum(),
            name=region,
            hoverinfo='x+y+z+text+name',
            stackgroup='one'))

fig.update_layout(title="COVID-19 Deaths in Africa (Countries with greater than 50 confirmed deaths)",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for region in df_africa['Country/Region'].unique():
    if df_africa[(df_africa['date'] == df_africa['date'].iloc[-1]) & (df_africa['Country/Region'] == region)]['Confirmed'].sum() > 100:
        fig.add_trace(go.Scatter(
            x=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['date'].first(),
            y=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['Active'].sum(),
            name=region,
            hoverinfo='x+y+z+text+name',
        ))

fig.update_layout(title="COVID-19 Active Cases in Africa (Countries with greater than 100 confirmed cases)",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%
fig = go.Figure()
for region in df_africa['Country/Region'].unique():
    if df_africa[(df_africa['date'] == df_africa['date'].iloc[-1]) & (df_africa['Country/Region'] == region)]['Confirmed'].sum() > 50:
        fig.add_trace(go.Scatter(
            x=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['date'].first(),
            y=df_africa[df_africa['Country/Region'] ==
                        region].groupby('date')['Recovered'].sum(),
            name=region,
            hoverinfo='x+y+z+text+name',
        ))

fig.update_layout(title="COVID-19 Recovered Cases in Africa (Countries with greater than 50 confirmed recoveries)",
                  xaxis_title="Date",
                  yaxis_title="Number of Individuals")

fig.show()


# %%


import glob
import io
import re
from datetime import date, timedelta

import numpy as np
import pandas as pd
import requests


def etl():
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

    global_data = df.to_csv('global_data.csv', index=False)

    df.drop(['FIPS', 'Admin2', 'Combined_Key',
             '404: Not Found'], axis=1, inplace=True)

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

    df_africa = df[df['Country/Region'].isin(africa)]

    df_africa.drop(['Province/State', 'Province_State',
                    'Last Update', 'Last_Update'], axis=1, inplace=True)

    df_africa = df_africa[['date',
                           'Country/Region',
                           'Confirmed',
                           'Deaths',
                           'Recovered',
                           'Lat',
                           'Latitude', 'Long_', 'Longitude']]

    df_africa['Confirmed'] = df_africa['Confirmed'].fillna(0).astype(int)
    df_africa['Deaths'] = df_africa['Deaths'].fillna(0).astype(int)
    df_africa['Recovered'] = df_africa['Recovered'].fillna(0).astype(int)
    df_africa['Active'] = df_africa['Confirmed'] - \
        df_africa['Deaths'] - df_africa['Recovered']

    df_africa['Lat'] = df_africa.apply(
        lambda row: row['Latitude']if np.isnan(row['Lat']) else row['Lat'],
        axis=1
    )

    df_africa['Long_'] = df_africa.apply(
        lambda row: row['Longitude']if np.isnan(
            row['Long_']) else row['Long_'],
        axis=1
    )
    df_africa.drop(['Latitude', 'Longitude'], axis=1, inplace=True)
    df_africa.rename(columns={'Lat': 'Latitude',
                              'Long_': 'Longitude'}, inplace=True)

    african_data = df_africa.to_csv('africa_data.csv', index=False)

    return global_data, african_data

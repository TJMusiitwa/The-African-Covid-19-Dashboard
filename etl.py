import glob
import io
import re
from datetime import date, timedelta

import numpy as np
import pandas as pd
import requests


def etl(source='web'):
    if source == 'folder':
        # Load files from folder
        path = 'data'
        all_files = glob.glob(path + "/*.csv")

        files = []

        for filename in all_files:
            file = re.search(r'([0-9]{2}\-[0-9]{2}\-[0-9]{4})', filename)[0]
            print(file)
            df = pd.read_csv(filename, index_col=None, header=0)
            df['date'] = pd.to_datetime(file)
            df.rename(columns={'Province_State': 'Province/State',
                               'Country_Region': 'Country/Region',
                               'Lat': 'Latitude',
                               'Long_': 'Longitude'}, inplace=True)
            files.append(df)

    elif source == 'web':
        # Load files from web
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
            df.rename(
                columns={'Country_Region': 'Country/Region'}, inplace=True)
            files.append(df)

    df = pd.concat(files, axis=0, ignore_index=True, sort=False)

    df.drop(['Province/State', 'Province_State', 'Last Update', 'Last_Update',
             'FIPS', 'Admin2', 'Combined_Key', '404: Not Found'], axis=1, inplace=True)

    # Re-order the columns for readability
    df = df[['date',
             'Country/Region',
             'Confirmed',
             'Deaths',
             'Recovered',
             'Latitude',
             'Longitude']]
    # Fill missing values as 0; create Active cases column
    df['Confirmed'] = df['Confirmed'].fillna(0).astype(int)
    df['Deaths'] = df['Deaths'].fillna(0).astype(int)
    df['Recovered'] = df['Recovered'].fillna(0).astype(int)
    df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

    # Replace missing values for longitude
    df['Long_'] = df.apply(
        lambda row: row['Longitude']if np.isnan(
            row['Long_']) else row['Long_'],
        axis=1)

    df['Lat'] = df.apply(
        lambda row: row['Latitude']if np.isnan(row['Lat']) else row['Lat'],
        axis=1)
    return df


def africa_data(data):
    africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Côte d’Ivoire', 'Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi',
              'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe', 'Congo (Brazzaville)', 'Ivory Coast', 'Congo (Kinshasa)', 'Republic of the Congo', 'Gambia, The']
    df_africa = data[data['Country/Region'].isin(africa)]
    df_africa = df_africa.drop('Province/State', axis=1)
    return df_africa


def na_data(data):
    north = ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia', 'Sudan']
    df_na = data[data['Country/Region'].isin(north)]
    df_na = df_na.drop('Province/State', axis=1)
    return df_na


def sa_data(data):
    south = ['Botswana', 'Eswatini', 'Lesotho', 'Namibia', 'South Africa']
    df_sa = data[data['Country/Region'].isin(south)]
    df_sa = df_sa.drop('Province/State', axis=1)
    return df_sa


def ca_data(data):
    central = ['Cameroon', 'Central African Republic', 'Chad',
               'Congo (Brazzaville)', 'Angola', 'Equatorial Guinea', 'Gabon', 'Sao Tome and Príncipe', 'Congo (Kinshasa)', 'Republic of the Congo', ]
    df_ca = data[data['Country/Region'].isin(central)]
    df_ca = df_ca.drop('Province/State', axis=1)
    return df_ca


def wa_data(data):
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
    df_wa = data[data['Country/Region'].isin(west)]
    df_wa = df_wa.drop('Province/State', axis=1)
    return df_wa


def ea_data(data):
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
    df_ea = data[data['Country/Region'].isin(east)]
    df_ea = df_ea.drop('Province/State', axis=1)
    return df_ea


if __name__ == '__main__':
    data = etl()
    data.to_csv('dashboard_data.csv', index=False)

    df_africa = africa_data(data)
    df_africa.to_csv('df_africa.csv', index=False)

    df_ea = ea_data(data)
    df_ea.to_csv('df_ea.csv', index=False)

    df_wa = wa_data(data)
    df_wa.to_csv('df_wa.csv', index=False)

    df_ca = ca_data(data)
    df_ca.to_csv('df_ca.csv', index=False)

    df_sa = sa_data(data)
    df_sa.to_csv('df_sa.csv', index=False)

    df_na = na_data(data)
    df_na.to_csv('df_na.csv', index=False)

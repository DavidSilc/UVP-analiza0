import requests
import pandas as pd


def pridobi_uredi(sirina, dolzina, zac, konec):

    # sestavimo zahtevo
    str_sirina = str(sirina)
    str_dolzina = str(dolzina)
    API = "https://archive-api.open-meteo.com/v1/archive?latitude=" + str_sirina + "&longitude="+str_dolzina + "&start_date=" + \
        zac + "&end_date=" + konec + \
        "&daily=temperature_2m_max,rain_sum,precipitation_hours,shortwave_radiation_sum&timezone=auto"

    # shranimo odgovor in spravimo podatke v format JSON
    odgovor = requests.get(API)
    podatkiJson = odgovor.json()

    dnevno = podatkiJson['daily']

    # ustvarimo pandas dataframe za lazjo obdelavo podatkov
    df = pd.DataFrame(dnevno)

    # prevedmo stolpce
    slovar = {'time': 'datum',
              'temperature_2m_max': 'temperatura',
              'rain_sum': 'dež_sum',
              'precipitation_hours': 'dež_ure',
              'shortwave_radiation_sum': 'radijacija'}
    df.rename(columns=slovar, inplace=True)

    return df


def shrani_tabelo(df, ime):
    name = ime + ".csv"
    df.to_csv(name, index=False)

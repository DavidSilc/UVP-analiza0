import pandas as pd
import matplotlib.pyplot as plt


def groupiranje_leta_meseci(df):
    df['datum'] = pd.to_datetime(df['datum'])

    df['mesec'] = df['datum'].dt.month
    df['leto'] = df['datum'].dt.year

    mesecno_povprecje = df.groupby(['leto', 'mesec']).agg({
        'temperatura': 'mean',
        'dež_sum': 'sum',
        'dež_ure': 'sum',
        'radijacija': 'sum'
    }).reset_index()

    return mesecno_povprecje

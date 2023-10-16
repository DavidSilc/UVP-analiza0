import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def grafi_mesecnih_povprecij(mesecno_povprecje):

    _, axs = plt.subplots(4, 1, figsize=(10, 10), sharex=False)

    axs[0].bar(mesecno_povprecje['mesec'],
               mesecno_povprecje['temperatura'], color='red')
    axs[0].set_ylabel('Temperatura (°C)')
    axs[0].set_title('Povprečne mesečne temperature')

    axs[1].bar(mesecno_povprecje['mesec'],
               mesecno_povprecje['dež_sum'], color='blue')
    axs[1].set_ylabel('Seštevek padavin (mm)')
    axs[1].set_title('Seštevek mesečnih padavin')

    axs[2].bar(mesecno_povprecje['mesec'],
               mesecno_povprecje['dež_ure'], color='green')
    axs[2].set_ylabel('Padavine v urah')
    axs[2].set_title('Čas mesečnih padavin')

    axs[3].bar(mesecno_povprecje['mesec'],
               mesecno_povprecje['radijacija'], color='yellow')
    axs[3].set_xlabel('Mesec')
    axs[3].set_ylabel('Sončno sevanje (Megajoules)')
    axs[3].set_title('Mesečno sončno sevanje')

    plt.xticks(rotation=50)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def grafi_letnih_povprecij(letno_povprecje):

    _, axs = plt.subplots(4, 1, figsize=(10, 10), sharex=False)

    axs[0].bar(letno_povprecje['leto'],
               letno_povprecje['temperatura'], color='red')
    axs[0].set_ylabel('Temperatura (°C)')
    axs[0].set_title('Povprečne letne temperature')

    axs[1].bar(letno_povprecje['leto'],
               letno_povprecje['dež_sum'], color='blue')
    axs[1].set_ylabel('Seštevek padavin (mm)')
    axs[1].set_title('Seštevek letnih padavin')

    axs[2].bar(letno_povprecje['leto'],
               letno_povprecje['dež_ure'], color='green')
    axs[2].set_ylabel('Padavine v urah')
    axs[2].set_title('Čas letnih padavin')

    axs[3].bar(letno_povprecje['leto'],
               letno_povprecje['radijacija'], color='yellow')
    axs[3].set_xlabel('Leto')
    axs[3].set_ylabel('Sončno sevanje (Megajoules)')
    axs[3].set_title('Letno sončno sevanje')

    plt.xticks(rotation=50)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def heatmap_temperatura(df):

    df['datum'] = pd.to_datetime(df['datum'])

    df['leto'] = df['datum'].dt.year
    df['dan'] = df['datum'].dt.dayofyear

    heatmap_data = df.pivot(
        index='leto', columns='dan', values='temperatura')

    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="YlGnBu", cbar_kws={
                'label': 'temperatura (°C)'}, linewidths=0.6)

    # Uredi graf
    plt.xlabel("Dan v letu")
    plt.ylabel("Leto")
    plt.title("Vzorci dnevnih temperatur zadnjih 30 let")

    # prikazi graf
    plt.show()

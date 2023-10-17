import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def groupiranje_leta_meseci(df):
    df['datum'] = pd.to_datetime(df['datum'])

    df['mesec'] = df['datum'].dt.month
    df['leto'] = df['datum'].dt.year

    mesecno_povprecje = df.groupby(['leto', 'mesec']).agg({
        'temperatura': 'mean',
        'dež_sum': 'mean',
        'dež_ure': 'mean',
        'radijacija': 'mean'
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
    axs[3].set_ylabel('Sončno sevanje (MJ)')
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


def heatmap_radijacija(df):

    df['datum'] = pd.to_datetime(df['datum'])

    df['leto'] = df['datum'].dt.year
    df['dan'] = df['datum'].dt.dayofyear

    heatmap_data = df.pivot(
        index='leto', columns='dan', values='radijacija')

    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="YlGnBu", cbar_kws={
                'label': 'radijacija (MJ)'}, linewidths=0.6)

    # Uredi graf
    plt.xlabel("Dan v letu")
    plt.ylabel("Leto")
    plt.title("Vzorci dnevnega sončnega sevanja zadnjih 30 let")

    # prikazi graf
    plt.show()


def graf_mediana_max_min(df, vrsta):
    annual_stats = df.groupby('leto').agg({
        'temperatura': [vrsta],
        'dež_sum': [vrsta],
        'dež_ure': [vrsta],
        'radijacija': [vrsta]
    }).reset_index()
    slovar = {
        'min': 'najmanjša/e',
        'max': 'največja/e',
        'median': 'mediana'
    }

    leta = annual_stats['leto']

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.bar(leta, annual_stats['temperatura'][vrsta],
            label=slovar[vrsta] + " temperatura", color="purple")
    plt.legend()
    plt.xlabel('Leto')
    plt.ylabel(slovar[vrsta] + " temperatura (°C)")

    plt.subplot(2, 2, 2)
    plt.bar(leta, annual_stats['dež_sum'][vrsta],
            label=slovar[vrsta] + ' padavine', color="green")
    plt.legend()
    plt.xlabel('Leto')
    plt.ylabel(slovar[vrsta] + " padavine (mm)")

    plt.subplot(2, 2, 3)
    plt.bar(leta, annual_stats['dež_ure']
            [vrsta], label=slovar[vrsta] + " ure padavin", color='red')
    plt.legend()
    plt.xlabel('Leto')
    plt.ylabel(slovar[vrsta] + ' ure padavin')

    plt.subplot(2, 2, 4)
    plt.bar(leta, annual_stats['radijacija']
            [vrsta], label=slovar[vrsta] + ' sončne radijacije', color='black')
    plt.legend()
    plt.xlabel('Leto')
    plt.ylabel(slovar[vrsta] + ' sončne radijacije (Megajoules)')

    plt.tight_layout()
    plt.show()

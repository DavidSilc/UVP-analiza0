# UVP-analiza

Avtor: David Planinšek Šilc

Za projektno nalogo pri predmetu Uvod v programiranje sem pripravil analizo vremenskih razmer. Podatke sem dobil iz arhiva vremenskih razmer, kjer so zbrani podatki o vremenu od leta 1940 do danes. V projektni nalogi pridobim podatke iz **API**, jih **obdelam**, **shranim** tiste, ki jih potrebujem za analizo, ter na koncu predstavim analizo z **Jupyter Notebook**.

API in njegovo dokumentacijo sem našel na [Uradni Open-Meteo strani](https://open-meteo.com/ "open-meteo").

Odločil sem se za obdelavo podatkov o največji dnevni temperaturi 2 metra nad zemljo, seštevek padavin na dan v milimetrih, koliko ur na dan so padale padavine in seštevek sončne radijacije v enem dnevu izmerjena v mega joulih.

## Navodila za uporabo

V datoteki _podatki.py_ se nahajata funkcije, ki pridobita podatke iz API, jih ustrezno uredita, prevedeta in shranita v _.csv_ datoteko.
Na začetku analize v Jupyter Notebooku, se nahajajo časovni intervali ter zemljepisna širina in dolžina, ki sem jih izbral jaz za potrebe prikaza podatkov. Uporabnik si lahko poljubno izbira časovne intervale in lokacijo, in s tem spreminja rezultate analize. Jaz sem izbral podatke za Slovenijo, ki ima se nahaja na kordinatih **_46.0833_** in **_15.0_** v časovnem obdobju od **_1.1.1990_** do **_1.1.2020_**.

V datoteki _analiza.py_ se nahajajo funkcije, ki analizirajo izbrane podatke, in jih primerno prikažejo na različnih grafih.

Uporabnik prenese vse datoteke .py in glavno datoteko _rezultati.ipynb_, mora še namestiti vse knjižnice, ki so bile uporabljene za analizo. To so:
`pandas`, `matplotlib`, `seaborn`, `requests` in `sklearn`

Ko ima uporabnik naloženo vse potrebno lahko zažene _rezultati.ipynb_.

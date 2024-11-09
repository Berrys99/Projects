Popis projektu:
projekt slouží k extrakci výsledků parlamentních voleb 2017 v jednotlivích okresech.

Instalace knihoven:
Všchny externí knihovny použité v tomto projektu jsou přiložené v souboru "requirements.txt".
Všechny najednou nainstalujeme pomocí příkazu: pip install -r requirements.txt

Spuštění projektu:
Pro spuštění projektu v příkazovém řádku, jsou zapotřebí 2 argumenty.
př.:
py projekt_3.py "<odkaz_okresu>" <název_vysledného_souboru.csv>

Výběr okresu:
Na stránce https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ vybereme okres tak že ve sloupci "výběr obce" klikneme na "X" podle toho jaký okres chceme zvolit.
Následně okopírujeme url, které vložíme jako první argument.

Příklad projektu pro výsledky v okrese Mladá Boleslav:
1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107
2. argument: vysledky_mlada_boleslav.csv

py projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107" vysledky_mlada_boleslav.csv
!!!NEZAPOMENOUT NA UVOZOVKY!!!

Průběh stahování:
Downloading data from chosen url: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2107
Writing data to the file: vysledky_mlada_boleslav.csv

Částečný výstup:
code	location	registered	envelops	valid	Občanská demokratická strana	Řád národa - Vlastenecká unie	CESTA ODPOVĚDNÉ SPOLEČNOSTI	Česká str.sociálně demokrat.
535427	Bakov nad Jizerou	3 922	2 551	2 539	285	3	3	204	1	179	153	27	32	36	2	1	252	2	2	113	864	1	8	42	2	18	4	6	295	4

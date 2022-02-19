import os
from pprint import pprint
import csv

import bs4.element
import requests
from bs4 import BeautifulSoup


def main(url):
    # zpracuj odpoved serveru
    url = url
    response = requests.get(url)
    # print(response.text)

    parsed_soup = BeautifulSoup(response.text, 'html.parser')

    # najdi prvni tabulku
    table_tag_top = parsed_soup.find('table', {'class': 'table'})
    print(table_tag_top.prettify())
    print(type(table_tag_top))
    pprint(dir(table_tag_top))

    # selekce elementu tr, cili radku
    vsechny_tr = table_tag_top.find_all('tr')
    print(dir(vsechny_tr))
    print(vsechny_tr[2])
    print(type(vsechny_tr))
    print(type(vsechny_tr[1]))

    # selekce jednotlivych bunek td od indexu 2, to je prvni nazev obce
    vysledky = []
    for tr in vsechny_tr[2:]:
        td_na_radku = tr.find_all('td')
        data_obce = vyber_atributy_z_radku(td_na_radku)
        vysledky.append(data_obce)
        # ten samy zapis, ale na jednom radku
        # vysledky.append(vyber_atributy_z_radku(tr.find_all('td')))
    # stejny zapis pomoci komprehence
    # vysledky = [vyber_atributy_z_radku(tr.find_all('td'))
    #             for tr in vsechny_tr[2:]]

    pprint(vysledky)

    zapis_data(vysledky, 'prvni_tabulka.csv')


def vyber_atributy_z_radku(tr_tag: bs4.element.ResultSet):
    """
    Z kazdeho radku (tr) vyber urcite bunky (td)[index]
    a zabal je do slovniku
    :param tr_tag: vsechny_tr
    :return: dict
    """
    return {
        'Kod obce': tr_tag[0].get_text(),
        'Nazev obce': tr_tag[1].get_text()
    }


def zapis_data(data: list, jmeno_souboru: str) -> str:
    with open(jmeno_souboru, mode='w', encoding='UTF-8', newline='') as csv_output:
        sloupce = data[0].keys()
        writer = csv.DictWriter(csv_output, fieldnames=sloupce)
        writer.writeheader()
        writer.writerows(data)
        print("File written")



    # kod_obce = [x.get_text() for x in parsed_soup.find_all('td', {'class': 'cislo'})]
    # nazev_obce = [x.get_text() for x in parsed_soup.find_all('td', {'class': 'overflow_name'})]
    # # pprint(parsed_soup.find_all('td', {'class': 'cislo'}))
    # # pprint(parsed_soup.find_all('td', {'class': 'overflow_name'}))
    # print(kod_obce)
    # print(nazev_obce)

#     filtruj_kod_z_radku(kod_obce)
#
#
# def filtruj_kod_z_radku(a_tag):
#     radky = a_tag.get_text().splitlines()
#     print(radky)

    # data = dict(zip(kod_obce, nazev_obce))
    # print(data)
    #
    #
    #
    #
    # for kod in kod_obce:
    #     print(kod)
    # #
    # # for nazev in nazev_obce:
    # #     print(nazev.text)
    # #
    # #
    # with open('soubor1.csv', mode='w', encoding='UTF=8', newline='') as output:
    #     header = ['Kod obce', 'Nazev obce']
    #     writer = csv.writer(output)
    #     writer.writerow(header)
    #     writer.writerows(data)
    #
    #     print('File written')

    # sloupce = data[0].keys()
    # zapis = csv.DictWriter(csv_output, fieldnames=sloupce)
    # zapis.writeheader()
    # zapis.writerows(data)



#
#     table_tag_obec = soup.find('table', {'class': 'table'})
#     # print(table_tag_obec)
#
#     tr_tags = table_tag_obec.find_all('tr')
#     print(tr_tags[2:])
#     #
#     print(vyber_atributy_z_radku(tr_tags))
#
# def vyber_atributy_z_radku(tr_tag: 'import bs4.element'):
#     """
#     z kazdeho radku (tr) vyber urcite bunky (td)[index]
#     a zabal je do slovniku
#     """
#     return {
#         'Cislo': tr_tag[0].get_text(),
#         'Jmeno obce': tr_tag[1].get_text()

    # }
    #
    # vysledky = []
    #
    # for tr in tr_tags[1:]:
    #     vysledky.append(vyber_atributy_z_radku(tr.find_all('td')))
    #
    # pprint(vysledky)
    #
    #
    # data_o_stranach = [
    #     vyber_atributy_z_radku(tr.find_all('th'))
    #     for tr in vsechny_tr[1:]
    # ]
    #
    # pprint(data_o_stranach)


if __name__ == '__main__':
    main('https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103')

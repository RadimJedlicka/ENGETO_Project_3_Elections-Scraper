# ENGETO_Project_3_Elections-Scraper
## Popis projektu:

Závěrečný projekt prověří tvé znalosti nejenom z posledních lekcí, ale z celého kurzu. 
Tvým úkolem bude vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu.

Napiš takový skript, který vybere jakýkoliv územní celek z tohoto odkazu 
Např. X u Benešov odkazuje sem . Z tohoto odkazu chcete vyscrapovat výsledky hlasování 
pro všechny obce (resp. pomocí X ve sloupci Výběr okrsku).


## Jak postupovat
1. Na svém počítači si vytvoříte vlastní virtuální prostředí (speciálně pro tento úkol)
2. Do nově vytvořeného prostředí si přes IDE (nebo příkazový řádek) nainstalujete potřebné knihovny třetích stran
3. Vygenerujete soubor requirements.txt, který obsahuje soupis všech knihoven a jejich verzí (nevypisovat ručně!)
4. Výsledný soubor budete spouštět pomocí 2 argumentů (ne pomocí funkce input). 
   První argument obsahuje odkaz, který územní celek chcete scrapovat (př. územní celek Prostějov ), druhý argument obsahuje jméno výstupního souboru (př. vysledky_prostejov.csv)
5. Pokud uživatel nezadá oba argumenty (ať už nesprávné pořadí, nebo argument, který neobsahuje správný odkaz), 
   program jej upozorní a nepokračuje.
6. Následně dopište README.md soubor, který uživatele seznámíte se svým projektem. 
   Jak nainstalovat potřebné knihovny ze souboru requirements.txt, jak spustit váš soubor, 
   příp. doplnit ukázku, kde demonstrujete váš kód na konkrétním odkaze s konkrétním výpisem.

## Projekt bude obsahovat
1. Soubor s programem (.py), který pro správný běh potřebuje 2 argumenty při spuštění
2. Soubor se seznamem knihoven a verzí (requirements.txt)
3. Stručnou dokumentaci (popis, instalace knihoven, ukázka) (README.md)
4. Soubor s uloženým výstupem (.csv)

## Výstup bude obsahovat
Ve výstupu (soubor .csv) každý řádek obsahuje informace pro konkrétní obec. Tedy podobu:
1. kód obce
2. název obce
3. voliči v seznamu
4. vydané obálky
5. platné hlasy
6. kandidující strany

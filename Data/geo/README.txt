# README KDZ_Stadtregionen_GEM_20160101

Stadtregionen.at ist ein Projekt des Österreichischen Städtebunds und des KDZ – Zentrum für Verwaltungsforschung.
Mehr Infos: http://stadtregionen.at/definitionen

Der Datensatz beinhaltet alle Gemeinden aus Österreich die entweder in einer Kern- oder Außenzone einer Stadtregion liegen.
Eine Stadtregion verfügt jeweils über eine Kernzone sowie einer Außenzone. Die Zuordnung der Gemeinden kann über die Attribute "sr_region" und "sr_zone" erfolgen.
Projektion: EPSG:31287 https://epsg.io/31287

# ATTRIBUTE
gkz - Amtliche Gemeindekennzahl
name - Gemeindename
sr_region -  Stadtregion-ID: "SR020" = Stadtregion Graz
sr_zone - Zonen-ID: "SR021" = Kernzone Stadtregion Graz, "SR022" = Außenzone Graz
sr_name - Name der Stadtregion
is_core - 1=Gemeinde liegt in Kernzone, 0= Gemeinde liegt in Außenzone

# DATENBASIS
OGDEXT_GEM_1_STATISTIK_AUSTRIA_20160101 http://data.statistik.gv.at/data/OGDEXT_GEM_1_STATISTIK_AUSTRIA_20160101.zip
CC-BY-3.0: Statistik Austria - data.statistik.gv.at
Datum der Veröffentlichung: 01.01.2016

#LIZENZ
Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 2.0 https://creativecommons.org/licenses/by/2.0/
Datenquelle: stadtregionen.at - KDZ - Zentrum für Verwaltungsforschung, Statisik Austria

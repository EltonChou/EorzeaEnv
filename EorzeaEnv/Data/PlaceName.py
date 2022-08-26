
from typing import Literal, Mapping, TypedDict, Union

from ..eorzea_lang import EorzeaLang


class PlaceInfoDict(TypedDict):
    index: int
    place_name: str


place_name: Mapping[
    Union[EorzeaLang, Literal['de', 'en', 'fr', 'ja']],
    Mapping[str, PlaceInfoDict]
] = {
    'de': {'abalathisches wolkenmeer': {'index': 2100,
                                        'place_name': 'Abalathisches '
                                        'Wolkenmeer'},
           'abanisches grenzland': {'index': 2406,
                                    'place_name': 'Abanisches '
                                    'Grenzland'},
           'abendrot-wacht': {'index': 2214,
                              'place_name': 'Abendrot-Wacht'},
           'achtzehnter stock': {'index': 1660,
                                 'place_name': 'Achtzehnter Stock'},
           'adlerblick (eingangshalle)': {'index': 3694,
                                          'place_name': 'Adlerblick '
                                          '(Eingangshalle)'},
           'adlerblick (wohnung)': {'index': 3695,
                                    'place_name': 'Adlerblick '
                                    '(Wohnung)'},
           'admiralsbrücke': {'index': 351, 'place_name': 'Admiralsbrücke'},
           'aglaia': {'index': 4167, 'place_name': 'Aglaia'},
           'aitiaskop': {'index': 4146, 'place_name': 'Aitiaskop'},
           'akadaemia anyder': {'index': 3007,
                                'place_name': 'Akadaemia Anyder'},
           'akh afah': {'index': 1399, 'place_name': 'Akh Afah'},
           'ala mhigo': {'index': 2691, 'place_name': 'Ala Mhigo'},
           'alexander': {'index': 2041, 'place_name': 'Alexander'},
           'alt-gridania': {'index': 53, 'place_name': 'Alt-Gridania'},
           'alt-sharlayan': {'index': 3706, 'place_name': 'Alt-Sharlayan'},
           'altar von djanan qhat': {'index': 2339,
                                     'place_name': 'Altar von Djanan '
                                     'Qhat'},
           'alter stollen': {'index': 3427, 'place_name': 'Alter Stollen'},
           'alzadaals vermächtnis': {'index': 4154,
                                     'place_name': 'Alzadaals '
                                     'Vermächtnis'},
           'am rande des endes': {'index': 3686,
                                  'place_name': 'Am Rande des Endes'},
           'amaurot': {'index': 2985, 'place_name': 'Amaurot'},
           'amh araeng': {'index': 2955, 'place_name': 'Amh Araeng'},
           'anamnesis anyder': {'index': 3467,
                                'place_name': 'Anamnesis Anyder'},
           'antiturm': {'index': 2088, 'place_name': 'Antiturm'},
           'antriebszylinder der ragnarök': {'index': 467,
                                             'place_name': 'Antriebszylinder '
                                             'der '
                                             'Ragnarök'},
           'anwesen der fortemps': {'index': 2320,
                                    'place_name': 'Anwesen der '
                                    'Fortemps'},
           'aquapolis': {'index': 1799, 'place_name': 'Aquapolis'},
           'arm des sohnes': {'index': 1723,
                              'place_name': 'Arm des Sohnes'},
           'arm des vaters': {'index': 1638,
                              'place_name': 'Arm des Vaters'},
           'arretur p1t6': {'index': 2265, 'place_name': 'Arretur P1T6'},
           'arretur s1t7': {'index': 2256, 'place_name': 'Arretur S1T7'},
           'arretur z1t9': {'index': 2266, 'place_name': 'Arretur Z1T9'},
           'aschenfall': {'index': 3469, 'place_name': 'Aschenfall'},
           'atem des schöpfers': {'index': 1841,
                                  'place_name': 'Atem des Schöpfers'},
           'atlas-gipfel': {'index': 3217, 'place_name': 'Atlas-Gipfel'},
           'augen des schöpfers': {'index': 1835,
                                   'place_name': 'Augen des Schöpfers'},
           'azim-steppe': {'index': 2411, 'place_name': 'Azim-Steppe'},
           'azys lla': {'index': 2101, 'place_name': 'Azys Lla'},
           'badehaus bokairo': {'index': 2413,
                                'place_name': 'Badehaus Bokairo'},
           'baelsar-wall': {'index': 1857, 'place_name': 'Baelsar-Wall'},
           'bahamuts herz': {'index': 1409, 'place_name': 'Bahamuts Herz'},
           'bardams probe': {'index': 2833, 'place_name': 'Bardams Probe'},
           'baum des urteils': {'index': 1363,
                                'place_name': 'Baum des Urteils'},
           'beichtstuhl von toupasa dem älteren': {'index': 3228,
                                                   'place_name': 'Beichtstuhl '
                                                   'von '
                                                   'Toupasa '
                                                   'dem '
                                                   'Älteren'},
           "belah'dias fall": {'index': 2498,
                               'place_name': "Belah'dias Fall"},
           'blutender limbus': {'index': 4135,
                                'place_name': 'Blutender Limbus'},
           'bozja-südfront': {'index': 3534,
                              'place_name': 'Bozja-Südfront'},
           'brücke': {'index': 2371, 'place_name': 'Brücke'},
           "brüllvolx' langrast": {'index': 36,
                                   'place_name': "Brüllvolx' Langrast"},
           'burg selard': {'index': 3620, 'place_name': 'Burg Selard'},
           'castrum abania': {'index': 2665,
                              'place_name': 'Castrum Abania'},
           'castrum fluminis': {'index': 2799,
                                'place_name': 'Castrum Fluminis'},
           'castrum meridianum': {'index': 260,
                                  'place_name': 'Castrum Meridianum'},
           'chateau cosmea': {'index': 3385,
                              'place_name': 'Chateau Cosmea'},
           'chocobo-platz': {'index': 1500, 'place_name': 'Chocobo-Platz'},
           'chrysalis': {'index': 1390, 'place_name': 'Chrysalis'},
           'crystarium': {'index': 2951, 'place_name': 'Crystarium'},
           'das deck': {'index': 3470, 'place_name': 'Das Deck'},
           'das diadem': {'index': 1647, 'place_name': 'Das Diadem'},
           'das fenn': {'index': 2408, 'place_name': 'Das Fenn'},
           'das grab der lohe': {'index': 357,
                                 'place_name': 'Das Grab der Lohe'},
           'das herz': {'index': 3214, 'place_name': 'Das Herz'},
           'das karussell von lyhe ghiah': {'index': 3644,
                                            'place_name': 'Das '
                                            'Karussell '
                                            'von Lyhe '
                                            'Ghiah'},
           'das sternengrab': {'index': 4100,
                               'place_name': 'Das Sternengrab'},
           'das tosende auge': {'index': 459,
                                'place_name': 'Das Tosende Auge'},
           'deltametrie 1.0': {'index': 2357,
                               'place_name': 'Deltametrie 1.0'},
           'deltametrie 2.0': {'index': 2358,
                               'place_name': 'Deltametrie 2.0'},
           'deltametrie 3.0': {'index': 2359,
                               'place_name': 'Deltametrie 3.0'},
           'deltametrie 4.0': {'index': 2360,
                               'place_name': 'Deltametrie 4.0'},
           'delubrum reginae': {'index': 3597,
                                'place_name': 'Delubrum Reginae'},
           "der große wald rak'tika": {'index': 2957,
                                       'place_name': 'Der Große Wald '
                                       "Rak'tika"},
           'der hüter des sees': {'index': 418,
                                  'place_name': 'Der Hüter des Sees'},
           'der kaiserliche thron': {'index': 3568,
                                     'place_name': 'Der Kaiserliche '
                                     'Thron'},
           'der nabel': {'index': 359, 'place_name': 'Der Nabel'},
           'der trauernde heilige ': {'index': 392,
                                      'place_name': 'Der Trauernde '
                                      'Heilige '},
           'der traumbaum': {'index': 548, 'place_name': 'Der Traumbaum'},
           'der turm, paradigmenbrecher': {'index': 3647,
                                           'place_name': 'Der Turm, '
                                           'Paradigmenbrecher'},
           'der wogenbrecher': {'index': 1334,
                                'place_name': 'Der Wogenbrecher'},
           'die endeavor': {'index': 3477, 'place_name': 'Die Endeavor'},
           'die fraktal-kontinuum': {'index': 2148,
                                     'place_name': 'Die '
                                     'Fraktal-Kontinuum'},
           'die große leere': {'index': 3225,
                               'place_name': 'Die Große Leere'},
           'die kopierte fabrik': {'index': 3425,
                                   'place_name': 'Die kopierte Fabrik'},
           'die königliche stadt rabanastre': {'index': 2372,
                                               'place_name': 'Die '
                                               'königliche '
                                               'Stadt '
                                               'Rabanastre'},
           'die misery': {'index': 1960, 'place_name': 'Die Misery'},
           'die puppenfestung': {'index': 3576,
                                 'place_name': 'Die Puppenfestung'},
           'die ragnarök': {'index': 466, 'place_name': 'Die Ragnarök'},
           'die sanduhr': {'index': 617, 'place_name': 'Die Sanduhr'},
           'die stadt der tränen': {'index': 1742,
                                    'place_name': 'Die Stadt der '
                                    'Tränen'},
           'die verschlungenen schatten von bahamut': {'index': 1759,
                                                       'place_name': 'Die '
                                                       'Verschlungenen '
                                                       'Schatten '
                                                       'von '
                                                       'Bahamut'},
           'die versunkene stadt skalla': {'index': 2367,
                                           'place_name': 'Die '
                                           'versunkene '
                                           'Stadt Skalla'},
           'die zinnen': {'index': 2407, 'place_name': 'Die Zinnen'},
           'dohn mheg': {'index': 2979, 'place_name': 'Dohn Mheg'},
           'dom der einkehr': {'index': 112,
                               'place_name': 'Dom der Einkehr'},
           'domanische enklave': {'index': 2813,
                                  'place_name': 'Domanische Enklave'},
           'dorf des nebels': {'index': 425,
                               'place_name': 'Dorf des Nebels'},
           'dornmarsch': {'index': 360, 'place_name': 'Dornmarsch'},
           'dravanisches hinterland': {'index': 2001,
                                       'place_name': 'Dravanisches '
                                       'Hinterland'},
           'dravanisches vorland': {'index': 2000,
                                    'place_name': 'Dravanisches '
                                    'Vorland'},
           'dun scaith': {'index': 1868, 'place_name': 'Dun Scaith'},
           'einsame insel': {'index': 4043, 'place_name': 'Einsame Insel'},
           'elle des sohnes': {'index': 1714,
                               'place_name': 'Elle des Sohnes'},
           'elle des vaters': {'index': 1633,
                               'place_name': 'Elle des Vaters'},
           'elpis': {'index': 3713, 'place_name': 'Elpis'},
           'empfangszimmer': {'index': 1429,
                              'place_name': 'Empfangszimmer'},
           'empyreum': {'index': 4139, 'place_name': 'Empyreum'},
           'empyreum - zimmer': {'index': 3692,
                                 'place_name': 'Empyreum - Zimmer'},
           'endgültigkeit': {'index': 2449, 'place_name': 'Endgültigkeit'},
           'erzbasilika': {'index': 2327, 'place_name': 'Erzbasilika'},
           'eulmore': {'index': 2952, 'place_name': 'Eulmore'},
           'euphoratron': {'index': 4111, 'place_name': 'Euphoratron'},
           'eureka anemos': {'index': 2414, 'place_name': 'Eureka Anemos'},
           'eureka hydatos': {'index': 2545,
                              'place_name': 'Eureka Hydatos'},
           'eureka pagos': {'index': 2462, 'place_name': 'Eureka Pagos'},
           'eureka pyros': {'index': 2530, 'place_name': 'Eureka Pyros'},
           'faust des sohnes': {'index': 1708,
                                'place_name': 'Faust des Sohnes'},
           'faust des vaters': {'index': 1628,
                                'place_name': 'Faust des Vaters'},
           'feld der ehre': {'index': 1740, 'place_name': 'Feld der Ehre'},
           'feste dzemael': {'index': 64, 'place_name': 'Feste Dzemael'},
           'fockmast (eingangshalle)': {'index': 1811,
                                        'place_name': 'Fockmast '
                                        '(Eingangshalle)'},
           'fockmast (wohnung)': {'index': 1812,
                                  'place_name': 'Fockmast (Wohnung)'},
           'forschungstrakt für die geheimnisse des lebens': {'index': 4250,
                                                              'place_name': 'Forschungstrakt '
                                                              'für '
                                                              'die '
                                                              'Geheimnisse '
                                                              'des '
                                                              'Lebens'},
           'frohehalde': {'index': 2082, 'place_name': 'Frohehalde'},
           'frondales physiatrische akademie': {'index': 695,
                                                'place_name': 'Frondales '
                                                'Physiatrische '
                                                'Akademie'},
           'fundamente': {'index': 2300, 'place_name': 'Fundamente'},
           'gandoph-donnersteppe': {'index': 3468,
                                    'place_name': 'Gandoph-Donnersteppe'},
           'gangos': {'index': 3478, 'place_name': 'Gangos'},
           'garlemald': {'index': 3710, 'place_name': 'Garlemald'},
           'gasthaus gaffelschoner': {'index': 733,
                                      'place_name': 'Gasthaus '
                                      'Gaffelschoner'},
           'gefechtsplattform des g-retters': {'index': 3663,
                                               'place_name': 'Gefechtsplattform '
                                               'des '
                                               'G-Retters'},
           'geisterschloss': {'index': 1834,
                              'place_name': 'Geisterschloss'},
           'gerichtssaal': {'index': 2336, 'place_name': 'Gerichtssaal'},
           'geschlossene raumzeit': {'index': 3017,
                                     'place_name': 'Geschlossene '
                                     'Raumzeit'},
           'gesellschaftswerkstätte: dorf des nebels': {'index': 1227,
                                                        'place_name': 'Gesellschaftswerkstätte: '
                                                        'Dorf '
                                                        'des '
                                                        'Nebels'},
           'gesellschaftswerkstätte: empyreum': {'index': 3693,
                                                 'place_name': 'Gesellschaftswerkstätte: '
                                                 'Empyreum'},
           'gesellschaftswerkstätte: kelchkuppe': {'index': 1228,
                                                   'place_name': 'Gesellschaftswerkstätte: '
                                                   'Kelchkuppe'},
           'gesellschaftswerkstätte: lavendelbeete': {'index': 1229,
                                                      'place_name': 'Gesellschaftswerkstätte: '
                                                      'Lavendelbeete'},
           'gesellschaftswerkstätte: shirogane': {'index': 2271,
                                                  'place_name': 'Gesellschaftswerkstätte: '
                                                  'Shirogane'},
           'ghimlyt-finsternis': {'index': 2586,
                                  'place_name': 'Ghimlyt-Finsternis'},
           'gletscher': {'index': 3487, 'place_name': 'Gletscher'},
           'glühender limbus': {'index': 3797,
                                'place_name': 'Glühender Limbus'},
           'gold saucer': {'index': 1484, 'place_name': 'Gold Saucer'},
           'goldklamm': {'index': 65, 'place_name': 'Goldklamm'},
           'gottesportal': {'index': 4024, 'place_name': 'Gottesportal'},
           'greifenbrücke': {'index': 386, 'place_name': 'Greifenbrücke'},
           'grenzenloses blau': {'index': 2151,
                                 'place_name': 'Grenzenloses Blau'},
           'große gubal-bibliothek': {'index': 2038,
                                      'place_name': 'Große '
                                      'Gubal-Bibliothek'},
           'grund des mondes': {'index': 3684,
                                'place_name': 'Grund des Mondes'},
           'gulg': {'index': 2997, 'place_name': 'Gulg'},
           'gästezimmer des meghaduta-tempels': {'index': 4039,
                                                 'place_name': 'Gästezimmer '
                                                 'des '
                                                 'Meghaduta-Tempels'},
           'halatali': {'index': 49, 'place_name': 'Halatali'},
           'halle der beschwörung': {'index': 379,
                                     'place_name': 'Halle der '
                                     'Beschwörung'},
           'halle der bestie': {'index': 694,
                                'place_name': 'Halle der Bestie'},
           'halle der glücksaltäre': {'index': 2485,
                                      'place_name': 'Halle der '
                                      'Glücksaltäre'},
           'halle der prüfung': {'index': 3471,
                                 'place_name': 'Halle der Prüfung'},
           'handelshaus-sitzungsraum': {'index': 2927,
                                        'place_name': 'Handelshaus-Sitzungsraum'},
           'haukke-herrenhaus': {'index': 59,
                                 'place_name': 'Haukke-Herrenhaus'},
           'hauptquartier der allianz': {'index': 2862,
                                         'place_name': 'Hauptquartier '
                                         'der Allianz'},
           'hauptquartier der lemuren': {'index': 4022,
                                         'place_name': 'Hauptquartier '
                                         'der Lemuren'},
           'hauptquartier der palastwache': {'index': 354,
                                             'place_name': 'Hauptquartier '
                                             'der '
                                             'Palastwache'},
           'hauptsaal': {'index': 3817, 'place_name': 'Hauptsaal'},
           'heiligtum der qalyana': {'index': 2299,
                                     'place_name': 'Heiligtum der '
                                     'Qalyana'},
           'heiligtum der schlange': {'index': 2510,
                                      'place_name': 'Heiligtum der '
                                      'Schlange'},
           'herz des schöpfers': {'index': 1847,
                                  'place_name': 'Herz des Schöpfers'},
           'himmelsstadt': {'index': 3435, 'place_name': 'Himmelsstadt'},
           'himmelssäule': {'index': 2775, 'place_name': 'Himmelssäule'},
           'himmlische arena': {'index': 2548,
                                'place_name': 'Himmlische Arena'},
           'historisches amdapor': {'index': 125,
                                    'place_name': 'Historisches '
                                    'Amdapor'},
           'holminster': {'index': 3050, 'place_name': 'Holminster'},
           'holosphäre': {'index': 1304, 'place_name': 'Holosphäre'},
           'höllengrund': {'index': 2496, 'place_name': 'Höllengrund'},
           'höllenspund': {'index': 2762, 'place_name': 'Höllenspund'},
           'il mheg': {'index': 2956, 'place_name': 'Il Mheg'},
           'interdimensionaler riss': {'index': 2737,
                                       'place_name': 'Interdimensionaler '
                                       'Riss'},
           'irrungen der qitari': {'index': 3018,
                                   'place_name': 'Irrungen der Qitari'},
           'isolationstrakt für parasitäre lebensformen': {'index': 4196,
                                                           'place_name': 'Isolationstrakt '
                                                           'für '
                                                           'parasitäre '
                                                           'Lebensformen'},
           'isomorph-quartiere': {'index': 3222,
                                  'place_name': 'Isomorph-Quartiere'},
           'jadelichtung': {'index': 2354, 'place_name': 'Jadelichtung'},
           'kampfplatz': {'index': 1664, 'place_name': 'Kampfplatz'},
           'kanäle von uznair': {'index': 2340,
                                 'place_name': 'Kanäle von Uznair'},
           'kargland': {'index': 2851, 'place_name': 'Kargland'},
           'kelchkuppe': {'index': 427, 'place_name': 'Kelchkuppe'},
           'kelchkuppe - zimmer': {'index': 1158,
                                   'place_name': 'Kelchkuppe - Zimmer'},
           'kernsektor der ragnarök': {'index': 468,
                                       'place_name': 'Kernsektor der '
                                       'Ragnarök'},
           'kholusia': {'index': 2954, 'place_name': 'Kholusia'},
           'kienkan': {'index': 2847, 'place_name': 'Kienkan'},
           'klause der grimmigen': {'index': 2805,
                                    'place_name': 'Klause der '
                                    'Grimmigen'},
           'kloster von orbonne': {'index': 2864,
                                   'place_name': 'Kloster von Orbonne'},
           'kobai goten (eingangshalle)': {'index': 2272,
                                           'place_name': 'Kobai Goten '
                                           '(Eingangshalle)'},
           'kobai goten (wohnung)': {'index': 2273,
                                     'place_name': 'Kobai Goten '
                                     '(Wohnung)'},
           'kommandantur des großmeisters': {'index': 2335,
                                             'place_name': 'Kommandantur '
                                             'des '
                                             'Großmeisters'},
           'kommandobrücke der ragnarök': {'index': 469,
                                           'place_name': 'Kommandobrücke '
                                           'der Ragnarök'},
           'kommandobrücke rvh-03': {'index': 1305,
                                     'place_name': 'Kommandobrücke '
                                     'RVH-03'},
           'kommandobrücke rvh-04': {'index': 1410,
                                     'place_name': 'Kommandobrücke '
                                     'RVH-04'},
           'kommandobrücke rvh-06': {'index': 1408,
                                     'place_name': 'Kommandobrücke '
                                     'RVH-06'},
           'kommandozimmer von nophicas schar ': {'index': 346,
                                                  'place_name': 'Kommandozimmer '
                                                  'von '
                                                  'Nophicas '
                                                  'Schar '},
           'kompass der schwalbe': {'index': 2801,
                                    'place_name': 'Kompass der '
                                    'Schwalbe'},
           'kristallzwilling': {'index': 2982,
                                'place_name': 'Kristallzwilling'},
           'krähennest': {'index': 1803, 'place_name': 'Krähennest'},
           'ktisis hyperboreia': {'index': 3759,
                                  'place_name': 'Ktisis Hyperboreia'},
           'kugane': {'index': 2404, 'place_name': 'Kugane'},
           'kugane-brücke': {'index': 2499, 'place_name': 'Kugane-Brücke'},
           'kupferglocken-mine': {'index': 48,
                                  'place_name': 'Kupferglocken-Mine'},
           'königliche menagerie': {'index': 2709,
                                    'place_name': 'Königliche '
                                    'Menagerie'},
           'königlicher luftschiff-landeplatz': {'index': 2708,
                                                 'place_name': 'Königlicher '
                                                 'Luftschiff-Landeplatz'},
           'königlicher palast': {'index': 2294,
                                  'place_name': 'Königlicher Palast'},
           'königlicher tanzgarten': {'index': 3218,
                                      'place_name': 'Königlicher '
                                      'Tanzgarten'},
           'labyrinth der alten': {'index': 478,
                                   'place_name': 'Labyrinth der Alten'},
           'labyrinthos': {'index': 3708, 'place_name': 'Labyrinthos'},
           'last des sohnes': {'index': 1731,
                               'place_name': 'Last des Sohnes'},
           'last des vaters': {'index': 1645,
                               'place_name': 'Last des Vaters'},
           'lavendelbeete': {'index': 426, 'place_name': 'Lavendelbeete'},
           'lavendelbeete - zimmer': {'index': 1159,
                                      'place_name': 'Lavendelbeete - '
                                      'Zimmer'},
           'leichtfeder-arena': {'index': 2313,
                                 'place_name': 'Leichtfeder-Arena'},
           'leofards zimmer': {'index': 1804,
                               'place_name': 'Leofards Zimmer'},
           'lilienhügel (eingangshalle)': {'index': 1813,
                                           'place_name': 'Lilienhügel '
                                           '(Eingangshalle)'},
           'lilienhügel (wohnung)': {'index': 1814,
                                     'place_name': 'Lilienhügel '
                                     '(Wohnung)'},
           'lustiges bankett': {'index': 3696,
                                'place_name': 'Lustiges Bankett'},
           'malikahs brunnen': {'index': 3139,
                                'place_name': 'Malikahs Brunnen'},
           'manderville-tische': {'index': 2549,
                                  'place_name': 'Manderville-Tische'},
           'mare lamentorum': {'index': 3711,
                               'place_name': 'Mare Lamentorum'},
           'matoyas atelier': {'index': 3590,
                               'place_name': 'Matoyas Atelier'},
           'matoyas höhle': {'index': 2036, 'place_name': 'Matoyas Höhle'},
           'medias res': {'index': 4098, 'place_name': 'Medias Res'},
           'meteoritenkrater': {'index': 1301,
                                'place_name': 'Meteoritenkrater'},
           'mor dhona': {'index': 67, 'place_name': 'Mor Dhona'},
           'mordion-kerker': {'index': 153, 'place_name': 'Mordion-Kerker'},
           'nald-kreuzgang': {'index': 40, 'place_name': 'Nald-Kreuzgang'},
           'nanamo-windrad (eingangshalle)': {'index': 1815,
                                              'place_name': 'Nanamo-Windrad '
                                              '(Eingangshalle)'},
           'nanamo-windrad (wohnung)': {'index': 1816,
                                        'place_name': 'Nanamo-Windrad '
                                        '(Wohnung)'},
           'nebeldorf - zimmer': {'index': 1157,
                                  'place_name': 'Nebeldorf - Zimmer'},
           'nereus-graben': {'index': 3216, 'place_name': 'Nereus-Graben'},
           'nest des drachen': {'index': 2050,
                                'place_name': 'Nest des Drachen'},
           'neu-gridania': {'index': 52, 'place_name': 'Neu-Gridania'},
           'nichts-arche': {'index': 2181, 'place_name': 'Nichts-Arche'},
           'nichtssphäre': {'index': 3596, 'place_name': 'Nichtssphäre'},
           'nimmerreich': {'index': 2130, 'place_name': 'Nimmerreich'},
           'nimmerwo-garten': {'index': 3635,
                               'place_name': 'Nimmerwo-Garten'},
           'nordwald': {'index': 57, 'place_name': 'Nordwald'},
           'nördliches thanalan': {'index': 46,
                                   'place_name': 'Nördliches Thanalan'},
           'obere decks': {'index': 28, 'place_name': 'Obere Decks'},
           'obere ätheroakustische grabung': {'index': 464,
                                              'place_name': 'Obere '
                                              'ätheroakustische '
                                              'Grabung'},
           'oberes la noscea': {'index': 34,
                                'place_name': 'Oberes La Noscea'},
           'okular': {'index': 3223, 'place_name': 'Okular'},
           'omega-kontrollraum': {'index': 1887,
                                  'place_name': 'Omega-Kontrollraum'},
           'omphalos': {'index': 4031, 'place_name': 'Omphalos'},
           'onsal hakair': {'index': 3378, 'place_name': 'Onsal Hakair'},
           'opferkammer': {'index': 2083, 'place_name': 'Opferkammer'},
           'ostwald': {'index': 55, 'place_name': 'Ostwald'},
           "paglth'an": {'index': 2936, 'place_name': "Paglth'an"},
           'palast der toten': {'index': 1793,
                                'place_name': 'Palast der Toten'},
           'palast des wanderers': {'index': 37,
                                    'place_name': 'Palast des '
                                    'Wanderers'},
           'pforten des pandæmoniums': {'index': 3769,
                                        'place_name': 'Pforten des '
                                        'Pandæmoniums'},
           'pharos sirius': {'index': 230, 'place_name': 'Pharos Sirius'},
           'porta decumana': {'index': 4032,
                              'place_name': 'Porta Decumana'},
           'praetorium': {'index': 430, 'place_name': 'Praetorium'},
           'privathaus (dorf des nebels)': {'index': 1101,
                                            'place_name': 'Privathaus '
                                            '(Dorf des '
                                            'Nebels)'},
           'privathaus (empyreum)': {'index': 3690,
                                     'place_name': 'Privathaus '
                                     '(Empyreum)'},
           'privathaus (kelchkuppe)': {'index': 1104,
                                       'place_name': 'Privathaus '
                                       '(Kelchkuppe)'},
           'privathaus (lavendelbeete)': {'index': 1107,
                                          'place_name': 'Privathaus '
                                          '(Lavendelbeete)'},
           'privathaus (shirogane)': {'index': 1894,
                                      'place_name': 'Privathaus '
                                      '(Shirogane)'},
           'privathütte (dorf des nebels)': {'index': 1100,
                                             'place_name': 'Privathütte '
                                             '(Dorf des '
                                             'Nebels)'},
           'privathütte (empyreum)': {'index': 3689,
                                      'place_name': 'Privathütte '
                                      '(Empyreum)'},
           'privathütte (kelchkuppe)': {'index': 1103,
                                        'place_name': 'Privathütte '
                                        '(Kelchkuppe)'},
           'privathütte (lavendelbeete)': {'index': 1106,
                                           'place_name': 'Privathütte '
                                           '(Lavendelbeete)'},
           'privathütte (shirogane)': {'index': 1893,
                                       'place_name': 'Privathütte '
                                       '(Shirogane)'},
           'privatresidenz (dorf des nebels)': {'index': 1102,
                                                'place_name': 'Privatresidenz '
                                                '(Dorf '
                                                'des '
                                                'Nebels)'},
           'privatresidenz (empyreum)': {'index': 3691,
                                         'place_name': 'Privatresidenz '
                                         '(Empyreum)'},
           'privatresidenz (kelchkuppe)': {'index': 1105,
                                           'place_name': 'Privatresidenz '
                                           '(Kelchkuppe)'},
           'privatresidenz (lavendelbeete)': {'index': 1108,
                                              'place_name': 'Privatresidenz '
                                              '(Lavendelbeete)'},
           'privatresidenz (shirogane)': {'index': 1895,
                                          'place_name': 'Privatresidenz '
                                          '(Shirogane)'},
           'propylaion': {'index': 3926, 'place_name': 'Propylaion'},
           'psimetrie 1.0': {'index': 2725, 'place_name': 'Psimetrie 1.0'},
           'psimetrie 2.0': {'index': 2736, 'place_name': 'Psimetrie 2.0'},
           'radz-at-han': {'index': 3707, 'place_name': 'Radz-at-Han'},
           'raum der transparenz': {'index': 2715,
                                    'place_name': 'Raum der '
                                    'Transparenz'},
           'regenerationssektor rvh-06': {'index': 1407,
                                          'place_name': 'Regenerationssektor '
                                          'RVH-06'},
           'reisen-schrein': {'index': 2392,
                              'place_name': 'Reisen-Schrein'},
           'reisen-schreinweg': {'index': 2391,
                                 'place_name': 'Reisen-Schreinweg'},
           'revier des rathalos': {'index': 2448,
                                   'place_name': 'Revier des Rathalos'},
           'rhalgrs wacht': {'index': 2403, 'place_name': 'Rhalgrs Wacht'},
           'rhotano-see': {'index': 462, 'place_name': 'Rhotano-See'},
           'richtfeuer von ridorana': {'index': 2483,
                                       'place_name': 'Richtfeuer von '
                                       'Ridorana'},
           'ridorana-katarakt': {'index': 2451,
                                 'place_name': 'Ridorana-Katarakt'},
           'robbenholm': {'index': 496, 'place_name': 'Robbenholm'},
           'rubinsee': {'index': 2409, 'place_name': 'Rubinsee'},
           'ruheräume': {'index': 3818, 'place_name': 'Ruheräume'},
           'ruinen von amdapor': {'index': 128,
                                  'place_name': 'Ruinen von Amdapor'},
           'sankt endalim-theologikum': {'index': 2337,
                                         'place_name': 'Sankt '
                                         'Endalim-Theologikum'},
           'sankt mocianne-arboretum': {'index': 2034,
                                        'place_name': 'Sankt '
                                        'Mocianne-Arboretum'},
           'sastasha-höhle': {'index': 35, 'place_name': 'Sastasha-Höhle'},
           'schatzkammer': {'index': 2295, 'place_name': 'Schatzkammer'},
           'schicksalsweg': {'index': 406, 'place_name': 'Schicksalsweg'},
           'schiffbrecher-insel': {'index': 1377,
                                   'place_name': 'Schiffbrecher-Insel'},
           'schlacht um norvrandt': {'index': 3511,
                                     'place_name': 'Schlacht um '
                                     'Norvrandt'},
           'schloss kugane': {'index': 2298,
                              'place_name': 'Schloss Kugane'},
           'schneekleid': {'index': 404, 'place_name': 'Schneekleid'},
           'schwarzer hof von troia': {'index': 4180,
                                       'place_name': 'Schwarzer Hof von '
                                       'Troia'},
           'schwebende stadt nym': {'index': 2527,
                                    'place_name': 'Schwebende Stadt '
                                    'Nym'},
           'seele des schöpfers': {'index': 1853,
                                   'place_name': 'Seele des Schöpfers'},
           'seenland': {'index': 2953, 'place_name': 'Seenland'},
           'separationstrakt für pflanzliche lebensformen': {'index': 4198,
                                                             'place_name': 'Separationstrakt '
                                                             'für '
                                                             'pflanzliche '
                                                             'Lebensformen'},
           'shirogane': {'index': 2412, 'place_name': 'Shirogane'},
           'shirogane - zimmer': {'index': 2270,
                                  'place_name': 'Shirogane - Zimmer'},
           'shisui-palast': {'index': 2779, 'place_name': 'Shisui-Palast'},
           'sicherheitstrakt für toxische lebenformen': {'index': 4249,
                                                         'place_name': 'Sicherheitstrakt '
                                                         'für '
                                                         'toxische '
                                                         'Lebenformen'},
           'sigmametrie 1.0': {'index': 2717,
                               'place_name': 'Sigmametrie 1.0'},
           'sigmametrie 2.0': {'index': 2718,
                               'place_name': 'Sigmametrie 2.0'},
           'sigmametrie 3.0': {'index': 2719,
                               'place_name': 'Sigmametrie 3.0'},
           'sigmametrie 4.0': {'index': 2720,
                               'place_name': 'Sigmametrie 4.0'},
           'signalkontrollstation': {'index': 3486,
                                     'place_name': 'Signalkontrollstation'},
           'singularitäts-reaktor': {'index': 2178,
                                     'place_name': 'Singularitäts-Reaktor'},
           'sirenen-see': {'index': 2297, 'place_name': 'Sirenen-See'},
           'sitz der hohepriesterin': {'index': 4185,
                                       'place_name': 'Sitz der '
                                       'Hohepriesterin'},
           'smileton': {'index': 3770, 'place_name': 'Smileton'},
           'sohm al': {'index': 2031, 'place_name': 'Sohm Al'},
           'sohr khai': {'index': 2090, 'place_name': 'Sohr Khai'},
           'sonnenstein': {'index': 481, 'place_name': 'Sonnenstein'},
           'sonnenwind': {'index': 356, 'place_name': 'Sonnenwind'},
           'steinerne wacht': {'index': 401,
                               'place_name': 'Steinerne Wacht'},
           'stigma-4': {'index': 3783, 'place_name': 'Stigma-4'},
           'strahlenkranz der makellosigkeit': {'index': 3219,
                                                'place_name': 'Strahlenkranz '
                                                'der '
                                                'Makellosigkeit'},
           'strategieraum': {'index': 4023, 'place_name': 'Strategieraum'},
           'strebewerk': {'index': 2301, 'place_name': 'Strebewerk'},
           'sturmes krone': {'index': 4045, 'place_name': 'Sturmes Krone'},
           'syrcus-schlucht': {'index': 3221,
                               'place_name': 'Syrcus-Schlucht'},
           'syrcus-turm': {'index': 493, 'place_name': 'Syrcus-Turm'},
           'sägerschrei': {'index': 47, 'place_name': 'Sägerschrei'},
           'südliches thanalan': {'index': 45,
                                  'place_name': 'Südliches Thanalan'},
           'südwald': {'index': 56, 'place_name': 'Südwald'},
           'tausend löcher von toto-rak': {'index': 61,
                                           'place_name': 'Tausend '
                                           'Löcher von '
                                           'Toto-Rak'},
           'tempel der faust': {'index': 2707,
                                'place_name': 'Tempel der Faust'},
           'tempest': {'index': 2958, 'place_name': 'Tempest'},
           'thal-kreuzgang': {'index': 41, 'place_name': 'Thal-Kreuzgang'},
           'thavnair': {'index': 3709, 'place_name': 'Thavnair'},
           'theaterwerkstatt': {'index': 2370,
                                'place_name': 'Theaterwerkstatt'},
           'thok ast thok': {'index': 2081, 'place_name': 'Thok ast Thok'},
           'tiefer wald': {'index': 54, 'place_name': 'Tiefer Wald'},
           'tiefstes inneres': {'index': 152,
                                'place_name': 'Tiefstes Inneres'},
           'totenacker tam-tara': {'index': 58,
                                   'place_name': 'Totenacker Tam-Tara'},
           'transzendenz-laboratorium': {'index': 2296,
                                         'place_name': 'Transzendenz-Laboratorium'},
           'trister limbus': {'index': 3798,
                              'place_name': 'Trister Limbus'},
           'trockendock von castrum marinum': {'index': 3581,
                                               'place_name': 'Trockendock '
                                               'von '
                                               'Castrum '
                                               'Marinum'},
           'turm von babil': {'index': 4118,
                              'place_name': 'Turm von Babil'},
           'turm von zot': {'index': 3736, 'place_name': 'Turm von Zot'},
           'ultima thule': {'index': 3712, 'place_name': 'Ultima Thule'},
           'untere decks': {'index': 29, 'place_name': 'Untere Decks'},
           'untere ätheroakustische grabung': {'index': 465,
                                               'place_name': 'Untere '
                                               'ätheroakustische '
                                               'Grabung'},
           'unteres la noscea': {'index': 31,
                                 'place_name': 'Unteres La Noscea'},
           'urkristall': {'index': 3685, 'place_name': 'Urkristall'},
           'vanaspati': {'index': 4015, 'place_name': 'Vanaspati'},
           'verborgene schlucht': {'index': 2589,
                                   'place_name': 'Verborgene Schlucht'},
           'verbotener flügel': {'index': 4034,
                                 'place_name': 'Verbotener Flügel'},
           'verlies von eulmore': {'index': 3595,
                                   'place_name': 'Verlies von Eulmore'},
           'verliese von lyhe ghiah': {'index': 3229,
                                       'place_name': 'Verliese von Lyhe '
                                       'Ghiah'},
           'verlorene ruinen': {'index': 3542,
                                'place_name': 'Verlorene Ruinen'},
           'versteck der kürbishexe': {'index': 4040,
                                       'place_name': 'Versteck der '
                                       'Kürbishexe'},
           'versunkener tempel von qarn': {'index': 50,
                                           'place_name': 'Versunkener '
                                           'Tempel von '
                                           'Qarn'},
           'verteidigungslinie ghimlyt': {'index': 3442,
                                          'place_name': 'Verteidigungslinie '
                                          'Ghimlyt'},
           'wachstube der bruderschaft': {'index': 1800,
                                          'place_name': 'Wachstube der '
                                          'Bruderschaft'},
           'wachstube der legion': {'index': 1801,
                                    'place_name': 'Wachstube der '
                                    'Legion'},
           'wachstube des mahlstroms': {'index': 1802,
                                        'place_name': 'Wachstube des '
                                        'Mahlstroms'},
           'wallende nebel': {'index': 2002,
                              'place_name': 'Wallende Nebel'},
           'wasserrosentisch': {'index': 347,
                                'place_name': 'Wasserrosentisch'},
           'welt der dunkelheit': {'index': 1431,
                                   'place_name': 'Welt der Dunkelheit'},
           'weltensalon': {'index': 1665, 'place_name': 'Weltensalon'},
           'wendeklipp': {'index': 3571, 'place_name': 'Wendeklipp'},
           'wendeklipp-küste': {'index': 3570,
                                'place_name': 'Wendeklipp-Küste'},
           'westliches hochland von coerthas': {'index': 2200,
                                                'place_name': 'Westliches '
                                                'Hochland '
                                                'von '
                                                'Coerthas'},
           'westliches la noscea': {'index': 33,
                                    'place_name': 'Westliches La '
                                    'Noscea'},
           'westliches thanalan': {'index': 42,
                                   'place_name': 'Westliches Thanalan'},
           'wolfshöhlen-pier': {'index': 358,
                                'place_name': 'Wolfshöhlen-Pier'},
           'xelphatol': {'index': 1792, 'place_name': 'Xelphatol'},
           'yanxia': {'index': 2410, 'place_name': 'Yanxia'},
           'zadnor-hochebene': {'index': 3662,
                                'place_name': 'Zadnor-Hochebene'},
           'zentral-azys lla': {'index': 2179,
                                'place_name': 'Zentral-Azys Lla'},
           'zentrale decks': {'index': 1303,
                              'place_name': 'Zentrale Decks'},
           'zentrale decks rvh-06': {'index': 1406,
                                     'place_name': 'Zentrale Decks '
                                     'RVH-06'},
           'zentrales hochland von coerthas': {'index': 63,
                                               'place_name': 'Zentrales '
                                               'Hochland '
                                               'von '
                                               'Coerthas'},
           'zentrales la noscea': {'index': 30,
                                   'place_name': 'Zentrales La Noscea'},
           'zentrales thanalan': {'index': 43,
                                  'place_name': 'Zentrales Thanalan'},
           'zeros unterschlupf': {'index': 4038,
                                  'place_name': 'Zeros Unterschlupf'},
           'zum wolkenschäfchen': {'index': 2310,
                                   'place_name': 'Zum Wolkenschäfchen'},
           'ätherochemisches forschungslabor': {'index': 2147,
                                                'place_name': 'Ätherochemisches '
                                                'Forschungslabor'},
           'äußere ruinen': {'index': 1374, 'place_name': 'Äußere Ruinen'},
           'äußere schächte': {'index': 1302,
                               'place_name': 'Äußere Schächte'},
           'äußeres la noscea': {'index': 350,
                                 'place_name': 'Äußeres La Noscea'},
           'östliches la noscea': {'index': 32,
                                   'place_name': 'Östliches La Noscea'},
           'östliches thanalan': {'index': 44,
                                  'place_name': 'Östliches Thanalan'}},
    'en': {'aery': {'index': 2050, 'place_name': 'The Aery'},
           'aetherochemical research facility': {'index': 2147,
                                                 'place_name': 'Aetherochemical '
                                                 'Research '
                                                 'Facility'},
           'aglaia': {'index': 4167, 'place_name': 'Aglaia'},
           'aitiascope': {'index': 4146, 'place_name': 'The Aitiascope'},
           'akadaemia anyder': {'index': 3007,
                                'place_name': 'Akadaemia Anyder'},
           'akh afah amphitheatre': {'index': 1399,
                                     'place_name': 'Akh Afah '
                                     'Amphitheatre'},
           'ala mhigo': {'index': 2691, 'place_name': 'Ala Mhigo'},
           'alexander': {'index': 2041, 'place_name': 'Alexander'},
           "alzadaal's legacy": {'index': 4154,
                                 'place_name': "Alzadaal's Legacy"},
           'amaurot': {'index': 2985, 'place_name': 'Amaurot'},
           'amdapor keep': {'index': 128, 'place_name': 'Amdapor Keep'},
           'amh araeng': {'index': 2955, 'place_name': 'Amh Araeng'},
           'anamnesis anyder': {'index': 3467,
                                'place_name': 'Anamnesis Anyder'},
           'andron': {'index': 3818, 'place_name': 'Andron'},
           'antitower': {'index': 2088, 'place_name': 'The Antitower'},
           'aquapolis': {'index': 1799, 'place_name': 'The Aquapolis'},
           'arm of the father': {'index': 1638,
                                 'place_name': 'The Arm of the Father'},
           'arm of the son': {'index': 1723,
                              'place_name': 'The Arm of the Son'},
           'ashfall': {'index': 3469, 'place_name': 'Ashfall'},
           'atlas peak': {'index': 3217, 'place_name': 'Atlas Peak'},
           'aurum vale': {'index': 65, 'place_name': 'Aurum Vale'},
           'azim steppe': {'index': 2411, 'place_name': 'The Azim Steppe'},
           'azys lla': {'index': 2101, 'place_name': 'Azys Lla'},
           "baelsar's wall": {'index': 1857,
                              'place_name': "Baelsar's Wall"},
           "bardam's mettle": {'index': 2833,
                               'place_name': "Bardam's Mettle"},
           'battlehall': {'index': 1665, 'place_name': 'The Battlehall'},
           'binding coil of bahamut': {'index': 1759,
                                       'place_name': 'The Binding Coil '
                                       'of Bahamut'},
           'blessed treasury': {'index': 2295,
                                'place_name': 'The Blessed Treasury'},
           'blue sky': {'index': 2548, 'place_name': 'Blue Sky'},
           'bokairo inn': {'index': 2413, 'place_name': 'Bokairo Inn'},
           'bowl of embers': {'index': 357, 'place_name': 'Bowl of Embers'},
           'bozjan southern front': {'index': 3534,
                                     'place_name': 'Bozjan Southern '
                                     'Front'},
           "brayflox's longstop": {'index': 36,
                                   'place_name': "Brayflox's Longstop"},
           'breath of the creator': {'index': 1841,
                                     'place_name': 'Breath of the '
                                     'Creator'},
           'burden of the father': {'index': 1645,
                                    'place_name': 'The Burden of the '
                                    'Father'},
           'burden of the son': {'index': 1731,
                                 'place_name': 'The Burden of the Son'},
           'burn': {'index': 2851, 'place_name': 'The Burn'},
           'burning heart': {'index': 1409,
                             'place_name': 'The Burning Heart'},
           'bygone gaol': {'index': 3595, 'place_name': 'Bygone Gaol'},
           'carteneau flats: borderland ruins': {'index': 1374,
                                                 'place_name': 'Carteneau '
                                                 'Flats: '
                                                 'Borderland '
                                                 'Ruins'},
           'castrum abania': {'index': 2665,
                              'place_name': 'Castrum Abania'},
           'castrum fluminis': {'index': 2799,
                                'place_name': 'Castrum Fluminis'},
           'castrum marinum drydocks': {'index': 3581,
                                        'place_name': 'Castrum Marinum '
                                        'Drydocks'},
           'castrum meridianum': {'index': 260,
                                  'place_name': 'Castrum Meridianum'},
           'caustic purgatory': {'index': 4249,
                                 'place_name': 'The Caustic Purgatory'},
           'central azys lla': {'index': 2179,
                                'place_name': 'Central Azys Lla'},
           'central decks': {'index': 1303, 'place_name': 'Central Decks'},
           'central shroud': {'index': 54, 'place_name': 'Central Shroud'},
           'central thanalan': {'index': 43,
                                'place_name': 'Central Thanalan'},
           'chocobo square': {'index': 1500,
                              'place_name': 'Chocobo Square'},
           'chrysalis': {'index': 1390, 'place_name': 'The Chrysalis'},
           'churning mists': {'index': 2002,
                              'place_name': 'The Churning Mists'},
           'cinder drift': {'index': 3442, 'place_name': 'Cinder Drift'},
           'cloud nine': {'index': 2310, 'place_name': 'Cloud Nine'},
           'coerthas central highlands': {'index': 63,
                                          'place_name': 'Coerthas '
                                          'Central '
                                          'Highlands'},
           'coerthas western highlands': {'index': 2200,
                                          'place_name': 'Coerthas '
                                          'Western '
                                          'Highlands'},
           'command room': {'index': 351, 'place_name': 'Command Room'},
           'company workshop - empyreum': {'index': 3693,
                                           'place_name': 'Company '
                                           'Workshop - '
                                           'Empyreum'},
           'company workshop - mist': {'index': 1227,
                                       'place_name': 'Company Workshop '
                                       '- Mist'},
           'company workshop - shirogane': {'index': 2271,
                                            'place_name': 'Company '
                                            'Workshop - '
                                            'Shirogane'},
           'company workshop - the goblet': {'index': 1228,
                                             'place_name': 'Company '
                                             'Workshop - '
                                             'The Goblet'},
           'company workshop - the lavender beds': {'index': 1229,
                                                    'place_name': 'Company '
                                                    'Workshop '
                                                    '- '
                                                    'The '
                                                    'Lavender '
                                                    'Beds'},
           'confessional of toupasa the elder': {'index': 3228,
                                                 'place_name': 'The '
                                                 'Confessional '
                                                 'of '
                                                 'Toupasa '
                                                 'the '
                                                 'Elder'},
           'containment bay p1t6': {'index': 2265,
                                    'place_name': 'Containment Bay '
                                    'P1T6'},
           'containment bay s1t7': {'index': 2256,
                                    'place_name': 'Containment Bay '
                                    'S1T7'},
           'containment bay z1t9': {'index': 2266,
                                    'place_name': 'Containment Bay '
                                    'Z1T9'},
           'copied factory': {'index': 3425,
                              'place_name': 'The Copied Factory'},
           'copperbell mines': {'index': 48,
                                'place_name': 'Copperbell Mines'},
           'core': {'index': 3214, 'place_name': 'The Core'},
           'crown of the immaculate': {'index': 3219,
                                       'place_name': 'The Crown of the '
                                       'Immaculate'},
           'crystarium': {'index': 2951, 'place_name': 'The Crystarium'},
           'cuff of the father': {'index': 1633,
                                  'place_name': 'The Cuff of the '
                                  'Father'},
           'cuff of the son': {'index': 1714,
                               'place_name': 'The Cuff of the Son'},
           "cutter's cry": {'index': 47, 'place_name': "Cutter's Cry"},
           "dalamud's shadow": {'index': 1301,
                                'place_name': "Dalamud's Shadow"},
           'dancing plague': {'index': 3218,
                              'place_name': 'The Dancing Plague'},
           'dark inside': {'index': 3684, 'place_name': 'The Dark Inside'},
           'dead ends': {'index': 4100, 'place_name': 'The Dead Ends'},
           'deltascape v1.0': {'index': 2357,
                               'place_name': 'Deltascape V1.0'},
           'deltascape v2.0': {'index': 2358,
                               'place_name': 'Deltascape V2.0'},
           'deltascape v3.0': {'index': 2359,
                               'place_name': 'Deltascape V3.0'},
           'deltascape v4.0': {'index': 2360,
                               'place_name': 'Deltascape V4.0'},
           'delubrum reginae': {'index': 3597,
                                'place_name': 'Delubrum Reginae'},
           'diadem': {'index': 1647, 'place_name': 'The Diadem'},
           'dohn mheg': {'index': 2979, 'place_name': 'Dohn Mheg'},
           'doman enclave': {'index': 2813,
                             'place_name': 'The Doman Enclave'},
           'dravanian forelands': {'index': 2000,
                                   'place_name': 'The Dravanian '
                                   'Forelands'},
           'dravanian hinterlands': {'index': 2001,
                                     'place_name': 'The Dravanian '
                                     'Hinterlands'},
           'drowned city of skalla': {'index': 2367,
                                      'place_name': 'The Drowned City '
                                      'of Skalla'},
           'dun scaith': {'index': 1868, 'place_name': 'Dun Scaith'},
           'dungeons of lyhe ghiah': {'index': 3229,
                                      'place_name': 'The Dungeons of '
                                      'Lyhe Ghiah'},
           'dusk vigil': {'index': 2214, 'place_name': 'Dusk Vigil'},
           'dzemael darkhold': {'index': 64,
                                'place_name': 'Dzemael Darkhold'},
           'east shroud': {'index': 55, 'place_name': 'East Shroud'},
           'eastern la noscea': {'index': 32,
                                 'place_name': 'Eastern La Noscea'},
           'eastern thanalan': {'index': 44,
                                'place_name': 'Eastern Thanalan'},
           'eighteenth floor': {'index': 1660,
                                'place_name': 'The Eighteenth Floor'},
           'elpis': {'index': 3713, 'place_name': 'Elpis'},
           'emanation': {'index': 2299, 'place_name': 'Emanation'},
           'empty': {'index': 3225, 'place_name': 'The Empty'},
           'empyreum': {'index': 4139, 'place_name': 'Empyreum'},
           'endeavor': {'index': 3477, 'place_name': 'The Endeavor'},
           'eorzean alliance headquarters': {'index': 2862,
                                             'place_name': 'Eorzean '
                                             'Alliance '
                                             'Headquarters'},
           'eorzean subterrane': {'index': 152,
                                  'place_name': 'Eorzean Subterrane'},
           'eulmore': {'index': 2952, 'place_name': 'Eulmore'},
           'eureka anemos': {'index': 2414, 'place_name': 'Eureka Anemos'},
           'eureka hydatos': {'index': 2545,
                              'place_name': 'Eureka Hydatos'},
           'eureka pagos': {'index': 2462, 'place_name': 'Eureka Pagos'},
           'eureka pyros': {'index': 2530, 'place_name': 'Eureka Pyros'},
           'excavation tunnels': {'index': 3427,
                                  'place_name': 'Excavation Tunnels'},
           'excitatron 6000': {'index': 4111,
                               'place_name': 'The Excitatron 6000'},
           'eyes of the creator': {'index': 1835,
                                   'place_name': 'Eyes of the Creator'},
           "fall of belah'dia": {'index': 2498,
                                 'place_name': "The Fall of Belah'dia"},
           'falling city of nym': {'index': 2527,
                                   'place_name': 'The Falling City of '
                                   'Nym'},
           'feasting grounds': {'index': 1664,
                                'place_name': 'The Feasting Grounds'},
           'fell court of troia': {'index': 4180,
                                   'place_name': 'The Fell Court of '
                                   'Troia'},
           'fervid limbo': {'index': 3797,
                            'place_name': 'The Fervid Limbo'},
           'fields of glory': {'index': 1740,
                               'place_name': 'The Fields of Glory'},
           'final day': {'index': 3686, 'place_name': 'The Final Day'},
           'firmament': {'index': 3435, 'place_name': 'The Firmament'},
           'first altar of djanan qhat': {'index': 2339,
                                          'place_name': 'The First '
                                          'Altar of '
                                          'Djanan Qhat'},
           'fist of the father': {'index': 1628,
                                  'place_name': 'The Fist of the '
                                  'Father'},
           'fist of the son': {'index': 1708,
                               'place_name': 'The Fist of the Son'},
           'flame barracks': {'index': 1801,
                              'place_name': 'Flame Barracks'},
           'fortemps manor': {'index': 2320,
                              'place_name': 'Fortemps Manor'},
           'foundation': {'index': 2300, 'place_name': 'Foundation'},
           'fractal continuum': {'index': 2148,
                                 'place_name': 'The Fractal Continuum'},
           'fringes': {'index': 2406, 'place_name': 'The Fringes'},
           "frondale's home for friendless foundlings": {'index': 695,
                                                         'place_name': "Frondale's "
                                                         'Home '
                                                         'for '
                                                         'Friendless '
                                                         'Foundlings'},
           'g-savior deck': {'index': 3663, 'place_name': 'G-Savior Deck'},
           'gandof thunder plains': {'index': 3468,
                                     'place_name': 'The Gandof Thunder '
                                     'Plains'},
           'gangos': {'index': 3478, 'place_name': 'Gangos'},
           'garden of nowhere': {'index': 3635,
                                 'place_name': 'The Garden of Nowhere'},
           'garlemald': {'index': 3710, 'place_name': 'Garlemald'},
           'gates of pandæmonium': {'index': 3769,
                                    'place_name': 'The Gates of '
                                    'Pandæmonium'},
           'ghimlyt dark': {'index': 2586,
                            'place_name': 'The Ghimlyt Dark'},
           'goblet': {'index': 427, 'place_name': 'The Goblet'},
           'gold saucer': {'index': 1484, 'place_name': 'The Gold Saucer'},
           'grand cosmos': {'index': 3385,
                            'place_name': 'The Grand Cosmos'},
           'great glacier': {'index': 3487, 'place_name': 'Great Glacier'},
           'great gubal library': {'index': 2038,
                                   'place_name': 'The Great Gubal '
                                   'Library'},
           'great hunt': {'index': 2448, 'place_name': 'The Great Hunt'},
           'griffin crossing': {'index': 386,
                                'place_name': 'Griffin Crossing'},
           'halatali': {'index': 49, 'place_name': 'Halatali'},
           'hall of summoning': {'index': 379,
                                 'place_name': 'Hall of Summoning'},
           'hall of the bestiarii': {'index': 694,
                                     'place_name': 'Hall of the '
                                     'Bestiarii'},
           'halo': {'index': 3470, 'place_name': 'The Halo'},
           'haukke manor': {'index': 59, 'place_name': 'Haukke Manor'},
           'haunted manor': {'index': 1834, 'place_name': 'Haunted Manor'},
           'heart of the creator': {'index': 1847,
                                    'place_name': 'Heart of the '
                                    'Creator'},
           'heart of the sworn': {'index': 354,
                                  'place_name': 'Heart of the Sworn'},
           'heaven-on-high': {'index': 2775,
                              'place_name': 'Heaven-on-High'},
           "hells' kier": {'index': 2496, 'place_name': "Hells' Kier"},
           "hells' lid": {'index': 2762, 'place_name': "Hells' Lid"},
           "heroes' gauntlet": {'index': 3511,
                                'place_name': "The Heroes' Gauntlet"},
           'hidden gorge': {'index': 2589, 'place_name': 'Hidden Gorge'},
           'hollow purgatory': {'index': 4198,
                                'place_name': 'The Hollow Purgatory'},
           'holminster switch': {'index': 3050,
                                 'place_name': 'Holminster Switch'},
           'holocharts': {'index': 1304, 'place_name': 'The Holocharts'},
           'hourglass': {'index': 617, 'place_name': 'The Hourglass'},
           'house of the fierce': {'index': 2805,
                                   'place_name': 'The House of the '
                                   'Fierce'},
           'howling eye': {'index': 459, 'place_name': 'The Howling Eye'},
           'hullbreaker isle': {'index': 1377,
                                'place_name': 'Hullbreaker Isle'},
           'ic-04 main bridge': {'index': 1410,
                                 'place_name': 'IC-04 Main Bridge'},
           'ic-06 central decks': {'index': 1406,
                                   'place_name': 'IC-06 Central Decks'},
           'ic-06 main bridge': {'index': 1408,
                                 'place_name': 'IC-06 Main Bridge'},
           'ic-06 regeneration grid': {'index': 1407,
                                       'place_name': 'IC-06 '
                                       'Regeneration '
                                       'Grid'},
           'idyllshire': {'index': 2082, 'place_name': 'Idyllshire'},
           'il mheg': {'index': 2956, 'place_name': 'Il Mheg'},
           'ingleside apartment': {'index': 3695,
                                   'place_name': 'Ingleside Apartment'},
           'ingleside apartment lobby': {'index': 3694,
                                         'place_name': 'Ingleside '
                                         'Apartment '
                                         'Lobby'},
           'intercessory': {'index': 1429, 'place_name': 'Intercessory'},
           'interdimensional rift': {'index': 2737,
                                     'place_name': 'The '
                                     'Interdimensional '
                                     'Rift'},
           'jade stoa': {'index': 2354, 'place_name': 'The Jade Stoa'},
           'keeper of the lake': {'index': 418,
                                  'place_name': 'The Keeper of the '
                                  'Lake'},
           'kholusia': {'index': 2954, 'place_name': 'Kholusia'},
           'kienkan': {'index': 2847, 'place_name': 'Kienkan'},
           'kobai goten apartment': {'index': 2273,
                                     'place_name': 'Kobai Goten '
                                     'Apartment'},
           'kobai goten apartment lobby': {'index': 2272,
                                           'place_name': 'Kobai Goten '
                                           'Apartment '
                                           'Lobby'},
           'ktisis hyperboreia': {'index': 3759,
                                  'place_name': 'Ktisis Hyperboreia'},
           'kugane': {'index': 2404, 'place_name': 'Kugane'},
           'kugane castle': {'index': 2298, 'place_name': 'Kugane Castle'},
           'kugane ohashi': {'index': 2499, 'place_name': 'Kugane Ohashi'},
           'labyrinth of the ancients': {'index': 478,
                                         'place_name': 'Labyrinth of '
                                         'the Ancients'},
           'labyrinthos': {'index': 3708, 'place_name': 'Labyrinthos'},
           'lakeland': {'index': 2953, 'place_name': 'Lakeland'},
           'last trace': {'index': 3542, 'place_name': 'The Last Trace'},
           'lavender beds': {'index': 426,
                             'place_name': 'The Lavender Beds'},
           'laxan loft': {'index': 3620, 'place_name': 'Laxan Loft'},
           'lemures headquarters': {'index': 4022,
                                    'place_name': 'Lemures '
                                    'Headquarters'},
           "leofard's chambers": {'index': 1804,
                                  'place_name': "Leofard's Chambers"},
           'lightfeather proving grounds': {'index': 2313,
                                            'place_name': 'The '
                                            'Lightfeather '
                                            'Proving '
                                            'Grounds'},
           'lily hills apartment': {'index': 1814,
                                    'place_name': 'Lily Hills '
                                    'Apartment'},
           'lily hills apartment lobby': {'index': 1813,
                                          'place_name': 'Lily Hills '
                                          'Apartment '
                                          'Lobby'},
           'liminal space': {'index': 3017, 'place_name': 'Liminal Space'},
           'limitless blue': {'index': 2151,
                              'place_name': 'The Limitless Blue'},
           'limsa lominsa lower decks': {'index': 29,
                                         'place_name': 'Limsa Lominsa '
                                         'Lower Decks'},
           'limsa lominsa upper decks': {'index': 28,
                                         'place_name': 'Limsa Lominsa '
                                         'Upper Decks'},
           'lochs': {'index': 2408, 'place_name': 'The Lochs'},
           'lost canals of uznair': {'index': 2340,
                                     'place_name': 'The Lost Canals of '
                                     'Uznair'},
           'lost city of amdapor': {'index': 125,
                                    'place_name': 'The Lost City of '
                                    'Amdapor'},
           'lotus stand': {'index': 347, 'place_name': 'Lotus Stand'},
           'lower aetheroacoustic exploratory site': {'index': 465,
                                                      'place_name': 'Lower '
                                                      'Aetheroacoustic '
                                                      'Exploratory '
                                                      'Site'},
           'lower la noscea': {'index': 31,
                               'place_name': 'Lower La Noscea'},
           'maelstrom barracks': {'index': 1802,
                                  'place_name': 'Maelstrom Barracks'},
           'main bridge': {'index': 1305, 'place_name': 'Main Bridge'},
           'main hall': {'index': 3817, 'place_name': 'Main Hall'},
           "malikah's well": {'index': 3139,
                              'place_name': "Malikah's Well"},
           'manderville tables': {'index': 2549,
                                  'place_name': 'The Manderville '
                                  'Tables'},
           'mare lamentorum': {'index': 3711,
                               'place_name': 'Mare Lamentorum'},
           "matoya's cave": {'index': 2036, 'place_name': "Matoya's Cave"},
           "matoya's relict": {'index': 3590,
                               'place_name': "Matoya's Relict"},
           'medias res': {'index': 4098, 'place_name': 'Medias Res'},
           'meghaduta guest chambers': {'index': 4039,
                                        'place_name': 'Meghaduta Guest '
                                        'Chambers'},
           'middle la noscea': {'index': 30,
                                'place_name': 'Middle La Noscea'},
           'misery': {'index': 1960, 'place_name': 'The Misery'},
           'mist': {'index': 425, 'place_name': 'Mist'},
           'mizzenmast inn': {'index': 733, 'place_name': 'Mizzenmast Inn'},
           'mor dhona': {'index': 67, 'place_name': 'Mor Dhona'},
           'mordion gaol': {'index': 153, 'place_name': 'Mordion Gaol'},
           'mothercrystal': {'index': 3685,
                             'place_name': 'The Mothercrystal'},
           'mt. gulg': {'index': 2997, 'place_name': 'Mt. Gulg'},
           'navel': {'index': 359, 'place_name': 'The Navel'},
           'nereus trench': {'index': 3216,
                             'place_name': 'The Nereus Trench'},
           'nethergate': {'index': 4024, 'place_name': 'The Nethergate'},
           'neverreap': {'index': 2130, 'place_name': 'Neverreap'},
           'new gridania': {'index': 52, 'place_name': 'New Gridania'},
           'north shroud': {'index': 57, 'place_name': 'North Shroud'},
           'northern thanalan': {'index': 46,
                                 'place_name': 'Northern Thanalan'},
           'ocular': {'index': 3223, 'place_name': 'The Ocular'},
           'old gridania': {'index': 53, 'place_name': 'Old Gridania'},
           'old sharlayan': {'index': 3706, 'place_name': 'Old Sharlayan'},
           'omega control': {'index': 1887, 'place_name': 'Omega Control'},
           'omphalos': {'index': 4031, 'place_name': 'The Omphalos'},
           'onsal hakair': {'index': 3378, 'place_name': 'Onsal Hakair'},
           'orbonne monastery': {'index': 2864,
                                 'place_name': 'The Orbonne Monastery'},
           'outer coil': {'index': 1302, 'place_name': 'The Outer Coil'},
           'outer la noscea': {'index': 350,
                               'place_name': 'Outer La Noscea'},
           "paglth'an": {'index': 2936, 'place_name': "Paglth'an"},
           'palace of the dead': {'index': 1793,
                                  'place_name': 'The Palace of the '
                                  'Dead'},
           'parrock': {'index': 1803, 'place_name': 'The Parrock'},
           'peaks': {'index': 2407, 'place_name': 'The Peaks'},
           'pendants personal suite': {'index': 3222,
                                       'place_name': 'The Pendants '
                                       'Personal Suite'},
           'pestilent purgatory': {'index': 4196,
                                   'place_name': 'The Pestilent '
                                   'Purgatory'},
           "phantoms' feast": {'index': 3696,
                               'place_name': "The Phantoms' Feast"},
           'pharos sirius': {'index': 230, 'place_name': 'Pharos Sirius'},
           'pillars': {'index': 2301, 'place_name': 'The Pillars'},
           'porta decumana': {'index': 4032,
                              'place_name': 'The Porta Decumana'},
           'praetorium': {'index': 430, 'place_name': 'The Praetorium'},
           'prima vista bridge': {'index': 2371,
                                  'place_name': 'The Prima Vista '
                                  'Bridge'},
           'prima vista tiring room': {'index': 2370,
                                       'place_name': 'The Prima Vista '
                                       'Tiring Room'},
           'private chambers - empyreum': {'index': 3692,
                                           'place_name': 'Private '
                                           'Chambers - '
                                           'Empyreum'},
           'private chambers - mist': {'index': 1157,
                                       'place_name': 'Private Chambers '
                                       '- Mist'},
           'private chambers - shirogane': {'index': 2270,
                                            'place_name': 'Private '
                                            'Chambers - '
                                            'Shirogane'},
           'private chambers - the goblet': {'index': 1158,
                                             'place_name': 'Private '
                                             'Chambers - '
                                             'The Goblet'},
           'private chambers - the lavender beds': {'index': 1159,
                                                    'place_name': 'Private '
                                                    'Chambers '
                                                    '- '
                                                    'The '
                                                    'Lavender '
                                                    'Beds'},
           'private cottage - empyreum': {'index': 3689,
                                          'place_name': 'Private '
                                          'Cottage - '
                                          'Empyreum'},
           'private cottage - mist': {'index': 1100,
                                      'place_name': 'Private Cottage - '
                                      'Mist'},
           'private cottage - shirogane': {'index': 1893,
                                           'place_name': 'Private '
                                           'Cottage - '
                                           'Shirogane'},
           'private cottage - the goblet': {'index': 1103,
                                            'place_name': 'Private '
                                            'Cottage - '
                                            'The Goblet'},
           'private cottage - the lavender beds': {'index': 1106,
                                                   'place_name': 'Private '
                                                   'Cottage '
                                                   '- The '
                                                   'Lavender '
                                                   'Beds'},
           'private house - empyreum': {'index': 3690,
                                        'place_name': 'Private House - '
                                        'Empyreum'},
           'private house - mist': {'index': 1101,
                                    'place_name': 'Private House - '
                                    'Mist'},
           'private house - shirogane': {'index': 1894,
                                         'place_name': 'Private House - '
                                         'Shirogane'},
           'private house - the goblet': {'index': 1104,
                                          'place_name': 'Private House '
                                          '- The Goblet'},
           'private house - the lavender beds': {'index': 1107,
                                                 'place_name': 'Private '
                                                 'House - '
                                                 'The '
                                                 'Lavender '
                                                 'Beds'},
           'private mansion - empyreum': {'index': 3691,
                                          'place_name': 'Private '
                                          'Mansion - '
                                          'Empyreum'},
           'private mansion - mist': {'index': 1102,
                                      'place_name': 'Private Mansion - '
                                      'Mist'},
           'private mansion - shirogane': {'index': 1895,
                                           'place_name': 'Private '
                                           'Mansion - '
                                           'Shirogane'},
           'private mansion - the goblet': {'index': 1105,
                                            'place_name': 'Private '
                                            'Mansion - '
                                            'The Goblet'},
           'private mansion - the lavender beds': {'index': 1108,
                                                   'place_name': 'Private '
                                                   'Mansion '
                                                   '- The '
                                                   'Lavender '
                                                   'Beds'},
           'propylaion': {'index': 3926, 'place_name': 'Propylaion'},
           'psiscape v1.0': {'index': 2725, 'place_name': 'Psiscape V1.0'},
           'psiscape v2.0': {'index': 2736, 'place_name': 'Psiscape V2.0'},
           "puppets' bunker": {'index': 3576,
                               'place_name': "The Puppets' Bunker"},
           'qitana ravel': {'index': 3018,
                            'place_name': 'The Qitana Ravel'},
           'radz-at-han': {'index': 3707, 'place_name': 'Radz-at-Han'},
           'ragnarok': {'index': 466, 'place_name': 'The Ragnarok'},
           'ragnarok central core': {'index': 468,
                                     'place_name': 'Ragnarok Central '
                                     'Core'},
           'ragnarok drive cylinder': {'index': 467,
                                       'place_name': 'Ragnarok Drive '
                                       'Cylinder'},
           'ragnarok main bridge': {'index': 469,
                                    'place_name': 'Ragnarok Main '
                                    'Bridge'},
           "rak'tika greatwood": {'index': 2957,
                                  'place_name': "The Rak'tika "
                                  'Greatwood'},
           'reisen temple': {'index': 2392, 'place_name': 'Reisen Temple'},
           'reisen temple road': {'index': 2391,
                                  'place_name': 'Reisen Temple Road'},
           'resonatorium': {'index': 2296,
                            'place_name': 'The Resonatorium'},
           'restricted archives': {'index': 4034,
                                   'place_name': 'Restricted Archives'},
           "rhalgr's reach": {'index': 2403,
                              'place_name': "Rhalgr's Reach"},
           'rhotano sea': {'index': 462, 'place_name': 'Rhotano Sea'},
           'ridorana cataract': {'index': 2451,
                                 'place_name': 'The Ridorana Cataract'},
           'ridorana lighthouse': {'index': 2483,
                                   'place_name': 'The Ridorana '
                                   'Lighthouse'},
           'rising stones': {'index': 481,
                             'place_name': 'The Rising Stones'},
           'roost': {'index': 548, 'place_name': 'The Roost'},
           'royal airship landing': {'index': 2708,
                                     'place_name': 'The Royal Airship '
                                     'Landing'},
           'royal city of rabanastre': {'index': 2372,
                                        'place_name': 'The Royal City '
                                        'of Rabanastre'},
           'royal menagerie': {'index': 2709,
                               'place_name': 'The Royal Menagerie'},
           'royal palace': {'index': 2294, 'place_name': 'Royal Palace'},
           'ruby bazaar offices': {'index': 2927,
                                   'place_name': 'Ruby Bazaar Offices'},
           'ruby sea': {'index': 2409, 'place_name': 'The Ruby Sea'},
           'ruling chamber': {'index': 2336,
                              'place_name': 'Ruling Chamber'},
           'sacrificial chamber': {'index': 2083,
                                   'place_name': 'Sacrificial Chamber'},
           "saint endalim's scholasticate": {'index': 2337,
                                             'place_name': 'Saint '
                                             "Endalim's "
                                             'Scholasticate'},
           "saint mocianne's arboretum": {'index': 2034,
                                          'place_name': 'Saint '
                                          "Mocianne's "
                                          'Arboretum'},
           'sanctum of the twelve': {'index': 112,
                                     'place_name': 'Sanctum of the '
                                     'Twelve'},
           'sanguine limbo': {'index': 4135,
                              'place_name': 'The Sanguine Limbo'},
           'sastasha': {'index': 35, 'place_name': 'Sastasha'},
           'sea of clouds': {'index': 2100,
                             'place_name': 'The Sea of Clouds'},
           'seal rock': {'index': 496, 'place_name': 'Seal Rock'},
           'seat of sacrifice': {'index': 3568,
                                 'place_name': 'The Seat of Sacrifice'},
           'seat of the first bow': {'index': 346,
                                     'place_name': 'Seat of the First '
                                     'Bow'},
           'seat of the foremost': {'index': 4185,
                                    'place_name': 'Seat of the '
                                    'Foremost'},
           'seat of the lord commander': {'index': 2335,
                                          'place_name': 'Seat of the '
                                          'Lord '
                                          'Commander'},
           'shifting altars of uznair': {'index': 2485,
                                         'place_name': 'The Shifting '
                                         'Altars of '
                                         'Uznair'},
           'shifting oubliettes of lyhe ghiah': {'index': 3644,
                                                 'place_name': 'The '
                                                 'Shifting '
                                                 'Oubliettes '
                                                 'of Lyhe '
                                                 'Ghiah'},
           'shirogane': {'index': 2412, 'place_name': 'Shirogane'},
           'shisui of the violet tides': {'index': 2779,
                                          'place_name': 'Shisui of the '
                                          'Violet Tides'},
           'sigmascape v1.0': {'index': 2717,
                               'place_name': 'Sigmascape V1.0'},
           'sigmascape v2.0': {'index': 2718,
                               'place_name': 'Sigmascape V2.0'},
           'sigmascape v3.0': {'index': 2719,
                               'place_name': 'Sigmascape V3.0'},
           'sigmascape v4.0': {'index': 2720,
                               'place_name': 'Sigmascape V4.0'},
           'singularity reactor': {'index': 2178,
                                   'place_name': 'Singularity Reactor'},
           'sirensong sea': {'index': 2297,
                             'place_name': 'The Sirensong Sea'},
           'smileton': {'index': 3770, 'place_name': 'Smileton'},
           'sneaky hollow': {'index': 4040, 'place_name': 'Sneaky Hollow'},
           'snowcloak': {'index': 404, 'place_name': 'Snowcloak'},
           'sohm al': {'index': 2031, 'place_name': 'Sohm Al'},
           'sohr khai': {'index': 2090, 'place_name': 'Sohr Khai'},
           'soul of the creator': {'index': 1853,
                                   'place_name': 'Soul of the Creator'},
           'south shroud': {'index': 56, 'place_name': 'South Shroud'},
           'southern thanalan': {'index': 45,
                                 'place_name': 'Southern Thanalan'},
           'sphere of naught': {'index': 3596,
                                'place_name': 'Sphere of Naught'},
           'stagnant limbo': {'index': 3798,
                              'place_name': 'The Stagnant Limbo'},
           'steps of faith': {'index': 406, 'place_name': 'Steps of Faith'},
           'stigma dreamscape': {'index': 3783,
                                 'place_name': 'The Stigma Dreamscape'},
           'stone vigil': {'index': 401, 'place_name': 'Stone Vigil'},
           "storm's crown": {'index': 4045, 'place_name': "Storm's Crown"},
           'strategy room': {'index': 4023, 'place_name': 'Strategy Room'},
           'striking tree': {'index': 1363,
                             'place_name': 'The Striking Tree'},
           'stygian insenescence cells': {'index': 4250,
                                          'place_name': 'Stygian '
                                          'Insenescence '
                                          'Cells'},
           "sultana's breath apartment": {'index': 1816,
                                          'place_name': "Sultana's "
                                          'Breath '
                                          'Apartment'},
           "sultana's breath apartment lobby": {'index': 1815,
                                                'place_name': "Sultana's "
                                                'Breath '
                                                'Apartment '
                                                'Lobby'},
           'sunken temple of qarn': {'index': 50,
                                     'place_name': 'The Sunken Temple '
                                     'of Qarn'},
           "swallow's compass": {'index': 2801,
                                 'place_name': "The Swallow's Compass"},
           'syrcus tower': {'index': 493, 'place_name': 'Syrcus Tower'},
           'syrcus trench': {'index': 3221,
                             'place_name': 'The Syrcus Trench'},
           'tam-tara deepcroft': {'index': 58,
                                  'place_name': 'The Tam-Tara '
                                  'Deepcroft'},
           'tempest': {'index': 2958, 'place_name': 'The Tempest'},
           'temple of the fist': {'index': 2707,
                                  'place_name': 'The Temple of the '
                                  'Fist'},
           'terncliff': {'index': 3571, 'place_name': 'Terncliff'},
           'terncliff bay': {'index': 3570, 'place_name': 'Terncliff Bay'},
           'thavnair': {'index': 3709, 'place_name': 'Thavnair'},
           'thok ast thok': {'index': 2081, 'place_name': 'Thok ast Thok'},
           'thornmarch': {'index': 360, 'place_name': 'Thornmarch'},
           'thousand maws of toto-rak': {'index': 61,
                                         'place_name': 'The Thousand '
                                         'Maws of '
                                         'Toto-Rak'},
           'topmast apartment': {'index': 1812,
                                 'place_name': 'Topmast Apartment'},
           'topmast apartment lobby': {'index': 1811,
                                       'place_name': 'Topmast Apartment '
                                       'Lobby'},
           "tower at paradigm's breach": {'index': 3647,
                                          'place_name': 'The Tower at '
                                          "Paradigm's "
                                          'Breach'},
           'tower of babil': {'index': 4118,
                              'place_name': 'The Tower of Babil'},
           'tower of zot': {'index': 3736,
                            'place_name': 'The Tower of Zot'},
           'transmission control': {'index': 3486,
                                    'place_name': 'Transmission '
                                    'Control'},
           'transparency': {'index': 2715, 'place_name': 'Transparency'},
           "trial's threshold": {'index': 3471,
                                 'place_name': "Trial's Threshold"},
           'twin adder barracks': {'index': 1800,
                                   'place_name': 'Twin Adder Barracks'},
           'twinning': {'index': 2982, 'place_name': 'The Twinning'},
           "ul'dah - steps of nald": {'index': 40,
                                      'place_name': "Ul'dah - Steps of "
                                      'Nald'},
           "ul'dah - steps of thal": {'index': 41,
                                      'place_name': "Ul'dah - Steps of "
                                      'Thal'},
           'ultima thule': {'index': 3712, 'place_name': 'Ultima Thule'},
           'ultimacy': {'index': 2449, 'place_name': 'Ultimacy'},
           'unnamed island': {'index': 4043,
                              'place_name': 'Unnamed Island'},
           'upper aetheroacoustic exploratory site': {'index': 464,
                                                      'place_name': 'Upper '
                                                      'Aetheroacoustic '
                                                      'Exploratory '
                                                      'Site'},
           'upper la noscea': {'index': 34,
                               'place_name': 'Upper La Noscea'},
           'vanaspati': {'index': 4015, 'place_name': 'Vanaspati'},
           'vault': {'index': 2327, 'place_name': 'The Vault'},
           'void ark': {'index': 2181, 'place_name': 'Void Ark'},
           'waking sands': {'index': 356, 'place_name': 'The Waking Sands'},
           "wanderer's palace": {'index': 37,
                                 'place_name': "The Wanderer's Palace"},
           'weeping city of mhach': {'index': 1742,
                                     'place_name': 'The Weeping City of '
                                     'Mhach'},
           'weeping saint': {'index': 392,
                             'place_name': 'The Weeping Saint'},
           'western la noscea': {'index': 33,
                                 'place_name': 'Western La Noscea'},
           'western thanalan': {'index': 42,
                                'place_name': 'Western Thanalan'},
           'whorleater': {'index': 1334, 'place_name': 'The Whorleater'},
           "wolves' den pier": {'index': 358,
                                'place_name': "Wolves' Den Pier"},
           'world of darkness': {'index': 1431,
                                 'place_name': 'The World of Darkness'},
           'wreath of snakes': {'index': 2510,
                                'place_name': 'The Wreath of Snakes'},
           'xelphatol': {'index': 1792, 'place_name': 'Xelphatol'},
           'yanxia': {'index': 2410, 'place_name': 'Yanxia'},
           'zadnor': {'index': 3662, 'place_name': 'Zadnor'},
           "zero's domain": {'index': 4038, 'place_name': "Zero's Domain"}},
    'fr': {'abîme infini de bahamut': {'index': 1759,
                                       'place_name': 'Abîme infini de '
                                       'Bahamut'},
           'akadaemia anydre': {'index': 3007,
                                'place_name': 'Akadaemia Anydre'},
           'ala mhigo': {'index': 2691, 'place_name': 'Ala Mhigo'},
           'alexander': {'index': 2041, 'place_name': 'Alexander'},
           'amaurote': {'index': 2985, 'place_name': 'Amaurote'},
           'amh araeng': {'index': 2955, 'place_name': 'Amh Araeng'},
           "amphithéâtre d'akh afah": {'index': 1399,
                                       'place_name': 'Amphithéâtre '
                                       "d'Akh Afah"},
           'anamnesis anydre': {'index': 3467,
                                'place_name': 'Anamnesis Anydre'},
           "antichambre de l'épreuve": {'index': 3471,
                                        'place_name': 'Antichambre de '
                                        "l'épreuve"},
           'appartements du palais du meghaduta': {'index': 4039,
                                                   'place_name': 'Appartements '
                                                   'du '
                                                   'palais '
                                                   'du '
                                                   'Meghaduta'},
           'aquapole': {'index': 1799, 'place_name': 'Aquapole'},
           'arboretum sainte-mocianne': {'index': 2034,
                                         'place_name': 'Arboretum '
                                         'Sainte-Mocianne'},
           'arbre du jugement': {'index': 1363,
                                 'place_name': 'Arbre du jugement'},
           'arche du néant': {'index': 2181,
                              'place_name': 'Arche du néant'},
           'archives interdites du noumène': {'index': 4034,
                                              'place_name': 'Archives '
                                              'interdites '
                                              'du '
                                              'Noumène'},
           'arrière-pays dravanien': {'index': 2001,
                                      'place_name': 'Arrière-pays '
                                      'dravanien'},
           'arène triple triade': {'index': 1665,
                                   'place_name': 'Arène Triple Triade'},
           'atelier abandonné de matoya': {'index': 3590,
                                           'place_name': 'Atelier '
                                           'abandonné de '
                                           'Matoya'},
           'atelier de compagnie - brumée': {'index': 1227,
                                             'place_name': 'Atelier de '
                                             'compagnie - '
                                             'Brumée'},
           'atelier de compagnie - empyrée': {'index': 3693,
                                              'place_name': 'Atelier de '
                                              'compagnie '
                                              '- Empyrée'},
           'atelier de compagnie - la coupe': {'index': 1228,
                                               'place_name': 'Atelier '
                                               'de '
                                               'compagnie '
                                               '- La '
                                               'Coupe'},
           'atelier de compagnie - lavandière': {'index': 1229,
                                                 'place_name': 'Atelier '
                                                 'de '
                                                 'compagnie '
                                                 '- '
                                                 'Lavandière'},
           'atelier de compagnie - shirogane': {'index': 2271,
                                                'place_name': 'Atelier '
                                                'de '
                                                'compagnie '
                                                '- '
                                                'Shirogane'},
           "auberge de l'artimon": {'index': 733,
                                    'place_name': 'Auberge de '
                                    "L'Artimon"},
           'auberge du bokairo': {'index': 2413,
                                  'place_name': 'Auberge du Bokairo'},
           'avancée de la foi': {'index': 406,
                                 'place_name': 'Avancée de la Foi'},
           'avant-pays dravanien': {'index': 2000,
                                    'place_name': 'Avant-pays '
                                    'dravanien'},
           'azurée': {'index': 3435, 'place_name': 'Azurée'},
           'azys lla': {'index': 2101, 'place_name': 'Azys Lla'},
           'aérodrome royal': {'index': 2708,
                               'place_name': 'Aérodrome royal'},
           'banquet cauchemardesque': {'index': 3696,
                                       'place_name': 'Banquet '
                                       'cauchemardesque'},
           'base militaire des pantins': {'index': 3576,
                                          'place_name': 'Base militaire '
                                          'des Pantins'},
           'basse-noscea': {'index': 31, 'place_name': 'Basse-Noscea'},
           'bassin cendreux': {'index': 3469,
                               'place_name': 'Bassin cendreux'},
           'bivouac de brayflox': {'index': 36,
                                   'place_name': 'Bivouac de Brayflox'},
           'bloc des créations arborescentes': {'index': 4198,
                                                'place_name': 'Bloc des '
                                                'créations '
                                                'arborescentes'},
           'bloc des créatures extrêmement nocives': {'index': 4249,
                                                      'place_name': 'Bloc '
                                                      'des '
                                                      'créatures '
                                                      'extrêmement '
                                                      'nocives'},
           'bloc des organismes parasites': {'index': 4196,
                                             'place_name': 'Bloc des '
                                             'organismes '
                                             'parasites'},
           'briseur de marées': {'index': 1334,
                                 'place_name': 'Briseur de marées'},
           'brumée': {'index': 425, 'place_name': 'Brumée'},
           'cabine de leofard': {'index': 1804,
                                 'place_name': 'Cabine de Leofard'},
           'cale sèche de castrum marinum': {'index': 3581,
                                             'place_name': 'Cale sèche '
                                             'de Castrum '
                                             'Marinum'},
           "canaux perdus d'uznair": {'index': 2340,
                                      'place_name': 'Canaux perdus '
                                      "d'Uznair"},
           'carrière de lesteplume': {'index': 2313,
                                      'place_name': 'Carrière de '
                                      'Lesteplume'},
           "caserne de l'ordre des deux vipères": {'index': 1800,
                                                   'place_name': 'Caserne '
                                                   'de '
                                                   "l'ordre "
                                                   'des '
                                                   'Deux '
                                                   'Vipères'},
           'caserne des immortels': {'index': 1801,
                                     'place_name': 'Caserne des '
                                     'Immortels'},
           'caserne du maelstrom': {'index': 1802,
                                    'place_name': 'Caserne du '
                                    'Maelstrom'},
           'castrum abania': {'index': 2665,
                              'place_name': 'Castrum Abania'},
           'castrum fluminis': {'index': 2799,
                                'place_name': 'Castrum Fluminis'},
           'castrum meridianum': {'index': 260,
                                  'place_name': 'Castrum Meridianum'},
           'cataractes de ridorana': {'index': 2451,
                                      'place_name': 'Cataractes de '
                                      'Ridorana'},
           'caverne de matoya': {'index': 2036,
                                 'place_name': 'Caverne de Matoya'},
           'cercle des intrépides': {'index': 2805,
                                     'place_name': 'Cercle des '
                                     'Intrépides'},
           'chaire du lotus': {'index': 347,
                               'place_name': 'Chaire du Lotus'},
           'chambre individuelle - brumée': {'index': 1157,
                                             'place_name': 'Chambre '
                                             'individuelle '
                                             '- Brumée'},
           'chambre individuelle - empyrée': {'index': 3692,
                                              'place_name': 'Chambre '
                                              'individuelle '
                                              '- Empyrée'},
           'chambre individuelle - la coupe': {'index': 1158,
                                               'place_name': 'Chambre '
                                               'individuelle '
                                               '- La '
                                               'Coupe'},
           'chambre individuelle - lavandière': {'index': 1159,
                                                 'place_name': 'Chambre '
                                                 'individuelle '
                                                 '- '
                                                 'Lavandière'},
           'chambre individuelle - shirogane': {'index': 2270,
                                                'place_name': 'Chambre '
                                                'individuelle '
                                                '- '
                                                'Shirogane'},
           'chambre à coucher': {'index': 3818,
                                 'place_name': 'Chambre à coucher'},
           'champs de la gloire': {'index': 1740,
                                   'place_name': 'Champs de la Gloire'},
           'chemin du sanctuaire reisen': {'index': 2391,
                                           'place_name': 'Chemin du '
                                           'sanctuaire '
                                           'Reisen'},
           "chutes de belah'dia": {'index': 2498,
                                   'place_name': "Chutes de Belah'dia"},
           "château d'amdapor": {'index': 128,
                                 'place_name': "Château d'Amdapor"},
           'château de ganlag': {'index': 3620,
                                 'place_name': 'Château de Ganlag'},
           'château de kugane': {'index': 2298,
                                 'place_name': 'Château de Kugane'},
           'château de troïa': {'index': 4180,
                                'place_name': 'Château de Troïa'},
           'ciel azur': {'index': 2548, 'place_name': 'Ciel azur'},
           'cité croulante de nym': {'index': 2527,
                                     'place_name': 'Cité croulante de '
                                     'Nym'},
           'cité défendue de mhach': {'index': 1742,
                                      'place_name': 'Cité défendue de '
                                      'Mhach'},
           'cité engloutie de skalla': {'index': 2367,
                                        'place_name': 'Cité engloutie '
                                        'de Skalla'},
           'cité royale de rabanastre': {'index': 2372,
                                         'place_name': 'Cité royale de '
                                         'Rabanastre'},
           'clairière de jade': {'index': 2354,
                                 'place_name': 'Clairière de Jade'},
           "clinique pédiatrique de l'académie médicale de frondale": {'index': 695,
                                                                       'place_name': 'Clinique '
                                                                       'pédiatrique '
                                                                       'de '
                                                                       "l'Académie "
                                                                       'médicale '
                                                                       'de '
                                                                       'Frondale'},
           "compas de l'hirondelle": {'index': 2801,
                                      'place_name': 'Compas de '
                                      "l'Hirondelle"},
           "confessionnal de toupasa l'ancien": {'index': 3228,
                                                 'place_name': 'Confessionnal '
                                                 'de '
                                                 'Toupasa '
                                                 "l'ancien"},
           'cosmos coruscant': {'index': 3385,
                                'place_name': 'Cosmos coruscant'},
           "couronne de l'immaculé": {'index': 3219,
                                      'place_name': 'Couronne de '
                                      "l'Immaculé"},
           'couvercle des enfers': {'index': 2762,
                                    'place_name': 'Couvercle des '
                                    'enfers'},
           'cratère des tisons': {'index': 357,
                                  'place_name': 'Cratère des tisons'},
           'crique aux tributs': {'index': 2295,
                                  'place_name': 'Crique aux tributs'},
           'cristal-mère': {'index': 3685, 'place_name': 'Cristal-mère'},
           'cristarium': {'index': 2951, 'place_name': 'Cristarium'},
           'cylindre propulseur du ragnarok': {'index': 467,
                                               'place_name': 'Cylindre '
                                               'propulseur '
                                               'du '
                                               'Ragnarok'},
           "cœur d'azys lla": {'index': 2179,
                               'place_name': "Cœur d'Azys Lla"},
           "cœur d'éden": {'index': 3214, 'place_name': "Cœur d'Éden"},
           'cœur de bahamut': {'index': 1409,
                               'place_name': 'Cœur de Bahamut'},
           'deltastice v1.0': {'index': 2357,
                               'place_name': 'Deltastice v1.0'},
           'deltastice v2.0': {'index': 2358,
                               'place_name': 'Deltastice v2.0'},
           'deltastice v3.0': {'index': 2359,
                               'place_name': 'Deltastice v3.0'},
           'deltastice v4.0': {'index': 2360,
                               'place_name': 'Deltastice v4.0'},
           'delubrum reginae': {'index': 3597,
                                'place_name': 'Delubrum Reginae'},
           'demeure de la femme à tête de citrouille': {'index': 4040,
                                                        'place_name': 'Demeure '
                                                        'de '
                                                        'la '
                                                        'femme '
                                                        'à '
                                                        'tête '
                                                        'de '
                                                        'citrouille'},
           'dohn mheg': {'index': 2979, 'place_name': 'Dohn Mheg'},
           'domaine divin - aglaé': {'index': 4167,
                                     'place_name': 'Domaine divin - '
                                     'Aglaé'},
           'domaine du roi des cieux': {'index': 2448,
                                        'place_name': 'Domaine du roi '
                                        'des cieux'},
           'donjon hypogéen du lyhe ghiah': {'index': 3229,
                                             'place_name': 'Donjon '
                                             'hypogéen du '
                                             'Lyhe Ghiah'},
           'dun scaith': {'index': 1868, 'place_name': 'Dun Scaith'},
           'dédale antique': {'index': 478, 'place_name': 'Dédale antique'},
           'elpis': {'index': 3713, 'place_name': 'Elpis'},
           'empyrée': {'index': 4139, 'place_name': 'Empyrée'},
           'enchevêtrement des qitari': {'index': 3018,
                                         'place_name': 'Enchevêtrement '
                                         'des Qitari'},
           'entrée des ruines mécaniques': {'index': 3427,
                                            'place_name': 'Entrée des '
                                            'ruines '
                                            'mécaniques'},
           'eulmore': {'index': 2952, 'place_name': 'Eulmore'},
           'eurêka anemos': {'index': 2414, 'place_name': 'Eurêka Anemos'},
           'eurêka hydatos': {'index': 2545,
                              'place_name': 'Eurêka Hydatos'},
           'eurêka pagos': {'index': 2462, 'place_name': 'Eurêka Pagos'},
           'eurêka pyros': {'index': 2530, 'place_name': 'Eurêka Pyros'},
           "fantasmagorie d'ultima": {'index': 2449,
                                      'place_name': 'Fantasmagorie '
                                      "d'Ultima"},
           'festin des loups': {'index': 1664,
                                'place_name': 'Festin des loups'},
           'fissure interdimensionnelle': {'index': 2737,
                                           'place_name': 'Fissure '
                                           'interdimensionnelle'},
           'fond des enfers': {'index': 2496,
                               'place_name': 'Fond des enfers'},
           'force de bardam': {'index': 2833,
                               'place_name': 'Force de Bardam'},
           'forteresse de dzemael': {'index': 64,
                                     'place_name': 'Forteresse de '
                                     'Dzemael'},
           'forêt centrale': {'index': 54, 'place_name': 'Forêt centrale'},
           "forêt de l'est": {'index': 55, 'place_name': "Forêt de l'est"},
           'forêt du nord': {'index': 57, 'place_name': 'Forêt du nord'},
           'forêt du sud': {'index': 56, 'place_name': 'Forêt du sud'},
           'fosse de nérée': {'index': 3216,
                              'place_name': 'Fosse de Nérée'},
           'front sud de bozja': {'index': 3534,
                                  'place_name': 'Front sud de Bozja'},
           'gangos': {'index': 3478, 'place_name': 'Gangos'},
           'gardien du lac': {'index': 418, 'place_name': 'Gardien du lac'},
           'garlemald': {'index': 3710, 'place_name': 'Garlemald'},
           'geôle de mordion': {'index': 153,
                                'place_name': 'Geôle de Mordion'},
           'gold saucer': {'index': 1484, 'place_name': 'Gold Saucer'},
           'gorge de syrcus': {'index': 3221,
                               'place_name': 'Gorge de Syrcus'},
           'gorge dérobée': {'index': 2589, 'place_name': 'Gorge dérobée'},
           'gouffre hurlant': {'index': 47,
                               'place_name': 'Gouffre hurlant'},
           'grand autel de djanan qhat': {'index': 2339,
                                          'place_name': 'Grand autel de '
                                          'Djanan Qhat'},
           'grand glacier': {'index': 3487, 'place_name': 'Grand Glacier'},
           'grand-lac': {'index': 2953, 'place_name': 'Grand-Lac'},
           'grande bibliothèque de gubal': {'index': 2038,
                                            'place_name': 'Grande '
                                            'bibliothèque '
                                            'de Gubal'},
           'halatali': {'index': 49, 'place_name': 'Halatali'},
           "hall d'argent": {'index': 354, 'place_name': "Hall d'argent"},
           'hall des bestiarii': {'index': 694,
                                  'place_name': 'Hall des Bestiarii'},
           'halo pinaculaire': {'index': 3215,
                                'place_name': 'Halo pinaculaire'},
           'haute-noscea': {'index': 34, 'place_name': 'Haute-Noscea'},
           'hautes terres du coerthas central': {'index': 63,
                                                 'place_name': 'Hautes '
                                                 'terres '
                                                 'du '
                                                 'Coerthas '
                                                 'central'},
           'hautes terres du coerthas occidental': {'index': 2200,
                                                    'place_name': 'Hautes '
                                                    'terres '
                                                    'du '
                                                    'Coerthas '
                                                    'occidental'},
           'hauts plateaux de zadnor': {'index': 3662,
                                        'place_name': 'Hauts plateaux '
                                        'de Zadnor'},
           'holminster': {'index': 3050, 'place_name': 'Holminster'},
           'hurlœil': {'index': 361, 'place_name': 'Hurlœil'},
           'hurlœil (abord)': {'index': 459,
                               'place_name': 'Hurlœil (abord)'},
           'hyperborée': {'index': 3759, 'place_name': 'Hyperborée'},
           'hypogée de tam-tara': {'index': 58,
                                   'place_name': 'Hypogée de Tam-Tara'},
           'idyllée': {'index': 2082, 'place_name': 'Idyllée'},
           'il mheg': {'index': 2956, 'place_name': 'Il Mheg'},
           'interstice du chant onirique': {'index': 4098,
                                            'place_name': 'Interstice '
                                            'du chant '
                                            'onirique'},
           "ishgard - l'assise": {'index': 2300,
                                  'place_name': "Ishgard - L'Assise"},
           'ishgard - les contreforts': {'index': 2301,
                                         'place_name': 'Ishgard - Les '
                                         'Contreforts'},
           'jardin du désespoir': {'index': 3635,
                                   'place_name': 'Jardin du désespoir'},
           'jardin secret du lyhe ghiah': {'index': 3644,
                                           'place_name': 'Jardin secret '
                                           'du Lyhe '
                                           'Ghiah'},
           "jetée de l'antre des loups": {'index': 358,
                                          'place_name': 'Jetée de '
                                          "l'Antre des "
                                          'loups'},
           'kholusia': {'index': 2954, 'place_name': 'Kholusia'},
           'kienkan': {'index': 2847, 'place_name': 'Kienkan'},
           'kobai goten (appartement)': {'index': 2273,
                                         'place_name': 'Kobai Goten '
                                         '(appartement)'},
           'kobai goten (hall)': {'index': 2272,
                                  'place_name': 'Kobai Goten (hall)'},
           'kugane': {'index': 2404, 'place_name': 'Kugane'},
           "l'aire": {'index': 2050, 'place_name': "L'Aire"},
           "l'ambition": {'index': 3477, 'place_name': "L'Ambition"},
           "l'antitour": {'index': 2088, 'place_name': "L'Antitour"},
           "l'escarre": {'index': 2851, 'place_name': "L'Escarre"},
           "l'immensité bleue": {'index': 2151,
                                 'place_name': "L'Immensité bleue"},
           "l'issue aux impasses": {'index': 4100,
                                    'place_name': "L'Issue aux "
                                    'Impasses'},
           "l'observatoire": {'index': 3223,
                              'place_name': "L'Observatoire"},
           "l'âme du créateur": {'index': 1853,
                                 'place_name': "L'Âme du Créateur"},
           "l'écheveau": {'index': 1302, 'place_name': "L'Écheveau"},
           "l'écume des cieux d'abalathia": {'index': 2100,
                                             'place_name': "L'Écume des "
                                             'cieux '
                                             "d'Abalathia"},
           "l'écume des cieux de dravania": {'index': 2002,
                                             'place_name': "L'Écume des "
                                             'cieux de '
                                             'Dravania'},
           "l'étendue de rhalgr": {'index': 2403,
                                   'place_name': "L'Étendue de Rhalgr"},
           'la chrysalide': {'index': 1390, 'place_name': 'La Chrysalide'},
           'la coupe': {'index': 427, 'place_name': 'La Coupe'},
           'la tempête': {'index': 2958, 'place_name': 'La Tempête'},
           'la voûte': {'index': 2327, 'place_name': 'La Voûte'},
           "laboratoire d'études des secrets du vivant": {'index': 4250,
                                                          'place_name': 'Laboratoire '
                                                          "d'études "
                                                          'des '
                                                          'secrets '
                                                          'du '
                                                          'vivant'},
           'laboratoire de magismologie': {'index': 2147,
                                           'place_name': 'Laboratoire '
                                           'de '
                                           'magismologie'},
           "laboratoire impérial d'étude sur les résonnants": {'index': 2296,
                                                               'place_name': 'Laboratoire '
                                                               'impérial '
                                                               "d'étude "
                                                               'sur '
                                                               'les '
                                                               'Résonnants'},
           'large de rocasternes': {'index': 3570,
                                    'place_name': 'Large de '
                                    'Rocasternes'},
           'lavandière': {'index': 426, 'place_name': 'Lavandière'},
           'le bras du fils': {'index': 1723,
                               'place_name': 'Le Bras du Fils'},
           'le bras du père': {'index': 1638,
                               'place_name': 'Le Bras du Père'},
           "le coin de l'âtre (appartement)": {'index': 3695,
                                               'place_name': 'Le Coin '
                                               "de l'Âtre "
                                               '(appartement)'},
           "le coin de l'âtre (hall)": {'index': 3694,
                                        'place_name': 'Le Coin de '
                                        "l'Âtre (hall)"},
           'le continuum fractal': {'index': 2148,
                                    'place_name': 'Le Continuum '
                                    'fractal'},
           'le cœur du créateur': {'index': 1847,
                                   'place_name': 'Le Cœur du Créateur'},
           'le diadème': {'index': 1647, 'place_name': 'Le Diadème'},
           'le fardeau du fils': {'index': 1731,
                                  'place_name': 'Le Fardeau du Fils'},
           'le fardeau du père': {'index': 1645,
                                  'place_name': 'Le Fardeau du Père'},
           'le grand vide': {'index': 3225, 'place_name': 'Le Grand Vide'},
           'le labyrinthos': {'index': 3708,
                              'place_name': 'Le Labyrinthos'},
           'le misère': {'index': 1960, 'place_name': 'Le Misère'},
           'le mât de hune (appartement)': {'index': 1812,
                                            'place_name': 'Le Mât de '
                                            'hune '
                                            '(appartement)'},
           'le mât de hune (hall)': {'index': 1811,
                                     'place_name': 'Le Mât de hune '
                                     '(hall)'},
           'le nombril': {'index': 359, 'place_name': 'Le Nombril'},
           'le paddock': {'index': 1803, 'place_name': 'Le Paddock'},
           'le perchoir': {'index': 548, 'place_name': 'Le Perchoir'},
           'le phare de ridorana': {'index': 2483,
                                    'place_name': 'Le Phare de '
                                    'Ridorana'},
           'le poignet du fils': {'index': 1714,
                                  'place_name': 'Le Poignet du Fils'},
           'le poignet du père': {'index': 1633,
                                  'place_name': 'Le Poignet du Père'},
           'le poing du fils': {'index': 1708,
                                'place_name': 'Le Poing du Fils'},
           'le poing du père': {'index': 1628,
                                'place_name': 'Le Poing du Père'},
           'le propylée': {'index': 3926, 'place_name': 'Le Propylée'},
           'le ragnarok': {'index': 466, 'place_name': 'Le Ragnarok'},
           'le sablier': {'index': 617, 'place_name': 'Le Sablier'},
           'le saint affligé': {'index': 392,
                                'place_name': 'Le Saint affligé'},
           'le souffle de la sultane (appartement)': {'index': 1816,
                                                      'place_name': 'Le '
                                                      'Souffle '
                                                      'de '
                                                      'la '
                                                      'Sultane '
                                                      '(appartement)'},
           'le souffle de la sultane (hall)': {'index': 1815,
                                               'place_name': 'Le '
                                               'Souffle '
                                               'de la '
                                               'Sultane '
                                               '(hall)'},
           'le souffle du créateur': {'index': 1841,
                                      'place_name': 'Le Souffle du '
                                      'Créateur'},
           'le trône du sacrifice': {'index': 3568,
                                     'place_name': 'Le Trône du '
                                     'Sacrifice'},
           "legs d'alzadaal": {'index': 4154,
                               'place_name': "Legs d'Alzadaal"},
           'les lacs': {'index': 2408, 'place_name': 'Les Lacs'},
           'les marges': {'index': 2406, 'place_name': 'Les Marges'},
           'les neuf-nuages': {'index': 2310,
                               'place_name': 'Les Neuf-Nuages'},
           'les nuées de brandons': {'index': 3442,
                                     'place_name': 'Les Nuées de '
                                     'Brandons'},
           'les pendants': {'index': 3222, 'place_name': 'Les Pendants'},
           'les pics': {'index': 2407, 'place_name': 'Les Pics'},
           'les ténèbres de ghimlyt': {'index': 2586,
                                       'place_name': 'Les Ténèbres de '
                                       'Ghimlyt'},
           'les yeux du créateur': {'index': 1835,
                                    'place_name': 'Les Yeux du '
                                    'Créateur'},
           'limbes du pandæmonium - abîme': {'index': 4135,
                                             'place_name': 'Limbes du '
                                             'Pandæmonium '
                                             '- Abîme'},
           'limbes du pandæmonium - cloaque': {'index': 3798,
                                               'place_name': 'Limbes du '
                                               'Pandæmonium '
                                               '- '
                                               'Cloaque'},
           'limbes du pandæmonium - fournaise': {'index': 3797,
                                                 'place_name': 'Limbes '
                                                 'du '
                                                 'Pandæmonium '
                                                 '- '
                                                 'Fournaise'},
           'limbes du pandæmonium - parvis': {'index': 3769,
                                              'place_name': 'Limbes du '
                                              'Pandæmonium '
                                              '- Parvis'},
           "limsa lominsa - l'entrepont": {'index': 29,
                                           'place_name': 'Limsa Lominsa '
                                           '- '
                                           "L'Entrepont"},
           'limsa lominsa - le tillac': {'index': 28,
                                         'place_name': 'Limsa Lominsa - '
                                         'Le Tillac'},
           'lisière de ronces': {'index': 360,
                                 'place_name': 'Lisière de ronces'},
           'ludodrome': {'index': 4111, 'place_name': 'Ludodrome'},
           'macle de syrcus': {'index': 2982,
                               'place_name': 'Macle de Syrcus'},
           'maisonnette - brumée': {'index': 1100,
                                    'place_name': 'Maisonnette - '
                                    'Brumée'},
           'maisonnette - empyrée': {'index': 3689,
                                     'place_name': 'Maisonnette - '
                                     'Empyrée'},
           'maisonnette - la coupe': {'index': 1103,
                                      'place_name': 'Maisonnette - La '
                                      'Coupe'},
           'maisonnette - lavandière': {'index': 1106,
                                        'place_name': 'Maisonnette - '
                                        'Lavandière'},
           'maisonnette - shirogane': {'index': 1893,
                                       'place_name': 'Maisonnette - '
                                       'Shirogane'},
           'manoir des fortemps': {'index': 2320,
                                   'place_name': 'Manoir des Fortemps'},
           'manoir des haukke': {'index': 59,
                                 'place_name': 'Manoir des Haukke'},
           'manoir hanté': {'index': 1834, 'place_name': 'Manoir hanté'},
           'manteneige': {'index': 404, 'place_name': 'Manteneige'},
           'mare lamentorum': {'index': 3711,
                               'place_name': 'Mare Lamentorum'},
           'mer de rhotano': {'index': 462, 'place_name': 'Mer de Rhotano'},
           'mer de rubis': {'index': 2409, 'place_name': 'Mer de Rubis'},
           'mer du chant des sirènes': {'index': 2297,
                                        'place_name': 'Mer du Chant des '
                                        'sirènes'},
           'mille gueules de toto-rak': {'index': 61,
                                         'place_name': 'Mille Gueules '
                                         'de Toto-Rak'},
           'mines de clochecuivre': {'index': 48,
                                     'place_name': 'Mines de '
                                     'Clochecuivre'},
           "monastère d'orbonne": {'index': 2864,
                                   'place_name': "Monastère d'Orbonne"},
           'monde des ténèbres': {'index': 1431,
                                  'place_name': 'Monde des Ténèbres'},
           'mont atlas': {'index': 3217, 'place_name': 'Mont Atlas'},
           'mont gulg': {'index': 2997, 'place_name': 'Mont Gulg'},
           'mor dhona': {'index': 67, 'place_name': 'Mor Dhona'},
           'muraille de baelsar': {'index': 1857,
                                   'place_name': 'Muraille de Baelsar'},
           'ménagerie royale': {'index': 2709,
                                'place_name': 'Ménagerie royale'},
           'nalloncques': {'index': 2130, 'place_name': 'Nalloncques'},
           'noscea centrale': {'index': 30,
                               'place_name': 'Noscea centrale'},
           'noscea extérieure': {'index': 350,
                                 'place_name': 'Noscea extérieure'},
           'noscea occidentale': {'index': 33,
                                  'place_name': 'Noscea occidentale'},
           'noscea orientale': {'index': 32,
                                'place_name': 'Noscea orientale'},
           'nouvelle gridania': {'index': 52,
                                 'place_name': 'Nouvelle Gridania'},
           'noyau central du ragnarok': {'index': 468,
                                         'place_name': 'Noyau central '
                                         'du Ragnarok'},
           'ombrage du météore': {'index': 1301,
                                  'place_name': 'Ombrage du Météore'},
           'omphalos': {'index': 4031, 'place_name': 'Omphalos'},
           'onsal hakair': {'index': 3378, 'place_name': 'Onsal Hakair'},
           'orée de la fin': {'index': 3686,
                              'place_name': 'Orée de la fin'},
           "paglth'an": {'index': 2936, 'place_name': "Paglth'an"},
           'palais aux marées violettes': {'index': 2779,
                                           'place_name': 'Palais aux '
                                           'Marées '
                                           'violettes'},
           'palais des morts': {'index': 1793,
                                'place_name': 'Palais des morts'},
           'palais du vagabond': {'index': 37,
                                  'place_name': 'Palais du Vagabond'},
           "palais royal d'ala mhigo": {'index': 2294,
                                        'place_name': 'Palais royal '
                                        "d'Ala Mhigo"},
           'pavillon - brumée': {'index': 1101,
                                 'place_name': 'Pavillon - Brumée'},
           'pavillon - empyrée': {'index': 3690,
                                  'place_name': 'Pavillon - Empyrée'},
           'pavillon - la coupe': {'index': 1104,
                                   'place_name': 'Pavillon - La Coupe'},
           'pavillon - lavandière': {'index': 1107,
                                     'place_name': 'Pavillon - '
                                     'Lavandière'},
           'pavillon - shirogane': {'index': 1894,
                                    'place_name': 'Pavillon - '
                                    'Shirogane'},
           'phare de sirius': {'index': 230,
                               'place_name': 'Phare de Sirius'},
           'pilier des cieux': {'index': 2775,
                                'place_name': 'Pilier des Cieux'},
           'plaine foudroyée de gandof': {'index': 3468,
                                          'place_name': 'Plaine '
                                          'foudroyée de '
                                          'Gandof'},
           'plaine-aux-lys (appartement)': {'index': 1814,
                                            'place_name': 'Plaine-aux-Lys '
                                            '(appartement)'},
           'plaine-aux-lys (hall)': {'index': 1813,
                                     'place_name': 'Plaine-aux-Lys '
                                     '(hall)'},
           'pont du prima vista': {'index': 2371,
                                   'place_name': 'Pont du Prima Vista'},
           'pont ohashi': {'index': 2499, 'place_name': 'Pont Ohashi'},
           'pont principal du ragnarok': {'index': 469,
                                          'place_name': 'Pont principal '
                                          'du Ragnarok'},
           'pont principal rci-04': {'index': 1410,
                                     'place_name': 'Pont principal '
                                     'RCI-04'},
           'pont principal rci-06': {'index': 1408,
                                     'place_name': 'Pont principal '
                                     'RCI-06'},
           "pont supérieur d'éden": {'index': 3470,
                                     'place_name': 'Pont supérieur '
                                     "d'Éden"},
           'ponton du gardien-g': {'index': 3663,
                                   'place_name': 'Ponton du Gardien-G'},
           'porta decumana': {'index': 4032,
                              'place_name': 'Porta Decumana'},
           'porte des dieux': {'index': 4024,
                               'place_name': 'Porte des Dieux'},
           'praetorium': {'index': 430, 'place_name': 'Praetorium'},
           'premier pont rci-03': {'index': 1305,
                                   'place_name': 'Premier pont RCI-03'},
           "prisme de l'aitia": {'index': 4146,
                                 'place_name': "Prisme de l'Aitia"},
           "prison d'eulmore": {'index': 3595,
                                'place_name': "Prison d'Eulmore"},
           'prison lunaire': {'index': 3684,
                              'place_name': 'Prison lunaire'},
           'psistice v1.0': {'index': 2725, 'place_name': 'Psistice v1.0'},
           'psistice v2.0': {'index': 2736, 'place_name': 'Psistice v2.0'},
           'puits de malikah': {'index': 3139,
                                'place_name': 'Puits de Malikah'},
           'quartier enclavé de doma': {'index': 2813,
                                        'place_name': 'Quartier enclavé '
                                        'de Doma'},
           "quartier général de l'alliance": {'index': 2862,
                                              'place_name': 'Quartier '
                                              'général de '
                                              "l'Alliance"},
           'radz-at-han': {'index': 3707, 'place_name': 'Radz-at-Han'},
           "rak'tika": {'index': 2957, 'place_name': "Rak'tika"},
           'refuge des roches': {'index': 481,
                                 'place_name': 'Refuge des roches'},
           'refuge des sables': {'index': 356,
                                 'place_name': 'Refuge des sables'},
           'repaire des lémures': {'index': 4022,
                                   'place_name': 'Repaire des Lémures'},
           'risette-sur-lune': {'index': 3770,
                                'place_name': 'Risette-sur-lune'},
           'rocasternes': {'index': 3571, 'place_name': 'Rocasternes'},
           'rocher des tréfonds': {'index': 496,
                                   'place_name': 'Rocher des tréfonds'},
           'ruines frontalières': {'index': 1374,
                                   'place_name': 'Ruines frontalières'},
           'réacteur de singularité': {'index': 2178,
                                       'place_name': 'Réacteur de '
                                       'singularité'},
           "réplique de l'usine désaffectée": {'index': 3425,
                                               'place_name': 'Réplique '
                                               'de '
                                               "l'usine "
                                               'désaffectée'},
           'réseau de régénération rci-06': {'index': 1407,
                                             'place_name': 'Réseau de '
                                             'régénération '
                                             'RCI-06'},
           'rêve électrique de stigma-4': {'index': 3783,
                                           'place_name': 'Rêve '
                                           'électrique de '
                                           'Stigma-4'},
           "salle d'accueil du bazar de rubis": {'index': 2927,
                                                 'place_name': 'Salle '
                                                 "d'accueil "
                                                 'du '
                                                 'Bazar '
                                                 'de '
                                                 'Rubis'},
           'salle de bal de titania': {'index': 3218,
                                       'place_name': 'Salle de bal de '
                                       'Titania'},
           'salle de commandement du carquois': {'index': 346,
                                                 'place_name': 'Salle '
                                                 'de '
                                                 'commandement '
                                                 'du '
                                                 'Carquois'},
           'salle de contrôle': {'index': 3486,
                                 'place_name': 'Salle de contrôle'},
           "salle de contrôle d'oméga": {'index': 1887,
                                         'place_name': 'Salle de '
                                         'contrôle '
                                         "d'Oméga"},
           'salle de contrôle rci-03': {'index': 1304,
                                        'place_name': 'Salle de '
                                        'contrôle RCI-03'},
           'salle de réception': {'index': 1429,
                                  'place_name': 'Salle de réception'},
           'salle de répétition du prima vista': {'index': 2370,
                                                  'place_name': 'Salle '
                                                  'de '
                                                  'répétition '
                                                  'du '
                                                  'Prima '
                                                  'Vista'},
           'salle des convocations': {'index': 379,
                                      'place_name': 'Salle des '
                                      'convocations'},
           'salle des développeurs': {'index': 1660,
                                      'place_name': 'Salle des '
                                      'développeurs'},
           'salle des offrandes': {'index': 2083,
                                   'place_name': 'Salle des offrandes'},
           'salle des opérations': {'index': 4023,
                                    'place_name': 'Salle des '
                                    'opérations'},
           'salle des primiciers': {'index': 4185,
                                    'place_name': 'Salle des '
                                    'primiciers'},
           'salle des sentences': {'index': 2336,
                                   'place_name': 'Salle des sentences'},
           "salon de l'amiral": {'index': 351,
                                 'place_name': "Salon de l'Amiral"},
           'salon principal': {'index': 3817,
                               'place_name': 'Salon principal'},
           'sanctuaire des douze': {'index': 112,
                                    'place_name': 'Sanctuaire des '
                                    'Douze'},
           'sanctuaire du grand serpent': {'index': 2510,
                                           'place_name': 'Sanctuaire du '
                                           'Grand '
                                           'Serpent'},
           'sanctuaire reisen': {'index': 2392,
                                 'place_name': 'Sanctuaire Reisen'},
           'sastasha': {'index': 35, 'place_name': 'Sastasha'},
           'scolasticat saint-endalim': {'index': 2337,
                                         'place_name': 'Scolasticat '
                                         'Saint-Endalim'},
           'secteur central rci-03': {'index': 1303,
                                      'place_name': 'Secteur central '
                                      'RCI-03'},
           'secteur central rci-06': {'index': 1406,
                                      'place_name': 'Secteur central '
                                      'RCI-06'},
           'shirogane': {'index': 2412, 'place_name': 'Shirogane'},
           'sigmastice v1.0': {'index': 2717,
                               'place_name': 'Sigmastice v1.0'},
           'sigmastice v2.0': {'index': 2718,
                               'place_name': 'Sigmastice v2.0'},
           'sigmastice v3.0': {'index': 2719,
                               'place_name': 'Sigmastice v3.0'},
           'sigmastice v4.0': {'index': 2720,
                               'place_name': 'Sigmastice v4.0'},
           "site impérial d'exploration inférieur": {'index': 465,
                                                     'place_name': 'Site '
                                                     'impérial '
                                                     "d'exploration "
                                                     'inférieur'},
           "site impérial d'exploration supérieur": {'index': 464,
                                                     'place_name': 'Site '
                                                     'impérial '
                                                     "d'exploration "
                                                     'supérieur'},
           'siège du capitaine général': {'index': 2335,
                                          'place_name': 'Siège du '
                                          'capitaine '
                                          'général'},
           'sohm al': {'index': 2031, 'place_name': 'Sohm Al'},
           'sohr khai': {'index': 2090, 'place_name': 'Sohr Khai'},
           'sous-sol éorzéen': {'index': 152,
                                'place_name': 'Sous-sol éorzéen'},
           "sphère de l'absence": {'index': 3596,
                                   'place_name': "Sphère de l'absence"},
           'square des chocobos': {'index': 1500,
                                   'place_name': 'Square des chocobos'},
           "steppe d'azim": {'index': 2411, 'place_name': "Steppe d'Azim"},
           'tables des manderville': {'index': 2549,
                                      'place_name': 'Tables des '
                                      'Manderville'},
           'temple du poing': {'index': 2707,
                               'place_name': 'Temple du Poing'},
           'temple enseveli de qarn': {'index': 50,
                                       'place_name': 'Temple enseveli '
                                       'de Qarn'},
           "temple sacré d'uznair": {'index': 2485,
                                     'place_name': 'Temple sacré '
                                     "d'Uznair"},
           'territoire de zero': {'index': 4038,
                                  'place_name': 'Territoire de Zero'},
           'thanalan central': {'index': 43,
                                'place_name': 'Thanalan central'},
           'thanalan méridional': {'index': 45,
                                   'place_name': 'Thanalan méridional'},
           'thanalan occidental': {'index': 42,
                                   'place_name': 'Thanalan occidental'},
           'thanalan oriental': {'index': 44,
                                 'place_name': 'Thanalan oriental'},
           'thanalan septentrional': {'index': 46,
                                      'place_name': 'Thanalan '
                                      'septentrional'},
           'thavnair': {'index': 3709, 'place_name': 'Thavnair'},
           'thok ast thok': {'index': 2081, 'place_name': 'Thok ast Thok'},
           'toison des tempêtes': {'index': 4045,
                                   'place_name': 'Toison des tempêtes'},
           'tour de babil': {'index': 4118, 'place_name': 'Tour de Babil'},
           'tour de la contingence': {'index': 3647,
                                      'place_name': 'Tour de la '
                                      'Contingence'},
           'tour de syrcus': {'index': 493, 'place_name': 'Tour de Syrcus'},
           'tour de zott': {'index': 3736, 'place_name': 'Tour de Zott'},
           'transparence': {'index': 2715, 'place_name': 'Transparence'},
           'traversée de norvrandt': {'index': 3511,
                                      'place_name': 'Traversée de '
                                      'Norvrandt'},
           'traversée du griffon': {'index': 386,
                                    'place_name': 'Traversée du '
                                    'Griffon'},
           "ul'dah - faubourg de nald": {'index': 40,
                                         'place_name': "Ul'dah - "
                                         'Faubourg de '
                                         'Nald'},
           "ul'dah - faubourg de thal": {'index': 41,
                                         'place_name': "Ul'dah - "
                                         'Faubourg de '
                                         'Thal'},
           'ultima thulé': {'index': 3712, 'place_name': 'Ultima Thulé'},
           'unité de contention p1p6': {'index': 2265,
                                        'place_name': 'Unité de '
                                        'contention P1P6'},
           'unité de contention s1p7': {'index': 2256,
                                        'place_name': 'Unité de '
                                        'contention S1P7'},
           'unité de contention z1p9': {'index': 2266,
                                        'place_name': 'Unité de '
                                        'contention Z1P9'},
           'univers différentiel': {'index': 3017,
                                    'place_name': 'Univers '
                                    'différentiel'},
           "val d'aurum": {'index': 65, 'place_name': "Val d'Aurum"},
           'vanaspati': {'index': 4015, 'place_name': 'Vanaspati'},
           "vestiges de la cité d'amdapor": {'index': 125,
                                             'place_name': 'Vestiges de '
                                             'la cité '
                                             "d'Amdapor"},
           'vestiges oubliés': {'index': 3542,
                                'place_name': 'Vestiges oubliés'},
           'vieille gridania': {'index': 53,
                                'place_name': 'Vieille Gridania'},
           'vieille sharlayan': {'index': 3706,
                                 'place_name': 'Vieille Sharlayan'},
           'vigile de pierre': {'index': 401,
                                'place_name': 'Vigile de Pierre'},
           'vigile du crépuscule': {'index': 2214,
                                    'place_name': 'Vigile du '
                                    'Crépuscule'},
           'villa - brumée': {'index': 1102,
                              'place_name': 'Villa - Brumée'},
           'villa - empyrée': {'index': 3691,
                               'place_name': 'Villa - Empyrée'},
           'villa - la coupe': {'index': 1105,
                                'place_name': 'Villa - La Coupe'},
           'villa - lavandière': {'index': 1108,
                                  'place_name': 'Villa - Lavandière'},
           'villa - shirogane': {'index': 1895,
                                 'place_name': 'Villa - Shirogane'},
           'xelphatol': {'index': 1792, 'place_name': 'Xelphatol'},
           'yanxia': {'index': 2410, 'place_name': 'Yanxia'},
           'émanation': {'index': 2299, 'place_name': 'Émanation'},
           'île de crèvecarène': {'index': 1377,
                                  'place_name': 'Île de Crèvecarène'},
           'île sans nom': {'index': 4043, 'place_name': 'Île sans nom'}},
    'ja': {'gセイヴァー戦闘甲板': {'index': 3663, 'place_name': 'Gセイヴァー戦闘甲板'},
           'かいはつしつ': {'index': 1660, 'place_name': 'かいはつしつ'},
           'アイズ・オブ・アレキサンダー': {'index': 1835,
                              'place_name': 'アイズ・オブ・アレキサンダー'},
           'アイティオン星晶鏡': {'index': 4146, 'place_name': 'アイティオン星晶鏡'},
           'アクアポリス': {'index': 1799, 'place_name': 'アクアポリス'},
           'アク・アファー円形劇場': {'index': 1399, 'place_name': 'アク・アファー円形劇場'},
           'アジス・ラー': {'index': 2101, 'place_name': 'アジス・ラー'},
           'アジムステップ': {'index': 2411, 'place_name': 'アジムステップ'},
           'アトラス山頂': {'index': 3217, 'place_name': 'アトラス山頂'},
           'アドミラルブリッジ：提督室': {'index': 351, 'place_name': 'アドミラルブリッジ：提督室'},
           'アナイダアカデミア': {'index': 3007, 'place_name': 'アナイダアカデミア'},
           'アニドラス・アナムネーシス': {'index': 3467, 'place_name': 'アニドラス・アナムネーシス'},
           'アバラシア雲海': {'index': 2100, 'place_name': 'アバラシア雲海'},
           'アム・アレーン': {'index': 2955, 'place_name': 'アム・アレーン'},
           'アメノミハシラ': {'index': 2775, 'place_name': 'アメノミハシラ'},
           'アラミゴ': {'index': 2691, 'place_name': 'アラミゴ'},
           'アラミゴ王宮': {'index': 2294, 'place_name': 'アラミゴ王宮'},
           'アラミゴ王宮屋上庭園': {'index': 2709, 'place_name': 'アラミゴ王宮屋上庭園'},
           'アラミゴ王立飛空艇発着場': {'index': 2708, 'place_name': 'アラミゴ王立飛空艇発着場'},
           'アルザダール海底遺跡群': {'index': 4154, 'place_name': 'アルザダール海底遺跡群'},
           'アーム・オブ・ゴルディオス': {'index': 1638, 'place_name': 'アーム・オブ・ゴルディオス'},
           'アーム・オブ・ミダース': {'index': 1723, 'place_name': 'アーム・オブ・ミダース'},
           'アーモロート': {'index': 2985, 'place_name': 'アーモロート'},
           'イシュガルド教皇庁': {'index': 2327, 'place_name': 'イシュガルド教皇庁'},
           'イシュガルド：上層': {'index': 2301, 'place_name': 'イシュガルド：上層'},
           'イシュガルド：下層': {'index': 2300, 'place_name': 'イシュガルド：下層'},
           'イディルシャイア': {'index': 2082, 'place_name': 'イディルシャイア'},
           'イマキュレートクラウン': {'index': 3219, 'place_name': 'イマキュレートクラウン'},
           'イル・メグ': {'index': 2956, 'place_name': 'イル・メグ'},
           'イングルサイド：ロビー': {'index': 3694, 'place_name': 'イングルサイド：ロビー'},
           'イングルサイド：部屋': {'index': 3695, 'place_name': 'イングルサイド：部屋'},
           'ウズネアカナル': {'index': 2340, 'place_name': 'ウズネアカナル'},
           'ウズネアカナル祭殿': {'index': 2485, 'place_name': 'ウズネアカナル祭殿'},
           'ウルダハ商館応接室': {'index': 2927, 'place_name': 'ウルダハ商館応接室'},
           'ウルダハ：ザル回廊': {'index': 41, 'place_name': 'ウルダハ：ザル回廊'},
           'ウルダハ：ナル回廊': {'index': 40, 'place_name': 'ウルダハ：ナル回廊'},
           'ウルティマ・トゥーレ': {'index': 3712, 'place_name': 'ウルティマ・トゥーレ'},
           'ウルヴズジェイル係船場': {'index': 358, 'place_name': 'ウルヴズジェイル係船場'},
           'ウルヴズジェイル演習場': {'index': 1664, 'place_name': 'ウルヴズジェイル演習場'},
           'エウレカ：アネモス帯': {'index': 2414, 'place_name': 'エウレカ：アネモス帯'},
           'エウレカ：パゴス帯': {'index': 2462, 'place_name': 'エウレカ：パゴス帯'},
           'エウレカ：ヒュダトス帯': {'index': 2545, 'place_name': 'エウレカ：ヒュダトス帯'},
           'エウレカ：ピューロス帯': {'index': 2530, 'place_name': 'エウレカ：ピューロス帯'},
           'エオルゼア同盟軍本陣': {'index': 2862, 'place_name': 'エオルゼア同盟軍本陣'},
           'エオルゼア地下空間': {'index': 152, 'place_name': 'エオルゼア地下空間'},
           'エキサイトロン': {'index': 4111, 'place_name': 'エキサイトロン'},
           'エデンコア': {'index': 3214, 'place_name': 'エデンコア'},
           'エデン甲板': {'index': 3470, 'place_name': 'エデン甲板'},
           'エルピス': {'index': 3713, 'place_name': 'エルピス'},
           'エンデバー号': {'index': 3477, 'place_name': 'エンデバー号'},
           'エンピレアム': {'index': 4139, 'place_name': 'エンピレアム'},
           'エンピレアム：コテージ': {'index': 3689, 'place_name': 'エンピレアム：コテージ'},
           'エンピレアム：ハウス': {'index': 3690, 'place_name': 'エンピレアム：ハウス'},
           'エンピレアム：プライベートルーム': {'index': 3692,
                                'place_name': 'エンピレアム：プライベートルーム'},
           'エンピレアム：レジデンス': {'index': 3691, 'place_name': 'エンピレアム：レジデンス'},
           'エンピレアム：地下工房': {'index': 3693, 'place_name': 'エンピレアム：地下工房'},
           'オムファロス': {'index': 4031, 'place_name': 'オムファロス'},
           'オメガ管制室': {'index': 1887, 'place_name': 'オメガ管制室'},
           'オンサル・ハカイル': {'index': 3378, 'place_name': 'オンサル・ハカイル'},
           'オ・ゴモロ火口神殿': {'index': 359, 'place_name': 'オ・ゴモロ火口神殿'},
           'オーラムヴェイル': {'index': 65, 'place_name': 'オーラムヴェイル'},
           'オールド・シャーレアン': {'index': 3706, 'place_name': 'オールド・シャーレアン'},
           'カステッルム・マリヌム・ドライドック': {'index': 3581,
                                  'place_name': 'カステッルム・マリヌム・ドライドック'},
           'カストルム・アバニア': {'index': 2665, 'place_name': 'カストルム・アバニア'},
           'カストルム・フルーミニス': {'index': 2799, 'place_name': 'カストルム・フルーミニス'},
           'カストルム・メリディアヌム': {'index': 260, 'place_name': 'カストルム・メリディアヌム'},
           'カッターズクライ': {'index': 47, 'place_name': 'カッターズクライ'},
           'カッパーベル銅山': {'index': 48, 'place_name': 'カッパーベル銅山'},
           'カフ・オブ・ゴルディオス': {'index': 1633, 'place_name': 'カフ・オブ・ゴルディオス'},
           'カフ・オブ・ミダース': {'index': 1714, 'place_name': 'カフ・オブ・ミダース'},
           'カルテノー平原：外縁遺跡群': {'index': 1374, 'place_name': 'カルテノー平原：外縁遺跡群'},
           'カルン埋没寺院': {'index': 50, 'place_name': 'カルン埋没寺院'},
           'カードバトルルーム': {'index': 1665, 'place_name': 'カードバトルルーム'},
           'ガレマルド': {'index': 3710, 'place_name': 'ガレマルド'},
           'ガンエン廟': {'index': 2801, 'place_name': 'ガンエン廟'},
           'ガンゴッシュ': {'index': 3478, 'place_name': 'ガンゴッシュ'},
           'ガンドフ雷平原': {'index': 3468, 'place_name': 'ガンドフ雷平原'},
           'キタンナ神影洞': {'index': 3018, 'place_name': 'キタンナ神影洞'},
           'ギムリトダーク': {'index': 2586, 'place_name': 'ギムリトダーク'},
           'ギムリト防衛ライン': {'index': 3442, 'place_name': 'ギムリト防衛ライン'},
           'ギラバニア山岳地帯': {'index': 2407, 'place_name': 'ギラバニア山岳地帯'},
           'ギラバニア湖畔地帯': {'index': 2408, 'place_name': 'ギラバニア湖畔地帯'},
           'ギラバニア辺境地帯': {'index': 2406, 'place_name': 'ギラバニア辺境地帯'},
           'クガネ': {'index': 2404, 'place_name': 'クガネ'},
           'クガネ城': {'index': 2298, 'place_name': 'クガネ城'},
           'クガネ大橋': {'index': 2499, 'place_name': 'クガネ大橋'},
           'クリスタリウム': {'index': 2951, 'place_name': 'クリスタリウム'},
           'クルザス中央高地': {'index': 63, 'place_name': 'クルザス中央高地'},
           'クルザス西部高地': {'index': 2200, 'place_name': 'クルザス西部高地'},
           'グブラ幻想図書館': {'index': 2038, 'place_name': 'グブラ幻想図書館'},
           'グラン・コスモス': {'index': 3385, 'place_name': 'グラン・コスモス'},
           'グリダニア：新市街': {'index': 52, 'place_name': 'グリダニア：新市街'},
           'グリダニア：旧市街': {'index': 53, 'place_name': 'グリダニア：旧市街'},
           'グリフィン大橋': {'index': 386, 'place_name': 'グリフィン大橋'},
           'グルグ火山': {'index': 2997, 'place_name': 'グルグ火山'},
           'グンヒルド・ディルーブラム': {'index': 3597, 'place_name': 'グンヒルド・ディルーブラム'},
           'コルシア島': {'index': 2954, 'place_name': 'コルシア島'},
           'コンテイメントベイp1t6': {'index': 2265, 'place_name': 'コンテイメントベイP1T6'},
           'コンテイメントベイs1t7': {'index': 2256, 'place_name': 'コンテイメントベイS1T7'},
           'コンテイメントベイz1t9': {'index': 2266, 'place_name': 'コンテイメントベイZ1T9'},
           'ゴブレットビュート': {'index': 427, 'place_name': 'ゴブレットビュート'},
           'ゴブレットビュート：コテージ': {'index': 1103,
                              'place_name': 'ゴブレットビュート：コテージ'},
           'ゴブレットビュート：ハウス': {'index': 1104, 'place_name': 'ゴブレットビュート：ハウス'},
           'ゴブレットビュート：プライベートルーム': {'index': 1158,
                                   'place_name': 'ゴブレットビュート：プライベートルーム'},
           'ゴブレットビュート：レジデンス': {'index': 1105,
                               'place_name': 'ゴブレットビュート：レジデンス'},
           'ゴブレットビュート：地下工房': {'index': 1228,
                              'place_name': 'ゴブレットビュート：地下工房'},
           'ゴールドソーサー': {'index': 1484, 'place_name': 'ゴールドソーサー'},
           'サスタシャ浸食洞': {'index': 35, 'place_name': 'サスタシャ浸食洞'},
           'サベネア島': {'index': 3709, 'place_name': 'サベネア島'},
           'ザトゥノル高原': {'index': 3662, 'place_name': 'ザトゥノル高原'},
           'ザ・バーン': {'index': 2851, 'place_name': 'ザ・バーン'},
           'シリウス大灯台': {'index': 230, 'place_name': 'シリウス大灯台'},
           'シルクスの塔': {'index': 493, 'place_name': 'シルクスの塔'},
           'シルクスの峡間': {'index': 3221, 'place_name': 'シルクスの峡間'},
           'シルクス・ツイニング': {'index': 2982, 'place_name': 'シルクス・ツイニング'},
           'シロガネ': {'index': 2412, 'place_name': 'シロガネ'},
           'シロガネ：コテージ': {'index': 1893, 'place_name': 'シロガネ：コテージ'},
           'シロガネ：ハウス': {'index': 1894, 'place_name': 'シロガネ：ハウス'},
           'シロガネ：プライベートルーム': {'index': 2270,
                              'place_name': 'シロガネ：プライベートルーム'},
           'シロガネ：レジデンス': {'index': 1895, 'place_name': 'シロガネ：レジデンス'},
           'シロガネ：地下工房': {'index': 2271, 'place_name': 'シロガネ：地下工房'},
           'シンギュラリティ・リアクター': {'index': 2178,
                              'place_name': 'シンギュラリティ・リアクター'},
           'シールロック': {'index': 496, 'place_name': 'シールロック'},
           'ジャナン・カット地下祭壇': {'index': 2339, 'place_name': 'ジャナン・カット地下祭壇'},
           'スカラ': {'index': 2367, 'place_name': 'スカラ'},
           'スティグマ・フォー': {'index': 3783, 'place_name': 'スティグマ・フォー'},
           'ストーンヴィジル': {'index': 401, 'place_name': 'ストーンヴィジル'},
           'スノークローク大氷壁': {'index': 404, 'place_name': 'スノークローク大氷壁'},
           'スマイルトン': {'index': 3770, 'place_name': 'スマイルトン'},
           'セイレーン海': {'index': 2297, 'place_name': 'セイレーン海'},
           'ゼルファトル': {'index': 1792, 'place_name': 'ゼルファトル'},
           'ゼロの領域': {'index': 4038, 'place_name': 'ゼロの領域'},
           'ゼーメル要塞': {'index': 64, 'place_name': 'ゼーメル要塞'},
           'ソウル・オブ・アレキサンダー': {'index': 1853,
                              'place_name': 'ソウル・オブ・アレキサンダー'},
           'ソーム・アル': {'index': 2031, 'place_name': 'ソーム・アル'},
           'ソール・カイ': {'index': 2090, 'place_name': 'ソール・カイ'},
           'ゾットの塔': {'index': 3736, 'place_name': 'ゾットの塔'},
           'タムタラの墓所': {'index': 58, 'place_name': 'タムタラの墓所'},
           'ターンクリフ': {'index': 3571, 'place_name': 'ターンクリフ'},
           'ターンクリフ沖': {'index': 3570, 'place_name': 'ターンクリフ沖'},
           'ダスクヴィジル': {'index': 2214, 'place_name': 'ダスクヴィジル'},
           'チョコボスクウェア': {'index': 1500, 'place_name': 'チョコボスクウェア'},
           'テンペスト': {'index': 2958, 'place_name': 'テンペスト'},
           'ディアデム諸島': {'index': 1647, 'place_name': 'ディアデム諸島'},
           'トップマスト：ロビー': {'index': 1811, 'place_name': 'トップマスト：ロビー'},
           'トップマスト：部屋': {'index': 1812, 'place_name': 'トップマスト：部屋'},
           'トトラクの千獄': {'index': 61, 'place_name': 'トトラクの千獄'},
           'トロイアコート': {'index': 4180, 'place_name': 'トロイアコート'},
           'ドォーヌ・メグ': {'index': 2979, 'place_name': 'ドォーヌ・メグ'},
           'ドマ町人地': {'index': 2813, 'place_name': 'ドマ町人地'},
           'ドラゴンズエアリー': {'index': 2050, 'place_name': 'ドラゴンズエアリー'},
           'ドラヴァニア雲海': {'index': 2002, 'place_name': 'ドラヴァニア雲海'},
           'ナップルーム': {'index': 3818, 'place_name': 'ナップルーム'},
           'ナナモ大風車：ロビー': {'index': 1815, 'place_name': 'ナナモ大風車：ロビー'},
           'ナナモ大風車：部屋': {'index': 1816, 'place_name': 'ナナモ大風車：部屋'},
           'ニーム浮遊遺跡風特設アスレチック': {'index': 2527,
                                'place_name': 'ニーム浮遊遺跡風特設アスレチック'},
           'ヌーメノン大書院：禁書庫': {'index': 4034, 'place_name': 'ヌーメノン大書院：禁書庫'},
           'ネバーリープ': {'index': 2130, 'place_name': 'ネバーリープ'},
           'ネレウス海淵': {'index': 3216, 'place_name': 'ネレウス海淵'},
           'ハウケタ御用邸': {'index': 59, 'place_name': 'ハウケタ御用邸'},
           'ハウリングアイ外縁': {'index': 459, 'place_name': 'ハウリングアイ外縁'},
           'ハウリングアイ石塔群': {'index': 361, 'place_name': 'ハウリングアイ石塔群'},
           'ハラタリ修練所': {'index': 49, 'place_name': 'ハラタリ修練所'},
           'ハルブレーカー・アイル': {'index': 1377, 'place_name': 'ハルブレーカー・アイル'},
           'ハート・オブ・アレキサンダー': {'index': 1847,
                              'place_name': 'ハート・オブ・アレキサンダー'},
           'バインディングコイル': {'index': 1302, 'place_name': 'バインディングコイル'},
           'バエサルの長城': {'index': 1857, 'place_name': 'バエサルの長城'},
           'バハムートコア': {'index': 1409, 'place_name': 'バハムートコア'},
           'バブイルの塔': {'index': 4118, 'place_name': 'バブイルの塔'},
           'バルダム覇道': {'index': 2833, 'place_name': 'バルダム覇道'},
           'バーデン・オブ・ゴルディオス': {'index': 1645,
                              'place_name': 'バーデン・オブ・ゴルディオス'},
           'バーデン・オブ・ミダース': {'index': 1731, 'place_name': 'バーデン・オブ・ミダース'},
           'パガルザン': {'index': 2936, 'place_name': 'パガルザン'},
           'パロック繋留基地': {'index': 1803, 'place_name': 'パロック繋留基地'},
           'パンデモニウム正門': {'index': 3769, 'place_name': 'パンデモニウム正門'},
           'パンデモニウム辺獄下層': {'index': 3797, 'place_name': 'パンデモニウム辺獄下層'},
           'パンデモニウム辺獄水道': {'index': 3798, 'place_name': 'パンデモニウム辺獄水道'},
           'パンデモニウム辺獄深層': {'index': 4135, 'place_name': 'パンデモニウム辺獄深層'},
           'ヒドゥンゴージ': {'index': 2589, 'place_name': 'ヒドゥンゴージ'},
           'ヒュペルボレア造物院': {'index': 3759, 'place_name': 'ヒュペルボレア造物院'},
           'フィスト・オブ・ゴルディオス': {'index': 1628,
                              'place_name': 'フィスト・オブ・ゴルディオス'},
           'フィスト・オブ・ミダース': {'index': 1708, 'place_name': 'フィスト・オブ・ミダース'},
           'フィールド・オブ・グローリー': {'index': 1740,
                              'place_name': 'フィールド・オブ・グローリー'},
           'フォルタン伯爵邸': {'index': 2320, 'place_name': 'フォルタン伯爵邸'},
           'フラクタル・コンティニアム': {'index': 2148, 'place_name': 'フラクタル・コンティニアム'},
           'フロンデール薬学院小児病棟': {'index': 695, 'place_name': 'フロンデール薬学院小児病棟'},
           'ブルースカイ': {'index': 2548, 'place_name': 'ブルースカイ'},
           'ブレイフロクスの野営地': {'index': 36, 'place_name': 'ブレイフロクスの野営地'},
           'ブレス・オブ・アレキサンダー': {'index': 1841,
                              'place_name': 'ブレス・オブ・アレキサンダー'},
           'プロピュライオン': {'index': 3926, 'place_name': 'プロピュライオン'},
           'ベラフディア遺跡風特設アスレチック': {'index': 2498,
                                 'place_name': 'ベラフディア遺跡風特設アスレチック'},
           'ペンダント居住館：居室': {'index': 3222, 'place_name': 'ペンダント居住館：居室'},
           'ホルミンスター': {'index': 3050, 'place_name': 'ホルミンスター'},
           'ホーンテッドフィースト': {'index': 3696, 'place_name': 'ホーンテッドフィースト'},
           'ポルタ・デクマーナ': {'index': 4032, 'place_name': 'ポルタ・デクマーナ'},
           'マザークリスタル': {'index': 3685, 'place_name': 'マザークリスタル'},
           'マトーヤのアトリエ': {'index': 3590, 'place_name': 'マトーヤのアトリエ'},
           'マトーヤの洞窟': {'index': 2036, 'place_name': 'マトーヤの洞窟'},
           'マリカの大井戸': {'index': 3139, 'place_name': 'マリカの大井戸'},
           'ミスト・ヴィレッジ': {'index': 425, 'place_name': 'ミスト・ヴィレッジ'},
           'ミスト・ヴィレッジ：コテージ': {'index': 1100,
                              'place_name': 'ミスト・ヴィレッジ：コテージ'},
           'ミスト・ヴィレッジ：ハウス': {'index': 1101, 'place_name': 'ミスト・ヴィレッジ：ハウス'},
           'ミスト・ヴィレッジ：プライベートルーム': {'index': 1157,
                                   'place_name': 'ミスト・ヴィレッジ：プライベートルーム'},
           'ミスト・ヴィレッジ：レジデンス': {'index': 1102,
                               'place_name': 'ミスト・ヴィレッジ：レジデンス'},
           'ミスト・ヴィレッジ：地下工房': {'index': 1227,
                              'place_name': 'ミスト・ヴィレッジ：地下工房'},
           'ミゼリー号': {'index': 1960, 'place_name': 'ミゼリー号'},
           'メインホール': {'index': 3817, 'place_name': 'メインホール'},
           'メテオの陰地': {'index': 1301, 'place_name': 'メテオの陰地'},
           'メテオ探査坑浅部': {'index': 464, 'place_name': 'メテオ探査坑浅部'},
           'メテオ探査坑深部': {'index': 465, 'place_name': 'メテオ探査坑深部'},
           'メーガドゥータ宮の客間': {'index': 4039, 'place_name': 'メーガドゥータ宮の客間'},
           'モルディオン監獄': {'index': 153, 'place_name': 'モルディオン監獄'},
           'モードゥナ': {'index': 67, 'place_name': 'モードゥナ'},
           'ヤンサ': {'index': 2410, 'place_name': 'ヤンサ'},
           'ユールモア': {'index': 2952, 'place_name': 'ユールモア'},
           'ユールモア監獄棟': {'index': 3595, 'place_name': 'ユールモア監獄棟'},
           'ライトフェザー闘技場': {'index': 2313, 'place_name': 'ライトフェザー闘技場'},
           'ラクサン城': {'index': 3620, 'place_name': 'ラクサン城'},
           'ラグナロク級三番艦：作戦室': {'index': 1304, 'place_name': 'ラグナロク級三番艦：作戦室'},
           'ラグナロク級三番艦：第一艦橋': {'index': 1305,
                              'place_name': 'ラグナロク級三番艦：第一艦橋'},
           'ラグナロク級三番艦：艦体中央部': {'index': 1303,
                               'place_name': 'ラグナロク級三番艦：艦体中央部'},
           'ラグナロク級六番艦：再生制御区': {'index': 1407,
                               'place_name': 'ラグナロク級六番艦：再生制御区'},
           'ラグナロク級六番艦：第一艦橋': {'index': 1408,
                              'place_name': 'ラグナロク級六番艦：第一艦橋'},
           'ラグナロク級六番艦：艦体中央部': {'index': 1406,
                               'place_name': 'ラグナロク級六番艦：艦体中央部'},
           'ラグナロク級四番艦：第一艦橋': {'index': 1410,
                              'place_name': 'ラグナロク級四番艦：第一艦橋'},
           'ラグナロク級拘束艦': {'index': 466, 'place_name': 'ラグナロク級拘束艦'},
           'ラケティカ大森林': {'index': 2957, 'place_name': 'ラケティカ大森林'},
           'ラザハン': {'index': 3707, 'place_name': 'ラザハン'},
           'ラベンダーベッド': {'index': 426, 'place_name': 'ラベンダーベッド'},
           'ラベンダーベッド：コテージ': {'index': 1106, 'place_name': 'ラベンダーベッド：コテージ'},
           'ラベンダーベッド：ハウス': {'index': 1107, 'place_name': 'ラベンダーベッド：ハウス'},
           'ラベンダーベッド：プライベートルーム': {'index': 1159,
                                  'place_name': 'ラベンダーベッド：プライベートルーム'},
           'ラベンダーベッド：レジデンス': {'index': 1108,
                              'place_name': 'ラベンダーベッド：レジデンス'},
           'ラベンダーベッド：地下工房': {'index': 1229, 'place_name': 'ラベンダーベッド：地下工房'},
           'ラヴィリンソス': {'index': 3708, 'place_name': 'ラヴィリンソス'},
           'ラールガーズリーチ': {'index': 2403, 'place_name': 'ラールガーズリーチ'},
           'リェー・ギア・ダンジョン': {'index': 3229, 'place_name': 'リェー・ギア・ダンジョン'},
           'リェー・ギア・ダンジョン祭殿': {'index': 3644,
                              'place_name': 'リェー・ギア・ダンジョン祭殿'},
           'リドルアナ大瀑布': {'index': 2451, 'place_name': 'リドルアナ大瀑布'},
           'リムサ・ロミンサ：上甲板層': {'index': 28, 'place_name': 'リムサ・ロミンサ：上甲板層'},
           'リムサ・ロミンサ：下甲板層': {'index': 29, 'place_name': 'リムサ・ロミンサ：下甲板層'},
           'リリーヒルズ：ロビー': {'index': 1813, 'place_name': 'リリーヒルズ：ロビー'},
           'リリーヒルズ：部屋': {'index': 1814, 'place_name': 'リリーヒルズ：部屋'},
           'レイクランド': {'index': 2953, 'place_name': 'レイクランド'},
           'レオファードの私室': {'index': 1804, 'place_name': 'レオファードの私室'},
           'レムナント': {'index': 4100, 'place_name': 'レムナント'},
           'レムレースのオフィス': {'index': 4022, 'place_name': 'レムレースのオフィス'},
           'ロータノ海': {'index': 462, 'place_name': 'ロータノ海'},
           'ワンダラーパレス': {'index': 37, 'place_name': 'ワンダラーパレス'},
           'ヴァナスパティ樹海': {'index': 4015, 'place_name': 'ヴァナスパティ樹海'},
           '不滅隊兵舎': {'index': 1801, 'place_name': '不滅隊兵舎'},
           '不語仙の座卓': {'index': 347, 'place_name': '不語仙の座卓'},
           '中央ザナラーン': {'index': 43, 'place_name': '中央ザナラーン'},
           '中央ラノシア': {'index': 30, 'place_name': '中央ラノシア'},
           '中枢区画': {'index': 468, 'place_name': '中枢区画'},
           '亡霊屋敷 ホーンテッドマナー': {'index': 1834,
                              'place_name': '亡霊屋敷 ホーンテッドマナー'},
           '交信雷波塔管制室': {'index': 3486, 'place_name': '交信雷波塔管制室'},
           '人形タチノ軍事基地': {'index': 3576, 'place_name': '人形タチノ軍事基地'},
           '低地ドラヴァニア': {'index': 2001, 'place_name': '低地ドラヴァニア'},
           '低地ラノシア': {'index': 31, 'place_name': '低地ラノシア'},
           '作戦立案室': {'index': 4023, 'place_name': '作戦立案室'},
           '供物穴': {'index': 2083, 'place_name': '供物穴'},
           '創生樹隔離棟': {'index': 4198, 'place_name': '創生樹隔離棟'},
           '劇場艇プリマビスタ・ブリッジ': {'index': 2371,
                              'place_name': '劇場艇プリマビスタ・ブリッジ'},
           '劇場艇プリマビスタ・大道具部屋': {'index': 2370,
                               'place_name': '劇場艇プリマビスタ・大道具部屋'},
           '北ザナラーン': {'index': 46, 'place_name': '北ザナラーン'},
           '十二神大聖堂': {'index': 112, 'place_name': '十二神大聖堂'},
           '南ザナラーン': {'index': 45, 'place_name': '南ザナラーン'},
           '南方ボズヤ戦線': {'index': 3534, 'place_name': '南方ボズヤ戦線'},
           '双蛇党兵舎': {'index': 1800, 'place_name': '双蛇党兵舎'},
           '古アムダプール市街': {'index': 125, 'place_name': '古アムダプール市街'},
           '古代の民の迷宮': {'index': 478, 'place_name': '古代の民の迷宮'},
           '古城アムダプール': {'index': 128, 'place_name': '古城アムダプール'},
           '古木の神判地': {'index': 1363, 'place_name': '古木の神判地'},
           '名もなき島': {'index': 4043, 'place_name': '名もなき島'},
           '呪髪の風塔': {'index': 4045, 'place_name': '呪髪の風塔'},
           '嘆きの海': {'index': 3711, 'place_name': '嘆きの海'},
           '外地ラノシア': {'index': 350, 'place_name': '外地ラノシア'},
           '大トゥパサの崇神所': {'index': 3228, 'place_name': '大トゥパサの崇神所'},
           '大氷河': {'index': 3487, 'place_name': '大氷河'},
           '大草原の狩場': {'index': 2448, 'place_name': '大草原の狩場'},
           '大迷宮バハムート': {'index': 1759, 'place_name': '大迷宮バハムート'},
           '失われた遺跡': {'index': 3542, 'place_name': '失われた遺跡'},
           '失われた都 ラバナスタ': {'index': 2372, 'place_name': '失われた都 ラバナスタ'},
           '妖精王の舞踏場': {'index': 3218, 'place_name': '妖精王の舞踏場'},
           '始皇帝の玉座': {'index': 3568, 'place_name': '始皇帝の玉座'},
           '宝物殿': {'index': 2295, 'place_name': '宝物殿'},
           '宿屋「ミズンマスト」': {'index': 733, 'place_name': '宿屋「ミズンマスト」'},
           '宿屋「砂時計亭」': {'index': 617, 'place_name': '宿屋「砂時計亭」'},
           '寄生生物隔離棟': {'index': 4196, 'place_name': '寄生生物隔離棟'},
           '対リヴァイアサン双胴船': {'index': 1334, 'place_name': '対リヴァイアサン双胴船'},
           '封じられた聖塔 リドルアナ': {'index': 2483, 'place_name': '封じられた聖塔 リドルアナ'},
           '希望ノ砲台：「塔」': {'index': 3647, 'place_name': '希望ノ砲台：「塔」'},
           '帰燕館': {'index': 2847, 'place_name': '帰燕館'},
           '影の国ダン・スカー': {'index': 1868, 'place_name': '影の国ダン・スカー'},
           '徳測りし前室': {'index': 3471, 'place_name': '徳測りし前室'},
           '応接室': {'index': 1429, 'place_name': '応接室'},
           '戒律の殻': {'index': 1390, 'place_name': '戒律の殻'},
           '旅籠「九つの雲」': {'index': 2310, 'place_name': '旅籠「九つの雲」'},
           '旅館「とまり木」': {'index': 548, 'place_name': '旅館「とまり木」'},
           '星導山寺院': {'index': 2707, 'place_name': '星導山寺院'},
           '星見の間 ': {'index': 3223, 'place_name': '星見の間 '},
           '暗闇の領域': {'index': 3596, 'place_name': '暗闇の領域'},
           '月の底': {'index': 3684, 'place_name': '月の底'},
           '望海楼': {'index': 2413, 'place_name': '望海楼'},
           '東ザナラーン': {'index': 44, 'place_name': '東ザナラーン'},
           '東ラノシア': {'index': 32, 'place_name': '東ラノシア'},
           '果ての終焉': {'index': 3686, 'place_name': '果ての終焉'},
           '楽欲の僧院 オーボンヌ': {'index': 2864, 'place_name': '楽欲の僧院 オーボンヌ'},
           '機工城アレキサンダー': {'index': 2041, 'place_name': '機工城アレキサンダー'},
           '機械遺跡の坑道': {'index': 3427, 'place_name': '機械遺跡の坑道'},
           '次元の狭間': {'index': 2737, 'place_name': '次元の狭間'},
           '次元の狭間：迎賓室': {'index': 379, 'place_name': '次元の狭間：迎賓室'},
           '武神の闘技場': {'index': 2081, 'place_name': '武神の闘技場'},
           '死者の宮殿': {'index': 1793, 'place_name': '死者の宮殿'},
           '決闘裁判場': {'index': 2336, 'place_name': '決闘裁判場'},
           '漆黒決戦 ノルヴラント': {'index': 3511, 'place_name': '漆黒決戦 ノルヴラント'},
           '灰の旅程': {'index': 3469, 'place_name': '灰の旅程'},
           '炎帝祭跡': {'index': 357, 'place_name': '炎帝祭跡'},
           '烈士庵': {'index': 2805, 'place_name': '烈士庵'},
           '無の大地': {'index': 3225, 'place_name': '無の大地'},
           '猛毒生物隔離棟': {'index': 4249, 'place_name': '猛毒生物隔離棟'},
           '獄之底': {'index': 2496, 'place_name': '獄之底'},
           '獄之蓋': {'index': 2762, 'place_name': '獄之蓋'},
           '獣闘の間': {'index': 694, 'place_name': '獣闘の間'},
           '生命神秘研究棟': {'index': 4250, 'place_name': '生命神秘研究棟'},
           '白帝の竹林': {'index': 2354, 'place_name': '白帝の竹林'},
           '石の家': {'index': 481, 'place_name': '石の家'},
           '砂の家': {'index': 356, 'place_name': '砂の家'},
           '神勇隊司令室': {'index': 346, 'place_name': '神勇隊司令室'},
           '神殿騎士団総長室': {'index': 2335, 'place_name': '神殿騎士団総長室'},
           '神門の間': {'index': 4024, 'place_name': '神門の間'},
           '禁忌都市マハ': {'index': 1742, 'place_name': '禁忌都市マハ'},
           '禁絶幻想': {'index': 2449, 'place_name': '禁絶幻想'},
           '稼働隔壁': {'index': 467, 'place_name': '稼働隔壁'},
           '第一艦橋': {'index': 469, 'place_name': '第一艦橋'},
           '筆頭神官の間': {'index': 4185, 'place_name': '筆頭神官の間'},
           '紅梅御殿：ロビー': {'index': 2272, 'place_name': '紅梅御殿：ロビー'},
           '紅梅御殿：部屋': {'index': 2273, 'place_name': '紅梅御殿：部屋'},
           '紅玉海': {'index': 2409, 'place_name': '紅玉海'},
           '紫水宮': {'index': 2779, 'place_name': '紫水宮'},
           '結晶化空間': {'index': 2715, 'place_name': '結晶化空間'},
           '絶望の園': {'index': 3635, 'place_name': '絶望の園'},
           '美神の地下神殿': {'index': 2299, 'place_name': '美神の地下神殿'},
           '群青空域': {'index': 2151, 'place_name': '群青空域'},
           '聖アンダリム神学院': {'index': 2337, 'place_name': '聖アンダリム神学院'},
           '聖ダナフェンの落涙': {'index': 392, 'place_name': '聖ダナフェンの落涙'},
           '聖モシャーヌ植物園': {'index': 2034, 'place_name': '聖モシャーヌ植物園'},
           '茨の園': {'index': 360, 'place_name': '茨の園'},
           '蒼天街': {'index': 3435, 'place_name': '蒼天街'},
           '蛇神大社': {'index': 2510, 'place_name': '蛇神大社'},
           '被検世界「シグマ」v1.0': {'index': 2717, 'place_name': '被検世界「シグマ」V1.0'},
           '被検世界「シグマ」v2.0': {'index': 2718, 'place_name': '被検世界「シグマ」V2.0'},
           '被検世界「シグマ」v3.0': {'index': 2719, 'place_name': '被検世界「シグマ」V3.0'},
           '被検世界「シグマ」v4.0': {'index': 2720, 'place_name': '被検世界「シグマ」V4.0'},
           '被検世界「デルタ」v1.0': {'index': 2357, 'place_name': '被検世界「デルタ」V1.0'},
           '被検世界「デルタ」v2.0': {'index': 2358, 'place_name': '被検世界「デルタ」V2.0'},
           '被検世界「デルタ」v3.0': {'index': 2359, 'place_name': '被検世界「デルタ」V3.0'},
           '被検世界「デルタ」v4.0': {'index': 2360, 'place_name': '被検世界「デルタ」V4.0'},
           '被検世界「プサイ」v1.0': {'index': 2725, 'place_name': '被検世界「プサイ」V1.0'},
           '被検世界「プサイ」v2.0': {'index': 2736, 'place_name': '被検世界「プサイ」V2.0'},
           '複製サレタ工場廃墟': {'index': 3425, 'place_name': '複製サレタ工場廃墟'},
           '西ザナラーン': {'index': 42, 'place_name': '西ザナラーン'},
           '西ラノシア': {'index': 33, 'place_name': '西ラノシア'},
           '詩想空間': {'index': 4098, 'place_name': '詩想空間'},
           '超越技術研究所': {'index': 2296, 'place_name': '超越技術研究所'},
           '輝ける神域 アグライア': {'index': 4167, 'place_name': '輝ける神域 アグライア'},
           '逆さの塔': {'index': 2088, 'place_name': '逆さの塔'},
           '醴泉神社参道': {'index': 2391, 'place_name': '醴泉神社参道'},
           '醴泉神社境内': {'index': 2392, 'place_name': '醴泉神社境内'},
           '銀冑団総長室': {'index': 354, 'place_name': '銀冑団総長室'},
           '闇の世界': {'index': 1431, 'place_name': '闇の世界'},
           '階差閉宇宙': {'index': 3017, 'place_name': '階差閉宇宙'},
           '雲廊': {'index': 406, 'place_name': '雲廊'},
           '高地ドラヴァニア': {'index': 2000, 'place_name': '高地ドラヴァニア'},
           '高地ラノシア': {'index': 34, 'place_name': '高地ラノシア'},
           '魔人の隠れ家': {'index': 4040, 'place_name': '魔人の隠れ家'},
           '魔大陸中枢': {'index': 2179, 'place_name': '魔大陸中枢'},
           '魔導城プラエトリウム': {'index': 430, 'place_name': '魔導城プラエトリウム'},
           '魔導雀荘「マンダヴィル」': {'index': 2549, 'place_name': '魔導雀荘「マンダヴィル」'},
           '魔科学研究所': {'index': 2147, 'place_name': '魔科学研究所'},
           '魔航船ヴォイドアーク': {'index': 2181, 'place_name': '魔航船ヴォイドアーク'},
           '黒渦団兵舎': {'index': 1802, 'place_name': '黒渦団兵舎'},
           '黒衣森：中央森林': {'index': 54, 'place_name': '黒衣森：中央森林'},
           '黒衣森：北部森林': {'index': 57, 'place_name': '黒衣森：北部森林'},
           '黒衣森：南部森林': {'index': 56, 'place_name': '黒衣森：南部森林'},
           '黒衣森：東部森林': {'index': 55, 'place_name': '黒衣森：東部森林'},
           '黙約の塔': {'index': 418, 'place_name': '黙約の塔'}}
}

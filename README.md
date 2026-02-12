#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERTAALMACHINE - Nederlands ➔ Frans (Thema: Eten)
Een offline educatieve tool voor alle leeftijden (8-99 jaar)
Functies: Vertalen, Antwoordcontrole, Quiz, Werkwoordvervoegingen
"""

import random
import os
import sys
from typing import Dict, List, Tuple, Optional

class VertaalMachine:
    """Offline vertaalmachine voor Nederlands-Frans voedsel vocabulaire"""
    
    def __init__(self):
        """Initialiseer de vertaalmachine met volledige woordenlijst"""
        self.words_database = self._initialize_database()
        self.history = []
        self.score = 0
        
    def _initialize_database(self) -> List[Dict]:
        """Initialiseer de complete woordenlijst met 200+ woorden"""
        return [
            # FRUIT (20 woorden)
            {"nl": "appel", "fr": "pomme", "cat": "fruit", "desc": "Rood/groen fruit"},
            {"nl": "banaan", "fr": "banane", "cat": "fruit", "desc": "Geel tropisch fruit"},
            {"nl": "citroen", "fr": "citron", "cat": "fruit", "desc": "Geel sappig fruit"},
            {"nl": "sinaasappel", "fr": "orange", "cat": "fruit", "desc": "Oranje citrusfruit"},
            {"nl": "druif", "fr": "raisin", "cat": "fruit", "desc": "Klein rond fruit"},
            {"nl": "aardbei", "fr": "fraise", "cat": "fruit", "desc": "Rood bosfruit"},
            {"nl": "blauwe bessen", "fr": "myrtilles", "cat": "fruit", "desc": "Blauw klein fruit"},
            {"nl": "framboos", "fr": "framboise", "cat": "fruit", "desc": "Rood bosfruit"},
            {"nl": "perzik", "fr": "pêche", "cat": "fruit", "desc": "Oranje zacht fruit"},
            {"nl": "peer", "fr": "poire", "cat": "fruit", "desc": "Groen/geel fruit"},
            {"nl": "ananas", "fr": "ananas", "cat": "fruit", "desc": "Tropisch prikkelend fruit"},
            {"nl": "mango", "fr": "mangue", "cat": "fruit", "desc": "Tropisch zoet fruit"},
            {"nl": "kiwi", "fr": "kiwi", "cat": "fruit", "desc": "Groen fruitzaadje"},
            {"nl": "meloen", "fr": "melon", "cat": "fruit", "desc": "Zoet rond fruit"},
            {"nl": "watermeloen", "fr": "pastèque", "cat": "fruit", "desc": "Groot watery fruit"},
            {"nl": "mandarijn", "fr": "mandarine", "cat": "fruit", "desc": "Klein citrusfruit"},
            {"nl": "grapefruit", "fr": "pamplemousse", "cat": "fruit", "desc": "Groot citrusfruit"},
            {"nl": "dadel", "fr": "datte", "cat": "fruit", "desc": "Zoet tropisch fruit"},
            {"nl": "vijg", "fr": "figue", "cat": "fruit", "desc": "Purper fruit"},
            {"nl": "abrikoos", "fr": "abricot", "cat": "fruit", "desc": "Oranje sappig fruit"},
            
            # GROENTEN (30 woorden)
            {"nl": "tomaat", "fr": "tomate", "cat": "groenten", "desc": "Rode groente"},
            {"nl": "ui", "fr": "oignon", "cat": "groenten", "desc": "Smaakmaker groente"},
            {"nl": "knoflook", "fr": "ail", "cat": "groenten", "desc": "Sterke geur groente"},
            {"nl": "wortel", "fr": "carotte", "cat": "groenten", "desc": "Oranje groente"},
            {"nl": "sla", "fr": "laitue", "cat": "groenten", "desc": "Groen bladgroente"},
            {"nl": "komkommer", "fr": "concombre", "cat": "groenten", "desc": "Groene groente"},
            {"nl": "paprika", "fr": "poivron", "cat": "groenten", "desc": "Gekleurde groente"},
            {"nl": "broccoli", "fr": "brocoli", "cat": "groenten", "desc": "Groene kruisbloemige plant"},
            {"nl": "bloemkool", "fr": "chou-fleur", "cat": "groenten", "desc": "Witte bloem"},
            {"nl": "spinazie", "fr": "épinards", "cat": "groenten", "desc": "Groen bladgroente"},
            {"nl": "erwten", "fr": "pois", "cat": "groenten", "desc": "Kleine groene bolletjes"},
            {"nl": "maïs", "fr": "maïs", "cat": "groenten", "desc": "Geel graan"},
            {"nl": "bonen", "fr": "haricots", "cat": "groenten", "desc": "Peulvrucht"},
            {"nl": "aardappel", "fr": "pomme de terre", "cat": "groenten", "desc": "Knol groente"},
            {"nl": "prei", "fr": "poireau", "cat": "groenten", "desc": "Ui-achtige plant"},
            {"nl": "courgette", "fr": "courgette", "cat": "groenten", "desc": "Groene squash"},
            {"nl": "aubergine", "fr": "aubergine", "cat": "groenten", "desc": "Paarse groente"},
            {"nl": "artisjok", "fr": "artichaut", "cat": "groenten", "desc": "Groen groente"},
            {"nl": "asperge", "fr": "asperge", "cat": "groenten", "desc": "Dunne stengel groente"},
            {"nl": "champignon", "fr": "champignon", "cat": "groenten", "desc": "Schimmel"},
            {"nl": "truffel", "fr": "truffe", "cat": "groenten", "desc": "Dure schimmel"},
            {"nl": "spruiten", "fr": "choux de Bruxelles", "cat": "groenten", "desc": "Kleine koolsoort"},
            {"nl": "kool", "fr": "chou", "cat": "groenten", "desc": "Groene koolsoort"},
            {"nl": "rode kool", "fr": "chou rouge", "cat": "groenten", "desc": "Paarse koolsoort"},
            {"nl": "witlof", "fr": "endive", "cat": "groenten", "desc": "Bleek groente"},
            {"nl": "rucola", "fr": "roquette", "cat": "groenten", "desc": "Pepperig groente"},
            {"nl": "biet", "fr": "betterave", "cat": "groenten", "desc": "Rode knol"},
            {"nl": "radijs", "fr": "radis", "cat": "groenten", "desc": "Scherp groente"},
            {"nl": "bataat", "fr": "patate douce", "cat": "groenten", "desc": "Zoete knol"},
            {"nl": "bieslook", "fr": "ciboulette", "cat": "groenten", "desc": "Kleine ui plant"},
            
            # VLEES & VIS (20 woorden)
            {"nl": "vlees", "fr": "viande", "cat": "vlees", "desc": "Eetbaar dierlijk product"},
            {"nl": "kip", "fr": "poulet", "cat": "vlees", "desc": "Vogelsvlees"},
            {"nl": "rund", "fr": "boeuf", "cat": "vlees", "desc": "Rundvlees"},
            {"nl": "varken", "fr": "porc", "cat": "vlees", "desc": "Varkensvlees"},
            {"nl": "lam", "fr": "agneau", "cat": "vlees", "desc": "Lammevlees"},
            {"nl": "kalkoen", "fr": "dinde", "cat": "vlees", "desc": "Grote vogel"},
            {"nl": "eend", "fr": "canard", "cat": "vlees", "desc": "Watervogel"},
            {"nl": "gans", "fr": "oie", "cat": "vlees", "desc": "Grote watervogel"},
            {"nl": "konijn", "fr": "lapin", "cat": "vlees", "desc": "Klein dier"},
            {"nl": "vis", "fr": "poisson", "cat": "vis", "desc": "Zeeproduct"},
            {"nl": "zalm", "fr": "saumon", "cat": "vis", "desc": "Roze vis"},
            {"nl": "forel", "fr": "truite", "cat": "vis", "desc": "Zoetwatervis"},
            {"nl": "tong", "fr": "sole", "cat": "vis", "desc": "Platvis"},
            {"nl": "schol", "fr": "plie", "cat": "vis", "desc": "Vlakvis"},
            {"nl": "mosselen", "fr": "moules", "cat": "vis", "desc": "Weekdier"},
            {"nl": "oesters", "fr": "huîtres", "cat": "vis", "desc": "Shell weekdier"},
            {"nl": "garnalen", "fr": "crevettes", "cat": "vis", "desc": "Kleine schaalvis"},
            {"nl": "inktvis", "fr": "poulpe", "cat": "vis", "desc": "Achtarmig weekdier"},
            {"nl": "haring", "fr": "hareng", "cat": "vis", "desc": "Zilveren vis"},
            {"nl": "tonijn", "fr": "thon", "cat": "vis", "desc": "Grote oceaanvis"},
            
            # ZUIVEL (15 woorden)
            {"nl": "melk", "fr": "lait", "cat": "zuivel", "desc": "Witte vloeistof van koe"},
            {"nl": "kaas", "fr": "fromage", "cat": "zuivel", "desc": "Zuivelproduct"},
            {"nl": "boter", "fr": "beurre", "cat": "zuivel", "desc": "Gemaakt van melk"},
            {"nl": "yoghurt", "fr": "yaourt", "cat": "zuivel", "desc": "Gefermenteerde zuivel"},
            {"nl": "roomkaas", "fr": "fromage à tartiner", "cat": "zuivel", "desc": "Zachte kaas"},
            {"nl": "mozzarella", "fr": "mozzarella", "cat": "zuivel", "desc": "Italiaanse kaas"},
            {"nl": "cheddar", "fr": "cheddar", "cat": "zuivel", "desc": "Harde kaas"},
            {"nl": "parmezaan", "fr": "parmesan", "cat": "zuivel", "desc": "Italiaanse harde kaas"},
            {"nl": "blauwschimmelkaas", "fr": "bleu", "cat": "zuivel", "desc": "Moldy kaas"},
            {"nl": "camembert", "fr": "camembert", "cat": "zuivel", "desc": "Franse zachte kaas"},
            {"nl": "emmental", "fr": "emmental", "cat": "zuivel", "desc": "Zwitserse gaten kaas"},
            {"nl": "smeltkaas", "fr": "fromage fondu", "cat": "zuivel", "desc": "Smelt kaas"},
            {"nl": "room", "fr": "crème", "cat": "zuivel", "desc": "Dikke melkproduct"},
            {"nl": "slagroom", "fr": "crème fouettée", "cat": "zuivel", "desc": "Geklopt melk"},
            {"nl": "karnemelk", "fr": "babeurre", "cat": "zuivel", "desc": "Zure melkdrank"},
            
            # BAKKERIJ (15 woorden)
            {"nl": "brood", "fr": "pain", "cat": "bakkerij", "desc": "Bakkerij product"},
            {"nl": "croissant", "fr": "croissant", "cat": "bakkerij", "desc": "Frans hoorngebak"},
            {"nl": "baguette", "fr": "baguette", "cat": "bakkerij", "desc": "Lang Frans brood"},
            {"nl": "focaccia", "fr": "focaccia", "cat": "bakkerij", "desc": "Italiaans olie brood"},
            {"nl": "pita", "fr": "pain pita", "cat": "bakkerij", "desc": "Zakbrood"},
            {"nl": "naan", "fr": "naan", "cat": "bakkerij", "desc": "Indisch brood"},
            {"nl": "tortilla", "fr": "tortilla", "cat": "bakkerij", "desc": "Mexicaans brood"},
            {"nl": "koekje", "fr": "biscuit", "cat": "bakkerij", "desc": "Krokant gebakje"},
            {"nl": "cake", "fr": "gâteau", "cat": "bakkerij", "desc": "Zoete taart"},
            {"nl": "taart", "fr": "tarte", "cat": "bakkerij", "desc": "Grote zoete lekkernij"},
            {"nl": "pannenkoek", "fr": "crêpe", "cat": "bakkerij", "desc": "Dunne cakevorm"},
            {"nl": "waffel", "fr": "gaufre", "cat": "bakkerij", "desc": "Tegelvorm gebak"},
            {"nl": "muffin", "fr": "muffin", "cat": "bakkerij", "desc": "Rond cupcake"},
            {"nl": "donut", "fr": "beignet", "cat": "bakkerij", "desc": "Oliebollensnoepje"},
            {"nl": "broodje", "fr": "petit pain", "cat": "bakkerij", "desc": "Klein brood"},
            
            # GERECHTEN (20 woorden)
            {"nl": "soep", "fr": "soupe", "cat": "gerechten", "desc": "Warm gerecht"},
            {"nl": "salade", "fr": "salade", "cat": "gerechten", "desc": "Koud gerecht met groenten"},
            {"nl": "pasta", "fr": "pâtes", "cat": "gerechten", "desc": "Italiaans gerecht"},
            {"nl": "pizza", "fr": "pizza", "cat": "gerechten", "desc": "Italiaans gebakken brood"},
            {"nl": "sandwich", "fr": "sandwich", "cat": "gerechten", "desc": "Dubbel brood voedsel"},
            {"nl": "burger", "fr": "burger", "cat": "gerechten", "desc": "Rundvlees brood"},
            {"nl": "sushi", "fr": "sushi", "cat": "gerechten", "desc": "Japanse rijst rol"},
            {"nl": "taco", "fr": "taco", "cat": "gerechten", "desc": "Mexicaans voedsel"},
            {"nl": "falafel", "fr": "falafel", "cat": "gerechten", "desc": "Kikkererwtengebak"},
            {"nl": "couscous", "fr": "couscous", "cat": "gerechten", "desc": "Noord-Afrikaans graan"},
            {"nl": "risotto", "fr": "risotto", "cat": "gerechten", "desc": "Italiaans rijst gerecht"},
            {"nl": "curry", "fr": "curry", "cat": "gerechten", "desc": "Aziatische bereiding"},
            {"nl": "omelet", "fr": "omelette", "cat": "gerechten", "desc": "Eigerecht"},
            {"nl": "ratatouille", "fr": "ratatouille", "cat": "gerechten", "desc": "Frans groente gerecht"},
            {"nl": "stew", "fr": "ragoût", "cat": "gerechten", "desc": "Stoofpot gerecht"},
            {"nl": "gratin", "fr": "gratin", "cat": "gerechten", "desc": "Ovenschotel"},
            {"nl": "quiche", "fr": "quiche", "cat": "gerechten", "desc": "Frans hartige taart"},
            {"nl": "bouillabaisse", "fr": "bouillabaisse", "cat": "gerechten", "desc": "Frans visgerecht"},
            {"nl": "cassoulet", "fr": "cassoulet", "cat": "gerechten", "desc": "Frans bonenstoof"},
            {"nl": "blanquette", "fr": "blanquette", "cat": "gerechten", "desc": "Frans witte stoof"},
            
            # DRANKEN (15 woorden)
            {"nl": "water", "fr": "eau", "cat": "dranken", "desc": "Helder vocht"},
            {"nl": "thee", "fr": "thé", "cat": "dranken", "desc": "Warm drankje"},
            {"nl": "koffie", "fr": "café", "cat": "dranken", "desc": "Donker warm drankje"},
            {"nl": "sap", "fr": "jus", "cat": "dranken", "desc": "Fruitvloeistof"},
            {"nl": "wijn", "fr": "vin", "cat": "dranken", "desc": "Alcoholisch drankje"},
            {"nl": "bier", "fr": "bière", "cat": "dranken", "desc": "Licht alcoholisch drankje"},
            {"nl": "frisdrank", "fr": "boisson gazeuse", "cat": "dranken", "desc": "Bruisend drankje"},
            {"nl": "milkshake", "fr": "milkshake", "cat": "dranken", "desc": "Melk drankje"},
            {"nl": "smoothie", "fr": "smoothie", "cat": "dranken", "desc": "Vloeibaar fruit mengsel"},
            {"nl": "limonade", "fr": "limonade", "cat": "dranken", "desc": "Citroendrank"},
            {"nl": "cider", "fr": "cidre", "cat": "dranken", "desc": "Appelwijn"},
            {"nl": "champagne", "fr": "champagne", "cat": "dranken", "desc": "Feestdrankje"},
            {"nl": "whisky", "fr": "whisky", "cat": "dranken", "desc": "Sterke drank"},
            {"nl": "vodka", "fr": "vodka", "cat": "dranken", "desc": "Scherpste drank"},
            {"nl": "rum", "fr": "rhum", "cat": "dranken", "desc": "Tropische drank"},
            
            # NOTEN & ZADEN (10 woorden)
            {"nl": "noot", "fr": "noix", "cat": "noten", "desc": "Harde schaal"},
            {"nl": "amandel", "fr": "amande", "cat": "noten", "desc": "Groenachtige noot"},
            {"nl": "pinda", "fr": "cacahuète", "cat": "noten", "desc": "Ondergrondse noot"},
            {"nl": "kastanje", "fr": "châtaigne", "cat": "noten", "desc": "Bruine herfst noot"},
            {"nl": "kokosnoot", "fr": "noix de coco", "cat": "noten", "desc": "Tropische noot"},
            {"nl": "pistache", "fr": "pistache", "cat": "noten", "desc": "Groene noot"},
            {"nl": "paranoot", "fr": "noix du Brésil", "cat": "noten", "desc": "Grote noot"},
            {"nl": "macadamianoot", "fr": "noix de macadamia", "cat": "noten", "desc": "Ronde noot"},
            {"nl": "hazelnoot", "fr": "noisette", "cat": "noten", "desc": "Bruine noot"},
            {"nl": "zonnebloempitten", "fr": "graines de tournesol", "cat": "noten", "desc": "Zaden"},
            
            # KRUIDEN & SPECERIJEN (20 woorden)
            {"nl": "zout", "fr": "sel", "cat": "kruiden", "desc": "Smaakmakend kristal"},
            {"nl": "peper", "fr": "poivre", "cat": "kruiden", "desc": "Hete kruid"},
            {"nl": "kaneel", "fr": "cannelle", "cat": "kruiden", "desc": "Bruin kruid"},
            {"nl": "nootmuskaat", "fr": "noix de muscade", "cat": "kruiden", "desc": "Warme kruid"},
            {"nl": "gember", "fr": "gingembre", "cat": "kruiden", "desc": "Pittig kruid"},
            {"nl": "kurkuma", "fr": "curcuma", "cat": "kruiden", "desc": "Geel kruid"},
            {"nl": "paprikapoeder", "fr": "paprika", "cat": "kruiden", "desc": "Rood kruid"},
            {"nl": "cayennepeper", "fr": "piment de Cayenne", "cat": "kruiden", "desc": "Hete kruid"},
            {"nl": "vanille", "fr": "vanille", "cat": "kruiden", "desc": "Zoete kruid"},
            {"nl": "peterselie", "fr": "persil", "cat": "kruiden", "desc": "Groen kruid"},
            {"nl": "dille", "fr": "aneth", "cat": "kruiden", "desc": "Groen kruid"},
            {"nl": "basilicum", "fr": "basilic", "cat": "kruiden", "desc": "Sappig kruid"},
            {"nl": "oregano", "fr": "origan", "cat": "kruiden", "desc": "Droog kruid"},
            {"nl": "timjan", "fr": "thym", "cat": "kruiden", "desc": "Lavendel kruid"},
            {"nl": "rozemarijn", "fr": "romarin", "cat": "kruiden", "desc": "Sterke kruid"},
            {"nl": "salie", "fr": "sauge", "cat": "kruiden", "desc": "Groen kruid"},
            {"nl": "munt", "fr": "menthe", "cat": "kruiden", "desc": "Verfrissend kruid"},
            {"nl": "bieslook", "fr": "ciboulette", "cat": "kruiden", "desc": "Kleine ui plant"},
            {"nl": "saffraan", "fr": "safran", "cat": "kruiden", "desc": "Goudkleurig kruid"},
            {"nl": "sterenis", "fr": "anis étoilé", "cat": "kruiden", "desc": "Sterrenvruchtkruid"},
            
            # ZOETSTOFFEN & SAUZEN (15 woorden)
            {"nl": "suiker", "fr": "sucre", "cat": "zoetstoffen", "desc": "Zoete stof"},
            {"nl": "honing", "fr": "miel", "cat": "zoetstoffen", "desc": "Zoete stof van bijen"},
            {"nl": "jam", "fr": "confiture", "cat": "conserven", "desc": "Ingemaakt fruit"},
            {"nl": "ketja", "fr": "catchup", "cat": "sausen", "desc": "Tomatensaus"},
            {"nl": "mayonaise", "fr": "mayonnaise", "cat": "sausen", "desc": "Emulsie saus"},
            {"nl": "mosterd", "fr": "moutarde", "cat": "sausen", "desc": "Pittige saus"},
            {"nl": "sojasaus", "fr": "sauce soja", "cat": "sausen", "desc": "Aziatische saus"},
            {"nl": "azijn", "fr": "vinaigre", "cat": "sausen", "desc": "Zure vloeistof"},
            {"nl": "pesto", "fr": "pesto", "cat": "sausen", "desc": "Basilicum saus"},
            {"nl": "salsa", "fr": "salsa", "cat": "sausen", "desc": "Tomatensaus dip"},
            {"nl": "hummus", "fr": "houmous", "cat": "gerechten", "desc": "Kikkererwten dip"},
            {"nl": "guacamole", "fr": "guacamole", "cat": "gerechten", "desc": "Avocado dip"},
            {"nl": "barbecuesaus", "fr": "sauce barbecue", "cat": "sausen", "desc": "Gerookt saus"},
            {"nl": "hollandaise", "fr": "sauce hollandaise", "cat": "sausen", "desc": "Buttery saus"},
            {"nl": "béchamel", "fr": "sauce béchamel", "cat": "sausen", "desc": "Witte saus"},
            
            # DESSERTS (15 woorden)
            {"nl": "ijsje", "fr": "glace", "cat": "dessert", "desc": "Koud dessert"},
            {"nl": "pudding", "fr": "pudding", "cat": "dessert", "desc": "Zachte vla"},
            {"nl": "yoghurtijs", "fr": "yaourt glacé", "cat": "dessert", "desc": "Bevroren yoghurt"},
            {"nl": "sorbet", "fr": "sorbet", "cat": "dessert", "desc": "Bevroren fruit"},
            {"nl": "créme brûlée", "fr": "crème brûlée", "cat": "dessert", "desc": "Gekarameliseerde room"},
            {"nl": "mousse", "fr": "mousse", "cat": "dessert", "desc": "Schuimige lekkernij"},
            {"nl": "panna cotta", "fr": "panna cotta", "cat": "dessert", "desc": "Italiaanse room dessert"},
            {"nl": "tiramisù", "fr": "tiramisu", "cat": "dessert", "desc": "Italiaanse lagenteert"},
            {"nl": "profiterole", "fr": "profiterole", "cat": "dessert", "desc": "Kleine room gebak"},
            {"nl": "éclair", "fr": "éclair", "cat": "dessert", "desc": "Langwerpig gebak"},
            {"nl": "chocolade", "fr": "chocolat", "cat": "snoep", "desc": "Zoete lekkernij"},
            {"nl": "snoep", "fr": "bonbon", "cat": "snoep", "desc": "Kleine zoete snoepjes"},
            {"nl": "caramel", "fr": "caramel", "cat": "snoep", "desc": "Gekarameliseerde snoep"},
            {"nl": "nougat", "fr": "nougat", "cat": "snoep", "desc": "Noten snoep"},
            {"nl": "fudge", "fr": "fudge", "cat": "snoep", "desc": "Zachte chocolade"},
            
            # WERKWOORDEN (15 woorden met vervoegingen)
            {
                "nl": "eten", "fr": "manger", "cat": "werkwoorden", "desc": "Voedsel naar binnen nemen",
                "conj": {"present": {"ik": "mange", "jij": "manges", "hij": "mange", "wij": "mangeons", "jullie": "mangez", "zij": "mangent"},
                         "past": {"ik": "ai mangé", "jij": "as mangé", "hij": "a mangé", "wij": "avons mangé", "jullie": "avez mangé", "zij": "ont mangé"},
                         "future": {"ik": "mangerai", "jij": "mangeras", "hij": "mangera", "wij": "mangerons", "jullie": "mangerez", "zij": "mangeront"}}
            },
            {
                "nl": "drinken", "fr": "boire", "cat": "werkwoorden", "desc": "Vloeistof naar binnen nemen",
                "conj": {"present": {"ik": "bois", "jij": "bois", "hij": "boit", "wij": "buvons", "jullie": "buvez", "zij": "boivent"},
                         "past": {"ik": "ai bu", "jij": "as bu", "hij": "a bu", "wij": "avons bu", "jullie": "avez bu", "zij": "ont bu"},
                         "future": {"ik": "boirai", "jij": "boiras", "hij": "boira", "wij": "boirons", "jullie": "boirez", "zij": "boiront"}}
            },
            {
                "nl": "koken", "fr": "cuisiner", "cat": "werkwoorden", "desc": "Voedsel bereiden",
                "conj": {"present": {"ik": "cuisine", "jij": "cuisines", "hij": "cuisine", "wij": "cuisinons", "jullie": "cuisinez", "zij": "cuisinent"},
                         "past": {"ik": "ai cuisiné", "jij": "as cuisiné", "hij": "a cuisiné", "wij": "avons cuisiné", "jullie": "avez cuisiné", "zij": "ont cuisiné"},
                         "future": {"ik": "cuisinerai", "jij": "cuisineras", "hij": "cuisinera", "wij": "cuisinerons", "jullie": "cuisinerez", "zij": "cuisineront"}}
            },
            {
                "nl": "bakken", "fr": "cuire", "cat": "werkwoorden", "desc": "Met hitte bereiden",
                "conj": {"present": {"ik": "cuis", "jij": "cuis", "hij": "cuit", "wij": "cuisons", "jullie": "cuisez", "zij": "cuisent"},
                         "past": {"ik": "ai cuit", "jij": "as cuit", "hij": "a cuit", "wij": "avons cuit", "jullie": "avez cuit", "zij": "ont cuit"},
                         "future": {"ik": "cuirai", "jij": "cuiras", "hij": "cuira", "wij": "cuirons", "jullie": "cuirez", "zij": "cuiront"}}
            },
            {
                "nl": "snijden", "fr": "couper", "cat": "werkwoorden", "desc": "Met mes verdelen",
                "conj": {"present": {"ik": "coupe", "jij": "coupes", "hij": "coupe", "wij": "coupons", "jullie": "coupez", "zij": "coupent"},
                         "past": {"ik": "ai coupé", "jij": "as coupé", "hij": "a coupé", "wij": "avons coupé", "jullie": "avez coupé", "zij": "ont coupé"},
                         "future": {"ik": "couperai", "jij": "couperas", "hij": "coupera", "wij": "couperons", "jullie": "couperez", "zij": "couperont"}}
            },
            {
                "nl": "mengen", "fr": "mélanger", "cat": "werkwoorden", "desc": "Combineren ingrediënten",
                "conj": {"present": {"ik": "mélange", "jij": "mélanges", "hij": "mélange", "wij": "mélangeons", "jullie": "mélangez", "zij": "mélangent"},
                         "past": {"ik": "ai mélangé", "jij": "as mélangé", "hij": "a mélangé", "wij": "avons mélangé", "jullie": "avez mélangé", "zij": "ont mélangé"},
                         "future": {"ik": "mélangerai", "jij": "mélangeras", "hij": "mélangera", "wij": "mélangerons", "jullie": "mélangerez", "zij": "mélangeront"}}
            },
            {
                "nl": "toevoegen", "fr": "ajouter", "cat": "werkwoorden", "desc": "Erbij doen",
                "conj": {"present": {"ik": "ajoute", "jij": "ajoutes", "hij": "ajoute", "wij": "ajoutons", "jullie": "ajoutez", "zij": "ajoutent"},
                         "past": {"ik": "ai ajouté", "jij": "as ajouté", "hij": "a ajouté", "wij": "avons ajouté", "jullie": "avez ajouté", "zij": "ont ajouté"},
                         "future": {"ik": "ajouterai", "jij": "ajouteras", "hij": "ajoutera", "wij": "ajouterons", "jullie": "ajouterez", "zij": "ajouteront"}}
            },
            {
                "nl": "serveren", "fr": "servir", "cat": "werkwoorden", "desc": "Geven voedsel",
                "conj": {"present": {"ik": "sers", "jij": "sers", "hij": "sert", "wij": "servons", "jullie": "servez", "zij": "servent"},
                         "past": {"ik": "ai servi", "jij": "as servi", "hij": "a servi", "wij": "avons servi", "jullie": "avez servi", "zij": "ont servi"},
                         "future": {"ik": "servirai", "jij": "serviras", "hij": "servira", "wij": "servirons", "jullie": "servirez", "zij": "serviront"}}
            },
            {
                "nl": "proeven", "fr": "goûter", "cat": "werkwoorden", "desc": "Smaak testen",
                "conj": {"present": {"ik": "goûte", "jij": "goûtes", "hij": "goûte", "wij": "goûtons", "jullie": "goûtez", "zij": "goûtent"},
                         "past": {"ik": "ai goûté", "jij": "as goûté", "hij": "a goûté", "wij": "avons goûté", "jullie": "avez goûté", "zij": "ont goûté"},
                         "future": {"ik": "goûterai", "jij": "goûteras", "hij": "goûtera", "wij": "goûterons", "jullie": "goûterez", "zij": "goûteront"}}
            },
            {
                "nl": "wassen", "fr": "laver", "cat": "werkwoorden", "desc": "Schoon maken",
                "conj": {"present": {"ik": "lave", "jij": "laves", "hij": "lave", "wij": "lavons", "jullie": "lavez", "zij": "lavent"},
                         "past": {"ik": "ai lavé", "jij": "as lavé", "hij": "a lavé", "wij": "avons lavé", "jullie": "avez lavé", "zij": "ont lavé"},
                         "future": {"ik": "laverai", "jij": "laveras", "hij": "lavera", "wij": "laverons", "jullie": "laverez", "zij": "laveront"}}
            },
            {
                "nl": "smaken", "fr": "avoir le goût de", "cat": "werkwoorden", "desc": "Smaak hebben",
                "conj": {"present": {"ik": "goûte de", "jij": "goûtes de", "hij": "goûte de", "wij": "goutons de", "jullie": "goûtez de", "zij": "goûtent de"},
                         "past": {"ik": "ai eu le goût de", "jij": "as eu le goût de", "hij": "a eu le goût de", "wij": "avons eu le goût de", "jullie": "avez eu le goût de", "zij": "ont eu le goût de"},
                         "future": {"ik": "aurai le goût de", "jij": "auras le goût de", "hij": "aura le goût de", "wij": "aurons le goût de", "jullie": "aurez le goût de", "zij": "auront le goût de"}}
            },
            {
                "nl": "roken", "fr": "fumer", "cat": "werkwoorden", "desc": "Dampen loslaten",
                "conj": {"present": {"ik": "fume", "jij": "fumes", "hij": "fume", "wij": "fumons", "jullie": "fumez", "zij": "fument"},
                         "past": {"ik": "ai fumé", "jij": "as fumé", "hij": "a fumé", "wij": "avons fumé", "jullie": "avez fumé", "zij": "ont fumé"},
                         "future": {"ik": "fumerai", "jij": "fumeras", "hij": "fumera", "wij": "fumerons", "jullie": "fumerez", "zij": "fumeront"}}
            },
            {
                "nl": "kauwen", "fr": "mâcher", "cat": "werkwoorden", "desc": "Fijn maken met tanden",
                "conj": {"present": {"ik": "mâche", "jij": "mâches", "hij": "mâche", "wij": "mâchons", "jullie": "mâchez", "zij": "mâchent"},
                         "past": {"ik": "ai mâché", "jij": "as mâché", "hij": "a mâché", "wij": "avons mâché", "jullie": "avez mâché", "zij": "ont mâché"},
                         "future": {"ik": "mâcherai", "jij": "mâcheras", "hij": "mâchera", "wij": "mâcherons", "jullie": "mâcherez", "zij": "mâcheront"}}
            },
            {
                "nl": "roosteren", "fr": "rôtir", "cat": "werkwoorden", "desc": "In oven bereiden",
                "conj": {"present": {"ik": "rôtis", "jij": "rôtis", "hij": "rôtit", "wij": "rôtissons", "jullie": "rôtissez", "zij": "rôtissent"},
                         "past": {"ik": "ai rôti", "jij": "as rôti", "hij": "a rôti", "wij": "avons rôti", "jullie": "avez rôti", "zij": "ont rôti"},
                         "future": {"ik": "rôtirai", "jij": "rôtiras", "hij": "rôtira", "wij": "rôtirons", "jullie": "rôtirez", "zij": "rôtiront"}}
            },
        ]
    
    def translate_word(self, word: str) -> Optional[Dict]:
        """Vertaal een Nederlands woord naar het Frans"""
        word_lower = word.lower().strip()
        for entry in self.words_database:
            if entry["nl"].lower() == word_lower:
                return entry
        return None
    
    def check_answer(self, dutch_word: str, user_answer: str) -> Tuple[bool, str]:
        """Controleer of het gegeven antwoord correct is"""
        user_answer = user_answer.lower().strip()
        translation = self.translate_word(dutch_word)
        
        if translation is None:
            return False, f"❌ '{dutch_word}' niet in database gevonden."
        
        correct_french = translation["fr"].lower()
        
        if user_answer == correct_french:
            return True, f"✅ Correct! '{dutch_word}' = '{translation['fr']}'"
        else:
            return False, f"❌ Fout! Het juiste antwoord is: '{translation['fr']}'"
    
    def get_conjugation(self, dutch_word: str, tense: str = "present") -> Optional[Dict]:
        """Geef werkwoordvervoegingen voor verschillende tijden"""
        translation = self.translate_word(dutch_word)
        
        if translation is None or "conj" not in translation:
            return None
        
        conjugations = translation.get("conj", {})
        return conjugations.get(tense, None)
    
    def get_words_by_category(self, category: str) -> List[Dict]:
        """Geef alle woorden van een bepaalde categorie"""
        return [w for w in self.words_database if w.get("cat") == category]
    
    def get_all_categories(self) -> List[str]:
        """Geef alle beschikbare categorieën"""
        return sorted(list(set(w.get("cat") for w in self.words_database)))
    
    def get_random_words(self, count: int = 5) -> List[Dict]:
        """Geef willekeurige woorden voor oefening"""
        return random.sample(self.words_database, min(count, len(self.words_database)))
    
    def quiz_mode(self, num_questions: int = 10) -> Dict:
        """Interactieve quiz-modus"""
        score = 0
        words = self.get_random_words(num_questions)
        results = []
        
        print("\n" + "="*70)
        print("🎓 QUIZ MODE - Vertaal Nederlands naar Frans (Thema: Eten)")
        print("="*70 + "\n")
        
        for i, word_entry in enumerate(words, 1):
            dutch = word_entry["nl"]
            print(f"[{i}/{num_questions}] Wat is het Franse woord voor '{dutch}'?")
            user_input = input("📝 Jouw antwoord: ").strip()
            
            is_correct, message = self.check_answer(dutch, user_input)
            print(message)
            
            if is_correct:
                score += 1
            
            results.append({
                "word": dutch,
                "user_answer": user_input,
                "correct": is_correct,
                "correct_answer": word_entry["fr"]
            })
            print()
        
        percentage = (score / num_questions) * 100
        print("="*70)
        print(f"📊 Quiz afgerond!")
        print(f"   Score: {score}/{num_questions} ({percentage:.1f}%)")
        print("="*70 + "\n")
        
        return {"score": score, "total": num_questions, "percentage": percentage, "results": results}
    
    def show_conjugations_interactive(self):
        """Toon werkwoordvervoegingen interactief"""
        print("\n" + "="*70)
        print("📚 WERKWOORD VERVOEGINGEN")
        print("="*70 + "\n")
        
        verbs = [w for w in self.words_database if w.get("cat") == "werkwoorden"]
        
        print("Beschikbare werkwoorden:")
        for i, verb in enumerate(verbs, 1):
            print(f"  {i}. {verb['nl']} ({verb['fr']})")
        
        while True:
            choice = input("\nKies een werkwoord (nummer) of 'exit': ").strip()
            
            if choice.lower() == "exit":
                break
            
            try:
                verb_idx = int(choice) - 1
                if 0 <= verb_idx < len(verbs):
                    verb = verbs[verb_idx]
                    print(f"\n✨ Vervoegingen voor '{verb['nl']}' ({verb['fr']}):\n")
                    
                    if "conj" in verb:
                        for tense, forms in verb["conj"].items():
                            print(f"  📖 {tense.upper()}:")
                            for pronoun, form in forms.items():
                                print(f"     {pronoun:12} → {form}")
                            print()
                    else:
                        print("  ❌ Geen vervoegingen beschikbaar")
                else:
                    print("❌ Ongeldige keuze")
            except ValueError:
                print("❌ Voer een getal in")
    
    def interactive_mode(self):
        """Interactieve vertalingsmodus"""
        print("\n" + "="*70)
        print("🌐 INTERACTIEVE VERTAALMACHINE - Nederlands ➔ Frans")
        print("   Thema: Eten | Voor alle leeftijden (8-99 jaar)")
        print("="*70)
        print("\n📋 BESCHIKBARE COMMANDO'S:")
        print("  • vertaal <woord>         - Vertaal een Nederlands woord")
        print("  • check <woord> <antwoord> - Controleer jouw antwoord")
        print("  • quiz [aantal]           - Start quiz-modus (standaard 10 vragen)")
        print("  • conjugatie <woord> [tense] - Toon werkwoordvervoegingen")
        print("  • categorieën             - Toon alle categorieën")
        print("  • toon [aantal]           - Toon willekeurige woorden")
        print("  • categorie [naam]        - Toon woorden van categorie")
        print("  • exit                    - Afsluiten")
        print("="*70 + "\n")
        
        while True:
            command = input("📝 Voer een opdracht in: ").strip().lower()
            
            if command == "exit":
                print("\n👋 Tot ziens! Veel succes met Frans leren! 🎉\n")
                break
            
            elif command.startswith("vertaal "):
                word = command.replace("vertaal ", "").strip()
                translation = self.translate_word(word)
                if translation:
                    print(f"\n✅ {translation['nl']} = {translation['fr']}")
                    if "desc" in translation:
                        print(f"   📖 {translation['desc']}")
                    print()
                else:
                    print(f"\n❌ '{word}' niet gevonden in database.\n")
            
            elif command.startswith("check "):
                parts = command.replace("check ", "").split(" ", 1)
                if len(parts) == 2:
                    dutch, answer = parts
                    is_correct, message = self.check_answer(dutch, answer)
                    print(f"\n{message}\n")
                else:
                    print("\n❌ Gebruik: check <nederlands woord> <jouw antwoord>\n")
            
            elif command.startswith("conjugatie "):
                parts = command.replace("conjugatie ", "").split()
                word = parts[0]
                tense = parts[1] if len(parts) > 1 else "present"
                
                conjugation = self.get_conjugation(word, tense)
                if conjugation:
                    print(f"\n✅ Vervoegingen voor '{word}' ({tense}):")
                    for pronoun, form in conjugation.items():
                        print(f"   {pronoun:12} → {form}")
                    print()
                else:
                    print(f"\n❌ Geen vervoegingen gevonden voor '{word}'\n")
            
            elif command == "categorieën":
                cats = self.get_all_categories()
                print(f"\n📚 Beschikbare categorieën ({len(cats)}):")
                for cat in cats:
                    count = len(self.get_words_by_category(cat))
                    print(f"   • {cat} ({count} woorden)")
                print()
            
            elif command.startswith("categorie "):
                cat_name = command.replace("categorie ", "").strip()
                words = self.get_words_by_category(cat_name)
                if words:
                    print(f"\n📚 Woorden in categorie '{cat_name}' ({len(words)}):")
                    for w in words:
                        print(f"   • {w['nl']:20} = {w['fr']}")
                    print()
                else:
                    print(f"\n❌ Categorie '{cat_name}' niet gevonden.\n")
            
            elif command.startswith("toon "):
                try:
                    count = int(command.replace("toon ", ""))
                    words = self.get_random_words(count)
                    print(f"\n📚 {count} willekeurige woorden:")
                    for w in words:
                        print(f"   • {w['nl']:20} = {w['fr']}")
                    print()
                except ValueError:
                    print("\n❌ Voer een getal in.\n")
            
            elif command.startswith("quiz"):
                try:
                    num = int(command.replace("quiz", "").strip()) if "quiz " in command else 10
                    self.quiz_mode(num)
                except ValueError:
                    print("\n❌ Voer een geldig getal in.\n")
            
            else:
                print("\n❌ Onbekende opdracht. Probeer opnieuw.\n")


def main():
    """Hoofdfunctie"""
    print("\n" + "🌟"*35)
    print("\n   WELKOM BIJ DE VERTAALMACHINE!")
    print("   Nederlands ➔ Frans (Thema: Eten)")
    print("   Offline | Gratis | Voor iedereen (8-99 jaar)")
    print("\n" + "🌟"*35 + "\n")
    
    vm = VertaalMachine()
    vm.interactive_mode()


if __name__ == "__main__":
    main()

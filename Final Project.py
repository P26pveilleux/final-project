import turtle
import random



european_countries = {
    "Norway": ["This country is famous for its fjords.", "It is the homeland of Vikings.", "The capital city is Oslo."],
    "Switzerland": ["This country is known for its delicious chocolate and watches.", "It is home to the Alps.", "The official languages spoken are German, French, Italian, and Romansh."],
    "France": ["This country is renowned for its cuisine and wine.", "It is home to the Eiffel Tower.", "The capital city is Paris."],
    "Italy": ["This country is famous for its art, architecture, and history.", "It is home to the Colosseum and the Vatican City.", "The capital city is Rome."],
    "Germany": ["This country is known for its precision engineering and beer.", "It is home to the Berlin Wall remnants.", "The capital city is Berlin."],
    "Spain": ["This country is known for its vibrant culture, including flamenco music and dance.", "It is home to landmarks like Sagrada Familia and Alhambra.", "The capital city is Madrid."],
    "United Kingdom": ["This country is famous for its royal family and iconic landmarks like Big Ben and Buckingham Palace.", "It consists of four constituent countries: England, Scotland, Wales, and Northern Ireland.", "The capital city is London."],
    "Greece": ["This country is known for its ancient history, including the Acropolis and Parthenon.", "It is considered the cradle of Western civilization.", "The capital city is Athens."],
    "Sweden": ["This country is known for its design, particularly in furniture and home goods.", "It is home to the ABBA museum and the Icehotel.", "The capital city is Stockholm."],
    "Netherlands": ["This country is famous for its windmills, tulips, and canals.", "It is known for its cycling culture.", "The capital city is Amsterdam."],
    "Albania": ["This country is known for its stunning coastline and ancient castles.", "It is one of the last countries in Europe to embrace democracy.", "The capital city is Tirana."],
    "Andorra": ["This country is famous for its ski resorts and tax haven status.", "It is one of the smallest countries in the world.", "The capital city is Andorra la Vella."],
    "Austria": ["This country is renowned for its classical music heritage and imperial history.", "It is home to the Alps and picturesque villages.", "The capital city is Vienna."],
    "Belarus": ["This country is known for its Soviet-era architecture and vast forests.", "It is often called Europe's last dictatorship.", "The capital city is Minsk."],
    "Belgium": ["This country is famous for its waffles, chocolate, and beer.", "It is home to the headquarters of the European Union.", "The capital city is Brussels."],
    "Bosnia and Herzegovina": ["This country is known for its historic Ottoman and Austro-Hungarian architecture.", "It has a complex ethnic and religious makeup.", "The capital city is Sarajevo."],
    "Bulgaria": ["This country is famous for its Black Sea coastline and ski resorts.", "It is home to a rich cultural heritage, including Thracian, Greek, and Roman ruins.", "The capital city is Sofia."],
    "Croatia": ["This country is renowned for its Adriatic coastline, medieval cities, and islands.", "It is known for its Game of Thrones filming locations.", "The capital city is Zagreb."],
    "Cyprus": ["This country is famous for its beaches, ancient ruins, and halloumi cheese.", "It is the birthplace of Aphrodite in Greek mythology.", "The capital city is Nicosia."],
    "Czech Republic": ["This country is known for its medieval architecture, beer, and historical sites.", "It is home to Prague Castle and Charles Bridge.", "The capital city is Prague."],
    "Denmark": ["This country is famous for its fairy-tale castles, Viking history, and hygge lifestyle.", "It is home to the oldest monarchy in the world.", "The capital city is Copenhagen."],
    "Estonia": ["This country is known for its digital society and medieval architecture.", "It is one of the least populous countries in the European Union.", "The capital city is Tallinn."],
    "Finland": ["This country is famous for its lakes, forests, and saunas.", "It is known for its design, including Marimekko and Iittala.", "The capital city is Helsinki."],
    "Greece": ["This country is known for its ancient history, including the Acropolis and Parthenon.", "It is considered the cradle of Western civilization.", "The capital city is Athens."],
    "Hungary": ["This country is famous for its thermal baths, paprika, and goulash.", "It is home to the largest synagogue in Europe.", "The capital city is Budapest."],
    "Iceland": ["This country is known for its stunning landscapes, including glaciers, volcanoes, and geysers.", "It is one of the most geologically active places in the world.", "The capital city is Reykjavik."],
    "Ireland": ["This country is famous for its lush green landscapes, friendly people, and pubs.", "It is known for its folklore, music, and literature.", "The capital city is Dublin."],
    "Kosovo": ["This country is known for its disputed status and recent history.", "It declared independence from Serbia in 2008.", "The capital city is Pristina."],
    "Latvia": ["This country is famous for its Baltic coastline, forests, and medieval Old Towns.", "It is one of the greenest countries in the world.", "The capital city is Riga."],
    "Liechtenstein": ["This country is known for its mountain villages, alpine landscapes, and low taxes.", "It is one of the wealthiest countries in the world.", "The capital city is Vaduz."],
    "Lithuania": ["This country is famous for its Baltic coastline, medieval architecture, and pagan roots.", "It has a long history of resistance to foreign domination.", "The capital city is Vilnius."],
    "Luxembourg": ["This country is known for its high standard of living and international finance sector.", "It is one of the founding members of the European Union.", "The capital city is Luxembourg City."],
    "Malta": ["This country is famous for its historic sites, including prehistoric temples and medieval towns.", "It is one of the smallest and most densely populated countries in the world.", "The capital city is Valletta."],
    "Moldova": ["This country is known for its wine culture and Soviet heritage.", "It is one of the least visited countries in Europe.", "The capital city is Chisinau."],
    "Monaco": ["This country is famous for its glamorous casinos, yacht-lined harbor, and Formula One Grand Prix.", "It is one of the wealthiest countries in the world.", "The capital city is Monaco."],
    "Montenegro": ["This country is known for its rugged mountains, medieval villages, and Adriatic coastline.", "It is one of the youngest countries in the world, gaining independence in 2006.", "The capital city is Podgorica."],
    "Netherlands": ["This country is famous for its windmills, tulips, and canals.", "It is known for its cycling culture.", "The capital city is Amsterdam."],
    "North Macedonia": ["This country is known for its Ottoman and Byzantine heritage, including the ancient city of Ohrid.", "It was formerly part of Yugoslavia.", "The capital city is Skopje."],
    "Poland": ["This country is famous for its medieval architecture, vodka, and pierogi.", "It is home to Auschwitz-Birkenau, a former Nazi concentration camp.", "The capital city is Warsaw."],
    "Portugal": ["This country is known for its historic cities, picturesque landscapes, and delicious cuisine.", "It is famous for its explorers, including Vasco da Gama and Ferdinand Magellan.", "The capital city is Lisbon."],
    "Romania": ["This country is famous for its castles, including Bran Castle, often associated with Dracula.", "It is home to one of the largest populations of brown bears in Europe.", "The capital city is Bucharest."],
    "Russia": ["This country is known for its vast size, diverse landscapes, and rich cultural heritage.", "It is the largest country in the world by land area.", "The capital city is Moscow."],
    "San Marino": ["This country is famous for its medieval architecture and being the world's oldest republic.", "It is surrounded by Italy.", "The capital city is San Marino."],
    "Serbia": ["This country is known for its hospitality, rakija, and vibrant nightlife.", "It was part of Yugoslavia until its dissolution in the 1990s.", "The capital city is Belgrade."],
     "Slovakia": ["This country is known for its stunning castles, medieval towns, and natural landscapes.", "It was formerly part of Czechoslovakia.", "The capital city is Bratislava."],
    "Slovenia": ["This country is famous for its picturesque landscapes, including Lake Bled and the Julian Alps.", "It is one of the most forested countries in Europe.", "The capital city is Ljubljana."],
    "Spain": ["This country is known for its vibrant culture, including flamenco music and dance.", "It is home to landmarks like Sagrada Familia and Alhambra.", "The capital city is Madrid."],
    "Sweden": ["This country is known for its design, particularly in furniture and home goods.", "It is home to the ABBA museum and the Icehotel.", "The capital city is Stockholm."],
    "Switzerland": ["This country is known for its delicious chocolate and watches.", "It is home to the Alps.", "The official languages spoken are German, French, Italian, and Romansh."],
    "Turkey": ["This country is known for its unique location bridging Europe and Asia.", "It has a rich history, including the Ottoman Empire and Byzantine architecture.", "The capital city is Ankara."],
    "Ukraine": ["This country is famous for its diverse landscapes, including the Carpathian Mountains and Black Sea coastline.", "It is the largest country in Europe by land area.", "The capital city is Kyiv."],
    "United Kingdom (UK)": ["This country is famous for its royal family and iconic landmarks like Big Ben and Buckingham Palace.", "It consists of four constituent countries: England, Scotland, Wales, and Northern Ireland.", "The capital city is London."],
    "Vatican City (Holy See)": ["This country is known for being the spiritual and administrative center of the Roman Catholic Church.", "It is the smallest independent state in the world by both area and population.", "The capital city is Vatican City."]
   
   
}

def display_facts(country):
    print("\nFacts about", country + ":")
    for fact in european_countries[country]:
        print("-", fact)

def eurofacts_quiz():
    print("Welcome to EuroFacts Quiz! Test your knowledge about European countries by guessing the country based on three facts. Let's begin!\n")

    # Shuffle the list of European countries
    countries = list(european_countries.keys())
    random.shuffle(countries)

    score = 0
    total_questions = 0

    for country in countries:
        total_questions += 1
        display_facts(country)
        guess = input("\nYour guess: ").strip().title()

        if guess == country:
            print("Correct! The answer is", country + ".")
            score += 1
        else:
            print("Incorrect! The correct answer is", country + ".")

    print("\nYour final score:", score, "out of", total_questions)

# Run the quiz
eurofacts_quiz()

import random

us_state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

def display_state(state):
    print("\nWhat is the capital of", state + "?")

def us_state_capitals_quiz():
    print("Welcome to the U.S. State Capitals Quiz! Test your knowledge by guessing the capital of each state. Let's begin!\n")

    # Shuffle the list of U.S. states
    states = list(us_state_capitals.keys())
    random.shuffle(states)

    score = 0
    total_questions = 0

    for state in states:
        total_questions += 1
        display_state(state)
        guess = input("\nYour guess: ").strip().title()

        if guess == us_state_capitals[state]:
            print("Correct! The capital of", state, "is", us_state_capitals[state] + ".")
            score += 1
        else:
            print("Incorrect! The capital of", state, "is", us_state_capitals[state] + ".")

    print("\nYour final score:", score, "out of", total_questions)

# Run the quiz
us_state_capitals_quiz()
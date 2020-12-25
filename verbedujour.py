from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import numpy as np

conjugation = {
    'sunday': 'present',
    'monday': 'passe compose',
    'tuesday': 'imparfait',
    'wednesday': 'futur',
    'thursday': 'conditionnel',
    'friday': 'subjonctif'
}

page = urlopen("http://la-conjugaison.nouvelobs.com/")
soup = BeautifulSoup(page, "html.parser")

verbe = soup.find(text="Le verbe : ").findNext('a').text
day = datetime.datetime.now().strftime("%A").lower()
if day == 'saturday': # randomly select conjugaison
    random_conjugation = np.random.choice(list(conjugation.values()))
    conjugation[day] = random_conjugation

# print("Verbe du jour: ", verbe.upper())
# print("La conjugaison du jour: ", conjugation[day].upper())
print("{}, {}, {}, {}".format(
        datetime.datetime.now().strftime("%Y-%m-%d"),
        day,
        verbe,
        conjugation[day]
    )
)

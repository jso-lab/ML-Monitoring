import pytest
import pandas as pd


Aliments = {
     'Fruit': ['Ananas', 'Banane', 'Fraise', 'Pomme'],
     'Couleur': ['jaune','jaune','rouge', 'vert'],
     'Type': ['exotique','exotique','locale','locale']
}

@pytest.fixture
def create_dataframe():
     df = pd.DataFrame(Aliments)
     return df



    



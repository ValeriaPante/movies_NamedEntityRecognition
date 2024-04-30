import Levenshtein
import pandas as pd
from typing import Dict
import json


class ValueStandardizer:
    """
    Tool that standardizes the name of entities
    """

    def __init__(self):

        with open('./data/standardValues.json', 'r') as f:
            self.dbValues = json.load(f)

    def standardize(self, entities: Dict) -> Dict:
        """
        Standardizes the value of entities

        Args:
            entities: dictionary of entities grouped by label (key: label, value: list of entities)
        Returns:
            dictionary of entities whose name has been standardized grouped by label (key: label, value: list of entities)
        """

        for key, values in entities.items():
            if len(values) == 0 or key not in ['TYPE', 'CAST','DIRECTOR','COUNTRY','TITLE','RATING','GENRE']:
                continue
            newValues = []
            standardValues = pd.DataFrame(self.dbValues[key], columns=['stdValue'])

            for v in values:
                standardValues["similarity"] = standardValues['stdValue'].apply(lambda x: Levenshtein.ratio(v,x.lower()))
                standardValues.sort_values(by="similarity", ascending=False, inplace=True)
                if standardValues["similarity"].values[0] > 0.65:
                    newValues.append(standardValues["stdValue"].values[0])

            if len(newValues) > 0:
                entities[key] = list(dict.fromkeys(newValues))  # removes duplicates
            else:
                entities[key] = []

        return entities


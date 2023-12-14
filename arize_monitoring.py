#!/usr/bin/env python
# coding: utf-8
 
# # Arize ML monitoring

# Step 1 : Chargement des modules

from arize.pandas.logger import Client, Schema
from arize.utils.types import ModelTypes, Environments, Schema, Metrics
import pandas as pd
from config.config import SPACE_KEY, API_KEY


# ## Step 2 : Chargement du dataset
# Dans ce notebook, nous chargeons les données depuis la base des datasets de Scikit-Learn
arize_client = Client(space_key=SPACE_KEY, api_key=API_KEY)


from sklearn.datasets import load_breast_cancer
breast_cancer_dataset = load_breast_cancer()


# ## Step 3 : Extraction des features, des prédictions et des actuals

breast_cancer_features = breast_cancer_dataset['data'] # feature data
breast_cancer_feature_names = breast_cancer_dataset['feature_names'] # feature names
breast_cancer_targets = breast_cancer_dataset['target'] # actual data
breast_cancer_target_names = breast_cancer_dataset['target_names'] # actual labels


target_name_transcription = [] # ceci deviendra notre listes des actuals

for i in breast_cancer_targets: 
  target_name_transcription.append(breast_cancer_target_names[i])


## Création d'un dataframe avec les données

df = pd.DataFrame(breast_cancer_features, columns=breast_cancer_feature_names)
df['actual_label'] = target_name_transcription
df['prediction_label'] = target_name_transcription

# this is optional, but makes this example more interesting in the platform
df['prediction_label'] = df['prediction_label'].iloc[::-1].reset_index(drop=True) 


# ## Step 4 : Chargement des données sur la plateforme Arize

schema = Schema(
    actual_label_column_name="actual_label",
    prediction_label_column_name="prediction_label",
    feature_column_names=[
       'mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'
       ]
)


response = arize_client.log(
    dataframe=df,
    schema=schema,
    model_id='breast_cancer_dataset', 
    model_version='v1',
    model_type=ModelTypes.BINARY_CLASSIFICATION,
    metrics_validation=[Metrics.CLASSIFICATION], 
    environment=Environments.PRODUCTION
) 


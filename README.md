# ML-Monitoring

---

| Notes                                                       |
| ----------------------------------------------------------- |
| Les captures d'écran sont contenues dans le dossier **img** |

|----------------------------------------------------------------
| Les tests sont dans le dossiers **tests** |

---

## Avertissement

Pour faire tourner ce projet, vous aurez besoin de créer un compte sur [Arize](https://app.arize.com/auth/join). Une fois le compte crée, il faut récupérer votre **API_KEY** et **SPACE_KEY**. Ils vous seront demandés dans la suite du code pour pouvoir se connecter à votre espace dans Arize, charger vos données et lancer tout le processus de monitoring.

## Initialisation

Cloner le dépôt dans un dossier en local. Vous pouvez aussi télécharger le dépôt via les options proposées par Github. Après avoir extrait l'archive des fichiers, ouvrir le dossier dans un éditeur de code. Dans le projet, j'ai utilisé Visual Studio Code.

## Environnement de travail

Avant tout, pensez à créer un environnement avec Python 3.7. Pourquoi? La réponse vient du fait que Arize à dévélopper son module de monitoring qui ne fonctionne pour l'heure qu'avec une version de Python antérieur.

1 - Créer un environnement dans Anaconda Navigator ou tout simplement dans un termninal `conda create -n <nom_de_l'environnement> python=3.7`

2 - Lancer la commande `pip install -r requirements.txt` pour installer les modules et bibliothèques nécessaires au bon fonctionnement de l'application.

3 - Vérifier que l'installation des modules s'est bien déroulée. Sinon corriger les erreurs via la console du terminal.

4 - Allez dans le répertoir `config` et dans le fichier `config.py` remplacer les valeurs des différentes clés avec celles que vous avez obtenues après votre inscription sur Arize.

5 - De nouveau dans le terminal, placer vous à la racine du projet et taper la commande :

- `python arize_monitoring.py`

Le script qui s'exécute accomplit toutes les tâches. Dans le terminal devrait s'afficher le résultat de la bonne exécution du script. Sinon vérifier et corriger les erreurs.

## Bonus

Un dossier `assets` a été ajouté à la fin du projet. Il contient un notebook jupyter pour tester un modèle de régression. Vous pouvez le modifier à souhait. Vous également le supprimer.

Merci d'avoir tester ce code !

## Me contacter

[Jean-Paul SOSSAH](https://www.linkedin.com/in/jean-paul-sossah/)

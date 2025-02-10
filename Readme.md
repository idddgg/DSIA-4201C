# Data Engineering - Projet GAMOUH Imad et DUONG Tony 

___

##                                                    Scraping du site BMW                                                            ##

___

Ce projet repose sur Docker Compose pour orchestrer trois services principaux :

Scraper : Le conteneur Scrapy exécute des spiders pour collecter des données (modèles BMW, vidéos, logos) et les insère dans MongoDB.

MongoDB : Garde les données scrappées dans des collections comme bmw_models et bmw_videos.

Dash : Récupère les données depuis MongoDB pour les afficher dynamiquement dans un dashboard.

Avant de lancer ce projet, assurez-vous que votre environnement de développement dispose des outils suivants :


**2. Prérequis**


#### A. Docker ####

Docker est essentiel pour exécuter les services (scraping, MongoDB, et Dash) dans des conteneurs isolés : il permet à chaque service de disposer de son propre environnement avec toutes ses dépendances, garantissant ainsi qu'il fonctionne de la même manière sur n'importe quelle machine. En résumé, Docker rend le système plus stable, portable et facile à maintenir.

#### B. Git ####

Git est nécessaire pour cloner le projet depuis un repository : il permet de copier l'intégralité du projet sur son ordinateur. 
Pour pouvoir cloner le répertoire, on se place dans le répertoire ou l'on souhaite cloner le programme puis on exécute la commande dans le bash :

`cd <Adresse du répertoire>`

Ensuite, on exécute la commande suivante dans le bash : 

`git clone <https://github.com/idddgg/DSIA-4201C>`

Félicitations ! Le projet a été cloné avec succès. Les prochaines étapes consisteront à rendre le site pleinement fonctionnel. On se  déplace à présent dans un répertoire spécifique du projet cloné afin de lancer le site en tapant la commande :

`cd 6Evaluation\Projet`

Nous pouvons enfin lancer le projet et accéder à notre merveilleux site. Pour cela, on exécute la commande suivante à l'aide de Docker Compose : c'est un outil qui permet de définir et de lancer plusieurs conteneurs Docker en même temps à partir d’un seul fichier.                                                                                                                                En résumé, il permet de démarrer tous les services nécessaires à notre application (Le scraping, MongoDB et Dash) avec une seule commande, tout en s'assurant qu’ils fonctionnent ensemble correctement.

`docker-compose up --build`

Après cette étape, tout sera compilé. Il ne reste plus qu'à visualiser en exécutant la commande suivante dans son navigateur ou on saisit l'URL suivante pour accéder au site :

http://127.0.0.1:8050/

Il peut arriver que l'interface Dash ne s'affiche pas correctement. Dans ce cas, il suffit de redémarrer le service Dash à l'aide de la commande suivante :

`docker-compose restart dash`

Ensuite, actualisez la page du site qui devrait s'afficher correctement. Voici quelques commandes supplémentaires pour Docker :                     

*Construire et lancer tous les services :*
`docker-compose up --build`

*Vérifier les logs des conteneurs :*
`docker-compose logs -f`

*Arrêter tous les services :*
`docker-compose down`

**2. Interface du site**

En accédant à la page principale du site, on découvre une vidéo représentant l’élégance et l’innovation de BMW.                        Quatre boutons sont ensuite affichés en dessous cette vidéo, représentant les types de véhicules actuellement disponibles sur le marché BMW : 
- électriques
- essence
- diesel 
- hybrides rechargeables

En cliquant sur l’un de ces boutons, on est redirigé vers une page dédiée au type de carburant sélectionné. Sur cette page, tous les modèles correspondants sont présentés, avec une image du véhicule et des informations détaillées, telles que le prix. Il est possible de naviguer entre les modèles à l’aide de deux boutons situés sur les côtés.

Enfin, une image située en bas de la page met en avant la qualité remarquable des intérieurs BMW.
Une vidéo est disponible montrant toutes les fonctionnalités du site.

## Détail ##

### A. Scraping ###

Le service **Scrapy** collecte des données sur le site web BMW et les envoie à MongoDB. Les spiders permettent une extraction ciblée et efficace :

1. ***bmw_models*** : Ce spider xtrait les modèles, types de carburant, prix et images directement depuis le HTML des pages.

2. ***bmw_video*** : Ce spider récupère une vidéo promotionnelle.

3. ***bmw_electric_video*** et ***bmw_specific_image*** : Ce spider scrape des logos et des images depuis certaines pages, en combinant utilisant Selenium pour gérer les contenus dynamiques.

Chaque spider peut être exécuté individuellement :

`docker-compose run scraper scrapy crawl <nom_du_spider>`

Cette combinaison de **Scrapy** pour les contenus statiques et de **Selenium** pour les contenus dynamiques permet une grande flexibilité , adaptée aux différents types de données scrapées. Une fois scrapée, le **pipeline** Scrapy insère les données dans deux collections MongoDB :

1. ***bmw_models*** pour les modèles de voitures. 

2. ***bmw_videos*** pour les vidéos,images et logos.

Les fichiers de pipelines et de spiders sont conçus pour être hautement configurables, permettant une adaptation rapide pour d'autres types de données ou sites web.                                                                                                                                    Par exemple, chaque spider est isolé dans son propre fichier, ce qui facilite les modifications ou ajouts futurs.
Ainsi, on peut retenir les éléments suivants sur la partie Scraping:

- Flexibilité : Le projet gère à la fois des contenus HTML statiques et des contenus dynamiques grâce à Selenium.

- Organisation : Chaque spider est contenu dans un fichier distinct, rendant les ajustements rapides et intuitifs.

- Évolutivité : Ajouter de nouvelles cibles ou adapter les spiders existants est simplifié grâce à la structure modulaire du projet.

___

### B. Stockage (à l'aide de MongoDB) ###

MongoDB joue un rôle clé dans ce projet en stockant deux types principaux de données scrappées :

Les modèles de voitures et leurs caractéristiques.

Les URL d’images ou de vidéos isolées pour un affichage dynamique.

Contrairement aux bases de données classiques qui stockent localement des fichiers, ici nous avons opté pour une approche basée sur les URLs. Cette solution permet :

. Une gestion optimisée de l’espace disque, car aucun fichier image ou vidéo n’est enregistré localement.

. Une mise à jour automatique des médias affichés sans nécessiter de duplication de données.

. Une meilleure scalabilité puisque le stockage des fichiers est externalisé sur des serveurs distants.

Ainsi, on a plusieurs collections :

- bmw_models : Cette collection conserve les détails complets des modèles BMW, y compris leurs noms, types de carburant, prix, et URL des images associées. Par exemple :

{
    "model": "BMW i4",
    "fuel_type": "électrique",
    "price": "à partir de 55 900 €",
    "image_url": "https://bmw.fr/image.jpg"
}

- bmw_videos : Cette collection est dédiée aux éléments médias tels que les vidéos promotionnelles ou les logos spécifiques. Par exemple :

{
    "video_url": "https://bmwgroup.com/vidéo.mp4"
}

Grâce à ce système, les médias sont accessibles en temps réel sans surcharger le stockage local. L’affichage des modèles et des vidéos est instantané, et tout changement côté serveur distant est immédiatement répercuté sur l’interface Dash.
MongoDB est déployé via Docker avec persistance des données dans un volume, garantissant que les données restent accessibles même après un redémarrage :

volumes:
  dbdata:/data/db

Cette architecture assure une fiabilité maximale pour la conservation des données et simplifie les opérations de sauvegarde. De plus, les requêtes sont optimisées pour interagir rapidement avec l'interface Dash.
En adoptant cette approche, le projet bénéficie d’une gestion efficace des ressources, et permet d'éviter les contraintes de stockage local et assure un affichage rapide et dynamique des contenus.

___

### C. Affichage (à l'aide de Dash) ###

Dash offre une interface utilisateur dynamique pour visualiser les données scrappées. L'architecture du code a été pensée pour faciliter la maintenance et l'évolution en séparant chaque composant clé dans des scripts dédiés.

- Exemple de l'architecture modulaire

. header.py : Gère l'affichage dynamique de l'en-tête avec les logos récupérés depuis MongoDB.

. footer.py : Contient le pied de page et les boutons de navigation globaux.

. main_content.py : Page d'accueil affichant une vidéo et les liens vers les différentes catégories de véhicules.

Un script EST dédié pour chaque type de véhicule (electrique.py, diesel.py, essence.py, hybride.py) : il permet de récupèrer dynamiquement les modèles depuis MongoDB, de génèrer une mise en page spécifique pour chaque catégorie.

. def.py : Centralise la gestion du carrousel et facilite la navigation entre les images.

L'approche modulaire garantit une flexibilité maximale, permettant d'ajouter ou de modifier une catégorie sans impacter l'ensemble du projet.

- Fonctionnalités clés

Carrousel interactif :
Permet de naviguer entre les images des modèles BMW grâce à un système de pagination dynamique.

```@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/electrique":
        return create_electrique_layout()
    ...
```
Cette structure rend l'application hautement maintenable et évolutive, assurant une expérience fluide aussi bien pour les utilisateurs que pour les développeurs.

Ce projet met en avant une architecture moderne et un code bien structuré, rendant la collaboration entre développeurs fluide et efficace.


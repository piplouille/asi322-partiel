Partiel de ASI322
===

# Architecture lambda

1. collecte des données avec appel à l'API Twitter -> Elasticsearch
2. Gestion des flux de messages -> Kafka
3. Stockage des données -> Hadoop. map reduce pour trier par hashtag ?
4. Analyse des données -> Kafka

# API Twitter

[Docs](https://developer.twitter.com/en/docs)

# Techno

## Elasticsearch
Logiciel pour indexation et recherche de données

### Kibana
Greffon de visualisation de données pour Elasticsearch

## Kafka
gestion des flux de msg

## Spark
Analyse des données

### Hadoop
Storage and process of large datasets

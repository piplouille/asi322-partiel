Partiel de ASI322
===

# Architecture lambda

1. collecte des données avec appel à l'API Twitter -> Kafka (cf article paragraphe 4.2)
2. Gestion des flux de messages -> Kafka
3. Stockage des données -> Hadoop. map reduce pour trier par hashtag ?
4. Analyse des données -> Kafka

# API Twitter

[Docs](https://developer.twitter.com/en/docs)

# Techno

### Kibana
Greffon de visualisation de données pour Elasticsearch

## Kafka
gestion des flux de msg
pour faire la liaison avec hdfs : ./kafka_2.12-2.2.0/bin/connect-standalone.sh ./kafka_2.12-2.2.0/config/connect-standalone.properties quickstart-hdfs.properties
pour l'instant ça marche pas doit y'avoir des trucs à changer dans les fichiers en paramètres des .properties par ex.
il faut lancer hadoop (comment ?) et mettre l'url hdfs dans le quickstart-hdfs.properties

## Spark
Analyse des données

### Hadoop
Storage and process of large datasets

## Non utilisée

### Elasticsearch
Logiciel pour indexation et recherche de données

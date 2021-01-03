Partiel de ASI322
===

# Comment lancer le projet
Lancer **Zookeeper** et **Kafka** : (à la racine du projet)
```
./projet.sh
```

Lancer le **producer** de Kafka : (à la racine du projet)
```
python3 producer.py
```

Lancer **Hadoop** avec Docker : (dans le dossier docker-hadoop)
```
sudo docker-compose up
```

Lancer le **connecteur** : (à la racine du projet)
```
./kafka_2.12-2.2.0/bin/connect-standalone.sh ./kafka_2.12-2.2.0/config/connect-standalone.properties confluentinc-kafka-connect-hdfs-10.0.0/etc/quickstart-hdfs.properties
```

# Architecture lambda

1. collecte des données avec appel à l'API Twitter -> **Kafka** (cf article dans ressources, paragraphe 4.2)
2. Gestion des flux de messages -> **Kafka**
3. Stockage des données -> **Hadoop** ; map reduce pour trier par hashtag
4. Analyse des données -> **Spark**

# Technologies utilisées

## Twitter API

[Documentation](https://developer.twitter.com/en/docs)

## Kafka
> Gestion des flux de messages

Pour faire la liaison Kafka-HDFS : cf [Partie 1](#comment-lancer-le-projet)

Les paramètres du connecteur sont dans le fichier ```confluentinc-kafka-connect-hdfs-10.0.0/etc/quickstart-hdfs.properties```.

### Hadoop
> Storage and process of large datasets

## Spark
> Analyse des données

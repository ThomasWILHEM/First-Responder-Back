# First Responder Back-End

**First Responder** est bien plus qu'une simple simulation. C'est une plongée au cœur de l'action en tant qu'opérateur de secours d'urgence. Dans ce back-end puissant, vous serez aux commandes de la gestion des situations de crise, réagissant à des appels urgents et déployant les équipes de secours nécessaires sur les lieux des incidents. L'objectif ultime est de sauver un maximum de vies tout en exploitant de manière optimale les ressources disponibles. Vous affronterez divers scénarios d'urgence, tels que des incendies, des accidents de la route et des catastrophes naturelles.

## Caractéristiques principales

- **Variété de Scénarios** : Vous serez confronté à une diversité de situations d'urgence, chacune exigeant une approche unique pour réussir.

- **Gestion Complète** : Prenez en charge une équipe complète de personnel, de véhicules et d'infrastructures, adaptant vos ressources aux besoins spécifiques de chaque incident.

- **Surveillance en Temps Réel** : Grâce à un accès à une carte du monde en temps réel, vous pourrez suivre les missions en cours et surveiller les déplacements des véhicules, prenant ainsi des décisions éclairées pour optimiser vos opérations de secours.

## Démarrage

Suivez ces étapes pour démarrer le back-end de **First Responder** :

1. Installez les bibliothèques requises en utilisant la commande suivante :

    ```bash
    pip install -r requirements.txt
    ```

2. Pour lancer la base de données et l'outil d'administration (Adminer), exécutez la commande suivante :

    ```bash
    docker-compose up -d
    ```

3. Enfin, démarrez l'application avec la commande suivante :

    ```bash
    uvicorn app.main:app --reload
    ```

Vous voilà prêt à plonger dans le monde trépidant de la gestion des urgences en utilisant le back-end robuste de **First Responder**. Sauvez des vies, gérez des ressources et faites face à l'inattendu. Bon jeu !
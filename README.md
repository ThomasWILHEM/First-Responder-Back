# First-Responder-Back

First Rsponder est une simulation d’opérateur de secours d’urgence où le joueur doit gérer des situations d'urgence simulées, en répondant à des appels et en envoyant des équipes de secours appropriées sur les lieux de l'incident. Le but est de sauver autant de vies que possible tout en gérant efficacement les ressources disponibles. Le jeu comprendra différents types de scénarios d'urgence, tels que des incendies, des accidents de la route et des catastrophes naturelles.

Le joueur devra également gérer toute une équipe de personnel, de véhicules et d'infrastructures en fonction des besoins de chaque situation.

Le joueur aura accès à une carte du monde en temps réel qui affichera les missions en cours et les véhicules en déplacement. Cela permettra au joueur de visualiser l'état actuel des opérations de secours et de prendre des décisions en conséquence.

## Démarage : 

Pour installer les librairies requises : 

    pip install -r requirements.txt

Pour démarrer la base de donnée et l'adminer : 
    
    docker composer up -d

Pour démarrer l'application : 

    uvicorn app.main:app --reload

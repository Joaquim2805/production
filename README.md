# Prototype

Attention : Le docker compose ne build pas les images, il faut donc build les 2 images avec les Dockerfile des dossiers front et back en leur donnant les bon noms :
- mon_image_fastapi => Pour l'image du back
- mon_image_front => Pour l'image du front
On peut ensuite exécuter : docker compose up, je vais voir si on peut demander un build des images directement dans le docker-compose

L'outil pgAdmin4 est dispoible en conteneur aussi voici les identifiants pour y accéder:
- email : admin@admin.com
- user : admin
- mdp : secret

La table user ne se crée pas automatiquement pour l'instant mais le pb sera corrigé d'ici peu,
pour l'initialiser il faut utiliser la méthode init_db() du fichier database.py mais je dois trouver un moyen de l'initialiser seulement si celle-ci n'existe pas pour éviter de se retrouver avec plusieurs tables user.

Je vais aussi "spliter" les composants login, register et header_user dans le dossier Views cela sera fait dans les prochains jours :)

N'hésite pas si tu veux que je modifie des trucs 

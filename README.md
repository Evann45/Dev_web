<style>
b { color: blue}
r { color: red}
a { color: aquamarine}
a1 {color: aqua}
</style>

# <r>Développement web</r>

# <b>Evann YANG Thomas RABILLON</b>

Tout d'abord lors de ce projet il nous a été demander de réaliser un site web avec flask.
Pour notre part il nous était possible de reprendre la suite du TP ou bien repartir de zéro, ici nous sommes reparties de zéro.
Nous avions pour but de réaliser un blog.

## <a>Ce dont nous avons réussi</a>

Lors de ce TP nous avons réussi à réaliser certaines fonctionnalités comme le fais de se connecter avec un id (l'adresse mail) mais aussi le fais de se déconnecter à partir d'un bouton introduit dans le nav barre. De plus si l'on n'a pas de compte on peut directement en créer un pour se connecter.

Ensuite nous avons ajouté les fonctionnalités principales d'un blog, comme le fait de poster des blogs en les créant mais aussi les supprimer, on peut aussi voir les postes des autres personnes, la liste de nos postes et aussi écrire des commentaires sur les postes. En outre les commentaires créés peuvent être supprimés un à un ou bien tous si l'on supprime directement le poste ou sont les commentaires. De plus nous avons introduit une barre de recherche permettant de rechercher les postes par leur titre, et renvoie si le titre ou les/la lettre introduit dans la recherche existe les ou le poste en question, sinon il renvoie une page blanche avec écris "Il n'y a pas de poste".

Enfin nous avons ajouté la fonctionnalité d'amener l'utilisateur directement sur la page login s'il n'est pas connecté et qu'il clique sur un des liens de la barre de navigation, de plus après qu'il se soit connecté ce dernier sera automatiquement emmené sur la page du lieu qu'il avait cliqué.
Bien que tout cela n'aurait pas pu être possible si nous n'avions pas réussi à lier les fichiers pythons, htmls et db.

## <a>Ce dont nous avons pas réussi</a>

Pour ce TP nous avons réussi à réaliser diverses fonctionnalités, mais bien que nous avons réalisé ce qu'il nous était demandé nous n'avons pas pu réaliser certaines fonctionnalités comme ajouter des likes sur les postes, le CSS du site web, ou encore le footer qui est dû au placement mal régler.

## <a>Synthèse</a>

Pour conclure, ce TP nous a permis d'approfondir nos connaissances sur flask et tous les frames Works avec, en réalisant diverses fonctionnalités et en faisant plusieurs liens entre différents languages. De plus ce Tp nous permis de revoir les notions du web (HTML/CSS) malgré que le côté CSS soit uniquement dû à BOOTSTRAP.

## <a1>Comment lancer le site web<a1>

Pour lancer le site web il faut d'abord installer des prérequis, qui sont les suivants :

source venv/bin/ activate (optionnel)
pip install -r requirements.txt

Enfin après avoir installé ces prérequis, il faut maintenant lancer la commande suivante : flask run
Puis aller sur le lien donné dans le terminal

## Si probleme de fonctionnalité

Réinitialiser la BD
flask initdb

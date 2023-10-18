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
Ensuite nous avons ajouté les fonctionnalités principales d'un blog, comme le fait de poster des blogs en les créant mais aussi les supprimer, on peut aussi voir les postes des autres personnes, la liste de nos postes et aussi nos commentaires.
Bien tout cela n'aurait pas pu être possible si nous n'avions pas réussi à lier les fichiers pythons, htmls et db.

## <a>Ce dont nous avons pas réussi</a>

Pour ce TP nous avons pas réussi a réaliser divers fonctionnalité, commme ajouter des like sur les postes, le CSS dit site web, ou encore le footer qui est du au placement mal régler.

## <a>Synthèse</a>

Pour conclure, ce TP nous a permis d'appronfondir nos connaissances sur flask et tout les frameworks avec. De plus ce tp nous permis de revoir les notions du web (HTML/CSS).

## <a1>Comment lancer le site web<a1>

Pour lancer le site web il faut d'abord installer des prérequis, qui sont les suivants :

source venv/bin/ activate (optionnel)
pip install flask
pip install python-dotenv
pip install bootstrap-flask
pip install flask- sqlalchemy
pip install flask-wtf
pip install flask-login

(vous pouvez directement aller dans le terminal et taper la commande suivante : pip install -r requirements.txt)

Enfin après avoir installé ces prérequis, il faut maintenant lancer la commande suivante : flask run
Puis aller sur le lien donné dans le terminal

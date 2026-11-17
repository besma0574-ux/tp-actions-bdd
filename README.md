# Exercice 3 : Ajouter JavaScript, Java et PHP (30 min)

**Objectif :** exécuter les tests des trois autres langages, chacun dans son propre job.

**Fichiers fournis :** les dossiers `node-app/`, `java-app/` et `php-app/` contiennent déjà le code, les tests et le fichier de configuration (`package.json` et `package-lock.json`, `pom.xml`, `composer.json`). Il n'y a rien à écrire en JavaScript, Java et PHP.

**Travail à faire :** dans `ci.yml`, ajouter trois jobs `node`, `java` et `php`, sur le modèle du job `python`. Chaque job commence par deux étapes identiques : récupérer le code, puis préparer la base de données (`bash db/setup.sh`). Ensuite, il suit ce tableau :

| Job | Installation du langage | Commandes (à lancer dans le dossier de l'application) |
|---|---|---|
| `node` | `actions/setup-node@v4` avec `node-version: 20` | `npm ci`, puis `npm test` (dossier `node-app`) |
| `java` | `actions/setup-java@v4` avec `distribution: temurin` et `java-version: 17` | `mvn -B package` (dossier `java-app`) |
| `php` | `shivammathur/setup-php@v2` avec `php-version: "8.3"` et `extensions: pdo, pdo_pgsql` | `composer install --no-interaction`, puis `vendor/bin/phpunit tests` (dossier `php-app`) |

**Résultat attendu :** quatre jobs (`python`, `node`, `java`, `php`) qui s'exécutent en même temps, tous verts.

## Envoyer le dossier sur GitHub

```bash
git init -b main
git add .
git commit -m "Message du commit"
git remote add origin https://github.com/VOTRE-COMPTE/tp-actions-bdd.git
git push -u origin main
```

Ensuite, ouvrir l'onglet **Actions** du dépôt pour suivre les exécutions.

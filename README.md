---


---

<h1 id="dockeriser--minio-et-api-rest">Dockeriser  Minio et API Rest</h1>
<p>Dans le docker-compose.yml se trouve un conteneur pour API Client Rest et de Server minio.</p>
<h3 id="dockeriser-une-application-java">Dockeriser une application Java</h3>
<p>Créer une image docker  de notre jar.<br>
Fichier Dockerfile :</p>
<pre><code>FROM openjdk:8-jre-alpine3.9
COPY target/S3Client-1.0-SNAPSHOT.jar /demo.jar
CMD ["java", "-jar", "/demo.jar"]
</code></pre>
<h3 id="docker-compose--communication-entre-conteneurs">Docker-compose : communication entre conteneurs</h3>
<p>Il est possible de spécifier le sous-réseau à utiliser dans le fichier Docker-compose.xml et d’attribuer des IP fixes au conteneur.</p>
<p>Docker-compose créera le réseau lors du build.</p>
<pre><code>sudo docker-compose up --build
</code></pre>
<p>Remarque: il n’est pas possible avec docker-compose de déterminer l’ordre de lancement des conteneurs cad qu’on ne peut pas attendre qu’un conteneur (ex: le serveur ) termine son lancement pour lancer le démarrage d’un autre conteneur (ex : le client).<br>
Il est possible de forcer cette ordre via d’autre méthode (utilisation de script).</p>
<p>Sur le site docker :</p>
<blockquote>
<p>Use a tool such as <a href="https://github.com/vishnubob/wait-for-it">wait-for-it</a>, <a href="https://github.com/jwilder/dockerize">dockerize</a>, or sh-compatible <a href="https://github.com/Eficode/wait-for">wait-for</a>. These are small wrapper scripts which you can include in your application’s image to poll a given host and port until it’s accepting TCP connections.</p>
</blockquote>


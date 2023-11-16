docker stop postgrestest
docker rm postgrestest
docker run --name postgrestest -p 5500:5432 -it -e POSTGRES_PASSWORD=ilovecheese postgres
qterminal -d -e "docker exec -it postgrestest bash
psql -U postgres
CREATE DATABASE memesdb;
\q
exit"

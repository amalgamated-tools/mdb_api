docker build -t movie_api .
docker tag movie_api docker.pkg.github.com/veverkap/mdb_api/movie_api:v3
docker push docker.pkg.github.com/veverkap/mdb_api/movie_api:v3
# docker run -d --name mdb_api -p 8080:80 mdb_api
# # docker logs -f mycontainer

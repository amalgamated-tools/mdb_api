docker build -t mdb_api .
docker tag mdb_api registry.veverka.net/mdb_api
docker push registry.veverka.net/mdb_api
# docker run -d --name mdb_api -p 8080:80 mdb_api
# # docker logs -f mycontainer

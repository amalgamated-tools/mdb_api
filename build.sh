docker build -t mdb_api .
# docker tag meatsweatweb registry.veverka.net/meatsweatweb
# docker push registry.veverka.net/meatsweatweb
docker run -d --name mycontainer -p 8080:80 mdb_api
# # docker logs -f mycontainer

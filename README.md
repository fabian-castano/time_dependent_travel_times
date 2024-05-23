# Instructions for the project

This project aims at improving routing in logistic process by considering the traffic congestion in the city. The project is divided into two parts:

1. **Data Collection**: The data is collected from  UBER movement, a public dataset that contains the travel time between two points in the city.
2. **Routing Algorithm**: The routing algorithm is developed using the data collected in the first part. The algorithm considers the traffic congestion in the city and provides the best route to the user.

Run the following command to start the container:


```sh
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/colombia-latest.osm.pbf
```

```
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-partition /data/colombia-latest.osrm
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-customize /data/colombia-latest.osrm
```

Run the image
```sh
docker run -t -i -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend osrm-routed --algorithm mld /data/colombia-latest.osrm
```

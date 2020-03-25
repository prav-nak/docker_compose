## A multi-container app using Flask and MySQL using docker-compose
This is based on the following awesome post 
[Dockerizing a Flask-MySQL app with docker-compose](https://stavshamir.github.io/python/dockerizing-a-flask-mysql-app-with-docker-compose/)

### tl;dr
1. Run ```docker-compose up```
2. Visit ```http://0.0.0.0:5000/```

### introduction
A suggested best practise in modern web-app development is to have the
independent services/components of the app run in their own separate containers. 
We will use ```docker-compose``` to facilitate the orchestration of the two independant containers into one working app.
Compose is a tool for defining and running multi-container docker applications. 
Using a configuration file, these multiple services can be created and started 
using a single command. 

Flask is a web development framework in python that is easy-to-use. 
Most apps require some sort of database to store and retrieve data. 
Hence we create two different docker containers and link them together. 

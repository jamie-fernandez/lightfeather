# LightFeather

### Project Setup

Built with MacOS. I don't know how good these instructions will be with other operating systems.

1. Clone the repository
```
$ git clone https://github.com/jamie-fernandez/lightfeather.git
```

2. Spin up the server powed by django with docker
```
$ docker-compose up --build
```

3. Open up a new terminal and cd into the frontend folder, then you should be able to turn on the vue app with `npm run serve`

4. If everything turned on as expected you should see the frontend at `http://localhost:8080/` the backend submit endpoint at `http://0.0.0.0:8000/api/submit/` and the supervisor endpoint at `http://0.0.0.0:8000/api/supervisors/`
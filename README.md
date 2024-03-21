<h1>DEVOPS</h1>

Simple Flask budget calculator with "log-in"

```
For log-in:
username = admin
password = password
```


<h1>Running the app</h1>

<h2>Build container</h2>

```docker
docker build -t [image_name] .
```

<h2>Run container</h2>

```docker
docker run -p 5000:5000 --name [container_name] [image_name]
```

<h2>Website available on <br></h2>

```cmd
127.0.0.1:5000 or localhost:5000
```
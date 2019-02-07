## Ashya Callback

This is a sample repo that shows how to implement a basic service that can be used
to receive IoT data streams.  

## Usage

It is best to use docker.  By running: 

```
docker run -p 5252:5252 -d ashya/callback 
```

You will then have a service on port `5252` that can receive `POST` requests.  You can then test by
running:

```
curl -X POST -d '{"some": "data"}' -H "Content-Type: application/json" localhost:5252
```

The contents of the `POST` data will be rendered back to you. 

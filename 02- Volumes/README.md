# Volumes

## About Volumes

In Docker, containers are designed to be ephemeral, meaning they are temporary and can be easily created or destroyed. However, there are scenarios where you need to **persist** data even after the container is stopped or removed. This is where Docker volumes come into play.

Docker volumes provide a way to store data outside the container’s file system, making it independent of the container’s lifecycle. This means that even if a container is deleted, the data stored in a volume remains intact and can be accessed by other containers. Volumes are the preferred method for persisting data generated or used by Docker containers because they are managed by Docker and provide several benefits:

**Data Persistence**: Volumes ensure that important data is not lost when containers are stopped or removed.
**Data Sharing**: Multiple containers can share and access the same data through volumes, facilitating collaboration between different services.
**Isolation**: Volumes are stored in a special location on the host machine that is managed by Docker, providing an additional layer of isolation.
**Performance**: Volumes are optimized for I/O operations and can offer better performance compared to other data storage methods like bind mounts.

Using Docker volumes is straightforward. You can create a volume, attach it to one or more containers, and ensure that your data persists even when containers are stopped or removed. In the following example, we'll walk through a simple use case to demonstrate how to create a volume, use it with a container, and verify that the data persists.


## Open a terminal and create a volume

```bash
docker volume create mydata
```

## List the volumes

```bash
docker volume ls
```

## Run a Redis container that will use the volume

```bash
docker run -d --name redis-test -v mydata:/data redis:latest
```

## Connect to the instance

```bash
docker exec -it redis-test bash
```

## Add some data to Redis

In the container's bash shell, run:

```bash
redis-cli
```

Set a key-value pair:

```bash
set mykey "Hello, Redis!"
```

Save the data to the volume:

```bash
save
```

Exit the Redis CLI and the container:

```bash
exit
exit
```

## Stop and remove the container

```bash
docker stop redis-test
docker rm redis-test
```

## Run it again and see if the data still exists

```bash
docker run -d --name redis-test -v mydata:/data redis:latest
docker exec -it redis-test bash
```

Inside the container's bash shell, run:

```bash
redis-cli
get mykey
```

You should see the output `"Hello, Redis!"` if the data was persisted correctly.

## Cleanup

```bash
docker stop redis-test
docker rm redis-test
docker volume rm mydata
```

This example shows how to use Docker volumes to persist data in a Redis container. The data stored in the Redis database will persist even if the container is stopped and removed, as it's stored in the `mydata` volume.
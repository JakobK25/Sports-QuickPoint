# Sports-QuickPoint

## Setup

#### Docker
```sh
#Build the image
docker build -t sports-quickpoint-db .

#Run the container
docker run --name sports-db -d -p 5432:5432 --env-file .env sports-quickpoint-db
```

# Sports-QuickPoint

## Setup

#### Docker
```sh
#Build the image
docker build -t sports-quickpoint-db .

#Run the container
docker run -d -p 5432:5432 --name sports-db sports-quickpoint-db
```

#GDG Surabaya
Web GDG Surabaya by Frans Siswanto 

#Engine
This code needs engine. The engine that run this code can be found in Docker Container.

1. Pull the container using `docker pull gdgsurabaya/web`
2. Pull the RabbitMQ host `docker pull rabbitmq:management`
3. Run the RabbitMQ container `docker run -d --hostname gdg_rabbit --name gdg_rabbit rabbitmq:management`
4. Run the container using `docker run -d -p 8000:8000 -p 80:80 --name gdg_web --link gdg_rabbit:rabbit -v /home/frans/gdg_surabaya:/root/web gdgsurabaya/web`

Mapping to `home/frans/gdg_surabaya` is only for development purpose. If you are not going to develop, please ignore `-v` command.

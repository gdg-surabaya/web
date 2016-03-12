# Let's get this party started
from bson import json_util
import falcon
import pika
import config


def crossdomain(req, resp):
    resp.set_header('Access-Control-Allow-Origin', '*')
#end def

class Register(object):
    def on_post(self, req, resp):
        document = dict(
            nama = req.get_param("txt_nama"),
            jenis_kelamin = req.get_param("rb_jenis_kelamin"),
            email = req.get_param("txt_email"),
            hp = req.get_param("txt_hp"),
            institusi = req.get_param("txt_institusi"),
            profesi = req.get_param("txt_profesi"),
            minat = req.get_param("txt_minat")
        )

        '''Send the data to RabbitMQ Queue'''
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.config["mq_host"]))
        channel = connection.channel()

        channel.queue_declare(queue='gdg_new_member', durable=True)

        message = json_util.dumps(document)
        channel.basic_publish(
            exchange='',
            routing_key='gdg_new_member',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode = 2,
            )
        )
        connection.close()
        '''end of sending data to RabbitMQ'''

        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json_util.dumps(document)

# falcon.API instances are callable WSGI apps
app = falcon.API(after=[crossdomain])

# Resources are represented by long-lived class instances
register = Register()

# things will handle all requests to the '/things' URL path
app.add_route('/register', register)
from subprocess import call
import os

def is_requirement_satisfied():
	return True if "RABBIT_PORT_5672_TCP_ADDR" in os.environ else False
#end def

def write_to_gdg_web():
	with open("/root/web/gdg_web/_config.yml","w",encoding="utf-8") as my_file:
		my_file.write("title: GDG Surabaya\n")
		my_file.write("email: manager.gdgsurabaya@gmail.com\n")
		my_file.write('baseurl: ""\n')
		my_file.write('url: http://gdgsurabaya.org\n')
		my_file.write("markdown: kramdown\n")
		my_file.write("port: 80\n")
		my_file.write("host: 0.0.0.0\n")
		my_file.write("webserver: http://gdgsurabaya.org:8000\n")
		my_file.close()
	#end with
#end def

def write_to_gdg_webservice():
	with open("/root/web/gdg_webservice/_config.yml","w",encoding="utf-8") as my_file:
		my_file.write("mq_host: {}\n".format(os.environ["RABBIT_PORT_5672_TCP_ADDR"]))
		my_file.close()
	#end with
#end def

def write_config():
	write_to_gdg_web()
	write_to_gdg_webservice()
#end def

def start_webservice():
	# Find a way to start gunicorn using Python or BASH
	call("bash start_webservice.sh".split(" "))
#end def

def start_jekyll():
	# TODO: Find a way to start Jekyll using Python or BASH
	call("bash start_jekyll.sh".split(" "))
#end def
	
def start_service():
	write_config()
	#start_webservice()
	#start_jekyll
#end def

if __name__ == "__main__":
	if is_requirement_satisfied():
		start_service()
	#end if
#end if
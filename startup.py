from subprocess import call
import os

def is_requirement_satisfied():
	return True if "RABBIT_PORT_5672_TCP_ADDR" in os.environ else False
#end def

def copy_rabbit_address_to_data():
	with open("rabbit.yml", "w", encoding="utf-8") as my_file:
		my_file.write("- address: {}".format(os.environ["RABBIT_PORT_5672_TCP_ADDR"]))
		my_file.close()
	#end with
#end def

def start_webservice():
	call("bash start_webservice.sh".split(" "))
#end def

def start_jekyll():
	call("bash start_jekyll.sh".split(" "))
#end def
	
def start_service():
	copy_rabbit_address_to_data()
	start_webservice()
	start_jekyll
#end def

if __name__ == "__main__":
	if is_requirement_satisfied():
		start_service()
	#end if
#end if
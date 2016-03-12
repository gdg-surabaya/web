import yaml

my_file = open("./_config.yml","r",encoding="utf-8")
docs = yaml.load_all(my_file)
config = dict()
for doc in docs:
	config.update(doc)
#end for
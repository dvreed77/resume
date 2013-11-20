from jinja2 import FileSystemLoader, Environment
import json

env = Environment(loader=FileSystemLoader('templates'))

data = {}
data['general'] = json.load(open("general.json"))
data['education'] = json.load(open("education.json"))
data['experience'] = json.load(open("experience.json"))
data['skills'] = json.load(open("skills.json"))

template = env.get_template('base.html')

with open('index.html', 'w') as fid:
	fid.write(template.render(**data))
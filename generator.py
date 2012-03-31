from mako.template import Template
import json
import sys

serie = sys.argv[1]
datafile = open(sys.argv[2],'r')

json_data = datafile.read()
data = json.loads(json_data)

mytemplate = Template(filename='templates/spot_hint_tmpl.html')

for mushroom in data['mushrooms']:
    print mushroom
    page = open(serie + '/' + mushroom + '.html', 'w')
    page.write(mytemplate.render(**data['mushrooms'][mushroom]))
    page.close()
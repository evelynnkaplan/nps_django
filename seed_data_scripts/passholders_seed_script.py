from faker import Faker
import yaml 

fake = Faker()

passholders = []
for i in range(1, 26):
  passholder = {}
  passholder['model'] = 'nps_django.passholder'
  passholder['pk'] = i
  passholder['fields'] = { 
    'first_name': fake.name().split(' ')[0], 
    'last_name': fake.name().split(' ')[1],
    }
  passholders.append(passholder)

with open('passholders.yaml', 'w') as outfile:
    yaml.dump(passholders, outfile, default_flow_style=False)





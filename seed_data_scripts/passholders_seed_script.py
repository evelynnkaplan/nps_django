from faker import Faker
import yaml 

fake = Faker()

passholders = []
for i in range(1, 301):
  passholder = {}
  passholder['model'] = 'nps_django.passholder'
  passholder['pk'] = i
  passholder['fields'] = { 
    'first_name': fake.first_name(), 
    'last_name': fake.last_name(),
    }
  passholders.append(passholder)

with open('passholders.yaml', 'w') as outfile:
    yaml.dump(passholders, outfile, default_flow_style=False)





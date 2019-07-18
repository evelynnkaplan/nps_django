from faker import Faker
import yaml 
import random

fake = Faker()

visits = []

for i in range(1, 701):
  visit = {}
  visit['model'] = 'nps_django.visit'
  visit['pk'] = i
  visit['fields'] = { 
    'passholder': random.choice(range(1, 301)),
    'date': fake.date_between(start_date="-2y", end_date="today"),
    'park': random.choice(range(1, 62))
    }
  visits.append(visit)

with open('visits.yaml', 'w') as outfile:
    yaml.dump(visits, outfile, default_flow_style=False)





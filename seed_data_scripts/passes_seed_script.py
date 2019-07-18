from faker import Faker
import yaml 
import random

fake = Faker()

passes = []

pass_types = [
  'Standard',
  'Senior Lifetime',
  'Senior Annual',
  'Access',
  'Military',
  '4th Grade',
  'Volunteer'
  ]
pass_costs = [45.00, 80.00, 75.00, 30.00, 25.00, 100.00, 95.00]
pass_ids = []

for i in range(1, 26):
  if i < 10:
    pass_ids.append(f'00000{i}')
  else: 
    pass_ids.append(f'0000{i}')


for i in range(1, 26):
  new_pass = {}
  new_pass['model'] = 'nps_django.pass'
  new_pass['pk'] = i
  new_pass['fields'] = { 
    'type': random.choice(pass_types),
    'pass_id': pass_ids.pop(),
    'passholder_primary': i,
    'expiration_date': fake.date_between(start_date="-1y", end_date="+1y"),
    'zip_code': fake.postcode(),
    'email': fake.ascii_safe_email(),
    'phone_num': fake.phone_number(),
    'cost': random.choice(pass_costs)
    }
  passes.append(new_pass)

with open('passes.yaml', 'w') as outfile:
    yaml.dump(passes, outfile, default_flow_style=False)





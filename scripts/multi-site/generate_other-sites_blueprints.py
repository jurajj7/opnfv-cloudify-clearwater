# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


import yaml

base_filename = "../../openstack-blueprint"
with open(base_filename + ".yaml") as f:
    conf_yaml = yaml.safe_load(f)
f.close()

for k in conf_yaml['node_templates'].keys():
  if k.startswith('ellis'):
    conf_yaml['node_templates'].pop(k)
    
for k in conf_yaml['outputs'].keys():
  if k.startswith('ellis'):
    conf_yaml['outputs'].pop(k)
    
with open(base_filename + "_other-site" + ".yaml", "w") as f:
    f.write(yaml.dump(conf_yaml))
f.close()
    

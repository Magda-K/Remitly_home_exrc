# Remitly_home_exrc

import json

def check_star(path):
    #Creating a funkction which checks if Resource statement contains '*'
    
    with open(path, 'r', encoding='utf-8') as plik:
    plik_json = json.load(plik)
    
    if 'PolicyDocument' in plik_json:
      policyDocument = plik_json['PolicyDocument']
        if 'Statement' in policyDocument:
          statements = policyDocument['Statement']
          for statement in statements:
            if 'Resource' in statement:
              resource = statement['Resource']
                if resource == '*':
                  return True
                else:
                  return False
          else:
            print('Cannot find Statement in {} file'.format(plik_json))
      else:
        print('Cannot find PolicyDocument in {} file'.format(plik_json))






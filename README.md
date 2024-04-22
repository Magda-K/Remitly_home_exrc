# Remitly_home_exrc

    import json

    def check_star(path):
        #Creating a funkction which checks if Resource statement in json document contains '*' if so return false else return true
        try:
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
                          return False
                        else:
                          return True
                  else:
                    print('Cannot find Statement in {} file'.format(plik_json))
              else:
                print('Cannot find PolicyDocument in {} file'.format(plik_json))
        except FileNotFoundError as e:
            print('Given file is not exist.\nDetails:\n{}'.format(e))
        except Exception as e:
            print('Sorry we have an error...\nGiven:\n{}'.format(e))


# Example of usage
result = check_star('path/plik.json')
print('Result of checking if the file contains single * (False if it does, True otherwise)\n', result)




import json

def check_star(plik_json):
    #Creating a funkction which checks if Resource statement contains '*'

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



with open("D:/udemy_python/plik.json", 'r', encoding='utf-8') as plik:
    dane = json.load(plik)
print(dane)

check_star(dane)
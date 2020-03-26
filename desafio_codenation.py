import requests
import json
import hashlib

base_url = "https://api.codenation.dev/v1/challenge/dev-ps/"

get_string = "generate-data?token="
post_string = "submit-solution?token="

token = "token"

data_get = requests.get(base_url+get_string+token)

data_json_get = json.loads(str(data_get.text))

numero_casas = data_json_get["numero_casas"]
cifrado = data_json_get["cifrado"]

decifrado = ""
for i in cifrado:
    if( (ord(i) > 96) and (ord(i) < 123) ):
        aux = ord(i)-numero_casas
        if(aux < 97):
            aux = 123 - (97-aux)
        decifrado += chr(aux)
    else:
        decifrado += i

resumo_criptografico = hashlib.sha1(decifrado.encode()).hexdigest()

conteudo_file = {"numero_casas": numero_casas,"token":token,"cifrado":cifrado,"decifrado":decifrado,"resumo_criptografico":resumo_criptografico}

json_file = json.dumps(conteudo_file)

print(json_file)

file = open('answer.json','w+')

file.write(json_file)

file.close()

file = {'answer': open('answer.json','rb')}

post_file = requests.post(base_url+post_string+token,files=file)

print(post_file.text)
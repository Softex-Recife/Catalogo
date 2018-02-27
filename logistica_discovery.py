import json

def get_json_empresas(retorno_json):
    # lista_empresas = extrai_empresas_json(retorno_json)
    # str_empresas = lista_empresas.join(",")
    # str_resposta = "{empresas = [" + str_empresas + "]}"
    # str_resposta = "{empresas : ['Pitang', 'Qualinfo']}"
    return retorno_json


def extrai_empresas_json(texto):
    try:
        empresas = []
        dicionario = json.loads(texto)
        resultados = dicionario["results"]
        for i in resultados:
            empresa = i["extracted_metadata"]["title"]
            empresas.append(empresa)
        return empresas
    except:
        return "{oops: aconteceu um erro}"


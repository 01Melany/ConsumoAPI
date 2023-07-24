import requests


def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:

        #print(f"Nombre Comun: {pais['name']['common']}")
        #print(f"Nombre Oficial: {pais['name']['official']}")
        #print(f"Nombre Oficial: {pais['official']}")


        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        print(f"Codigo Telefonico es: {pais['idd']['root'] + pais['idd']['suffixes'][0]}")



        if "currencies" in pais:
            for Codigo , inf in pais["currencies"].items():
                Nombre = inf["name"]
                print(f"Su tipo de moneda es: {Nombre}({Codigo})")

        #print(pais)


url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'
listar_nombre_paises(url)
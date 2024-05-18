import requests
import pandas as pd

def fetch_world_bank_data(indicator, country, start_year, end_year):
    url = f'http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json&per_page=1000'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al acceder a la API para el indicador {indicator}: {response.status_code}")
        return []

    data = response.json()
    if not data or len(data) < 2:
        print(f"No se encontraron datos para el indicador {indicator}")
        return []

    records = []
    for item in data[1]:
        record = {
            'Indicator': indicator,
            'Country': item['country']['value'],
            'Year': item['date'],
            'Value': item['value']
        }
        records.append(record)

    return records

# Indicadores relacionados con la discriminación
indicators = [
    'SP.POP.TOTL.FE.ZS',  # Población femenina (% del total)
    'SE.ENR.PRSC.FM.ZS',  # Tasa de inscripción femenina en la educación primaria
    'SL.TLF.CACT.FE.ZS',  # Tasa de participación femenina en la fuerza laboral
    'SG.GEN.PARL.ZS',  # Mujeres en parlamentos nacionales (%)
    'SH.STA.MMRT',  # Tasa de mortalidad materna (por 100,000 nacidos vivos)
    'SP.DYN.LE00.FE.IN',  # Esperanza de vida al nacer, mujeres (años)
    'SH.CON.1524.FM.ZS',  # Prevalencia de VIH, mujeres (% de la población de mujeres entre 15-24 años)
    'SL.EMP.TOTL.SP.FE.ZS',  # Empleo en la fuerza laboral, mujeres (% del total de empleados)
    'SH.HIV.INCD',  # Incidencia de VIH
    'SE.ADT.LITR.FE.ZS'  # Tasa de alfabetización, mujeres (% de mujeres de 15 años o más)
]

country = 'ALL'  # 'ALL' para todos los países
start_year = 2000
end_year = 2020

all_data = []
for indicator in indicators:
    data = fetch_world_bank_data(indicator, country, start_year, end_year)
    all_data.extend(data)

# Convertir a DataFrame y guardar en CSV
df = pd.DataFrame(all_data)
df.to_csv('world_bank_discrimination_data.csv', index=False)

print('Datos guardados en world_bank_discrimination_data.csv')

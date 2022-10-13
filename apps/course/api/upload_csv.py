import json

import pandas as pd


def read_csv_courses(file):
    df = pd.read_csv(file, encoding='latin-1')
    # Llenar campso NaN a 0
    df['PRE REQUISITO 1'] = df['PRE REQUISITO 1'].fillna(0)
    df['PRE REQUISITO 2'] = df['PRE REQUISITO 2'].fillna(0)

    # Convertir datos a Int
    df['PRE REQUISITO 1'] = df['PRE REQUISITO 1'].astype(int)
    df['PRE REQUISITO 2'] = df['PRE REQUISITO 2'].astype(int)

    prerequisite = []
    elective = []

    for i in range(len(df['PRE REQUISITO 1'])):
        aux = []
        if df['ELECTIVO'][i] == 0:
            elective.append(False)
        if df['ELECTIVO'][i] == 1:
            elective.append(True)
        if int(df['PRE REQUISITO 1'][i]) != 0:
            aux.insert(0, int(df['PRE REQUISITO 1'][i]))
        if int(df['PRE REQUISITO 2'][i]) != 0:
            aux.insert(1, int(df['PRE REQUISITO 2'][i]))
        prerequisite.append(aux)

    df3 = df
    # Reemplazando datos de la columna pre requisitos
    df3 = df3.drop(df3.columns[[4, 5]], axis='columns')
    df3.insert(4, "pre_requisite", prerequisite, allow_duplicates=True)

    # Reemplazamos datos de la columna electivo
    df3 = df3.drop(df3.columns[[10]], axis='columns')
    df3.insert(10, "ELECTIVO", elective, allow_duplicates=True)

    # Modificación de nombres de columnas
    df2 = df3.rename(columns={
        'CODIGO': 'code',
        'NOMBRE DE LA ASIGNATURA': 'name',
        'SEMESTRE': 'semester',
        'CREDITOS': 'credits',
        'HORAS TEORICAS': 'hours_theory',
        'HORAS SEMINARIO': 'hours_seminar',
        'HORAS TEORICO PRACTICAS': 'hours_theopractice',
        'HORAS PRACTICAS': 'hours_practice',
        'HORAS LABORATORIO': 'hours_laboratory',
        'ELECTIVO': 'elective'})

    # Convertir campo CODIGO como id principal
    # df2.set_index('CODIGO', inplace=True)
    # Json formatter (https://stackoverflow.com/questions/52712825/how-to-convert-pandas-dataframe-to-custom
    # -nested-json)
    json_file = json.dumps([{j: row[j] for j in df2.columns} for i, row in df2.iterrows()])

    return json_file

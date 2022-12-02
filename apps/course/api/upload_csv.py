import csv as csv_mod
import codecs
import copy

import pandas as pd

from apps.course.models import Course


def read_csv_courses(file, study_plan_id):
    df = None
    file2 = copy.deepcopy(file)
    dialect = csv_mod.Sniffer().sniff(codecs.EncodedFile(file2, "utf-8").readline().decode())

    if dialect.delimiter == ',':
        df = pd.read_csv(file, encoding='latin-1')
    elif dialect.delimiter == ';':
        df = pd.read_csv(file, encoding='latin-1', sep=';')

    # Llenar campso NaN a 0
    df['PRE REQUISITO 1'] = df['PRE REQUISITO 1'].fillna(0)
    df['PRE REQUISITO 2'] = df['PRE REQUISITO 2'].fillna(0)
    df['DEPARTAMENTO 1'] = df['DEPARTAMENTO 1'].fillna(0)
    df['DEPARTAMENTO 2'] = df['DEPARTAMENTO 2'].fillna(0)

    # Convertir datos a Int
    df['PRE REQUISITO 1'] = df['PRE REQUISITO 1'].astype(int)
    df['PRE REQUISITO 2'] = df['PRE REQUISITO 2'].astype(int)
    df['DEPARTAMENTO 1'] = df['DEPARTAMENTO 1'].astype(int)
    df['DEPARTAMENTO 2'] = df['DEPARTAMENTO 2'].astype(int)
    df['CODIGO'] = df['CODIGO'].astype(int)

    prerequisite = []
    elective = []

    study_plan = []
    department = []

    for i in range(len(df.index)):
        aux_e = []
        aux_d = []

        study_plan.append(int(study_plan_id))

        if df['ELECTIVO'][i] == 0:
            elective.append(False)
        if df['ELECTIVO'][i] == 1:
            elective.append(True)
        if int(df['PRE REQUISITO 1'][i]) != 0:
            aux_e.insert(0, int(df['PRE REQUISITO 1'][i]))
        if int(df['PRE REQUISITO 2'][i]) != 0:
            aux_e.insert(1, int(df['PRE REQUISITO 2'][i]))

        if int(df['DEPARTAMENTO 1'][i]) != 0:
            aux_d.insert(0, int(df['DEPARTAMENTO 1'][i]))
        if int(df['DEPARTAMENTO 2'][i]) != 0:
            aux_d.insert(1, int(df['DEPARTAMENTO 2'][i]))
        prerequisite.append(aux_e)
        department.append(aux_d)

    df3 = df
    # Reemplazando datos de la columna pre requisitos
    df3 = df3.drop(df3.columns[[4, 5]], axis='columns')
    df3.insert(4, "pre_requisite", prerequisite, allow_duplicates=True)

    # Reemplazamos datos de la columna electivo
    df3 = df3.drop(df3.columns[[10]], axis='columns')
    df3.insert(10, "ELECTIVO", elective, allow_duplicates=True)
    # df3.insert(11, "component", component, allow_duplicates=True)
    df3.insert(11, "study_plan", study_plan, allow_duplicates=True)
    df3.insert(12, "department", department, allow_duplicates=True)

    # Modificación de nombres de columnas
    df4 = df3.rename(columns={
        'CODIGO': 'code',
        'NOMBRE DE LA ASIGNATURA': 'name',
        'SEMESTRE': 'semester',
        'CREDITOS': 'credits',
        'HORAS TEORICAS': 'hours_theory',
        'HORAS SEMINARIO': 'hours_seminar',
        'HORAS TEORICO PRACTICAS': 'hours_theopractice',
        'HORAS PRACTICAS': 'hours_practice',
        'HORAS LABORATORIO': 'hours_laboratory',
        'ELECTIVO': 'elective',
        'COMPONENTE': 'component'
    }
    )

    df5 = df4.to_dict('records')

    model_instances = []
    for course in df5:
        aux_course = Course(
            code=course['code'],
            name=course['name'],
            semester=course['semester'],
            elective=course['elective'],
            credits=course['credits'],
            hours_theory=course['hours_theory'],
            hours_seminar=course['hours_seminar'],
            hours_theopractice=course['hours_theopractice'],
            hours_practice=course['hours_practice'],
            hours_laboratory=course['hours_laboratory'],
            component_id=course['component'],
            study_plan_id=course['study_plan']
        )

        aux_course.department.set([])
        aux_course.pre_requisite.set([])

        model_instances.append(aux_course)

    Course.objects.bulk_create(model_instances)

    for i in range(len(model_instances)):
        model_instances[i].department.set(df5[i]['department'])
        model_instances[i].pre_requisite.set(df5[i]['pre_requisite'])

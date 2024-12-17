from django.core.management.base import BaseCommand
import pandas as pd
from models.models import *
from numpy import nan
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Импортирование экселя в базу данных"

    def handle(self, *args, **options):
        df = pd.read_excel("./excel.xlsx", header=[6])
        df.index.get_loc(df[df['Unnamed: 1'] == 'Матвеев Вадим Юрьевич'].index[0])
        for row in df.values:
            ad = []
            if row[1] is not nan:
                org = ''
                suborg =''
                subsuborg =''
                sub_sub_division = ''
                try:
                    pos = Position.objects.get(title=row[0])
                except:
                    pos = Position(title=row[0])
                    pos.save()
                try:
                    cab = Cabinet.objects.get(title=row[4])
                except:
                    cab = Cabinet(title=row[4])
                    cab.save()
                for i in range(df.index.get_loc(df[df['Unnamed: 1'] == row[1]].index[0]),-1,-1):
                    if df.values[i][1] is nan:
                        ad.append(df.values[i][0])
                        if len(str(df.values[i][0]).split('. ')[0].split('.')) == 1:
                            break
                org = ad[-1]
                if len(str(ad[0]).split('. ')[0].split('.')) == 3:
                    suborg = ad[1]
                    subsuborg = ad[0]
                else:
                    suborg = ad[0]
                if subsuborg != "":
                    try:
                        sub_sub_division = SubSubDivision.objects.get(title=subsuborg)
                    except:
                        sub_sub_division = SubSubDivision(title=subsuborg)
                        sub_sub_division.save()
                try:
                    sub_division = Subdivision.objects.get(title=suborg)
                except:
                    sub_division = Subdivision(title=suborg)
                    if sub_sub_division != "":
                        sub_division.sub_sub_division = sub_sub_division
                    sub_division.save()
                try:
                    organization = Organization.objects.get(title=org)
                except:
                    organization = Organization(title=org)
                    organization.save()
                    organization.subdivisions.add(sub_division)
                    organization.save()
                # try:
                full_name = str(row[1]).split(" ")
                print(pos)
                employee = Employee(first_name=full_name[1], last_name=full_name[0], patronymic=full_name[2],
                                    birthday=row[2], work_phone=row[3], cabinet_id=cab, email=row[5], position_id=pos,
                                    username=full_name, password=make_password(full_name[0]))
                employee.subdivision = sub_division
                if sub_sub_division != "":
                    employee.sub_sub_division = sub_sub_division
                employee.save()
                # except:
                #     print("Пользователь")
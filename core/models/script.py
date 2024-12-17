import pandas as pd
from numpy import nan
from models import *

def main():
    df = pd.read_excel("╨Ю╤А╨│.╤Б╤В╤А╤Г╨║╤В╤Г╤А╨░.xlsx", header=[6])
    df.index.get_loc(df[df['Unnamed: 1'] == 'Матвеев Вадим Юрьевич'].index[0])
    for row in df.values:
        ad = []
        if row[1] is not nan:
            # print(row)
            try:
                Position(title=row[0]).save()
            except:
                pass
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
                subsuborg = ''
            try:
                sub_sub_division = SubSubDivision(title=subsuborg)
                sub_sub_division.save()
                sub_division = Subdivision(title=suborg)
                sub_division.sub_sub_division = sub_sub_division
                sub_division.save()
                organization = Organization(title=org)
                organization.subdivisions = sub_division
                organization.save()
            except:
                pass
            try:
                full_name = str(row[1]).split(" ")
                employee = Employee(first_name=full_name[1], last_name=full_name[0], patronymic=full_name[2],
                                    birthday=row[2], work_phone=row[3], email=row[4])
                employee.subdivision = sub_division
                employee.sub_sub_division = sub_sub_division
                employee.save()
            except:
                pass
            # print(org, suborg, subsuborg)
        # print()


if __name__ == "__main__":
    main()
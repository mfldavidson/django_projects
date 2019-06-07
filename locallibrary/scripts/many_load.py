import csv

# python3 manage.py runscript many_load

from unesco.models import Site, Region, Category, States, Iso

def run():
    file = open('whc-sites-2018-clean.csv')
    reader = csv.reader(file)
    next(reader)

    Site.objects.all().delete()
    Region.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        c, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(name=row[9])
        st, created = States.objects.get_or_create(name=row[8],region=r)
        i, created = Iso.objects.get_or_create(name=row[10],states=st)
        try:
            ar=float(row[6])
        except:
            ar=None
        si = Site(name=row[0],description=row[1],justification=row[2],year=row[3],longitude=row[4],latitude=row[5],area_hectares=ar,category=c,iso=i)
        si.save()
from django.shortcuts import render, redirect
from .models import SAPImport, Elementy, History
from django.http import HttpResponse
from datetime import datetime

# requierments
import MySQLdb
import unicodecsv as csv
import re
import os

# Create your views here.


def index(request):
    return render(
        request,
        'elementy/index.html',
        {'dane': SAPImport.objects.filter(ackDate=None)})


def import_danych(request):
    linie = []
    pattern = r'^[a-zA-Z\W]'
    with open(os.path.join('elementy', 'export', 'export_temp'), 'br') as f:
        spamreader = csv.reader(
            f, delimiter=';', encoding='utf-8', errors='ignore')
        for row in spamreader:
            linie.append(row)
    for each in linie:
        empty_line = re.search(pattern, each[0])
        if empty_line is None:
            E, created = Elementy.objects.get_or_create(nr=each[1])
            if not each[6] == '':
                ackDate = datetime.strptime(each[6], '%d.%m.%Y')
            else:
                ackDate = None
            SAPImport.objects.get_or_create(ta=each[0],
                                            material=E,
                                            name=each[2],
                                            scheduledDate=datetime.strptime(
                                                each[3], '%d.%m.%Y'),
                                            createDate=datetime.strptime(
                                                each[4], '%d.%m.%Y'),
                                            createTime=datetime.strptime(
                                                each[5], '%H:%M:%S'),
                                            ackDate=ackDate,
                                            ackTime=datetime.strptime(
                                                each[7], '%H:%M:%S'),
                                            )
    return redirect('/elementy')


def update(request, *args, **kwargs):
    try:
        _id = request.GET['mat_id']
        _name = request.GET['name']
        _value = request.GET['value']
        element = Elementy.objects.get(nr=_id)
        setattr(element, _name, _value)
        element.save()
        History.objects.create(element=element, opis=_name)
        return HttpResponse('success')
    except Exception:
        return HttpResponse('error')


def import_startych(request):
    conn = MySQLdb.connect('jan-svr-intra', 'itadmin', 'J@nipo1')
    cursor = conn.cursor()
    query = ''
    cursor.execute(query)

    return redirect('/elementy')

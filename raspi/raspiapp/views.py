from django.shortcuts import render
import json

# Create your views here.
def datajson(request):
    with open(r'C:\Users\ASUS ROG\PycharmProjects\little\Django\raspi\raspiapp\static\json_file.json') as json_data:
        data1 = json.load(json_data) # deserialises itjson

    json_data.close()

    return render(request, 'raspiapp/json.html', {'data2': data1})

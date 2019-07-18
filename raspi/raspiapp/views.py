from django.shortcuts import render
import json

# Create your views here.
# this is the setting for your JSON file using json module
def datajson(request):
    with open(r'..\yourpathproject\raspi\raspiapp\static\json_file.json') as json_data:
        data1 = json.load(json_data) # read the official page for detail information (https://docs.python.org/3/library/json.html)

    json_data.close()

    # use 'data2' as a variable to pass to your html file
    return render(request, 'raspiapp/json.html', {'data2': data1})


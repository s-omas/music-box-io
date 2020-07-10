import json

def denest():
    with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/my_config.json') as f:
        data = json.loads(f.read())

    new_dict = {}

    # removes nesting from json, outputs a single dict

    for key in data:
        nest1 = data[key]
        for x in nest1:
            if type(nest1[x]) is dict:
                nest2 = nest1[x]
                for y in nest2:
                    new_dict.update({y: nest2[y]})
            else:
                new_dict.update({x: nest1[x]})



    return new_dict


#
# denest()
#
# config = denest()
# with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/schema/schema.json') as f:
#     data = json.loads(f.read())
#
# properties = data['properties']
#
# for x in properties:
#     section = properties[x]
#     subsection = section["properties"]
#     for y in subsection:
#         print(subsection[y])
#         print[config[y]['title']]
#
#     # if subsection[y]['additionalProperties']:
#            # data['properties'][x][y]['properties']['default'] = config[y]
#        # else:
#            # data['properties'][x][y]['default'] = config[y]
#
#
# with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/schema/populated_schema.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)
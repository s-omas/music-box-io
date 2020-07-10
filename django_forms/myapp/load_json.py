import json

#adds all bottom-level key-value pairs in config file to python dict

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


#populates config file with data from web form fields

def repopulate():
    with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/config_dict.json') as f:
        config_dict = json.loads(f.read())

    with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/my_config.json') as h:
        config = json.loads(h.read())

    for key in config:
        nest1 = config[key]
        for x in nest1:
            if type(nest1[x]) is dict:
                nest2 = nest1[x]
                for y in nest2:
                    config[key][x].update({y: config_dict[y]})
            else:
                config[key].update({x: config_dict[x]})

    with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/my_config.json', 'w') as outfile:
        json.dump(config, outfile, indent=4)






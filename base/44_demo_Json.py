import json

def demo_json():
    d = dict(name='kepler', age='27')
    j = json.dumps(d)
    print(j)
    json_str = '{"age": 20, "name": "kepler"}'
    json_obj = json.loads(json_str)
    print(json_obj)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def objToStr(Person):
    return {
        'name': Person.name,
        'age': Person.age
    }

def StrToObj(d):
    return Person(d['name'], d['age'])

if __name__ == '__main__':
    demo_json()
    s = Person('kepler', 27)
    print(json.dumps(s, default=objToStr))
    print(json.dumps(s, default=lambda x : x.__dict__))
    json_str = '{"age": 20, "name": "kepler"}'
    print(json.loads(json_str, object_hook=StrToObj))
    obj = json.loads(json_str, object_hook=lambda x : Person(x['name'], x['age']))
    print(obj.age)
    print(obj.name)
import json
from typing import Dict, List
from apispec import APISpec

class EasyFlaskSwagger:
    def __init__(self, title, version="1.0.0", openapi_version="3.0.2", info='some information...') -> None:
        self.spec = APISpec(
            title=title,
            version=version,
            openapi_version=openapi_version,
            info=dict(description=info),
        )
        self.schemas = None
        self.paths = None
        self.tags = None
        self.descriptions = None

    def setSchemas(self, schemas: list) -> None:
        self.schemas = schemas

    def setPaths(self, paths: Dict) -> None:
        self.paths = paths
        self.tags = list(paths.keys())
    
    def setDescriptions(self, descriptions: dict) -> None:
        self.descriptions = descriptions

    def __generate(self) -> None:
        if self.paths == None or self.tags == None or self.schemas == None or self.descriptions == None:
            raise Exception('Use EasyFlaskSwagger.setSchemas and EasyFlaskSwagger.setPaths first before generating the json.\nFor more info visit: https://github.com/YashMakan/easy_flask_swagger/tree/main/tests/main.py')
        for scheme in self.schemas:
            properties = getProperties(scheme)
            self.spec.components.schema(
                scheme.__name__, {"properties": properties})

        for tag in self.tags:
            description = self.descriptions.get(tag)
            self.spec.tag({
                'name': tag.value,
                'description': description
            })

            for tag, endpoints in self.paths.items():
                endpointDatas = getEndpointData(endpoints)
                for endpointData in endpointDatas:
                    operations = {method: {
                        'tags': [tag.value],
                        'summary': endpointData.desc,
                        'produces': [
                            "application/json",
                        ],
                    } for method in endpointData.methods}
                    self.spec.path(
                        path=endpointData.path,
                        operations=operations
                    )

    def to_dict(self) -> dict:
        self.__generate()
        return self.spec.to_dict()

    def save_output(self, path: str) -> None:
        self.__generate
        with open(path, 'w') as f:
            json.dump(self.spec.to_dict(), f, ensure_ascii=True, indent=4)

class EndpointData:
    def __init__(self, path: str, methods: str, desc: str) -> None:
        self.path = path
        self.methods = methods.split(',')
        self.desc = desc

def getEndpointData(endpoints: list) -> List[EndpointData]:
    endpointDatas = [
        EndpointData(
            str(endpoint.__doc__).split(',')[0].strip(),
            str(endpoint.__doc__).split(',')[1].strip(),
            str(endpoint.__doc__).split(',')[1].strip()
        ) for endpoint in endpoints
    ]
    return endpointDatas


def getProperties(cls):
    def getType(type):
        types = {
            'str': 'string',
            'enum': 'string',
            'epoch': 'integer',
            'bool': 'boolean'
        }
        return ("string" if types.get(type) == None else types.get(type))

    docString = str(cls.__doc__)
    lines = docString.splitlines()
    print([line for line in lines])
    properties = {
        line.strip().split(',')[0]:
        (
            {'type': getType(line.strip().split(
                ',')[1]), 'description': line.strip().split(',')[2].strip()}
            if 'enum' not in line.strip().split(',')[1]
            else {
                'type': getType(line.strip().split(',')[1].split('[')[0]),
                'enum': ','.join(line.strip().split(',')[1:]).split('[')[1].split(']')[0].split(','),
                'description': line.strip().split(',')[-1].strip()
            })
            for line in lines if len(line.strip()) > 0
    }
    return properties

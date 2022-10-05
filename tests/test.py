from easy_flask_swagger import EasyFlaskSwagger
from basic_models import User
from basic_flask import signup
from enum import Enum
from pprint import pprint


class SwaggerTags(Enum):
    AUTHENTICATION = 'authentication'


efs = EasyFlaskSwagger("My Backend Documentation")

efs.setPaths({
    SwaggerTags.AUTHENTICATION: [signup],
})

efs.setSchemas([
    User
])

efs.setDescriptions({
  SwaggerTags.AUTHENTICATION: 'For user authentication'
})

pprint(efs.to_dict())

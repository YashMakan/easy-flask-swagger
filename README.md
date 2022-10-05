
![Logo](https://github.com/YashMakan/website-assets/blob/main/1_4ds0jvsMN6eAaWBd4fyL5g.png?raw=true)


# Easy Flask Swagger 

Easy Flask Swagger - Creating flask swagger documentation in few minutes with least possible effort.


## Installation

#### Using PIP

```bash
  pip install easy-flask-swagger
```
## Usage/Examples

```python
from easy_flask_swagger import EasyFlaskSwagger
efs = EasyFlaskSwagger("My Backend Documentation")
efs.setPaths({SwaggerTags.AUTHENTICATION: [signup]})
efs.setSchemas([User])
efs.setDescriptions({
  SwaggerTags.AUTHENTICATION: 'For user authentication'
})
pprint(efs.to_dict())
# And that's it 😁
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/YashMakan/easy-flask-swagger
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the tests/test.py file

```bash
  python tests/test.py
```


## Authors

- [@Yash Makan](https://www.github.com/YashMakan)


## MIT License


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



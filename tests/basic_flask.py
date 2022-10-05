from flask import Flask, request
from basic_models import User

app = Flask(__name__)


class Database:

    @staticmethod
    def doesUserExist(mobile_number: str) -> bool:
        return False
        
    @staticmethod
    def addUser(user: User) -> None:
        pass


@app.route('/signup', methods=['POST'])
def signup():
    '''
    /signup, post, signup the user
    '''
    data = request.get_json(force=True)
    user = User.fromJson(data)
    if(Database().doesUserExist(user.mobile_number)):
        return {'status': 'failure', 'status_code': 400, 'message': 'User already exists'}
    else:
        user.user_id = 'some-random-id'
        Database().addUser(user)
        return {'status': 'success', 'status_code': 200, 'message': 'User added successfully'}


if __name__ == "__main__":
    app.run(debug=True)

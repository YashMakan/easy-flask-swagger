class User:
    '''
    mobile_number, str, user mobile number
    first_name, str, user first name
    last_name, str, user last name
    about, str, something about user
    email, str, user email address
    gender, enum[MALE,FEMALE,OTHER], gender of the user
    is_verified, bool, is user verified
    user_id, str, id of the user
    '''
    mobile_number = 'mobile_number'
    first_name = 'first_name'
    last_name = 'last_name'
    about = 'about'
    email = 'email'
    gender = 'gender'
    is_verified = 'is_verified'
    user_id = 'user_id'
    _id = '_id'

    def __init__(self, mobile_number, first_name, last_name, about, email, gender, is_verified=False, user_id=None, _id=None):
        self.mobile_number = mobile_number
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.email = email
        self.gender = gender
        self.is_verified = is_verified
        self.user_id = user_id
        self._id = _id

    def toJson(self):
        return {
            User.mobile_number: self.mobile_number,
            User.first_name: self.first_name,
            User.last_name: self.last_name,
            User.about: self.about,
            User.email: self.email,
            User.gender: self.gender,
            User.is_verified: self.is_verified,
            User.user_id: self.user_id,
            User._id: self._id
        }

    @staticmethod
    def fromJson(json):
        return User(
            json.get(User.mobile_number),
            json.get(User.first_name),
            json.get(User.last_name),
            json.get(User.about),
            json.get(User.email),
            json.get(User.gender),
            json.get(User.is_verified),
            json.get(User.user_id),
            json.get(User._id),
        )

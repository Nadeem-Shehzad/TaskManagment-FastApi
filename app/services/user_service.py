class UserService:

    def get_users(self):
        return [
            {"name": "Ali", "age": 25},
            {"name": "Sara", "age": 22}
        ]
    
    def create_user(self, user):
        return {
            "message": "User created",
            "user": user
        }
    
user_service = UserService()    
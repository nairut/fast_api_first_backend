from ..schemas import UserIn, UserSchema, Login
from pathlib import Path
from fastapi import HTTPException, status


class Services():
    
    def create_fake_db_folder(self):
        FAKE_DB_FOLDER = Path("fake_db")
        FAKE_DB_FOLDER.mkdir(exist_ok=True)
        return FAKE_DB_FOLDER
    
    def add_user_fake_file(self, new_user: UserIn):
        FAKE_DB_FOLDER = self.create_fake_db_folder()

        user_id = 0
        for user in FAKE_DB_FOLDER.glob("*.txt"):
            user_id += 1

        user_with_id = UserSchema(**new_user.model_dump(), user_id=user_id + 1)
        user_db_file = FAKE_DB_FOLDER / f"{user_with_id.username}.txt"

        if user_db_file.exists():
            raise HTTPException(
                status_code=status.HTTP_302_FOUND,
                detail= 'User Already exist'
            )

        with open(user_db_file, 'w') as f:
            for key, value in user_with_id.model_dump().items():
                f.write(str(value) + '\n')

        return user_with_id

    def get_user_list(self):
        list_of_users = []
        FAKE_DB_FOLDER = self.create_fake_db_folder()
        for user in FAKE_DB_FOLDER.glob("*.txt"):
            with open(user, 'r') as f:
                lines = f.readlines()
                list_of_users.append({"username": lines[0].strip(), "email": lines[1].strip(), 'password': lines[2].strip(), 'user_id': lines[3].strip()})
                # print(lines)
                # list_of_users.append(lines)
        # print(list_of_users)
        return list_of_users


    
    def user_log_in(self, username: Login, password: Login):
        FAKE_DB_FOLDER = self.create_fake_db_folder()
        for user in FAKE_DB_FOLDER.glob("*.txt"):
            is_user = False
            with open(user, 'r') as f:
                usernameline = f.readline()
                if username.strip() == usernameline.strip():
                    emailline = f.readline()
                    passwordline = f.readline()
                    if passwordline.strip() == password.strip():
                        is_user = True

        if is_user == False:
            return is_user
        else:
            return is_user 
                


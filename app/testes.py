
from pathlib import Path


FAKE_DB_FOLDER = Path('fake_db')


username = 'Dina'
password = "123456"

for user in FAKE_DB_FOLDER.glob("*.txt"):
    is_user = False
    with open(user, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if username.strip() == line.strip():
                is_user = True
            if password.strip() == line.strip():
                is_user = True
        





# if __name__ == '__main__':
#     print("Starting server...")
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#     # http://localhost:8000/



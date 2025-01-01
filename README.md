## Django  Real Time Chat API

## OR Git Clone & go to main project directory run
 -  git clone https://github.com/zihad868/Django-Chat-Server
 -  pip install -r requirements.txt
 -  cd ChatServer
 -  python manage.py makemigrations
 -  python manage.py migrate
 -  python manage.py  createsuperuser
 -  python manage.py runserver


# API Documentation

### Authentication

- **POST** `/api/register/`
  - Body: `{"username": "string", "email": "your email" "password": "string", "first_name": "string", "last_name": "string"}`
 
    

- **POST** `/api/login/`
  - Get Refresh & Access Token
  - Body: `{"email": "string", "password": "string"}`
 
    

 - **GET** `/api/{user_id}`
   - Response: `Get User Details`


- **PATCH** `/api/{user id}/update/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Body: `{"email": "string"}`


- **PUT** `/api/{user id}/update/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Body: `{"username": "string", "email": "your email" "password": "string", "first_name": "string", "last_name": "string"}`

- **DELETE** `/api/{user id}/delete/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Response: `User deleted successfully.`

- **GET** `/api/users/protected/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Response Your Email`
 
- **LOGOUT** `/api/logout/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"refresh": "Your Refresh Token"}`
    -  Response: `User Logout successfully.`



### Chat + Join Group
- **GET** `/api/messages/{conversation_id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Message Details`

 - **POST** `/api/messages/{{conversation_id}}/send/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"receiver_user": "Receiver user id", "message": "string"}`

 - **POST** `/api/groups/create/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Body: `{"name": "String", "members": "[id, ..]"}`


  - **POST** `/api/groups/{group_id}/join/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
      

   
 - **POST** `/api/groups/{group_id}/leave/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`

  
  - **GET** `/api/messages/files/{file_id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`


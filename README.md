## Django  Real Time Chat API

## OR Git Clone & go to main project directory run
 -  git clone https://github.com/zihad868/ProjectManagementServer.git
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


### Projects
- **GET** `/api/projects/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Project Details`

 - **POST** `/api/projects/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"name": "string", "description": "string"}`

 - **GET** `/api/projects/{priject id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Specific Project Details`

  - **PATCH** `/api/projects/{priject id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"description": "string"}`
   
 - **PUT** `/api/projects/{priject id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"name": "string", "description": "string"}`
  
  - **DELETE** `/api/projects/{priject id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Response: `Project deleted successfully.`


### Task
- **GET** `/api/projects/{project_id}/tasks/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Project Details`



 - **POST** `/api/projects/{project id}/tasks/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"title": "string", "description": "string"}`

 
 - **GET** `/api/tasks/{task id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Specific task details` 


 - **PATCH** `/api/tasks/{task id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"title": "string"}`
  
   
 - **PUT** `/api/tasks/{task id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"title": "string", "description": "string"}`
  
  - **DELETE**  /api/tasks/{task id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Response: `Task deleted successfully.`



  ### Comments
- **GET** `/api/tasks/{task id}/comments/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Get comments specific task`


 - **POST** `/api/tasks/{task id}/comments/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"content": "string"}`

- **GET** `/api/comments/{comment id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    - Response: `Specific comment details`

 - **PATCH** `/api/comments/{comment id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"content": "string"}`
   
 - **PUT** `/api/comments/{comment id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Body: `{"content": "string"}`

      
  - **DELETE**  `/api/comments/{comment id}/`
    - Header: `{Authorization:  Bearer  {Your Login Token}}`
    -  Response: `Task deleted successfully.`

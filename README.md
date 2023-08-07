THIS REPO HAS A SIMPLE EXAMPLE TO HOW TO CREATE AN API USING FASTAPI PACKAGE

APIS:
base url : http://127.0.0.1:8000
1.File upload api : http://127.0.0.1:8000/uploadfile
    -Parameters : {file: file data} ** NOTE :- the file data has to be in form format 
    ex: apiTest.py is provided as an example.

SETUP COMMANDS:
1. install fastapi :-  pip install "fastapi[all]"
2. install sqlalchemy :- pip install sqlalchemy 

COMMAND TO START THE SERVER:

move to root folder and run following command:
1.  uvicorn main:app --reload 

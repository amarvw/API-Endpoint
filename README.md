# API-Endpoint

### Prerequisites for making the API Endpoint ###
 1. **python :** version 3.3  (Reason : pyodbc is supported for version 3.3 and lesser ones only)
 2. **pyodbc module**  (<https://code.google.com/p/pyodbc/>) **:** Used to connect to the database (MS-SQL) and get the data
 3. **flask-restful module** (<http://flask-restful.readthedocs.org/en/latest/quickstart.html#>) **:** Python framework for building    a RESTful API
 4. **curl** **:** command line tool to transfer data over various protocols
 5. **Database connection** **:** 
   *_connection_string = 'DRIVER={SQL  Server};SERVER=172.16.16.170,49333;DATABASE=HQAssignment;UID=sa;PWD=Passwd@321'_*

###To test the API, the steps to be followed are :###
1. We need to donwload and install **pyodbc** and **flask-restful**.
2. Keep the **"GetBestDealsAPI.py"** file in the **"C:\Python33\pypyodbc-1.3.3\pypyodbc-1.3.3\"** location
3. Change the database connection to the local server in the GetBestDealsAPI.py file and save the changes
4. Open command prompt in the **"C:\Python33\pypyodbc-1.3.3\pypyodbc-1.3.3\"** directory, and run the following command
    C:\Python33\pypyodbc-1.3.3\pypyodbc-1.3.3>GetBestDealsAPI.py
5. Open another command prompt, and execute the following command :
   C:\Python33\pypyodbc-1.3.3\pypyodbc-1.3.3>curl http://localhost:5000/offer/best-deal/1084/2015-11-14/2015-11-16
6. You should get the required output.






   
 


 
 

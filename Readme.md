# README.md  

Attempted using the Django and Django Rest Framework.  
Used djangorestframework-simplejwt to generate JWT Tokens.(Module 1)  
Used django-cors-headers to enable CORS.(Module 1 & 2 )  
used the website www.test-cors.org to check if CORS works.  

# Module1:
http://127.0.0.1:8000/login/ -> Login Page.  
http://127.0.0.1:8000/signup/ -> Sign Up Page.  


# Module2:  
http://127.0.0.1:8000/prod/listprods/ -> Lists all products in the database.  
http://127.0.0.1:8000/prod/product_details/<str:pk>/  -> Displays the product with the particular id.  
http://127.0.0.1:8000/prod/createSKU/ -> Creates the Product and saves it in the Database.  
http://127.0.0.1:8000/prod/product_update/<str:pk>/ -> Updates the Product with the corresponding id from the Database.  
http://127.0.0.1:8000/prod/product_del/<str:pk>/ -> Deletes the Product with the corresponding id from the Database.  

enter the product id inplace of <str:pk>.  

Did not implement basic authentication.  

http://127.0.0.1:8000/admin/ -> username = admin, password=admin.  

Mysql tables are in the folder sqltables. [users(module1) and products(module2)]. username= root, password=root.  


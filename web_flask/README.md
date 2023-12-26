# 0x04. AirBnB clone - Web framework
## Learning Objectives
What is a Web Framework
What is a Web Stack
How does a web framework differ from web stack
How to build a web framework with Flask
How to define routes in Flask
What is a route
How to handle variables in a route
What is a template
How to create a HTML response in Flask by using a template
How to create a dynamic template (loops, conditions…)
How to display in HTML data from a MySQL database

## Tasks
0. Hello Flask!
Write a script “0-hello_route.py” that starts a Flask web application. Your web application must be listening on 0.0.0.0, port 5000. You must use the route “/” to display “Hello HBNB!”. You must use the option strict_slashes=False in your route definition.

1. HBNB
Write a script “1-hbnb_route.py” that starts a Flask web application. 
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/” to display “Hello HBNB!”. 
You must use the route “/hbnb” to display “HBNB”. 
You must use the option “strict_slashes=False” in your route definition.

2. C is fun!
Write a script “2-c_route.py” that starts a Flask web application. 
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/”, to display “Hello HBNB!”. 
You must use the route “/hbnb”, to display “HBNB”. 
You must use the route “/c/<text>” to display “C “ followed by the value of the “text” variable (replace underscore symbols with a space). 
You must use the option “strict_slashess=False” in your route definition.

3. Python is cool!
Write a script “3-python_route.py” that starts a Flask web application. 
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/”, to display “Hello HBNB!”. 
You must use the route “/hbnb”, to display “HBNB”. 
You must use the route “/c/<text>” to display “C “ followed by the value of the “text” variable (replace underscore symbols with a space). 
You must use the route “/python/<text>” to display “Python “, followed by the value of the text variable (replace underscore symbols with a space. The default value of “text” is “is cool”. 
You must use the option “strict_slashess=False” in your route definition.

4. Is it a number?
Write a script “4-number_route.py” that starts a Flask web application. 
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/”, to display “Hello HBNB!”. 
You must use the route “/hbnb”, to display “HBNB”. 
You must use the route “/c/<text>” to display “C “ followed by the value of the “text” variable (replace underscore symbols with a space). 
You must use the route “/python/<text>” to display “Python “, followed by the value of the text variable (replace underscore symbols with a space. The default value of “text” is “is cool”. 
You must use the route “/number/<n>” to display “n is a number” only if n is an integer. 
You must use the option “strict_slashess=False” in your route definition.

5. Number template
Write a script “5-number_template.py” that starts a Flask web application. 
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/”, to display “Hello HBNB!”. 
You must use the route “/hbnb”, to display “HBNB”. 
You must use the route “/c/<text>” to display “C “ followed by the value of the “text” variable (replace underscore symbols with a space). 
You must use the route “/python/<text>” to display “Python “, followed by the value of the text variable (replace underscore symbols with a space. The default value of “text” is “is cool”. 
You must use the route “/number/<n>” to display “n is a number” only if n is an integer. 
You must use the route “/number_template/<n>” to display a HTML page only if n is an integer. The H1 tag of the html page must have “Number: n” inside the tag BODY.
You must use the option “strict_slashess=False” in your route definition.

6. Odd or even?
Write a script “6-number_odd_or_even.py” that starts a Flask web application.
Requirements
Your web application must be listening on 0.0.0.0, port 5000. 
You must use the route “/”, to display “Hello HBNB!”. 
You must use the route “/hbnb”, to display “HBNB”. 
You must use the route “/c/<text>” to display “C “ followed by the value of the “text” variable (replace underscore symbols with a space). 
You must use the route “/python/<text>” to display “Python “, followed by the value of the text variable (replace underscore symbols with a space. The default value of “text” is “is cool”. 
You must use the route “/number/<n>” to display “n is a number” only if n is an integer. 
You must use the route “/number_template/<n>” to display a HTML page only if n is an integer. The H1 tag of the html page must have “Number: n” inside the tag BODY.
You must use the route “/number_odd_or_even/<n>” to display a HTML page only if n is an integer. The H1 tag “Number: n is even|odd” inside the tag BODY.
You must use the option “strict_slashess=False” in your route definition.

7. Improve engines
Update “models/engine/file_storage.py” by adding a public method “def close(self)” call “reload()” method for deserializing the JSON file to objects.
Update “models/engine/db_storage.py” by adding a public method “def close(self)” call “remove()” method on the private session attribute (“self.__session”) or “close()” on the class “Session”.

8. List of states
Write a script “web_flask/7-states_list.py” that starts a Flask web application.
Requirements
Your web application must be listening on 0.0.0.0, port 5000.
You must use storage for fetching data from the storage engine.
You must remove the current SQLAlchemy Session after each request. You should declare a method to handle @app.teardown_appcontent and call in this method storage.close().
You must use the route “/states_list” to display a HTML page inside the tag BODY. The H1 tag should have “States”. The UL tag should have the list of all State objects present in DBStorage sorted by name. The list of all State objects should use the LI tag should have “<State>:<state.id>: <B><state.name></B>”.
You must use the option “strict_slashes=False” in your route definition.

9. Cities by states
Write a script “web_flask/8-cities_by_states.py” that starts a Flask web application.
Requirements
Your web application must be listening on 0.0.0.0, port 5000.
You must use “storage” for fetching data from the storage engine.
You must remove the current SQLAlchemy Session after each request. You should declare a method to handle “@app.teardown_appcontext”. You should call in this method “storage.close()”
You should use the route “/cities_by_states” to display a HTML page. Inside the tag BODY, use the H1 tag States. Use the UL tag with the list of all State objects present in DBStorage sorted by name. The LI tag should have the description “State: <state.id>: <B><state.name></B> +  UL tag with the list of City objects linked to the State sorted by name. The LI tag description of one “City: <city.id>: <B><city.name></B>”.
You must use the option strict_slashes=False in your route definition.

10. States and State
Write a script “web_flask/9-states.py” that starts a Flask web application.
Requirements
Your web application must be listening on 0.0.0.0, port 5000.
You must use “storage” for fetching data from the storage engine.
You must remove the current SQLAlchemy Session after each request. You should declare a method to handle “@app.teardown_appcontext”. You should call in this method “storage.close()”
You must use the route “/states” to display a HTML page. Inside the tag BODY, use the H1 tag “States”, UL tag with the list of all State objects present in DBStorage sorted by name.
You must use the route “/states/<id>” display a HTML page. Inside the tag BODY, if a State object is found with this id, H1 tag State, H3 tag Cities, UL tag with the list of City objects linked to the State sorted by name. Otherwise H1 tag “Not found!”.
You must use the option strict_slashes=False in your route definition.

11. HBNB filters
Write a script “web_flask/10-hbnb_filters.py” that starts a Flask web application.
Requirement
Your web application must be listening on 0.0.0.0, port 5000.
You must use “storage” for fetching data from the storage engine.
You must remove the current SQLAlchemy Session after each request. You should declare a method to handle “@app.teardown_appcontext”. You should call in this method “storage.close()”
You must use the route “/hbnb_filters” to display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static.
You must use the option strict_slashes=False in your route definition.

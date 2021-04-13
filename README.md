This project implements parts of the megaventory API in order to demostrate its abilities.

I started by taking a deep look into the available methods from the API's documentation. Then I examined carefully the requirements for the project.

I thought that it would be much cleaner to spilt each request to a different class.
Each class has almost the same logic. It starts by initializing the required variables. Then there is a setInfo function where we can adjust the variables.
getInfo returns all the variables. in some classes i wrote a basic get function to demostrate how the class can expand its capabilities easily.
Lastly there is a post method where is submits the values to the database.

Secret.py holds the apikey and for security reasons i erased it before commiting it to github.
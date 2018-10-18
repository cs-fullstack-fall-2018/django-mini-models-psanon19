# Mini project. Rendering data models, and reverse lookup

Use the attached starter project for your work. The starter project provides a pre-populated database of users, and a basic template as a home page, along with a route that points to a user listing page.

### Your challenge:

- Modify ```views.py``` to add the necessary code to inject the list of current users into the context for the ```apptwo/users.html``` context
- Modify the ```users.html``` template to iterate the list of users and display the First Name, Last Name, and Email address for each user from the database
- Modify the existing home page (```index.html```) so that it displays a link that will take you to your user list page (```users.html```)

(HINT: use the reverse URL filter to lookup the named route in ```urls.py```)


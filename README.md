# PROJECT COINK REGISTER

In this project, you can find the proposed test for hiring Python developer for COINK company.  The project consists of developing a web application thats allow users to fill out a form and check the database created from these registrations.

The project addresses the following potential problems:
- The user does not fill in all the fields.
- the user registers data that already exists.
## How to run the project?
To use this project, you need to download the entire project and run the file "Form_Web.py". After executeing this file, copy the localhost adrdress and paste it into your preffered browser. In the initial interface, you'll find two buttons. The first button enables you to register your data, while the second button allows you to view the information stored in the "table_customer" table.
## Project content
### database
The current project has a folder to named "database" that contains the database used to save the user's dates in a table called
"table_customer". This table has three columns: name, email and city. This folder encompasses all potencial and new databases. 
### static 
The "static" folder contains a file for controlling various formats on the developed website.
### templates
The "templates" directory constains two HTML files that generate the project's interfaces:
- **index.html:**This is the main window that contains the form, allowing users submit information or navigate to the database-checking window.
- **show_database.html:** In this window, users can review the database created from the submitted data.
### Database_Manager.py
This script is responsible for managing the database. The exectution of this script generate the database and the  "table_customer" table. This script enables to insertion of data into the database.
### Form_Web.py
This script utilizes flask to extract the data collected from the user interface and registers this data in the database. It defines the structure of the website.

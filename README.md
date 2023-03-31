# Data Visualization
This project is a data analysis and visualization web application that aims at solving the big data problem.
It does this by drawing meaningful information from data to help users make well informed decisions.

The application takes in csv files and provides insightful and interactive visuals which help the user to  understand the data better.

<p align="center">
Home Page
</p>

![home](https://github.com/johngithinji-cs/Data-Visualization-project/blob/main/app/static/README/home.png)


### Installation and Usage
```bash
# Clone this repository
$ git clone https://github.com/johngithinji-cs/Data-Visualization-project.git`

# enusre the pwd is .../Data-Visualization-project
$ pwd

# Run the application server
$ flask run
```

After running the application, navigate to local host port 5000 on your web browser and explore the application.
It contains an authentication mechanism implemented using the Flask-login package. This enable users to access 
certain priviledges only after logging in.

The user has the ability to upload csv files as well as choose the type of chart that he/she wants to to use 
to visualize the data.

![architecture](/architecture)

## API's
### authentication
> /login (GET and POST)
- Renders the login page and returns login data respectively

> /signup (GET and POST)
- Renders the signup page and returns sign up data respectively

> /logout
- Logs out the user

> /profile
- Profile page of the user (Can only be accessed once the user has logged in)

### application
> / (GET)
- The home mage

> /upload (GET and POST)
- Renders the upload page and returns the uploaded file, which is then stored in a folder

> /dashboard

> /demo

> /display

## Sample Views

<p align="center">
Upload Page
</p>

![input](https://github.com/johngithinji-cs/Data-Visualization-project/blob/main/app/static/README/upload.png)

<p align="center">
Input Page
</p>

![input](https://github.com/johngithinji-cs/Data-Visualization-project/blob/main/app/static/README/input.png)

<p align="center">
Visualization
</p>

![bar](https://github.com/johngithinji-cs/Data-Visualization-project/blob/main/app/static/README/bar.png)

## Tech Stacks - Languages and Libraries used
- Python
- HTML
- CSS (Bulma)
- MySQL
- pandas
- matplotlib
- pytest
- dash (deprecated)

## Authors
- [John Githinji](./https://github.com/johngithinji-cs)
- [Sharon Nderi](./https://github.com/SNderi)
- [William Mwangi](./https://github.com/william-4)

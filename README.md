# Where To Go:
A tourist website showing interesting places in and around Moscow.

### This website is up and running here:
[Click here](http://phoenixghost.pythonanywhere.com/).

### How to add more places?
- Go to the admin panel of your locally run website at `127.0.0.1:8000/admin`, or if the site is already deployed - just add '/admin' to the site path in your browser.

![image](https://user-images.githubusercontent.com/108229516/236901257-76be866e-9f3b-4c70-9802-8c746672cccb.png)

- Go to Venues and click '+ add' button:

![image](https://user-images.githubusercontent.com/108229516/236902012-5a9fbae3-ae05-404b-9d98-50b671016023.png)

- Then you can fill in the new location name, descriptions, coordinates, photos.


# To add a new user with access to database:
Go to Users catalog and create a new user, then set User permissions in Permissions add Staff status.

# Also you can add new venues by loading JSON files.
The JSON file structure should be:
```json
{
    "title": "New Venue Example",
    "imgs": [
        "https://picture_link_example_one.jpg",
        "https://picture_link_example_two.png",
        "https://picture_link_example_three.jpeg",
        "https://etc.jpg
    ],
    "description_short": "Short description text here.",
    "description_long": "Long description text here (HTML tags supported)",
    "coordinates": {
        "lng": "55.5555",
        "lat": "55.5555"
    }
}
```
**To add Venues by means of JSON files uploading use the "-path" argument command:
`python3 manage.py load_place -path <link to the json file>`**

If the files are uploading from GitHub vault please obtain the correct link via clicking the "Raw" button and copying the url in browser address line.


# How to make this site up and running:

- Download or clone [repo](https://github.com/Ph0enixGh0st/where_to_go.git)
- You must have Python 3.9 or higher already installed;
- Create the virtual environment with this command:
```
python3 -m venv venv
```
- Install the requirements using command:
```
pip3 install -r requirements.txt
```
Create `.env` file and set environment variables without whitespaces:
- SECRET KEY=your_project_secret_key
- DEBUG=False
- MEDIA_ROOT=media/
- MEDIA_URL=/media/
- STATIC_URL=/static/
- ALLOWED_HOSTS=[]
- STATIC_ROOT=assets

- Create superuser:
```
python3 manage.py createsuperuser
```
- The run the server with this command:
```
python3 manage.py runserver
```

### Project Goals

The project was made for educational purposes at online-course for web-developers [dvmn.org](https://dvmn.org/)
Venues were taken from [KudaGo](https://kudago.com).

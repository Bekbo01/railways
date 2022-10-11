# Django Railways tracker app

## Installation

> To use this project you must have *python*,  *pip*, *virtualenv* installed

### Clone the project

```git
git clone https://github.com/Bekbo01/railways.git
```

### create a virtual environment

unix / mac

```pyhton
virtualenv virtualenv_name
```

windows

```pyhton
virtualenv myenv
```

## activate the virtual environment
unix / mac

``` python
virtualenv -p /usr/bin/python3 virtualenv_name
```

windows

``` python
myenv\Scripts\activate
```



### Install project dependency

``` console
pip install -r requirements.txt
```

### create data base table 

```` console
python manage.py migrate
python manage.py makemigrations
````

### Start development server with the following commands

```` console
python manage.py runserver
````

> ps: when ever you want to start the development server you only have to run: ```` python manage.py runserver ````





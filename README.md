# Web Server HungrYT

Is a web service developed on Django with Postgresql for a food e-commerce.

## Getting Started

To clone the project use the comand:
```
$ git clone https://github.com/OsirisRoman/HungrYT.git
```
To start the server use:
```
$ cd HungrYT
$ python manage.py runserver
```

### Prerequisites

The prerequisites for execute the project are postgreSql, django, djangorestframework and psycopg2.
Also is important migrate the tables to our database to do these we use the command:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

NOTE: For this step is needed configure the login and name information of the database (edit /HungrYTWeb/settings.py)


### Installing

To install the software needed is important have pip installed read https://pypi.python.org/pypi/pip:

```
$ pip install django djangorestframework psycopg2

```
For postgresql we can install it from https://www.postgresql.org/download/

## Creating Modules or Apss
The project consist of a set of modules or apps. In order to create a new module enter the following command.
```
$ python manage.py startapp sales
```
The fisrt time that the app is created, it has the following files


```
\sales
  \migrations
    __init__.py
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
```

## Running the tests

The project have different test to verify the correct performance

### Test that the date of new sales are correctly obtain.

The test is for the module Sales, simulating that a new sale is added veryfing if the date of the sale is the actual date, and that the information on sales is correctly inserted.

```
$ python manage.py test sales.tests
```
or
```
$ python manage.py test sales
```
to run all the test cases of a specific module

## Authors

* **Hugo Betancourt** 
* **Osiris Roman** 
* **Andrés Riofrío** 
* **José Seraquive**
* **Oscar Guarnizo**
* **Emil Vega**
* **Joseph Gonzalez**
* **Giovanny Caluña**
* **Alejandro Valencia**
* **Henry Caraguay**

See also the list of [contributors](https://github.com/OsirisRoman/HungrYT/graphs/contributors) who participated in this project.

## License

See the [LICENSE.md](https://github.com/OsirisRoman/HungrYT/blob/master/LICENSE) file for details

## Programming guideline for introduce code.


* The name of the modules is in plural and with lowercase

* The classes start with uppercase

* The functions start with lowercase

* If the function name consist on two words both of them start with uppercase
```
Example: class SalesList(generics.ListCreateAPIView)
```

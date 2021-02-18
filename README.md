![](https://news.airbnb.com/wp-content/uploads/sites/4/2020/03/BeloRauschNewsroomSocial_200316.png)


# AirBnB clone - The console 🚀

This project consist about how to build a console that is a copy of the AirBnB project, this is just the first steep to build the whole project call AirBnB.


## What is the console and how works? ⚙️

The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler.

Input lines are parsed into two parts. The command, and any other text on the line.

## What can the interpreter do? 🔩

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## How to start it? 📦

The first thing to do is to download the repository and clone it into your local machine.

In your linux:

```
cd /home
```
Now clone the repository:
```
git clone https://github.com/sebastiancalleu/AirBnB_clone.git
```
Now got to the repository that was cloned
```
cd AirBnB_clone
```
Now to start the console:
```
./console.py
```


The console also can works like this, in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## How to use it? 📌
Here is an example to use `all`, `show`, `create`, `update` and `destroy`

```
holberton@AirBnB_clone$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb)
(hbnb) show BaseModel
** instance id missing **
(hbnb)
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb)
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb)
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb)
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb)
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb)
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

## Authors ✒️

Sebastian Calle Uribe
Yeferson Julian Losada Mendez

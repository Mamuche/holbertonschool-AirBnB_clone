<p align="center">
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://images.squarespace-cdn.com/content/v1/5a4bfe8bf09ca4228ceca3b7/1539139199598-ANH454IHZI1OKWONKRXY/logo.jpg?format=2500w">
 <source media="(prefers-color-scheme: light)" srcset="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIrK23KvJPB7XdZrIk9mHwe3GZvtsUZLjkh-eG6KRgCLeWu3MW0kFcggq4COpLmeZviQ&usqp=CAU">
 <img alt="image holberton school" src="https://apply.holbertonschool.com/auth/sign_up?country=fr&locale=fr">
</picture>
</p>

# **AirBnB clone - The console**

Write a command interpreter to manage your AirBnB objects.

## **Team and Tasks**

This project was released by Edem Djossou and Marion Laroche in [Holbertonschool](https://www.holbertonschool.fr/?gad_source=1&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGZshq5Y0wpTRGv4wPcY4bKSsX2uqJ0Q8YIAl5CLWh98Fr5Nqb4s6VhoCDUEQAvD_BwE)'s Bordeaux. We work on the campus every day and we make a Check in every morning and a Check out every afternoon. We divided the tasks, but we work in collaboration for all the project (decisions, organisation, commits...).

Our simple shell is a program that takes commands from the keyboard via the terminal, and gives them to the operating system to perform.

## **Its essential functionalities**

we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

## **List of allowed functions and system calls for this project**

- models
- engine
- __int__.py
- amennity.py
- base_model.py
- city.py
- place.py
- review.py
- state.py
- users.py
- test engine
- test_amenity
- test_base_model
- test_city
- test_place
- test_review
- test_state
- test user
- test base model_dict
- test fil_storage
- test save reload_model.py
- test save reload_user


## **Compilation**



## **Files**
## Classes :cl:

HolbertonBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the 
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HolbertonBnB instantiates an instance of 
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from 
any class instances stored in the JSON file `file.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the `file.json`.

## Console :computer:

The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.


## **Authors**
Djossou Edem [Github](https://github.com/edemdj).

Laroche Marion [Github](https://github.com/Mamuche).

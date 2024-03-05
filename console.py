#!/usr/bin/python3
"""program contains the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "
    __valid_classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_quit(self, arg):
        """cmd to exit the program"""
        return True

    def do_EOF(self, arg):
        """cmd to exit the program"""
        print('Quit command to exit the program')
        return True

    def emptyline(self):
        """cmd shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg in self.__valid_classes:
            new_instance = self.__valid_classes[arg]()
            models.storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1] if len(args) > 1 else "")
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = models.storage.all()
            obj = all_objects.get(key)
            if obj:
                del all_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = arg.split()
        all_instances = []

        if not args:
            for obj in models.storage.all().values():
                all_instances.append(str(obj))
            print(all_instances)
        elif args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                if args[0] in key:
                    all_instances.append(str(obj))
            print(all_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = models.storage.all()
            obj = all_objects.get(key)
            if obj:
                setattr(obj, args[2], eval(args[3]))
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""program contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """cmd to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """cmd to exit the program"""
        print()
        return True

    def emptyline(self):
        """cmd shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

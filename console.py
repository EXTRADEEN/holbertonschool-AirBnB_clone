#!/usr/bin/python3
"""Created class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Created a class that contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'
    class_name = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                  "Review"]

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Passed an empty line when ENTER
        """
        pass

    def do_create(self, line):
        """create a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the\
        class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            arg = line.split(" ")
            if arg[0] not in self.class_name:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = "{}.{}".format(arg[0], arg[1])
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    print(objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        arg = line.split(" ")
        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in objects.keys():
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name
        """

        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        arg = line.split(" ")
        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in objects.keys():
                print("** no instance found **")
            else:
                setattr(objects[key], arg[2], arg[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models import State, City, Amenity, Place, Review


class HBNBCommand(cmd.Cmd):
    """a class for the command interpreter"""

    prompt = "(hbnb)"

    def do_create(self, arg):
        """create a new instance of basemodel"""
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string representation of an instance"""
        if not args:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                else:
                    print(objects[key])

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in object:
                    print("** no instance found **")
                else:
                    del object[key]
                    storage.save()

    def do_all(self, arg):
        """print all string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User"]:
                print("** class doesnt exist **")
            else:
                filtered_objects = [str(obj) for key, obj in objects.items() if args[0] in key]
                print(filtered_objects)

    def do_update(self, arg):
        """updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(objects[key], args[2], eval(args[3]))
                    storage.save()

    def do_quit(self, arg):
        """quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """exit the command interpreter at the end of the file"""
        print()
        return True

    def emptyline(self, arg):
        """do nothing when an empty line is created"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

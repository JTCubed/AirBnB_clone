#!/usr/bin/env python3
"""entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_show(self, argv):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = argv.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                obj_dict = storage.all()
                if key in obj_dict:
                    print(obj_dict[key])
                else:
                    print("** no instance found **")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                new_instance = eval(f'{class_name}()')
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                obj_dict = storage.all()
                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        Usage: all [class name]
        """
        args = arg.split()
        obj_dict = storage.all()

        if not args:
            print([str(obj) for obj in obj_dict.values()])
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                    globals()[class_name], BaseModel):
                print("** class doesn't exist **")
            else:
                filtered_objs = [str(obj) for key, obj in obj_dict.items()
                                 if key.startswith(class_name + ".")]
                print(filtered_objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            instance_key = f"{class_name}.{instance_id}"
            if instance_key not in obj_dict:
                print("** no instance found **")
                return

            obj_instance = obj_dict[instance_key]
            attribute_name = args[2]
            attribute_value = args[3]

            setattr(obj_instance, attribute_name, attribute_value)
            obj_instance.save()

    def do_quit(self, arg):
        """
        exits the cmd for 'quit' as an arg to cmd
        """
        return True

    def do_EOF(self, line):
        """
        Exits the program cleanly
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
"""Point of entry of command interpreter"""
import cmd
import importlib
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
        "Place": Place
    }

    def checkClass(self, cmmd, oid):
        """Method that checks class-name existence and class existence"""

        if not cmmd:
            print("** class name missing **")
            return False
        elif cmmd not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif not oid:
            print("** instance id missing **")
            return False
        #elif oid == 0:
            #return True
        else:
            return True

    def do_create(self, cmmd):
        """Creates a new instance of BaseModel"""
        if cmmd:
            commands = cmmd.split(' ')
            # Used 1 as an oid to by-pass instance id check in checkClass()
            if not self.checkClass(commands[0], 1):
                    return
            else:
                newInst = HBNBCommand.__classes[cmmd]()
                storage.save()
                print(f"{newInst.id}")
        else:
            print("** class name missing **")

    def do_show(self, cmmd):
        """Prints class name and insatnce id"""
        if cmmd:
            commands = cmmd.split(' ')
            cname = commands[0]
            if len(commands) == 1:
                if not self.checkClass(cname, None):
                    return
            if len(commands) > 1:
                oid = commands[1]
                key = f"{commands[0]}.{commands[1]}"
                avail_id = storage.all()
                if key in avail_id:
                    instance = avail_id[key]
                    print(instance)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, cmmd):
        """Updates an object"""
        if cmmd:
            commands = cmmd.split(' ')
            cname = commands[0]
            if len(commands) == 1:
                if not self.checkClass(cname, None):
                    return
            if len(commands) > 1:
                oid = commands[1]
                key = f"{commands[0]}.{commands[1]}"
                avail_id = storage.all()
                if key in avail_id:
                    instance = avail_id[key]
                    if len(commands) < 3:
                        print("attribute name missing")
                        return
                    elif len(commands) < 4:
                        print("** value missing **")
                        return
                    else:
                        setattr(instance, commands[2], commands[3])

                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, cmmd):
        """Prints class name and insatnce id"""
        if cmmd:
            commands = cmmd.split(' ')
            cname = commands[0]
            if len(commands) == 1:
                if not self.checkClass(cname, None):
                    return
                print("** instance id missing **")
                return
            if len(commands) > 1:
                oid = commands[1]
                key = f"{commands[0]}.{commands[1]}"
                avail_id = storage.all()
                if key in avail_id:
                    del avail_id[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            self.checkClass(cmmd, 0)

    def do_all(self, cmmd):
        """ Prints all string representation of all instances"""
        new_list = []
        obj_list = storage.all()
        if not cmmd:
            for inst in obj_list.keys():
                obj = obj_list[inst]
                new_list.append(str(obj))
            print(new_list)
        else:
            commands = cmmd.split(' ')
            cname = commands[0]
            if not self.checkClass(cname, 1):
                return
            for i in obj_list.keys():
                c = i.split(".")
                if cname == c[0]:
                    obj = obj_list[i]
                    new_list.append(str(obj))
            print(new_list)

    def do_quit(self, line):
        """Exit the program"""
        return True

    def help_quit(self):
        """shows help info of quit command"""
        print("Quit command to exit the program")
        print("\n")

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def help_EOF(self):
        """shows help info of EOF command"""
        print("Quit command to exit the program\n", end=" ")
        print("\n")

    def emptyline(self):
        """When empty line is passed or  ENTER is pressed
        nothing should be  executed"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
"""Point of entry of command interpreter"""
import cmd
import importlib
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def checkClass(self, cmmd, oid):
        """Method that checks class-name existence and class existence"""

        mod = importlib.import_module("models.base_model")

        if not cmmd:
            print("** class name missing **")
            return False
        elif not hasattr(mod, cmmd):
            print("** class doesn't exist **")
            return False
        elif oid == 0:
            return True
        elif not oid:
            print("** instance id missing **")
            return False
        else:
            return True

    def do_create(self, cmmd):
        """Creates a new instance of BaseModel"""
        if not self.checkClass(cmmd, 0):
            pass
        else:
            bm = BaseModel()
            storage.save()
            print(f"{bm.id}")

    def do_show(self, cmmd):
        """Prints class name and insatnce id"""
        if cmmd:
            commands = cmmd.split(' ')
            cname = commands[0]
            if not self.checkClass(cname, None):
                return
            if len(commands) > 1:
                oid = commands[1]
                if not self.checkClass(cname, oid):
                    return
        else:
            self.checkClass(cmmd, 0)

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
        nothing should be  executed anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

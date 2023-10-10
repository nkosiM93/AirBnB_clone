#!/usr/bin/env python3
"""Point of entry of command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """When empty line is passed or  ENTER is pressed
        nothing should be  executed anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

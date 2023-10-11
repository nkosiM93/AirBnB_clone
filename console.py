#!/usr/bin/env python3
"""Point of entry of command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

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

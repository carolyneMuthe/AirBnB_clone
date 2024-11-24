#!/usr/bin/python3
# A simple command interpreter for AirBnB

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_help(self, arg):
        """Display available commands"""
        print("Documented commands (type help <topic>):")
        print("EOF  help  quit")

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

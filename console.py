#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Main class for AirB&b
    """

    intro = """ Welcom to AirB&B console

            -----------------------------------------------
            Description: Our fun AirB&B project
            Author     : Jean-José  & Idriss
            Version    : 1.0
            help       : Type help or ? to list commands
            -----------------------------------------------
            \n
            """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_create(self, args):
        """creates a new instance"""
        args_parsed = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        try:
            newInstance = eval(args_parsed[0])()
            newInstance.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_parsed = args.split()

        if len(args_parsed) == 0:
            print("** class name missing **")
            return
        if len(args_parsed) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args_parsed[0])
        except:
            print("** class doesn't exist **")

        objDict = storage.all()
        keyId = args_parsed[0] + "." + args_parsed[1]

        try:
            value = objDict[keyId]
            print(value)
        except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

import lldb
import time

def automat(debugger, command, result, dict):
        args = command.split(" ")
        if not len (args) == 3:
            print "Usage: 3 numbers in arguments"
            exit()

def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f automatik.automat automatik')

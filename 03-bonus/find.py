import lldb

def print_find(debugger, command, result, dict):
        target = debugger.GetSelectedTarget()
        if target:
                print str(target).find("l")

def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f find.print_find find')

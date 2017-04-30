import lldb

def print_replace(debugger, command, result, dict):
        target = debugger.GetSelectedTarget()
        if target:
                print str(target).replace("e", "z")

def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f replace.print_replace replace')

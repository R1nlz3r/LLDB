import lldb

def print_count(debugger, command, result, dict):
        target = debugger.GetSelectedTarget()
        if target:
                print str(target).count("e")

def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f count.print_count count')

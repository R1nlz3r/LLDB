import lldb

def print_uppercase(debugger, command, result, dict):
	target = debugger.GetSelectedTarget()
	print 'FT_' + str(target).upper()

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f uppercase.print_uppercase uppercase')

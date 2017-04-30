import lldb

def print_lowercase(debugger, command, result, dict):
	target = debugger.GetSelectedTarget()
	print 'FT_' + str(target).lower()

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f lowercase.print_lowercase lowercase')

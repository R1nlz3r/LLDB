import lldb

def print_reverse(debugger, command, result, dict):
	target = debugger.GetSelectedTarget()
	if target:
		print 'FT_' + str(target)[::-1]

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f reverse.print_reverse reverse')

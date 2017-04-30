import lldb
import time

def auto(debugger, command, result, dict):
        args = command.split(" ")
        if not len (args) == 3:
            print "Usage: 3 numbers in arguments"
            exit()

        debugger.SetAsync(True)
        debugger.HandleCommand("breakpoint set --name main")
        debugger.HandleCommand("process launch")
        debugger.HandleCommand("br s -f source.cpp -l 16 -i 1")
        debugger.HandleCommand("br s -f source.cpp -l 19 -o")
        debugger.HandleCommand("b source.cpp:32")
        debugger.HandleCommand("b source.cpp:41")
        debugger.HandleCommand("process continue")
        debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[0] + '\n')
        debugger.HandleCommand("expr tab[0] = tab[1]")
        debugger.HandleCommand("process continue")
        debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[1] + '\n')
        debugger.HandleCommand("expr int $swap = tab[1]")
        debugger.HandleCommand("process continue")
        debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[2] + '\n') 
        debugger.HandleCommand("expr count = 0; tab[2] = tab[1]; tab[1] = $swap")
        debugger.HandleCommand("process continue")
        debugger.HandleCommand("expr tmp = 0; int j = 0; while(j < max){tmp += min[j]; ++j;}")
        debugger.HandleCommand("process continue")
        debugger.HandleCommand("expr int k = 0; while(k < max){biggest = (biggest <= min[k])? min[k] : biggest; ++k;}; max = 0")
        debugger.HandleCommand("process continue")

def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f auto.auto auto')

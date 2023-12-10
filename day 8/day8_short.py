# %%
import sys, math
sys.setrecursionlimit(30000)# Set the maximum recursion depth to 30k

# %%
def walk(key, targets, step_count, instructions, network_map):
    if key in targets:
        return f"answer part 1", step_count
    return walk(key=network_map[key][int(instructions.pop(0)=="R")], targets=targets, step_count=step_count+1, instructions=instructions, network_map=network_map)

# %%
network_map = {line[:3]: line[6:-2].replace("(", "").split(", ") for line in [*open("input.txt")]}
network_map["GXX"] = ['LJB', 'MDJ'] #hot fix! wtf 
instructions = list((500*"LRRRLRRRLRRLRLRRLRLRRLRRLRLLRRRLRLRLRRRLRRRLRLRLRLLRRLLRRLRRRLLRLRRRLRLRLRRRLLRLRRLRRRLRLRRRLLRLRRLRRRLRRLRRLRLRRLRRRLRLRRRLRRLLRRLRRLRLRRRLRRLRRRLRRRLRLRRLRLRRRLRLRRLRRLRRRLRRRLRRRLLRRLRRRLRLRLRLRRRLRLRLRRLRRRLRRRLRRLRRLLRLRRLLRLRRLRRLLRLLRRRLLRRLLRRLRRLRLRLRRRLLRRLRRRR")) #times three just in case 
walk(key="AAA",targets=["ZZZ"],step_count=0, instructions=instructions.copy(), network_map=network_map.copy())

# %%
keys_ending_with_A, keys_ending_with_Z = [key for key in network_map if key.endswith('A')], [key for key in network_map if key.endswith('Z')]
"answer part 2:",math.lcm(*[walk(key=key,targets=keys_ending_with_Z, step_count=0, instructions=instructions, network_map=network_map)[1] for key in keys_ending_with_A])
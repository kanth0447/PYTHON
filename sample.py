import subprocess
import shlex
import json

df_array = [shlex.split(x) for x in subprocess.check_output(["df","-h"]).rstrip().split('\n')]
df_num_lines = df_array[:].__len__()
df_json = {}
df_json["filesystems"] = []

for row in range(1, df_num_lines):
    result = {}
    fsName = df_array[row][0]
    fsSize = df_array[row][1]
    fsUsed = df_array[row][2]
    fsAvail = df_array[row][3]
    fsUse = df_array[row][4]
    fsMountPoint = df_array[row][5]
    result["filesystem"] = {}
    result["filesystem"]["name"] = fsName
    result["filesystem"]["size"] = fsSize
    result["filesystem"]["used"] = fsUsed
    result["filesystem"]["Avail"] = fsAvail
    result["filesystem"]["use%"] = fsUse
    result["filesystem"]["mounted_on"] = fsMountPoint
    df_json["filesystems"].append(result)
print json.dumps(df_json, sort_keys=True, indent=2)
    
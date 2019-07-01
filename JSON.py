import subprocess
import shlex
import json

def main():
    df_array = [shlex.split(x) for x in
                subprocess.check_output(["df","-h"]).rstrip().split('\n')]
    df_num_lines = df_array[:].__len__()
    df_json = {}
    df_json["filesystems"] = []
    for row in range(1, df_num_lines):
        df_json["filesystems"].append(df_to_json(df_array[row]))
    print json.dumps(df_json, sort_keys=True, indent=2)
    return

def df_to_json(tokenList):
    result = {}
    fsName = tokenList[0]
    fsSize = tokenList[1]
    fsUsed = tokenList[2]
    fsAvail = tokenList[3]
    fsUse = tokenList[4]
    fsMountPoint = tokenList[5]
    result["filesystem"] = {}
    result["filesystem"]["name"] = fsName
    result["filesystem"]["size"] = fsSize
    result["filesystem"]["used"] = fsUsed
    result["filesystem"]["Avail"] = fsAvail
    result["filesystem"]["use%"] = fsUse
    result["filesystem"]["mounted_on"] = fsMountPoint
    return result

if __name__ == '__main__':
    main()
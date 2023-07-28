import subprocess, sys, os

def install(filepath: str, options: [str]) -> None:
    with open(filepath, "r", encoding='utf-8') as file:
        lines = [line for line in file.readlines() if line.strip() != ""]
        for line in lines:
            splitted = line.split()
            if len(options) > 0:

            else:


if __name__ == "__main__":
    args = sys.argv[1:]
    repopath = "/".join(os.path.realpath(__file__).split("/")[:-2])
    
    if len(args) > 0:
        filepath = os.path.join(repopath, "packages", args[0] + ".txt")
        install(filepath, args[1:])
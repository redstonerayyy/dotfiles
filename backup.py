import os

# ------------ backup config files ------------ #
def paths(repopath: str) -> None:

    # ------------ read file ------------ #
    file = open(os.path.join(repopath, "paths.conf"), encoding='utf-8')
    data = file.read()
    file.close()
    
    # ------------ parse config; get file path mappings ------------ #
    variables = []
    mappings = []
    
    i = 0
    buffer = ""
    descend = []
    while i < len(data):
        if data[i].isspace():
            pass
        elif data[i] in "{}":
            descend.append(buffer)
            buffer = ""
        else:
            buffer += data[i]
        
        i += 1
        
        # check buffer



def main() -> None:
    repopath = "/".join(os.path.realpath(__file__).split("/")[:-1])
    paths(repopath)

if __name__ == "__main__":
    main()

class Config:
    cfg={}
    def __init__(self, filename: str):
        header=""
        with open(filename, "r") as fs:
            lines=fs.readlines()
            for line in lines:
                l=line.strip()
                if len(l)==0:
                    continue
                if l[0]=="[" and l[-1]=="]":
                    header=l[1:-1]
                    self.cfg[header]={}
                elif "=" in l:
                    key_value=l.split("=")
                    self.cfg[header][key_value[0]]=key_value[1]

    def __getitem__(self, key):
        return self.cfg[key]

from hashlib import md5
import os
import yaml
import re

class Repo:
    def __init__(self, Root,Name,Version,Description,URL) -> None:
        self.Root   = Root
        self.URL    = URL 
        self.Name   = Name
        self.Description = Description
        self.Ver    = Version 

    def Enum(self):
        self.Path = []
        layer = 1
        w = os.walk(self.Root)
        for (dirpath, dirnames, filenames) in w:
            for i in filenames:
                path = dirpath+"/"+i
                if path[(len(path)-3):] == "lua":
                    self.Path.append(path)
    def Desc(self,path)->str:
        f = open(path).read()
        pat = r'METADATA(\s)*=(\s)*\{((.|\n)*)INFO(\s)*=(\s)*\[\[((.|\n)*?)\]\]((.|\n)*)\}'
        try:
            return re.findall(pat,f)[7]
        except:
            pass
    def Version(self,path)->float:
        return 1.0
    def TakeHash(self,path)->str:
        f = open(path).read()
        return md5(f.encode()).digest().hex()
    def Target(self):
        self.targets = []
        for i in self.Path:
            target = {
                "script":       self.URL+i[len(self.Root):],
                "description":  self.Desc(i),
                "version":      self.Version(i),
                "hash":         self.TakeHash(i),
                "path":         i[len(self.Root):],
                "tags":         ["tags"]
            }
            self.targets.append(target)
    def Compile(self):
        pack = {
            "author":       self.Name,
            "description":  self.Description,
            "version":      self.Ver,
            "target":       self.targets,
        }
        return pack
    def CreatePack(self):
        return yaml.dump(self.Compile())

if __name__ == "__main__":
    x = Repo(
        "/home/farinap/go/src/venera/scripts",
        "farinap5 <null>",
        1.0,
        "Default Package From Venera",
        "http://0.0.0.0:8000")
    x.Enum()
    x.Target()
    f = open("./package.yaml",'w')
    f.write(x.CreatePack())
    f.close()

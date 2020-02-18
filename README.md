# JSON Ref Resolver for standard JSON Schema with Max and Min Schema Generation

This is a python package having multiple utilities. 
[Github-flavored Markdown](https://github.com/deepstartup/pyjn/)

Warning : All the Files for ref-reslover should be placed under the same folder/dir.
1.pyjn.refsolver: input param (input file path) 
2.pyjn.maxjson:input param (json schema dict)
3.pyjn.minjson:input param (json schema dict)

#Data Returns in JSON format:
Example : 
import pyjn
pyjn=pyjn()
json_pathtest='C:/Users/Entity.json'
print(pyjn.refsolver(json_pathtest))
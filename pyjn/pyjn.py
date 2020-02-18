#!/usr/bin/env python
# coding: utf-8
#created : Arghadeep Chaudhury
#data:Feb-2020
import json
from flatten_json import flatten,unflatten
import re
class pyjn:
    def refsolver(self,fileloc):
        try:
            json_path=fileloc
        except Exception as e:
            print('json-path-file-issue',e)
        makeJsoncCommon=[]
        makeJsoncCommon=json_path.split('/')
        cPathPath=''
        for cPath in makeJsoncCommon[:len(makeJsoncCommon)-1]:
            cPathPath=cPathPath+'/'+cPath
        json_common=cPathPath[1:]+'/'
        list=[]
        JDF_list=[]
        InnerDictJSON=dict()
        def find_nth(string, substring, n):
            if(n == 1):
                return string.find(substring)
            else:
                return string.find(substring, find_nth(string, substring, n - 1) + 1)
        def update_json(json_path):
            with open(json_path) as json_file:  
                data=json.load(json_file)
                data['properties'].update(InnerDictJSON)
            return data
        with open(json_path) as json_file:  
            data=json.load(json_file)
        d=flatten(data)
        for key in d:
            if key[len(key)-4:len(key)]=='$ref':
                a = json_common + d[key][:d[key].find('#')]
                list=d[key][d[key].find('properties/'):].split('/')
                with open(a) as json_file:  
                    data1 = json.load(json_file)
                    x = "data1"+"['"+list[0]+"']"
                    eval_val=eval(x)
                    for test1 in eval_val:
                        for j in list:
                            if j in (test1):
                                dict1 = {j : eval_val[test1]}
                                InnerDictJSON.update(dict1)
        fnl_json=update_json(json_path)
        FltJSON=flatten(fnl_json)
        def merge_json(FltJSON,InnerDictJSON):
            for InFltJSON in FltJSON:
                if InFltJSON[len(InFltJSON)-4:len(InFltJSON)]=='$ref':
                    str=InFltJSON
                    refListVals=[]
                    refListVals=FltJSON[InFltJSON].split('/')
            #teston feb2020
                    refKeyTag=refListVals[len(refListVals)-1]
                    if refKeyTag in InnerDictJSON:
                        f=dict({str:InnerDictJSON[refKeyTag]})
                        FltJSON.update(f)
            return FltJSON
        FltJSON=merge_json(FltJSON,InnerDictJSON)
        x=flatten(FltJSON)
        def json_key_replace(x,charval,replace_with):
            for y in x:
                InFltJSON=y.replace(charval,replace_with)
                x[InFltJSON]=x.pop(y)
            return x
        x=json_key_replace(x,'_$ref_','_')
        fnl_json=unflatten(x)
        build_flat=flatten(fnl_json)
        build_flat=json_key_replace(build_flat,'_$ref_','_')
        try:
            fnl_json=unflatten(build_flat)
        except Exception as e:
            print('Issue Raised with unFlatten',e)
        try:
            FltJSON=flatten(fnl_json)
        except Exception as e:
            print('Issue Raised while Flatten',e)
        FltJSON=merge_json(FltJSON,InnerDictJSON)
        x=flatten(FltJSON)
        try:
            x=json_key_replace(x,'_$ref','')
            x=json_key_replace(x,'_$ref_','')
            x=json_key_replace(x,'$ref_','')
            x=json_key_replace(x,'_0','0')
            x=json_key_replace(x,'_1','1')
        except Exception as e:
            print('issue raised with json_key_replace',e)
        try:
            fnl_json=unflatten(x)
        except Exception as e:
            e
        modlist=[]
        for diffnode in fnl_json['properties']:
            if not diffnode in data['properties']:
                modlist.append(diffnode)
        for fnlreplacement in modlist:
            fnl_json['properties'].pop(fnlreplacement)
        try:
            fnl_json=json.dumps(fnl_json)
        except Exception as e:
            fnl_json=''
            print('Failed:',e)
        return fnl_json
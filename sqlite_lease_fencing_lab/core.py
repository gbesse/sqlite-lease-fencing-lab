import json,math
from .common import number,integer,identifier
import sqlite3
def run(d):
 values=d.get('values',['A-first','B-current','A-stale'])
 if not isinstance(values,list)or len(values)!=3:raise ValueError('values')
 for v in values:identifier(v)
 out={}
 for guarded in [False,True]:
  with sqlite3.connect(':memory:')as c:
   c.executescript('create table lease(token integer);insert into lease values(0);create table resource(value text,token integer);insert into resource values(NULL,0);')
   def acquire():c.execute('update lease set token=token+1');return c.execute('select token from lease').fetchone()[0]
   a=acquire();trace=[]
   def write(owner,token,value):
    query='update resource set value=?,token=?'+(' where token<=?'if guarded else '')
    cur=c.execute(query,(value,token,token)if guarded else(value,token));trace.append(dict(owner=owner,token=token,accepted=cur.rowcount==1))
   write('A',a,values[0]);b=acquire();write('B',b,values[1]);write('A',a,values[2]);value,token=c.execute('select *from resource').fetchone();out['fenced'if guarded else'unfenced']=dict(trace=trace,final_value=value,final_token=token)
 return out

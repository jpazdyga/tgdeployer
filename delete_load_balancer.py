import boto3
import json
import sys
import list_load_balancers
from pprint import pprint

conn = boto3.client('elb')

def lista():
 lista.lblist=list_load_balancers.array;

def delete():
 conn.delete_load_balancer(
  LoadBalancerName=lb
 )

def interactive():
 num=1
 print("\nChoose LB to delete:\n");
 for i in lista.lblist:
  print(num, i);
  num=num+1 
 lbn=input("Type the number only: ");
 slbn=int(lbn)
 index=slbn-1
 lb=list_load_balancers.array[index]

if len(sys.argv) > 1:
 lb = sys.argv[1];
 lista()
 if lb in lista.lblist:
  delete()
 else:
  print("You specified non-existing LB name. Please re-check this or run", sys.argv[0], "again.");
else:
 lista()
 interactive()

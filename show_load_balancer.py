import boto3
import json
import argparse
from pprint import pprint

conn = boto3.client('elb')

def list():
 list_load_balancers = conn.describe_load_balancers(
  LoadBalancerNames=[
   lbname,
  ],
 )
 pprint(list_load_balancers);

parser = argparse.ArgumentParser(description='Get the AWS Load Balancer details.')
parser.add_argument('loadbalancer', metavar='lbname', type=str, nargs='+', help='Load balancer name')
args = parser.parse_args()
lbname = args.loadbalancer[0];

list();

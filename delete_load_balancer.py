import boto3
import json
import argparse
import list_load_balancers
from pprint import pprint

conn = boto3.client('elb')

#parser = argparse.ArgumentParser(description='Get the AWS Load Balancer details.')
#parser.add_argument('loadbalancer', metavar='lbname', type=str, nargs='+', help='Load balancer name')
#args = parser.parse_args()
#lbname = args.loadbalancer[0];

list();

import os
import boto.ec2.elb
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import HealthCheck
from pprint import pprint

conn = ELBConnection()

def list ():
 list_load_balancers = conn.get_all_load_balancers()
 print(list_load_balancers);

list();

def create():
 zones = ['eu-west-1a','eu-west-1b','eu-west-1c']
 ports = [(80,80,'http')]
 security_groups = ['sg-de04e3ba']
 lb = conn.create_load_balancer('test1-loadbalancer', zones, ports, security_groups=security_groups)

create();

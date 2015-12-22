import boto3

conn = boto3.client('elb')
lbname = 'test1-loadbalancer';

def list ():
 list_load_balancers = conn.describe_load_balancers(
  LoadBalancerNames=[
   lbname,
  ],
 )
 print(list_load_balancers);

def create():
 listeners = [
  {'Protocol': 'http',
   'LoadBalancerPort': 80,
   'InstanceProtocol': 'http',
   'InstancePort': 80,
  }];
 zones = ['eu-west-1a','eu-west-1b','eu-west-1c']
 security_groups = ['sg-de04e3ba']
 lb = conn.create_load_balancer(
  LoadBalancerName=lbname, 
  Listeners=listeners, 
  AvailabilityZones=zones,
  SecurityGroups=security_groups)

def setupattr():
 conn.modify_load_balancer_attributes(
  LoadBalancerName=lbname,
  LoadBalancerAttributes={
   'CrossZoneLoadBalancing': {
    'Enabled': True,
   },
  }
 )

def setupstick():
 conn.create_lb_cookie_stickiness_policy(
  LoadBalancerName=lbname,
  PolicyName='DefaultLBStickiness-1',
  CookieExpirationPeriod=10,
 )

#list();
create();
setupattr();
setupstick();

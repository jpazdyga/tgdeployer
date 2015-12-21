import os
import boto.ec2.autoscale
from boto.ec2.autoscale import AutoScaleConnection
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup
from pprint import pprint

conn = AutoScaleConnection()

lcname = "test1-launch_config";
lbname = "test1-loadbalancer";
asgname = "test1-asg"

def list_lc ():
 list_launch_config = conn.get_all_launch_configurations()
 print(list_launch_config);

def list_asg ():
 list_auto_scaling_groups = conn.get_all_groups()
 print(list_auto_scaling_groups);

def create_lc():
 userdata = '#!/bin/bash\nyum install -y aws-cli\naws s3 cp s3://jblog-test-1/ecs.config /etc/ecs/ecs.config\necho ECS_CLUSTER=test1-cluster >> /etc/ecs/ecs.config';
 lc = LaunchConfiguration(name=lcname,
  image_id='ami-8073d3f3',
  instance_type='t2.micro',
  instance_monitoring='true',
  key_name='jpazdygapl',
  instance_profile_name='ecsInstanceRole',
  user_data=userdata,
  security_groups=['sg-de04e3ba']);
 conn.create_launch_configuration(lc);

def create_asg():
 availability_zones = ['eu-west-1a','eu-west-1b','eu-west-1c']
 load_balancers = [lbname]
 min_size=3
 max_size=9
 asg = AutoScalingGroup(group_name=asgname,
  load_balancers=load_balancers,
  availability_zones=availability_zones,
  launch_config=lcname,
  min_size=min_size,
  max_size=max_size,
  connection=conn)
 conn.create_auto_scaling_group(asg);

create_lc();
create_asg();

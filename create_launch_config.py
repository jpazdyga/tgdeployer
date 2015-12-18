import os
import boto.ec2.autoscale
from boto.ec2.autoscale import AutoScaleConnection
from boto.ec2.autoscale import LaunchConfiguration
from pprint import pprint

conn = AutoScaleConnection()

def list ():
 list_launch_config = conn.get_all_launch_configurations()
 print(list_launch_config);

list();

def create():
 userdata = '#!/bin/bash\nyum install -y aws-cli\naws s3 cp s3://jblog-test-1/ecs.config /etc/ecs/ecs.config\necho ECS_CLUSTER=jblog-test-1 >> /etc/ecs/ecs.config';
 lc = LaunchConfiguration(name='test1-launch_config',
  image_id='ami-8073d3f3',
  instance_type='t2.micro',
  instance_monitoring='true',
  key_name='jpazdygapl',
  instance_profile_name='ecsInstanceRole',
  user_data=userdata,
  security_groups=['sg-de04e3ba']);
 conn.create_launch_configuration(lc);

create();

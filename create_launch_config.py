import boto3

conn = boto3.client('autoscaling')

lcname = "test1-launch_config";
lbname = "test1-loadbalancer";

def list_lc ():
 list_launch_config = conn.get_all_launch_configurations()
 print(list_launch_config);

def create_lc():
 userdata = '#!/bin/bash\nyum install -y aws-cli\naws s3 cp s3://jblog-test-1/ecs.config /etc/ecs/ecs.config\necho ECS_CLUSTER=test1-cluster >> /etc/ecs/ecs.config';
 image_id='ami-8073d3f3'
 instance_type='t2.micro'
 instance_monitoring={ 'Enabled': True }
 key_name='jpazdygapl'
 instance_profile_name='ecsInstanceRole'
 security_groups=['sg-de04e3ba']
 
 conn.create_launch_configuration(
  LaunchConfigurationName=lcname,
  ImageId=image_id,
  InstanceType=instance_type,
  KeyName=key_name,
  InstanceMonitoring=instance_monitoring,
  SecurityGroups=security_groups,
  IamInstanceProfile=instance_profile_name,
  UserData=userdata,
 );

create_lc();

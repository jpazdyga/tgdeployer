import boto3

conn = boto3.client('autoscaling')

lcname = "test1-launch_config";
lbname = "test1-loadbalancer";
asgname = "test1-asg"

def list_asg ():
 list_auto_scaling_groups = conn.get_all_groups()
 print(list_auto_scaling_groups);

def create_asg():
 availabilityzones = ['eu-west-1a','eu-west-1b','eu-west-1c']
 loadbalancers = [lbname]
 minsize=3
 maxsize=9
 dcapacity=6
 dcooldown=300
 group_name=asgname
 launch_config=lcname
 
 conn.create_auto_scaling_group(
  AutoScalingGroupName=asgname,
  LaunchConfigurationName=lcname,
  MinSize=minsize,
  MaxSize=maxsize,
  DesiredCapacity=dcapacity,
  DefaultCooldown=dcooldown,
  AvailabilityZones=availabilityzones,
  LoadBalancerNames=loadbalancers,
 );

create_asg();

import boto3

conn = boto3.client('elb')
array = []

list_load_balancers = conn.describe_load_balancers(
 LoadBalancerNames=[],
 PageSize=20,
)
test = list_load_balancers.get('LoadBalancerDescriptions')
entity = 0;
for entity in test:
 val1 = entity.get('LoadBalancerName');
 array.append(val1)

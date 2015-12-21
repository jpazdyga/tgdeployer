import boto3

conn = boto3.client('ecs')

res = conn.deregister_task_definition(taskDefinition='test1:12')

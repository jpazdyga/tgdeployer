import boto3

conn = boto3.client('ecs')
clustername = "test1-cluster";
servicename = "test1-service";
taskdefinition = "test1";

container = [{
    'cpu': 128,
    'memory': 256,
    'essential': True,
    'image': 'jpazdyga/testapp-container:latest',
    'command': [],
    'name': 'test1',
    'portMappings': [{
        'hostPort': 80,
        'containerPort': 80,
        'protocol': 'tcp'
    }],
    'environment': [{
        'name': 'TEST',
        'value': 'TEST1'
    }]
}]

conn.register_task_definition(family='test1', containerDefinitions=container)

conn.create_cluster(clusterName=clustername)

conn.create_service(cluster=clustername,
    serviceName=servicename,
    taskDefinition=taskdefinition,
    loadBalancers=[
        {
            'loadBalancerName': 'test1-loadbalancer',
            'containerName': 'test1',
            'containerPort': 80
        },
    ],
    desiredCount=3,
    clientToken='secrettoken',
    role='ecsServiceRole')

#conn.run_task(cluster=clustername,
#    taskDefinition=taskdefinition,
#    count=3,
#    startedBy='automat')

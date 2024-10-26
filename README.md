# Auto Shadowsocks deployment


Avoid Creating a New VPC

	1.	Resource Limits: AWS has limits on the number of VPCs you can create per region (usually 5 by default). Constantly creating new VPCs will quickly hit these limits, requiring you to request limit increases from AWS, which can lead to delays and unnecessary complexity.
	2.	Network Complexity: Each VPC is an isolated network environment. Creating a new VPC each time means you would have to manage new routing tables, subnets, and internet gateways repeatedly. This adds complexity to your network architecture and makes it harder to manage.
	3.	Slow Deployment: Creating a VPC is generally slower than creating an instance within an existing VPC. Repeatedly creating and tearing down VPCs can slow down your deployment process.


Automated IP Rotation:
	•	Write a script or use automation tools (e.g., AWS Lambda or cron jobs) to periodically change the Elastic IPs associated with your instance. This will help keep your proxy service dynamic and frequently changing IP addresses.
	•	You can also have multiple proxy instances running in parallel, each with its own Elastic IP, to distribute the load and ensure redundancy.
    

Use an Existing VPC and Rotate IPs Dynamically

Instead of creating new VPCs, use a single, existing VPC and deploy your instances within it. You can then manage IP rotation by:

	1.	Assigning Elastic IPs (EIPs):
	•	Elastic IPs are static IPv4 addresses designed for dynamic cloud computing. You can allocate a pool of Elastic IPs in advance and associate/disassociate them with instances as needed.
	•	Each time you need to change the IP address of your proxy instance, you can disassociate the current Elastic IP and associate a new one.

```
# Allocate a new Elastic IP
aws ec2 allocate-address --domain vpc

# Associate the Elastic IP to an instance
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678
```



## Dev Container

Build the container for dev:

`
docker build -t python-terraform-dev .
`

or 
`
docker compose up --build
`

The official hashicorp container image can be used to run the .tf files generated.

```
docker run --rm -v $(pwd):/workspace -w /workspace hashicorp/terraform:latest init
```

##

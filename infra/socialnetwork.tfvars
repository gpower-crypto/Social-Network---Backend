

# elb_details - Configuration for Amazon Elastic Load Balancer (ELB)

elb_details = {
  loadbalancer_name = "socialnetwork-LB"         # Name of the ELB
  security_groups = ["sg-09bf7c51111cead33"]  # Security groups associated with the ELB
  subnets = ["subnet-03de38233ecd19df1", "subnet-03f413db3b3707c88"]  # Subnets for the ELB
  targetgroup_name = "socialnetwork-TG"          # Name of the target group
  targetgroup_port = 8000                      # Port used by the target group
  targetgroup_protocol = "HTTP"              # Protocol used by the target group
  health_check_protocol = "HTTP"             # Protocol used for health checks
  health_check_path = "/health"              # Health check path
  vpc_id = "vpc-0ec9e8d51308669e0"           # ID of the VPC
  listener_port = 8000                         # Port for the listener
  listener_protocol = "HTTP"                 # Protocol for the listener
}

# ecs_details - Configuration for Amazon Elastic Container Service (ECS)

ecs_details = {
  ecs_name = "socialnetwork"                       # Name of the ECS cluster
  ecs_task_definition = {
    cpu = "512"                                # CPU units for the task definition
    memory = "1024"                            # Memory for the task definition
  }
  ecs_service = {
    name = "socialnetwork"                         # Name of the ECS service
    subnets = ["subnet-03f413db3b3707c88"]    # Subnets for the ECS service
    security_groups = ["sg-09bf7c51111cead33"]  # Security groups for the ECS service
  }
}

ecr_details = {
  ecr_repository_name = "socialnetwork"           # Name of the ECR repository
  image_tag_mutability = "MUTABLE"            # Mutability of Docker image tags
  scan_images_on_push = false                 # Whether to scan images on push (true/false)
}
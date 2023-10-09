# Define an AWS ECS cluster for the Express Server
resource "aws_ecs_cluster" "express_server" {
  name = var.ecs_details.ecs_name  # Name for the ECS cluster
  tags = var.tags  # Tags to associate with the ECS cluster
}

# Define an AWS ECS task definition for the Express Server
resource "aws_ecs_task_definition" "express_task" {
  family                   = "service"  # The family name of the task definition
  network_mode             = "awsvpc"  # Network mode for the task
  requires_compatibilities = ["FARGATE"]  # Compatibility with Fargate
  execution_role_arn       = "arn:aws:iam::530934248749:role/ecs-role"  # IAM role for task execution
  task_role_arn            = "arn:aws:iam::530934248749:role/ecs-role"  # IAM role for the task
  cpu                      = var.ecs_details.ecs_task_definition.cpu  # CPU units for the task
  memory                   = var.ecs_details.ecs_task_definition.memory  # Memory for the task

  container_definitions = jsonencode([{
    name  = "socialnetwork-container"
    # we are going to refer to the public docker images available in the docker hub 
    # badri555/django-api:latest - django
    # badri555/express-api:latest - express
    image = "530934248749.dkr.ecr.us-east-1.amazonaws.com/socialnetwork:latest"  # Docker image for the container 

    portMappings = [{
      containerPort = 8000
      hostPort      = 8000
      protocol      = "tcp"
    }]
  }])

  tags = var.tags  # Tags to associate with the task definition
}

# Define an AWS ECS service for the Express Server
resource "aws_ecs_service" "expressJS_service" {
  name            = var.ecs_details.ecs_service.name  # Name for the ECS service
  cluster         = aws_ecs_cluster.express_server.id  # ID of the ECS cluster
  task_definition = aws_ecs_task_definition.express_task.arn  # ARN of the ECS task definition
  launch_type     = "FARGATE"  # Launch type for the service
  desired_count   = 1  # Number of desired tasks

  network_configuration {
    subnets         = var.ecs_details.ecs_service.subnets  # Subnets for the service
    security_groups = var.ecs_details.ecs_service.security_groups  # Security groups for the service
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.express-tg.arn  # ARN of the target group
    container_name   = "socialnetwork-container"  # Name of the container to associate with the target group
    container_port   = 8000  # Port to route traffic to within the container
  }
}

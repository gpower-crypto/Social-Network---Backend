# Create an AWS Application Load Balancer (ALB) for the Express Server
resource "aws_lb" "express_lb" {
  name               = var.elb_details.loadbalancer_name  # Name of the ALB
  internal           = false  # Internal ALB
  load_balancer_type = "application"  # ALB type (application)
  security_groups    = var.elb_details.security_groups  # List of security groups for the ALB
  subnets            = var.elb_details.subnets  # List of subnets where the ALB will be deployed
  tags               = var.tags  # Tags to associate with the ALB
}

# Create an AWS Target Group for the Express Server
resource "aws_lb_target_group" "express-tg" {
  name        = var.elb_details.targetgroup_name  # Name of the target group
  port        = var.elb_details.targetgroup_port  # Port to forward traffic to
  protocol    = var.elb_details.targetgroup_protocol  # Protocol used for the target group
  target_type = "ip"  # Target type (IP)
  vpc_id      = var.elb_details.vpc_id  # ID of the VPC where the target group resides

  health_check {
    healthy_threshold   = 2  # Number of consecutive successful health checks
    path               = var.elb_details.health_check_path  # Path for the health check
    protocol           = var.elb_details.health_check_protocol  # Protocol for the health check
    port               = "traffic-port"  # Port to use for health checks
    unhealthy_threshold = 10  # Number of consecutive unsuccessful health checks before marking as unhealthy
    timeout            = 120  # Timeout for health checks in seconds
    interval           = 300  # Interval between health checks in seconds
    matcher            = 200  # Status code to consider a healthy response
  }

  tags = var.tags  # Tags to associate with the target group
}

# Create an AWS ALB Listener for the Express Server
resource "aws_lb_listener" "express-listener" {
  load_balancer_arn = aws_lb.express_lb.arn  # ARN of the ALB
  port              = var.elb_details.listener_port  # Listener port
  protocol          = var.elb_details.listener_protocol  # Listener protocol

  default_action {
    type             = "forward"  # Action type (forward)
    target_group_arn = aws_lb_target_group.express-tg.arn  # ARN of the target group to forward traffic to
  }

  tags = var.tags  # Tags to associate with the ALB listener
}

# resource "aws_lb_listener" "express-listener" {
#   load_balancer_arn = aws_lb.express_lb.arn  # ARN of the ALB
#   port              =  "443" # Listener port
#   protocol          =  "HTTPS" # Listener protocol

#   default_action {
#     type             = "forward"  # Action type (forward)
#     target_group_arn = aws_lb_target_group.express-tg.arn  # ARN of the target group to forward traffic to
#   }

#   tags = var.tags  # Tags to associate with the ALB listener
# }

variable "elb_details" {
    type = object ({
        loadbalancer_name = string
        security_groups = list(string)
        subnets = list(string)
        targetgroup_name = string
        targetgroup_port = number
        targetgroup_protocol = string
        health_check_path = string
        health_check_protocol = string
        vpc_id = string
        listener_port = number
        listener_protocol = string
    })
    description = "This variable is for passing elb details dynamically"
    default = {
        loadbalancer_name = "expressJS-LB"
        security_groups = ["sg-04938edf09be9ef0b"]
        subnets = ["subnet-0836573c5ec7827cd","subnet-0f1b39831c4c1a350"]
        targetgroup_name = "expressJS-TG"
        targetgroup_port = 80
        targetgroup_protocol = "HTTP"
        health_check_protocol = "HTTP"
        health_check_path = "/health"
        vpc_id = "vpc-07efabca1c47c7703"
        listener_port = 80
        listener_protocol = "HTTP"
    }
}


variable "ecs_details" {
    type = object ({
        ecs_name = string
        ecs_task_definition = object ({
            cpu = string
            memory = string
        })
        ecs_service = object ({
            name = string
            subnets = list(string)
            security_groups = list(string)
        })
    })
    description = "This variable is for passing CodeBuild details dynamically"
    default = {
        ecs_name = "expressJS"
        ecs_task_definition ={
            cpu = "512"
            memory = "1024"
        }
        ecs_service = {
            name = "expressJS"
            subnets = ["subnet-0836573c5ec7827cd"]
            security_groups = ["sg-04938edf09be9ef0b"]
        }
    }
}

variable "ecr_details" {
    type = object ({
        ecr_repository_name = string
        image_tag_mutability = string
        scan_images_on_push = bool
    })
    description = "This variable is for passing ecr details dynamically"
    default = {
      ecr_repository_name = "socialnetwork"
      image_tag_mutability = "MUTABLE"
      scan_images_on_push = false
    }
}

variable "tags" {
  type        = map(string)
  description = "Map of tags to apply on the resources"
  default = {
    "Owner"      = "mk0604"
    "Iaac"       = "Terraform"
    "Name"       = "socialnetwork"
  }
}


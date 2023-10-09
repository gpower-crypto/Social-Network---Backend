# AWS ECR Repository Resource

# Define an AWS Elastic Container Registry (ECR) repository for storing Docker images.

resource "aws_ecr_repository" "ecr_repository" {
  name = var.ecr_details.ecr_repository_name  # Name of the ECR repository

  # Control whether Docker image tags can be mutated (e.g., overwritten) after they are created.
  image_tag_mutability = var.ecr_details.image_tag_mutability

  # Configure image scanning settings.
  image_scanning_configuration {
    scan_on_push = var.ecr_details.scan_images_on_push  # Enable or disable image scanning on image push.
  }

  tags = var.tags  # Tags to associate with the ECR repository for resource organization.
}

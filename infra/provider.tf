# Terraform Configuration

# Define the required AWS provider and its version
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# AWS Provider Configuration

# Configure the AWS provider to interact with AWS resources in the "us-east-1" region.
provider "aws" {
  region = "us-east-1"  # Update this with your desired AWS region

  # Note: You should consider using AWS credentials configuration (access_key and secret_key)
  # to authenticate with AWS. By default, Terraform uses the AWS CLI configuration for credentials.
}

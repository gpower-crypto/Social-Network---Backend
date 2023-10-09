terraform {
  backend "s3" {
     bucket         = "socialnetwork-project"
     key            = "socialnetwork-infra/terraform.tfstate"
     region         = "us-east-1"
  }
}
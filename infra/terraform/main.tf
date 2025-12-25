provider "aws" {
    region = var.aws_region
}

# Netzwerk
resource "aws_vpc" "main" {
    cidr_block = "10.0.0.0/16"
}

# Security 
resource "aws_security_group" "app_sg" {
    name = "app-security-group"
    description = "Allow HTTP access"
    vpc_id = aws_vpc.main.id
}

# Compute (Platzhalter)
resource "aws_instance" "app" {
    ami = "ami-123456" # fake
    instance_type = "t2.micro"
    security_groups = [aws_security_group.app_sg.name]
}
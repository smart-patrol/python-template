#!bin/bash 
REPO_NAME_DEFAULT=docker-image
ACCOUNT_ID_DEFAULT=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION_DEFAULT=$(aws configure get region)

REPO_NAME=${1:-${REPO_NAME_DEFAULT}}
AWS_ACCOUNT_ID=${2:-{ACCOUNT_ID_DEFAULT}}
AWS_REGION=${3:-${AWS_REGION_DEFAULT}}

aws ecr batch-delete-image --repository-name $REPO_NAME \
--image-ids imageTag=latest 

docker image rm $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest

aws ecr delete-repository --repository-name $REPO_NAME

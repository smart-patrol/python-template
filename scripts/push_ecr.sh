#!/bin/bash
REPO_NAME_DEFAULT=docker-image
ACCOUNT_ID_DEFAULT=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION_DEFAULT=$(aws configure get region)

REPO_NAME=${1:-${REPO_NAME_DEFAULT}}
AWS_ACCOUNT_ID=${2:-{ACCOUNT_ID_DEFAULT}}
AWS_REGION=${3:-${AWS_REGION_DEFAULT}}

# repository must exist and login needs to happen prior
# see: https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html
aws ecr create-repository --repository-name $REPO_NAME

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker build -t $REPO_NAME .

docker tag $REPO_NAME:latest  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest

#  scan for vulnerabilities
aws ecr put-image-scanning-configuration \
--repository-name $REPO \
--image-scanning-configuration scanOnPush=true

# find old image
OLD_IMAGE_DIGESTS=`aws ecr --region $AWS_REGION list-images --repository-name $REPO_NAME --filter tagStatus=UNTAGGED | jq '.imageIds | map({imageDigest: .imageDigest})'`

# delete old images if they exist
if [ ! "$OLD_IMAGE_DIGESTS" = '[]' ]; then
aws ecr --region $AWS_REGION batch-delete-image --repository-name $REPO_NAME --image-ids "$OLD_IMAGE_DIGESTS"
fi

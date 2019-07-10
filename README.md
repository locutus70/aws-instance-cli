# aws-instance-cli
Demo Project to manage AWS EC2 instances

## About

This project is a demo and uses boto3 to manage AWS EC2 instances

## Configuring

aws-instance-cli uses the configuration file created by the AWS cli. e.g.

`aws configure --profile instancecli`

## Running

`pipenv run python instance/instancecli.py <command> <subcommand> <--project=PROJECT>`

*command* is instances or volumes

*subcommand* depends on command

*project* is optional

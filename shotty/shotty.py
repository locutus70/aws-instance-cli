import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()  # The @ is the decorator. It wraps functions.
def list_instances():
    "List EC2 instances" # This is a doc string in python.
                         # Click uses doc strings.
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))

    return

if __name__ == '__main__':
    list_instances()

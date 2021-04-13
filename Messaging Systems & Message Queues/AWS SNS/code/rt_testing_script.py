import boto3
import sys
from pathlib import Path


sns_client = boto3.client('sns', region_name='us-west-2')
topic_arn = None
message = None


def establish_topic():
    global topic_arn
    try:
        response = sns_client.get_topic_attributes(
            TopicArn='arn:aws:sns:us-west-2:615699678464:TestTopic'
        )
        topic_arn = response['Attributes']['TopicArn']
    except Exception:
        response = sns_client.create_topic(
            Name='TestTopic',
            Attributes={
                'Policy': '{"Version":"2008-10-17","Id":"__default_policy_ID","Statement":[{"Sid":"__default_statement_ID","Effect":"Allow","Principal":{"AWS":"*"},"Action":["SNS:Publish","SNS:RemovePermission","SNS:SetTopicAttributes","SNS:DeleteTopic","SNS:ListSubscriptionsByTopic","SNS:GetTopicAttributes","SNS:Receive","SNS:AddPermission","SNS:Subscribe"],"Resource":"arn:aws:sns:us-west-2:615699678464:TestTopic","Condition":{"StringEquals":{"AWS:SourceOwner":"615699678464"}}},{"Sid":"__console_pub_0","Effect":"Allow","Principal":{"AWS":"*"},"Action":"SNS:Publish","Resource":"arn:aws:sns:us-west-2:615699678464:TestTopic"},{"Sid":"__console_sub_0","Effect":"Allow","Principal":{"AWS":"*"},"Action":["SNS:Subscribe","SNS:Receive"],"Resource":"arn:aws:sns:us-west-2:615699678464:TestTopic"}]}',
                'DisplayName': 'TestTopic',
                'FifoTopic': 'False'
            }
        )
        topic_arn = response['TopicArn']


def extract_mess_text(size):
    global message
    message_dir = "{}/DesignOfExperiments/messages/".format(str(Path(__file__).parents[3]))
    if size == 'tiny':
        with open(message_dir + 'tiny.txt', 'r') as file:
            _msg = file.read().splitlines()
            message = ''.join(_msg)
    elif size == 'small':
        with open(message_dir + 'small.txt', 'r') as file:
            _msg = file.read().splitlines()
            message = ''.join(_msg)
    elif size == 'medium':
        with open(message_dir + 'medium.txt', 'r') as file:
            _msg = file.read().splitlines()
            message = ''.join(_msg)
    elif size == 'large':
        with open(message_dir + 'large.txt', 'r') as file:
            _msg = file.read().splitlines()
            message = ''.join(_msg)
    elif size == 'xlarge':
        with open(message_dir + 'xlarge.txt', 'r') as file:
            _msg = file.read().splitlines()
            message = ''.join(_msg)
    else:
        print("No size provided!!!")


def generate_messages():
    sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        MessageStructure='string'
        # MessageAttributes={
        #     'string': {
        #         'DataType': 'String'
        #     }
        # },
    )


if __name__ == "__main__":
    message_size = sys.argv[1]
    establish_topic()
    extract_mess_text(message_size)
    generate_messages()

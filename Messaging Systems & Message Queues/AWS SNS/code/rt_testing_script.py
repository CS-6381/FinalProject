import boto3
import sys
from pathlib import Path


sns_client = boto3.client('sns', region_name='us-east-1')
topic_arn = None
message = None


def establish_topic():
    global topic_arn
    try:
        response = sns_client.get_topic_attributes(
            TopicArn='arn:aws:sns:us-east-1:615699678464:TestTopic'
        )
        topic_arn = response['Attributes']['TopicArn']
    except Exception:
        response = sns_client.create_topic(
            Name='TestTopic',
            Attributes={
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


def publish_messages(count):
    for _ in range(count):
        generate_message()


def generate_message():
    sns_client.publish(
        TopicArn=topic_arn,
        Message="There are not more than five primary colors (blue, yellow, red, white, and black), yet in combination they produce more hues than can ever been seen.",
        MessageStructure='string'
    )


if __name__ == "__main__":
    # message_size = sys.argv[1]
    execution_count = int(sys.argv[1])
    establish_topic()
    # extract_mess_text(message_size)
    publish_messages(execution_count)

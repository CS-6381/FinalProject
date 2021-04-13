import boto3


sns_client = boto3.client('sns', region_name='us-west-2')
topic_arn = None


def establish_topic():
    import pdb;pdb.set_trace()
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


def generate_messages(message):
    import pdb;pdb.set_trace()
    response = sns_client.publish(
        TopicArn='string',
        TargetArn='string',
        PhoneNumber='string',
        Message='string',
        Subject='string',
        MessageStructure='string',
        MessageAttributes={
            'string': {
                'DataType': 'string',
                'StringValue': 'string',
                'BinaryValue': b'bytes'
            }
        },
        MessageDeduplicationId='string',
        MessageGroupId='string'
    )



if __name__ == "__main__":
    establish_topic()
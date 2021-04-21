# Base Experiment (MQ)

This experiment is an extension of the [Base experiment](./Base.md) that is specific to MQ technologies.

## Qualitative Data

These metrics are inspired by Zhuangwei Kang's presentation he shared with us. Fill in with information you discover about your chosen MQ.

| Metric | Value |
| --- | --- |
| Centricity (data-centric or message-centric) | Amazon SNS is more message-centric as the primary focus of the software is to essentially send messages to whatever endpoint is necessary. |
| Connection (machine-to-machine or point-to-point) | Connection is from point to point. The data is generated through the SNS hub and sent to whatever end point the user desires.|
| Underlying Architecture (decentralized or hub-and-spoke) | Decentralized, there is not necessarily any connection back to the host once a message is sent off, it could be used as a hub and spoke if the user set up message points to be used in such a way.  https://aws.amazon.com/sns/faqs/ https://aws.amazon.com/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc 
|
| Protocol | HTTP/HTTPS, email, SMS |
| Transport(s) | “HTTP”, “HTTPS” – Subscribers specify a URL as part of the subscription registration; notifications will be delivered through an HTTP POST to the specified URL. ”Email”, “Email-JSON” – Messages are sent to registered addresses as email. Email-JSON sends notifications as a JSON object, while Email sends text-based email.“SQS” – Users can specify an SQS standard queue as the endpoint; Amazon SNS will enqueue a notification message to the specified queue (which subscribers can then process using SQS APIs such as ReceiveMessage, DeleteMessage, etc.). “SMS” – Messages are sent to registered phone numbers as SMS text messages.
|
| Data Serialization | If message delivery properties are not set in advance they are defaulted to JSON |
| Supports Queuing | Yes, utilizes either standard AWS SNS or FIFO queueing on the receiving end |
| Data Type Representation | JSON or Raw Data delivery, otherwise you can add additional properties onto the message being sent |
| QoS Parameters | Reference above listed links |
| Supports Dynamic Discovery | No, because the user must predefine the destination of the message |
| Communication Patterns | Operates in pub/sub fashion but the subscribers won’t receive a message until the publisher has sent and queued the appropriate places |
| Abstraction Layer | Provided within the software itself so that the user doesn’t directly have to deal with abstracting of the messaging system |
| Up-front Complexity | Creation of the Amazon SNS account and setup increases the initial complexity. Refer to https://aws.amazon.com/sns/faqs/ for other questions.  |
| Large Implementations | Offers 10 million subscriptions per topic, 100,000 topics per account, for any higher quotas they can be requested

With the exception of SMS messages, Amazon SNS messages can contain up to 256 KB of text data, including XML, JSON and unformatted text, each data is billed as 1 request each sms message can contain up to 140 bytes and the character limit depends on the encoding scheme. If you exceed the message size limit it is published as multiple messages.|


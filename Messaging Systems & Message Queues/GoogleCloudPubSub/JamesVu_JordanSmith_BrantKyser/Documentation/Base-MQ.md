**Base Experiment (MQ)**

This experiment is an extension of the [Base
experiment](https://github.com/CS-6381/FinalProject/blob/main/DesignOfExperiments/Base.md) that
is specific to MQ technologies.

**Qualitative Data**

These metrics are inspired by Zhuangwei Kang's presentation he shared
with us. Fill in with information you discover about your chosen MQ.

<table>
<thead>
<tr class="header">
<th><strong>Metric</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Centricity (data-centric or message-centric)</td>
<td>Message-centric. <a href="https://cloud.google.com/pubsub/docs/overview">https://cloud.google.com/pubsub/docs/overview</a>: Decoupled, asynchronous messaging service</td>
</tr>
<tr class="even">
<td>Connection (machine-to-machine or point-to-point)</td>
<td><a href="https://www.youtube.com/watch?v=f5DOsB7Nlw0">https://www.youtube.com/watch?v=f5DOsB7Nlw0</a>: Point to point since communicate using multiple terminals on the same computer</td>
</tr>
<tr class="odd">
<td>Underlying Architecture (decentralized or hub-and-spoke)</td>
<td><a href="https://cloud.google.com/managed-microsoft-ad/docs/hub-spoke">https://cloud.google.com/managed-microsoft-ad/docs/hub-spoke</a>: Hub and spoke. You can make a VPC (Virtual Private Cloud) in Google Cloud and connect to other projects/resources.</td>
</tr>
<tr class="even">
<td>Protocol</td>
<td><a href="https://towardsdatascience.com/publisher-subscriber-model-for-apps-and-data-ingestion-flows-b8ba7e85e992">https://towardsdatascience.com/publisher-subscriber-model-for-apps-and-data-ingestion-flows-b8ba7e85e992</a>: HTTP</td>
</tr>
<tr class="odd">
<td>Transport(s)</td>
<td><p><a href="https://cloud.google.com/load-balancing/docs/internal">https://cloud.google.com/load-balancing/docs/internal</a>: Google Cloud Pub Sub handles TCP and UDP when it comes to load balancing. Messages received from Google Cloud Pub Sub can be sent to an application that utilizes a protocol like TCP or UDP (e. g. a Python message sending/listening application).</p>
<p><a href="https://towardsdatascience.com/publisher-subscriber-model-for-apps-and-data-ingestion-flows-b8ba7e85e992">https://towardsdatascience.com/publisher-subscriber-model-for-apps-and-data-ingestion-flows-b8ba7e85e992</a>: HTTP</p></td>
</tr>
<tr class="even">
<td>Data Serialization</td>
<td><a href="https://docs.fastly.com/en/guides/log-streaming-google-cloud-pubsub">https://docs.fastly.com/en/guides/log-streaming-google-cloud-pubsub</a>: Data input into Google Cloud Pub Sub must be in JSON format.</td>
</tr>
<tr class="odd">
<td>Supports Queuing</td>
<td><p><a href="https://cloud.google.com/pubsub/docs/publisher">https://cloud.google.com/pubsub/docs/publisher</a>: Publisher makes and send messages to a topic with data, ordering key, and metadata.</p>
<p><a href="https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8">https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8</a>: Subscribers have message ordering property option.</p></td>
</tr>
<tr class="even">
<td>Data Type Representation</td>
<td><a href="https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage">https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage</a>: JSON that contains various data types such as string and TimeStamp</td>
</tr>
<tr class="odd">
<td>QoS Parameters</td>
<td><a href="https://cloud.google.com/iot/docs/how-tos/mqtt-bridge">https://cloud.google.com/iot/docs/how-tos/mqtt-bridge</a>: You can send messages through MQTT bridge to Cloud IoT core, which supports multiple QOS levels.</td>
</tr>
<tr class="even">
<td>Supports Dynamic Discovery</td>
<td><a href="https://cloud.google.com/pubsub/architecture">https://cloud.google.com/pubsub/architecture</a>: Google Cloud Pub/Sub dynamically tweaks publishers and subscribers based on message throughput.</td>
</tr>
<tr class="odd">
<td>Communication Patterns</td>
<td><p><a href="https://cloud.google.com/pubsub/docs/subscriber">https://cloud.google.com/pubsub/docs/subscriber</a>: Subscriber push/pull</p>
<p><a href="https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8">https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8</a>: Streaming pull, push/pull</p></td>
</tr>
<tr class="even">
<td>Abstraction Layer</td>
<td><a href="https://cloud.google.com/pubsub/architecture">https://cloud.google.com/pubsub/architecture</a>: For abstraction of implementation details, there exists a service proxy among clients and data senders that helps optimize connection for clients. The control plane assigns the publishers and subscribers to the servers. The data plane handles message transmission among publishers and subscribers.</td>
</tr>
<tr class="odd">
<td>Up-front Complexity</td>
<td><p><a href="https://cloud.google.com/pubsub/docs/overview">https://cloud.google.com/pubsub/docs/overview</a>: Option of Pub/Sub Lite</p>
<p><a href="https://cloud.google.com/pubsub/quotas">https://cloud.google.com/pubsub/quotas</a>: Quotas and usage</p>
<p><a href="https://cloud.google.com/pubsub/architecture">https://cloud.google.com/pubsub/architecture</a>: Horizontal scalability (add more devices)</p>
<p><a href="https://cloud.google.com/pubsub/docs/samples/pubsub-publish-with-error-handler">https://cloud.google.com/pubsub/docs/samples/pubsub-publish-with-error-handler</a>: Publish with error handling</p>
<p><a href="https://cloud.google.com/architecture/framework/reliability">https://cloud.google.com/architecture/framework/reliability</a>: Redundancy, rollback, traffic limit, recovery, failure detection, incremental changes, coordinate/document emergency response, capacity management</p>
<p><a href="https://cloud.google.com/pubsub/docs/publisher">https://cloud.google.com/pubsub/docs/publisher</a>: Failed publications are retried automatically.</p></td>
</tr>
<tr class="even">
<td>Large Implementations</td>
<td><p><a href="https://cloud.google.com/pubsub/quotas#:~:text=Resource%20limits,-Note%3A%20It%20is&amp;text=Retains%20unacknowledged%20messages%20in%20persistent,a%20subscription%2C%20the%20subscription%20expires">https://cloud.google.com/pubsub/quotas#:~:text=Resource%20limits,-Note%3A%20It%20is&amp;text=Retains%20unacknowledged%20messages%20in%20persistent,a%20subscription%2C%20the%20subscription%20expires</a>.: Google Cloud Pub Sub has certain max limits such as 10000 topics per project, 10 MB per message, 10 KB per schema, etc.</p>
<p><a href="https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8">https://medium.com/google-cloud/google-cloud-pub-sub-ordered-delivery-1e4181f60bc8</a>: Across a load-balanced set of subscribers, only 1 subscriber can be in a partition at a time. Thus, there is a limit on parallel processing. Possible solution: Put subscriber on topic with more shards but this means more topics to maintain and migration needs to be done more carefully.</p>
<p><a href="https://www.youtube.com/watch?v=f5DOsB7Nlw0">https://www.youtube.com/watch?v=f5DOsB7Nlw0</a></p>
<p>• Create Google Cloud account and set up features using website UI.</p>
<p>• Set up topic, which 1 publisher detects.</p>
<p>• Set up 2 subscribers.</p>
<p>• Install Python and Google SDK (<a href="https://cloud.google.com/sdk/docs/install">https://cloud.google.com/sdk/docs/install</a>).</p>
<p>• Open 3 terminals for 1 publisher and 2 subscribers.</p>
<p>• Messages are published and subscribed efficiently with little delay time in between.</p></td>
</tr>
</tbody>
</table>

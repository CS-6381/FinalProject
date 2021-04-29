### Instructions for installing Couchbase

### OS
- Ubuntu 
- 8 CPU
- 32 RAM

### Step 1: Install CouchBase Server

```curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-amd64.deb```
```sudo dpkg -i ./couchbase-release-1.0-amd64.deb```
```sudo apt-get update```
```sudo apt-get install couchbase-server-community```
```sudo apt-get install nginx```
```sudo service nginx start```

### Step 2: Install C SDK for libcouchbase (3.1)
```sudo wget -O - https://packages.couchbase.com/clients/c/repos/deb/couchbase.key | sudo apt-key add -```
```echo "deb https://packages.couchbase.com/clients/c/repos/deb/ubuntu1804 bionic bionic/main" | sudo tee /etc/apt/sources.list.d/couchbase.list```
```sudo apt update```
```sudo apt upgrade```
```sudo apt install libcouchbase3 libcouchbase-dev libcouchbase3-tools libcouchbase-dbg libcouchbase3-libev libcouchbase3-libevent```

### Step 3: Install Python SDK
```sudo apt install python3-pip```
```sudo apt-get install git-all python3-dev python3-pip```
```python3-setuptools cmake build-essential```
```sudo apt-get install libssl-dev```
```python3 -m pip install couchbase```
```pip3 install pandas```

### Working with Couchbase
- To use the command ```./couchbase-cli``` you may need to ```cd```  into ```opt/couchbase``` 

- To create and add to your cluster via the gui, visit: ```http://{your ip}:8091```

- On each OS/VM create a cluster, and on the OS/VM you choose as the main node, add the other vms/clusters as nodes. You can find more information here: [Create a cluster](https://docs.couchbase.com/server/current/manage/manage-nodes/create-cluster.html)
- In couchbase, a document is the equivalent of a row 
- Make sure that your security groups allow ingress and egress to ports such as 8091






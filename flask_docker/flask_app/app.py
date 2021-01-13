
from flask import Flask,jsonify
from flask_cors import CORS
from flask import request
from kafka import KafkaProducer
import json

# from kafka.admin import KafkaAdminClient, NewTopic


# admin_client = KafkaAdminClient(
#     bootstrap_servers="localhost:9092", 
#     client_id='test'
# )

# topic_list = []
# topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hello world"

@app.route('/simulate',methods=['POST'])
def simulate():
    if request.method == 'POST':
        # data = jsonify(request.json)
        data = request.json
        data = json.dumps(data).encode('utf-8')
        print("data",data)
        producer =  KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send(topic='BDA_Project', value =data)
        producer.flush()
        return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6007, debug=True)
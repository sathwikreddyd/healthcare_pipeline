from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_healthcare_data():
    data = {
        'patient_id': random.randint(1, 100),
        'heart_rate': random.randint(60, 100),
        'blood_pressure': random.randint(80, 120),
        'timestamp': int(time.time())
    }
    return data

if __name__ == "__main__":
    while True:
        data = generate_healthcare_data()
        producer.send('healthcare', value=data)
        print(f'Sent data: {data}')
        time.sleep(1)

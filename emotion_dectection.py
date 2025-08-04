import requests
import json

def emotion_detector(text_to_analyse):
    # Watson NLP EmotionPredict API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Required headers for the request
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Request payload with the text to analyse
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response to JSON
    response_json = response.json()
    
    # Return the text attribute from the response object
    return response_json

# Test (you can remove this later if not needed)
if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(json.dumps(result, indent=2))

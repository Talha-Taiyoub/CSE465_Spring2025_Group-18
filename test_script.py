import torch
from transformers import BertForSequenceClassification, BertTokenizer

MODEL_PATH = "bert_model.pt"
MODEL_NAME = "bert-base-uncased"

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

# Load the trained model
model = BertForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
model.load_state_dict(
    torch.load(MODEL_PATH, map_location=torch.device("cpu"))
)  # Load model to CPU
model.eval()


def predict_url(url):
    """Predict if a URL is phishing or legitimate."""
    # Tokenize the input URL
    inputs = tokenizer(
        url, padding=True, truncation=True, max_length=128, return_tensors="pt"
    )

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get prediction
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()  # Get class (0 or 1)

    return "Phishing" if prediction == 1 else "Legitimate"


if __name__ == "__main__":
    print("=== Phishing Detection System ===")
    while True:
        url = input("\nEnter a URL to classify (or type 'exit' to quit): ")
        if url.lower() == "exit":
            break
        result = predict_url(url)
        print(f"Prediction: {result}")

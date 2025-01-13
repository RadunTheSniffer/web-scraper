from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import extractor
#import sentiment

# Initialize the tokenizer and model for NER
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

# Create the NER pipeline
nlp = pipeline("ner", model=model, tokenizer=tokenizer)


#example = sentiment.analyze('https://www.bbc.com/news')  


#for item in example:
    #ner_results = nlp(item)
    #print(f"Text: {item}")
    #print(f"NER Results: {ner_results}")
    #print("\n")

def filter_redundant_texts(cleaned_data):
    #results = extractor.scrape_data(link)
    filtered_texts = []
    for item in cleaned_data:
        ner_results = nlp(item)
        
        # Extract text from NER results
        text = item
        # Filter based on named entities
        if len(ner_results) < 2:  # Adjust the threshold based on your needs
            continue
        
        # Filter based on text length
        if len(text) < 20:  # Adjust the length threshold based on your needs
            continue
        
        # Filter based on keywords
        keywords = ["Follow", "Subscribe", "More on"]
        if any(keyword in text for keyword in keywords):
            continue
        
        filtered_texts.append(text)
    
    return filtered_texts


   #work in progress , figuring out the logic and flow
    

# Example usage
#texts = ["'It's tricky, they fly a lot' - Arteta on Carabao Cup balls", "Follow BBC on:"]
#sentiments = ["Positive", "Neutral"]
#ner_results = [
#    [{'entity': 'B-ORG', 'score': 0.7772287, 'index': 16, 'word': 'Arte', 'start': 38, 'end': 42}, {'entity': 'B-MISC', 'score': 0.9982615, 'index': 19, 'word': 'Cara', 'start': 48, 'end': 52}, {'entity': 'I-MISC', 'score': 0.9977863, 'index': 20, 'word': '##bao', 'start': 52, 'end': 55}, {'entity': 'I-MISC', 'score': 0.9981798, 'index': 21, 'word': 'Cup', 'start': 56, 'end': 59}],
#    [{'entity': 'B-ORG', 'score': 0.9973673, 'index': 4, 'word': 'BBC', 'start': 13, 'end': 16}]
#]

#filtered_texts = filter_redundant_texts(texts, sentiments, ner_results)
#print(filtered_texts)


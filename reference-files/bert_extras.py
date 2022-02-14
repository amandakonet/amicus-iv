# pretrained model
bert = AutoModel.from_pretrained('bert-base-uncased')

# associated tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

# batch_sentences is a list
batch = tokenizer(batch_list[0], padding=True, truncation=True, return_tensors="pt")
print(batch)

from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
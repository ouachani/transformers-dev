from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save model == save time
model.save_pretrained('/models/' + model_name)

# Define your input text
input_text = "How are you bro ?!!"

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate the output
output = model.generate(input_ids)

# Decode the output
output_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(f"The model generated the following text: {output_text}")

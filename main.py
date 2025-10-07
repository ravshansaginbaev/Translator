import tkinter as tk
from tkinter import ttk, messagebox
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load the model and tokenizer
model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# Dictionary mapping language names to codes
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Russian": "ru",
    "Arabic": "ar",
    "German": "de",
    "Spanish": "es",
    "Uzbek": "uz"
}

# Function to perform translation
def translate_text():
    try:
        # Get selected language codes
        src_lang_name = src_lang_var.get()
        tgt_lang_name = tgt_lang_var.get()

        # Map language names to codes
        src_lang = language_codes.get(src_lang_name)
        tgt_lang = language_codes.get(tgt_lang_name)
        
        text = input_text.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        tokenizer.src_lang = src_lang
        encoded_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.get_lang_id(tgt_lang))
        translation = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
        
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Multilingual Translator")
root.geometry("600x400")

# Create and place widgets
tk.Label(root, text="Input Text:").pack(pady=5)
input_text = tk.Text(root, height=5)
input_text.pack(pady=5)

tk.Label(root, text="Source Language:").pack(pady=5)
src_lang_var = tk.StringVar(root)
src_lang_dropdown = ttk.Combobox(root, textvariable=src_lang_var, values=list(language_codes.keys()))
src_lang_dropdown.pack(pady=5)
src_lang_dropdown.current(0)  # Set default to the first language

tk.Label(root, text="Target Language:").pack(pady=5)
tgt_lang_var = tk.StringVar(root)
tgt_lang_dropdown = ttk.Combobox(root, textvariable=tgt_lang_var, values=list(language_codes.keys()))
tgt_lang_dropdown.pack(pady=5)
tgt_lang_dropdown.current(1)  # Set default to the second language

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

tk.Label(root, text="Translated Text:").pack(pady=5)
output_text = tk.Text(root, height=5)
output_text.pack(pady=5)

# Start the main loop
root.mainloop()

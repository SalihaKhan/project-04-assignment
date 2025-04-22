import streamlit as st
import base64
import urllib.parse
from string import ascii_letters

def caesar_cipher(text, shift, decrypt=False):
    result = []
    for char in text:
        if char in ascii_letters:
            shift_amount = -shift if decrypt else shift
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result.append(new_char.upper() if char.isupper() else new_char)
        else:
            result.append(char)
    return ''.join(result)

st.title("Encoder/Decoder App")
st.write("A simple tool for encoding and decoding text using various algorithms.")

# Input text
text = st.text_area("Enter your text here:")

# Algorithm selection
algorithm = st.selectbox(
    "Select encoding/decoding algorithm:",
    ["Base64", "URL", "Caesar Cipher", "Hexadecimal", "Binary"]
)

# Additional parameters for Caesar Cipher
if algorithm == "Caesar Cipher":
    shift = st.slider("Select shift amount:", 1, 25, 3)

# Operation selection
operation = st.radio("Select operation:", ["Encode", "Decode"])

# Process button
if st.button("Process"):
    if not text:
        st.warning("Please enter some text to process.")
    else:
        try:
            if algorithm == "Base64":
                if operation == "Encode":
                    result = base64.b64encode(text.encode()).decode()
                else:
                    result = base64.b64decode(text.encode()).decode()
            
            elif algorithm == "URL":
                if operation == "Encode":
                    result = urllib.parse.quote(text)
                else:
                    result = urllib.parse.unquote(text)
            
            elif algorithm == "Caesar Cipher":
                if operation == "Encode":
                    result = caesar_cipher(text, shift)
                else:
                    result = caesar_cipher(text, shift, decrypt=True)
            
            elif algorithm == "Hexadecimal":
                if operation == "Encode":
                    result = text.encode().hex()
                else:
                    result = bytes.fromhex(text).decode()
            
            elif algorithm == "Binary":
                if operation == "Encode":
                    result = ' '.join(format(ord(c), '08b') for c in text)
                else:
                    binary_values = text.split()
                    result = ''.join(chr(int(b, 2)) for b in binary_values)
            
            st.success("Result:")
            st.code(result)
            
            # Copy to clipboard button
            st.download_button(
                label="Copy to clipboard",
                data=result,
                file_name=f"{operation.lower()}_result.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Instructions
st.markdown("""
### Instructions:
1. Enter your text in the text area
2. Select an encoding/decoding algorithm
3. Choose whether to encode or decode
4. Click the "Process" button
5. View and copy your result
""")
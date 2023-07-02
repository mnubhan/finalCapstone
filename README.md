# finalCapstone
# Project Name: Cypher Encoder

## Description:
This project includes a Python script for a cypher encoder that transforms 
input messages using a custom rule. The script performs a cyclic shift of 
each letter in the message, 15 places forward in the alphabet. For 
example, it transforms 'a' into 'p' and 'p' into 'e'. The transformation 
maintains the case of the original letters and leaves non-alphabetic 
characters unchanged. The importance of this project lies in understanding 
the basics of text encoding and decoding which are fundamental concepts in 
cryptography.

## Table of Contents:
1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)

## Installation<a name="installation"></a>:
To install this project on your local machine, follow these steps:

1. First, clone the repository to your local machine. You can do this by 
running the following command in your terminal:

   ```
   git clone <repo_link>
   ```

   Replace `<repo_link>` with the URL of this repository.

2. Ensure you have Python 3 installed. You can check this by running:

   ```
   python --version
   ```

3. No external libraries are needed to run this project.

## Usage<a name="usage"></a>:
To use the cypher encoder, run the Python script `encoder.py` with the 
message you want to encode passed as an argument. Here is a usage example:

```shell
python encoder.py "Your message here"
```

You should replace "Your message here" with the actual message you want to 
encode. The script will print the encoded message.

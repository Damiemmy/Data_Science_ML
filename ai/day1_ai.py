# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5.6",
#     input="Explain what Python is in simple terms."
# )

# print(response.output_text)

def ask_ai(prompt):
    print("Prompt sent to AI:")
    print(prompt)

    # Temporary mock response
    response = "Python is a programming language used to give computers instructions."

    return response


prompt = "Explain what Python is in simple terms."

answer = ask_ai(prompt)

print("\nAI Response:")
print(answer)
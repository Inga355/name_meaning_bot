#------------------------------------------------------------------------------
# name_meaning_bot - Simple CLI chatbot:
# Ask for a first name -> return meaning & likely origin (concise, reliable)
#------------------------------------------------------------------------------

import os
import sys


#------------------------------------------------------------------------------
# load .env for OPENAI_API_KEY
#------------------------------------------------------------------------------

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


#------------------------------------------------------------------------------
# Setup Openai Client
#------------------------------------------------------------------------------

try:
    from openai import OpenAI
except Exception as e:
    print("OpenAI SDK not found. Please install with: pip install openai")
    raise

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: Please set OPENAI_API_KEY in your environment")
    sys.exit()

client = OpenAI(api_key=API_KEY)


#------------------------------------------------------------------------------
# Prompt instructions
#------------------------------------------------------------------------------

SYSTEM_INSTRUCTIONS = (
    "You are a NameSensei, a concise on-topic assistant for first-name etymology."
    "Given a first name, return: \n"
    "- Meaning (1-2 sentences) \n"
    "- Likely origin/language(s) \n"
    "- Common variants (omit if not notable) \n"
    "If multiple well-known etymologies extist, mention the top 1 or 2 without over-speculation."
    "Keep the entire answer under ~100 words, neutral and factual."
)

USER_TEMPLATE = (
    "First name: {name} \n \n"
    "Meaning: ...\n"
    "Origin: ...\n"
    "Variants: ..."
)


#------------------------------------------------------------------------------
# Core Call
#------------------------------------------------------------------------------

def fetch_name_info(name: str) -> str:
    """
    Call to OPENAI to get a concise meaning & origin for a given first name
    :param name: the first name to analyze
    :return: (str) A brief explanation of the name's meaning and origin, or an error message
             if the input is empty.
    """
    name = name.strip()
    if not name:
        return "Please provide a non-empty first name."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTIONS},
            {"role": "user", "content": USER_TEMPLATE.format(name=name)},
        ]
    )

    return response.choices[0].message.content.strip()


#------------------------------------------------------------------------------
# CLI
#------------------------------------------------------------------------------

def main():
    print("Hello! Tell me your first name and I'll share its meaning & likey origin.")
    print("Type 'exit' to quit. \n")

    while True:
        try:
            raw = input("First name: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("Bye!")
            break

        if not raw:
            continue

        if raw.lower() in ("exit", "quit", "q"):
            print("Bye!")
            break

        answer = fetch_name_info(raw)
        print("\n" + answer + "\n")



if __name__ == "__main__":
    main()
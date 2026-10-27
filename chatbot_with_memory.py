import os
import llm_client
import memory
import config

EXIT_COMMANDS = ['exit', 'quit']

def build_messages(user_input: str) -> list[dict]:
    messages = [{'role': 'system', 'content': config.SYSTEM_PROMPT}]
    messages.extend(memory.get_history())
    messages.append({"role": "user", "content": user_input})

    return messages


def main():

    """Run the chatloop until until the user writes exit or quit"""

    print("ChatBot with memory")
    print(f"Provider: {config.LLM_PROVIDER}")
    print(f"Type exit or quit to stop.\n")

    configuration_error = config.get_configuration_error()
    if configuration_error:
        print(f"Configuration problem: {configuration_error}")
        return

    while 1 :
        try: 
            user_input = input("You: Enter your query: ").strip()
        except (EOFError, KeyboardInterrupt) :
            print(f"GoodBye\n")
            return

        if user_input:
            print(f"Please enter a query: \n")
            continue

        if user_input.lower().strip() in EXIT_COMMANDS:
            print(f"GoodBye\n")
            return



        try:
            response = llm_client.ask_gemini(build_messages(user_input=user_input))
        except EOFError, KeyboardInterrupt :
            print(f"Soory! Something went wrong\n")
            continue


        memory.add_user_messages(user_input)
        memory.add_assistant_messages(response)

        print(f"Assitant: {response}")

    if __name__ == '__main__':
        main()
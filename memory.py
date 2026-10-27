conversation_history: list[dict] = []



def add_user_message(content: str ) :

    conversation_history.append({"role": "User", "content": content } )


def add_assistant_message(content: str) :
    conversation_history.append({"role": "assistant", "content": content } )

def get_history():
    return list(conversation_history)

def clear_memory():
    conversation_history.clear()
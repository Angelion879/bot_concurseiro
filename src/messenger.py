"""Message building and sending functions"""

def message_builder(content):
    """creates message string based on the news list"""

    message_content = []

    for tender in content:
        body = f"## [{tender[0]}]({tender[2]})\n{tender[1]}"
        message_content.append(body)

    message = "\n\n".join(message_content)

    return message

if __name__ == "__main__":
    holder = [['Concurso TJ AL', 'Situação atual: comissão formada', 'https://exemple.com'],
                    ['Concurso TJ PB', 'Situação atual: comissão formada', 'https://exemple.com']]

    message_body = message_builder(holder)
    print("message_body")

from LeChat import LeChat

def main():

    LOGO = r"""
    ▖  ▖▘  ▗     ▄▖▄▖
    ▛▖▞▌▌▛▘▜▘█▌▛▘▌▌▐ 
    ▌▝ ▌▌▄▌▐▖▙▖▌ ▛▌▟▖

    ChatBot based on Phi-3         
    """
    print(LOGO)

    chatbot = LeChat()
    user_input = ""

    while(True):
        user_input = input("user > ")
        if user_input == "quit":
            break
        
        ai_output = chatbot.generate(user_input={"user_input":user_input}, user_id='0')
        print(f"ai > {ai_output.content}", end="\n\n")

if __name__ == "__main__":
    main()
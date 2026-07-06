from LeChat import LeChat
import logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():

    logging.basicConfig(
        filename="logs/chat.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.WARNING,
    )

    logging.captureWarnings(True)

    LOGO = r"""
    ▖  ▖▘  ▗     ▄▖▄▖
    ▛▖▞▌▌▛▘▜▘█▌▛▘▌▌▐ 
    ▌▝ ▌▌▄▌▐▖▙▖▌ ▛▌▟▖

    ChatBot based on Phi-3         
    """
    print(bcolors.OKBLUE + LOGO + bcolors.ENDC)

    chatbot = LeChat()
    user_input = ""

    while(True):
        # user --
        user_input = input(bcolors.OKBLUE + "user > " + bcolors.ENDC)
        if user_input == "quit":
            break

        # ai --
        print(bcolors.OKBLUE + f"ai > " + bcolors.ENDC, end="")
        ai_output = chatbot.generate(user_input={"user_input":user_input}, user_id='0')
        for chunk in ai_output:
            print(chunk.content, end="", flush=True)

        # space between messages
        print("\n")

if __name__ == "__main__":
    main()
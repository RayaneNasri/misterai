from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

database = {}

class LeChat:
    """_summary_
    """

    def __init__(self):
        
        self.model= ChatLlamaCpp(
            model_path= "models/Phi-3-mini-4k-instruct-fp16.gguf",
            n_gpu_layers=-1,
            max_tokens=500,
            n_ctx=2048,
            seed=42,
            verbose=False
        )

        self.prompt = ChatPromptTemplate(
            [
                ("system", "you are a helpful assistant chatbot."),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{user_input}"),
            ]
        )

        self.with_history = RunnableWithMessageHistory(
            self.prompt | self.model,
            self._get_session_history,
            input_messages_key="user_input",
            history_messages_key="chat_history"
        )
    
    def _get_session_history(self, id: str)-> InMemoryChatMessageHistory:
        """_summary_

        Args:
            id (str): _description_

        Returns:
            InMemoryChatMessageHistory: _description_
        """
        
        global database
        if id not in database:
            database[id] = InMemoryChatMessageHistory()
        return database[id]
          
    def generate(self, user_input: dict[str, str], user_id: str):
        """_summary_

        Args:
            input_user (_type_): _description_
        """

        config = {"configurable": {"session_id": user_id}}
        output = self.with_history.stream(user_input, config=config)

        return output
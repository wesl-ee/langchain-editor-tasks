from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate user input from {input_language} to {output_language}. Only include the translation.",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI()

chain = _prompt | _model

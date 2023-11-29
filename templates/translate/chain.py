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
_model = ChatOpenAI(model="gpt-3.5-turbo-instruct")

chain = _prompt | _model

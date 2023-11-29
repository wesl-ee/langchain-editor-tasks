from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "The following is a {language} snippet. Explain what this snippet of code does.",
        ),
        (
            "human",
            "{text}",
        ),
    ]
)
_model = ChatOpenAI()

chain = _prompt | _model

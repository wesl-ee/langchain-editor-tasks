from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "The following is a {language} snippet. Code after the `<MID>` token is substituted where the `<FILL>` token is and correctly completes the code. `<PRE>`, `<FILL>`, `<SUF>` and `<MID>` are tokens and therefore do not need closing tags.",
        ),
        ("system", "<PRE>"),
        ("human", "{prefix}"),
        ("system", "<FILL>"),
        ("system", "<SUF>"),
        ("human", "{suffix}"),
        ("system", "<MID>"),
    ]
)
_model = ChatOpenAI(temperature=0.1, max_tokens=2048, model="gpt-3.5-turbo-16k")

chain = _prompt | _model

from fastapi import FastAPI
from langserve import add_routes
from templates.pirate_speak.chain import chain as pirate_speak_chain
from templates.translate.chain import chain as translate_chain
from templates.code_completion.chain import chain as code_completion_chain
from templates.code_explain.chain import chain as code_explain_chain

app = FastAPI(title="Retrieval App")

add_routes(app, pirate_speak_chain, path="/pirate-speak")
add_routes(app, translate_chain, path="/translate")
add_routes(app, code_completion_chain, path="/code-completion")
add_routes(app, code_explain_chain, path="/code-explain")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)

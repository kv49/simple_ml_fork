from fastapi import FastAPI
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from pydantic import BaseModel


class Answer(BaseModel):
    context: str
    question: str


def get_pipe_line(model_name):
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return nlp


app = FastAPI()
model_name = "deepset/roberta-base-squad2"
nlp = get_pipe_line(model_name)


@app.get("/")
def root():
    return {"message": 'Hello adsfasd'}


@app.post("/answer/")
def answer(item: Answer):
    QA_input = {"context": item.context}
    QA_input["question"] = item.question
    result = nlp(QA_input)
    return {"context": item.context,
            "question": item.question,
            "answer": result["answer"],
            "score": result["score"]}

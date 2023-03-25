#pip install streamlit==1.13
#pip install transformers
#pip install tensorflow
#pip install torch


import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

@st.cache(allow_output_mutation=True)
def get_pipe_line(model_name):
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return nlp

# Выводим заголовок страницы
st.title('Answering questions')

#context = st.text_input("Context: ", 'One can become a writer only if he is talented')
#question = st.text_input("Question: ", 'How can become a writer?')

context = st.text_area("Context: ", """OPENING A RESTAURANT.
Twelve months ago Robin Parker left his job at an insurance company. He now runs a restaurant which is doing very well since it opened four months ago.
Opening a restaurant was a big change for Robin. He loves travelling and all his favourite television programmes are about cooking. One day, he read in a newspaper about a doctor who left her job and moved to Italy to start a restaurant. He thought, “I can do that!” His wife wasn’t very happy about the idea, and neither was his father. But his brother, a bank manager, gave him lots of good ideas.
Robin lived in Oxford and had a job in London. He thought both places would be difficult to open a restaurant in, so he chose Manchester because he knew the city from his years at university. He found an empty building in a beautiful old street. It was old and needed a lot of repairs, but all the other buildings were expensive and he didn’t have much money.
Robin loves his new work. It’s difficult being the boss, but he has found an excellent chef. He says he enjoys talking to customers and some of them have become his good friends. He gets up at 6pm and often goes to bed after midnight. It’s a long day but he only starts to feel really tired when he takes time off at the weekends.
Robin’s restaurant is doing so well that he could take a long holiday. But he’s busy with his new idea to open a supermarket selling food from around the world. He’s already found a building near his restaurant.""")
question = st.text_area("Questions: ", """Did Robin's wife supported him?
Who helped Robin open his restaurant?
Where is Robin's restaurant?
Robin likes
Next, Robin wants to""")

model_name = "deepset/roberta-base-squad2"
nlp = get_pipe_line(model_name)

get_answer_button = False
if context and question:
    get_answer_button = st.button('Get the answer')
else:
    st.write("Please type context and questions related to the context")

if get_answer_button:
    QA_input = {"context":context}
    for q in question.splitlines():
        QA_input["question"] = q
        result = nlp(QA_input)
        st.write("Question: ",q)
        st.write("The answer is: ", result["answer"])
        st.write("Score: ", result["score"])
        st.write("")
else:
    st.write("")
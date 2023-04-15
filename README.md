Project 1. Simple ML app

## Content
0. [Team](.README.md#Team)
1. [Project description](README.md#Project-description)
2. [What problem are we solving?](README.md#What-problem-are-we-solving)
3. [Short info about initial data](README.md#Short-info-about-initial-data)
4. [Stages of the project](README.md#Stages-of-the-project)
5. [Results](README.md#Results)
6. [Conclusions](README.md#Conclusions)

### Team
- Viktor Roterman (ViktorRtm)
- Vyacheslav Kolotiy (kv49)
- Yyzhakov Sergey (PrintSmart)

:arrow_up:[to Content](_)

### Project description
Web/API app based on pre-trained model

:arrow_up:[to Content](_)


### What problem are we solving?
Need to create a simple application using a pre-trained model from open libraries

**Сompetition conditions:**
- Any model from open libraries
- Web or API application
- Application deployed in cloud

**QA metrics**     
... in procces ...


### Short info about initial data
We had:
- 5 libraries available
- 4 code hungry hands
- 3 crazy ideas
- 2 implementation options
- and only 1 chance to succeed

:arrow_up:[to Content](.README.md#Content)


### Stages of the project
1. Analyze existing models and choose the appropriate one.
2. Check the performance of the model.
3. Wrap it up in a UI.
4. Deploy in cluond.
5. Write the tests.
6. Do the tests.
7. Be happy.

:arrow_up:[to Content](.README.md#Content)


### Results:
Two options for implementing the application. 
#### 1) Web application on streamlit, for installation need:
Import following libraries:
```
pip install streamlit==1.13
pip install transformers
pip install tensorflow
pip install torch
```
... and for Running use command:
```
streamlit run web_answering.py 
```
#### 2) API application on FastAPI, for installation need:
Use this commands:
```
sudo apt update
sudo apt install python3.10-venv uvicorn
pip install -r requirements.txt
```
... and for Running use command:
```
uvicorn api_answering:app --host=0.0.0.0
```

:arrow_up:[to Content](.README.md#Content)


### Conclusions:
... in process ...

:arrow_up:[to Content](.README.md#Content)


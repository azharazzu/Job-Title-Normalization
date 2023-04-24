#                                                 Job-Title-Normalizatin 
The job title normalization service used to convert raw job title into standard job title. The developed model remove all unwanted/unnecessary things such as punctuations, emojis, company names, location names from the raw title. Model can expand short abbreviations into relevant form such as Jr into Junior, Sr into Senior, Vp into Vice president etc. For training the model almost 170 million data is used which involve the preprocessing and manual efforts.
    
## Contents
- [Application Description](#Application-Description)
- [Technology Used](#Technology-Used)
- [App URL](#App-URL)
- [Methodology](#Methodology)
- [Input](#Input)
- [Output](#Output)
- [Postman API](#Postman-API)
- [Deployment Process](#Deployment-Process)


##                                                 **Application description**

The job title normalization service used to convert raw job title into normalized job title which remove all unwanted(Url, Numbers, Special characters) and meaning less words from raw title and produce stander title.

## **Technology Used**

Python, Simple transformers, Flask

## **Business model**

Each user have different ways of writing about the same thing, with the help of job title normalization each title can be converted into one of the standard output title which can be further used for job recommendation or career pathway model.

## **App URL**

[](https://resume-parser.resume.io/parse)

## **Third party integrations**

No

## Methodology

![Untitled](https://user-images.githubusercontent.com/101692969/233233319-35c8a7a1-0b4a-4274-82bf-83003e35b018.png)


1. 170 Million linked in usa profile data is used to train the model.
2. Preprocessing involves the emojis, Stop-Words, non english titles and duplicates removal.
3. After preprocessing by choosing a threshold value of 500, approximate 100k unique raw titles were obtained.
4. On these 100k raw titles manual output labelling is done which gives us approximate 60k standard titles.
5. Facebook bart large model is trained on these 100k dataset and the loss value was around 0.02.
6. Streamlit and postman api is developed in which the input is raw title and output is standard    title

## Input
- Raw text job title

## Output
- Standard job title
<img width="775" alt="Screenshot 2023-04-21 at 10 39 18 AM" src="https://user-images.githubusercontent.com/101692969/233878668-9f23c078-c673-4826-a524-ac0ebf34ed26.png">


## Postman API

![Untitled (2)](https://user-images.githubusercontent.com/101692969/233233621-3ace3709-05aa-4f72-8cf3-f8804a242077.png)

Use a Token for authorization

![Untitled (3)](https://user-images.githubusercontent.com/101692969/233233672-ec979413-ef12-4ef1-9c0f-e4b7f9aeea18.png)


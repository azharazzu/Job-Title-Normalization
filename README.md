#                                                 Job-Title-Normalizatin.
    The job title normalization service used to convert raw job title into Standard job title.

##                                                 **Application description**

The job title normalization service used to convert raw job title into normalized job title which remove all unwanted(Url, Numbers, Special characters) and meaning less words from raw title and produce stander title.

## **Technology Used**

Python, Simple transformers, Flask

## **Business model**

Need to ask @Venky Thiru  about it

## **App URL**

[](https://resume-parser.resume.io/parse)

## **Third party integrations**

No

## Information

![Untitled](https://user-images.githubusercontent.com/101692969/233233319-35c8a7a1-0b4a-4274-82bf-83003e35b018.png)


1. For Job title normalization service we took LinkedIn data.
2. In First stage of cleaning we removed all kind of punctuations, emojis, Non-English words and removed all duplicates from the data.
3. Took EMSI 70k semi standard job title as a reference and did cosine similarity with TFIDF vectorization on cleaned LinkedIn data and filtered all raw job titles.
4. Manually labeled for preparing the training data for building the job title normalization model.
5. For Building the job title normalization model we took Facebook Bart transformer(Large) which works on the philosophy of encoder and decoder.
6. 

## Input

- Raw text job title
    
    Example: 
    
    1. Accenture Data Analyst
    2. sr. Data Scientist
    3. $4+*Software Developer%&^

## Output

Standard job title

Examples: 

1. Accenture Data Analyst =⇒ Data Analyst
2. sr. Data Scientist =⇒ Data Scientist
3. $4+*Software Developer%&^ =⇒ Software Developer

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d56db7cd-cac6-4839-a325-b08b1fb08568/Untitled.png)

## Example

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/584a0543-1256-4161-a8d2-91f9cdffdda3/Untitled.png)

Use a Token for authorization

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/02f08426-7e10-4c9d-ac80-e9d25da02647/Untitled.png)

## Deployment Process

[Deploy Guide](https://www.notion.so/Deploy-Guide-f6b8fce6a86d4dcf86e15b08038e1e17) 

## Infra

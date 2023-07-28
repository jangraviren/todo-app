import os

from google.cloud import aiplatform
from langchain import langchain


def main():
    # create a vertex ai client 
    client = aiplatform.gapic.EngineServiceClient()

    
    #Create a model name
    modelName = "todoModel"
    
    #create a model path to by joining the path
    modelPath = os.path.join("models",modelName)
    
    #lets now create a langChain framework model
    llm = langchain()
    
    #now lets load the data in to this model
    llm.load(modelPath)
    
    #lets now make a prediction 
    prediction = llm.predict("What are my today's todos tasks")
    
    print(prediction)
    
if __name__ == "__main__":
    main()
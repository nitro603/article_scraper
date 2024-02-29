from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from datetime import datetime
import dotenv

dotenv.load_dotenv()

def make_link(input):
    #https://www.w3schools.com/python/python_ref_string.asp //string methods
    #input: 1. Continued Israeli airstrikes flatten parts of Rafah amid slow progress for Gaza cease-fire - World
    #output goal: https://www.pbs.org/newshour/politics/trumps-2024-trials-where-they-stand-and-what-to-expect"
    
    input = input.lower()
    print(find_topic(input))
    #here take topic at the end
    #get the last quarter piece of the string and from that index to last part, find the first -, split to get topic
    
    replaced = input.replace(" ", "-")
    
    return replaced

def find_topic(input):
    #the reason why I do partial string is in case there's two "-"'s in the entire string
    partial_index = int(len(input) - 10)
    partial_string = input[partial_index:]
    
    start = partial_string.index("-") + 1
    topic = partial_string[start:]
    
    return topic

def collect_titles(url_list, query):
    openai = ChatOpenAI(
        model_name="gpt-4",
        max_tokens=2048
    )
    loader_list = []
    for i in url_list:
        print('loading url: %s' % i)
        loader_list.append(WebBaseLoader(i))

    index = VectorstoreIndexCreator().from_loaders(loader_list)
    ans = index.query(question=query,
                      llm=openai)
    print("")
    print(ans)

    #outfile_name = out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".out"
    #with open(outfile_name, 'w') as f:
    #    f.write(ans)



url_list = ["https://www.pbs.org/newshour/"];

prompt = '''
    Can you make a list containing the titles of the articles and their topic (example: politics, world or nation)
'''

#collect_titles(url_list, prompt)
print(make_link("- 2.  Capitol Hill fight over spending pushes country closer to government shutdown - Politics"))
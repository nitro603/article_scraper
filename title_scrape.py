from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from datetime import datetime
import dotenv

dotenv.load_dotenv()

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
    #print("")
    #print(ans)
    return ans

    #outfile_name = out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".out"
    #with open(outfile_name, 'w') as f:
    #    f.write(ans)
    
def make_array(input):
    array = input.splitlines()
    
    return array

def make_link(input):
    #https://www.w3schools.com/python/python_ref_string.asp //string methods
    #input: 1. Continued Israeli airstrikes flatten parts of Rafah amid slow progress for Gaza cease-fire - World
    #output goal: https://www.pbs.org/newshour/politics/trumps-2024-trials-where-they-stand-and-what-to-expect"
    
    input = input.lower()
    #here take topic at the end
    topic = find_topic(input)
    print(topic)
    #get the last quarter piece of the string and from that index to last part, find the first -, split to get topic
    
    #get substring
    replaced = input.replace(" ", "-")
    #replace "" by using ('"')
    result = replaced[5:len(replaced) - len(topic)]
    
    return result

def find_topic(input):
    #the reason why I do partial string is in case there's two "-"'s in the entire string
    partial_index = int(len(input) - 10)
    partial_string = input[partial_index:]
    
    start = partial_string.index("-") + 1
    topic = partial_string[start:]
    
    return topic


url_list = ["https://www.pbs.org/newshour/"];
prompt = '''
    Make a list containing the titles of the articles and their topic (example: politics, world or nation, if not specified just state not specified)?
'''

#array = make_array(collect_titles(url_list, prompt))
example1 = '''8. "U.S. Census changes how it identifies people by race and ethnicity, creates Middle Eastern category for first time" - Politics'''
make_link(example1)

#example2 = '''1. "Baltimore crews recover bodies of 2 killed in bridge collapse" - Not specified'''
#example3 = '''9. '‘What kind of future do I have in Mississippi’? Medicaid advocates push for expansion' - Topic: Health'''
#example4 = '''1. Title: "Baltimore crews recover bodies of 2 killed in bridge collapse" - Topic: Not specified'''
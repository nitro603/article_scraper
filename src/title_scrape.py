from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from datetime import datetime
import dotenv

dotenv.load_dotenv()

def collect_info(url_list, query):
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

def make_links(input):
    
    
    links = []
    for item in input:
        
        item = item.lower()
        
        topic = (find_topic(item))
        title = (find_title(item))
        link = topic + " " + title
        
        links.append(link)
        
        print(links)
    
    return links

def find_topic(input):
    #the reason why I do partial string is in case there's two "-"'s in the entire string
    partial_index = int(len(input) - 10)
    partial_string = input[partial_index:]
    
    start = partial_string.index("-") + 1
    topic = partial_string[start:]
    print(topic)
    return topic

def find_title(input):
    start = input.index('''"''')
    temp = input[start + 2: ]
    
    end = temp.index('''"''')
        
    print(start)
    print(temp[start:end])
    return "work in progress"


url_list = ["https://www.pbs.org/newshour/science"]
prompt = '''
    Make a list containing the titles of the articles and their topic (example: politics, world or nation, if not specified just state not specified)?
'''

#array = make_array(collect_info(url_list, prompt))
array = ['''1. "WATCH: Biden marks Earth Day with new grants for solar power" - Politics''', '''2. "Why does luck play such a big role in hockey games?" - Science''', '''3. "These coral reefs suffered major damage. Watch how restoration efforts helped bring them back" - Science', '4. "Critics had accused the U.S. Interior Department and Bureau of Land Management of failing to recognize the cultural significance of the San Pedro Valley to several Native American tribes" 
- Not Specified''', '''5. "Central U.S. faces severe thunderstorm threat and possible tornadoes" - Not Specified''', '''6. "Coral reefs across the globe once again endure mass bleaching amid warming oceans, scientists say" - Not Specified''']
make_links(array)

#print(make_link(example1))

#example2 = '''1. "Baltimore crews recover bodies of 2 killed in bridge collapse" - Not specified'''
#example3 = '''9. '‘What kind of future do I have in Mississippi’? Medicaid advocates push for expansion' - Topic: Health'''
#example4 = '''1. Title: "Baltimore crews recover bodies of 2 killed in bridge collapse" - Topic: Not specified'''
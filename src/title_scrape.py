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

    return ans

    #outfile_name = out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".out"
    #with open(outfile_name, 'w') as f:
    #    f.write(ans)
    
def make_array(input):
    array = input.splitlines()
    
    return array

def make_links(input):
    print(input)
    links = []
    for item in input:
        item = item.lower()
        topic = (find_topic(item))
        title = (find_title(item))
        link = "https://www.pbs.org/newshour/"+ topic + "/" + title
        
        links.append(link)
        
    return links

def find_topic(input):
    #the reason why I create a partial string is in case there's a second "-" earlier in the string
    partial_index = int(len(input) - 16)
    partial_string = input[partial_index:]
    
    start = partial_string.index("-") + 1
    topic = partial_string[start + 1:]
    return topic

def find_title(input):
    if "watch:" in input:
        input = input.replace("watch:", "watch-live")
    if "watch live:" in input:
        input = input.replace("watch live", "")
    if "," in input:
        input = input.replace(",", "")
    if "?" in input: 
        input = input.replace("?", "")
    if "." in input: 
        input = input.replace(".", "")
        
    start = input.index('''"''')
    temp = input[start + 2: ]
    end = temp.index('''"''')
        
    title = input[start + 1:end + 5]
    title = title.replace(" ", "-")
    return title


#url_list = ["https://www.cnbc.com/investing/"]
url_list = ["https://www.pbs.org/newshour/science"]

#prompt = '''  Make a list containing the titles of the articles and their topic (example: politics, world or nation, if not specified just state not specified)'''
prompt = ''' Make a list of titles from the articles on this website '''

#array = make_array(collect_info(url_list, prompt))
#array = ['''1. "WATCH: Biden marks Earth Day with new grants for solar power" - Politics''', '''2. "Why does luck play such a big role in hockey games?" - Science''', '''3. "These coral reefs suffered major damage. Watch how restoration efforts helped bring them back" - Science', '4. "Critics had accused the U.S. Interior Department and Bureau of Land Management of failing to recognize the cultural significance of the San Pedro Valley to several Native American tribes" - Not Specified''', '''5. "Central U.S. faces severe thunderstorm threat and possible tornadoes" - Not Specified''', '''6. "Coral reefs across the globe once again endure mass bleaching amid warming oceans, scientists say" - Not Specified''']
array = ['1. "Global talks to tackle plastic pollution hit critical stage" - World', '2. "WATCH: Biden marks Earth Day with new grants for solar power" - Politics', '3. "Why does luck play such a big role in hockey games?" - Science', '4. "These coral reefs suffered major damage. Watch how restoration efforts helped bring them back" - Science', '5. "More Americans worried about climate change, but few think Biden’s climate law will help, AP-NORC poll says" - Politics']

#print(array)
print(make_links(array))
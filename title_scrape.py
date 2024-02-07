from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from datetime import datetime
import dotenv

dotenv.load_dotenv()

def web_qa(url_list, query, out_name):
    openai = ChatOpenAI(
        model_name="gpt-3.5-turbo",
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

    outfile_name = out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".out"
    with open(outfile_name, 'w') as f:
        f.write(ans)



url_list = [
    "https://www.pbs.org/newshour/"
    ]

prompt = '''
    Can you make a list containing the titles of the articles and their topic (example: politics, world or nation)
'''

web_qa(url_list, prompt, "summary")
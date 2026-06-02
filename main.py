
from src.chains.rag_chain import chain

def main():

    print("..........Hello, Welcome to Health Chatbot...........")

    while True:
        question = input("Enter your query : ")
        if question == 'exit':
            break
        print("System : ", end=' ')
        for s in chain.stream(question):
            print(s, end=' ')
        print('\n')
    print("Thanks for chatting!")


if __name__ == "__main__": 
    main()

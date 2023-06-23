import google.generativeai as palm

def main():
    palm.configure(api_key='AIzaSyATrSgFd7MLVg2vATRAPHiAZz-4-IxeDKM')


    # Create a new conversation
    response = palm.chat(messages='Hello')

    # Last contains the model's response:
    print(response.last)
if "__name__" == "__main__":
    main()

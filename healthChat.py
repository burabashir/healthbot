import pandas as pd

# load your data into a dataframe
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I am your health assistant. How can I help you today?")

while True:
    #1. get user input and store the same into a virable
    user_text = input("\n You: ").lower()

    # Check if the user wants to exit the chat
    if user_text == "quit":
        print("Healthbot: Goodbye! Take care of your health.")
        break

    # create a variable with will store the details of the user input
    found_answer = False

    # come up with a loop through entire dataframe created before
    for index, row in df.iterrows():
        # clean up the keyboard from csv
        keywords_list = str(row["keywords"]).split(',')

        # below we check every keyword in that given row
        for word in keywords_list:
            clean_word = word.strip().lower()


        # if the keywords is inside of user's sentence
            if clean_word in user_text:
                print("Healthbot: ", row['response'])
                found_answer = True
                break #stop looking at other keywords

        if found_answer:
            break #stop looking at other answers since we already found one

        # if went through the entire dataframe and didn't find any answer, we will print the following message


    if not found_answer:
        print("Healthbot: I'm sorry, I didn't understand that. Can you please rephrase your question?")

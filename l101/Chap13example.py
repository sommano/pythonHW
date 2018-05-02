class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

# TODO define a class called BoredChatbot
class BoredChatbot(Chatbot):

    def __init__(self,name):
        self.name = name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        if len(prompt_from_human) > 1:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return "It is very interesting that you say: '" + prompt_from_human + "'"

# make a chatbot
def main():
    hal = BoredChatbot("hal")
    # introduce the chatbot and allow the user to say something
    human_message = input(hal.greeting())
    # respond to the user
    print(hal.response(human_message))

    # TODO: keep reading! see below

if __name__ == "__main__":
    main()

class Chat:
    def __init__( self):
        
        self.chatee = input("who are you chatting with?\n")
        self.last_message = input("what is your last message?\n")
        self.last_message_time = input("when was the last message sent?\n")

    def __str__(self): 
            return f"you are chatting with {self.chatee}"

    def open(self):
            return f"you judt opened the chat with{self.chatee} with the last message{self. last_message}that was sent at {self. last_message_time}"
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

final_emails = []
info = input()

while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)   # обект от класа Email
    final_emails.append(email_info)
    info = input()
indices = [int(index) for index in input().split(", ")] # четем вход и слагаме в лист

for i in indices:  #изращаме имейл само на обектите от посочените позиции на indices
    final_emails[i].send()  # това е обекта от листа final_emails на позиция [i]

for current_email in final_emails:  # за всички обекти от final emails  викаме метода get_info
    print(current_email.get_info())

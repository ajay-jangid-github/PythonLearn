
class Notification:
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")
      

    def notify_user(notifier: Notification):
        notifier.send()


    notify_user(EmailNotification())
    
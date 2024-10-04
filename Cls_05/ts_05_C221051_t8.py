class EmailService:
    def send(self, message):
        print(f"Sending Email : {message}\n")
        
class Notification:
    def __init__(self):
        self.service = EmailService()
        
    def notify(self, message):
        self.service.send(message)
        
        
message = Notification("This is Nahian")


class NotificationService:
    def send(self, message):
        pass
    
class EmailService:
    def send(self, message):
        print(f"Sent Email : {message}\n")
        
class Notification:
    def __init__(self, service:NotificationService):
        self.service = service
        
    def notify(self, message):
        self.service.send(message)
        
email_service = EmailService()
notification = Notification(email_service)
notification.notify("Hello")
    
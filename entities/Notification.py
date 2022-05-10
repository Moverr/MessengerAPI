import json


class Notification:
       

    def set_notification_channel(self, notification_channel):
        self.notification_channel = notification_channel

    def get_notification_channel(self):
        return self.notification_channel

    def set_notification_template(self, notfication_template):
        self.notfication_template = notfication_template

    def get_notification_template(self):
        return self.notfication_template

    def set__notification_body(self, notification_body):
        self.notification_body = notification_body

    def get_notification_body(self):
        return self.notification_body

    def set_notificatiton_subect(self, notification_subject):
        self.notification_subject = notification_subject

    def get_notification_subject(self):
        return self.notification_subject

    def set_notification_recipients(self, notification_recipients):
        self.notification_recipients = notification_recipients

    def get_notification_recipients(self):
        return self.notification_recipients

    def __str__(self) -> str:
        return "{0}".format(self.notification_channel)

    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__)


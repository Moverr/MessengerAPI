class Notification:
    """ NOTIFICATION_CHANNEL , SMS,EMAIL,PUSH etc"""
    NOTIFICATION_CHANNEL = ""
    NOTIFICATION_TEMPLATE = ""
    NOTIFICATION_SUBJECT = ""
    NOTIFICATION_BODY = ""
    NOTIFICATION_RECIPIENTS = ""



    def __init__(self):
        pass

    def set_notification_channel(self, NOTIFICATION_CHANNEL):
        self.NOTIFICATION_CHANNEL = NOTIFICATION_CHANNEL

    def get_notification_channel(self):
        return self.NOTIFICATION_CHANNEL

    def set_notification_template(self, NOTIFICATION_TEMPLATE):
        self.NOTIFICATION_TEMPLATE = NOTIFICATION_TEMPLATE

    def get_notification_template(self):
        return self.NOTIFICATION_TEMPLATE

    def set__notification_body(self, NOTIFICATION_BODY):
        self.NOTIFICATION_BODY = NOTIFICATION_BODY

    def get_notification_body(self):
        return self.NOTIFICATION_BODY

    def set_notificatiton_subect(self, NOTIFICATION_SUBJECT):
        self.NOTIFICATION_SUBJECT = NOTIFICATION_SUBJECT

    def get_notification_subject(self):
        return self.NOTIFICATION_SUBJECT

    def set_notification_recipients(self, NOTIFICATION_RECIPIENTS):
        self.NOTIFICATION_RECIPIENTS = NOTIFICATION_RECIPIENTS

    def get_notification_recipients(self):
        return self.NOTIFICATION_RECIPIENTS

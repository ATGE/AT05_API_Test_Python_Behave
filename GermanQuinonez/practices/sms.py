class SMS_store:
    """
    This class sms store can hold multiple SMS messages
    (i.e. its internal state will just be a list of messages).
    Each message is represented as a tuple
    """

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """
        this method makes new SMS tuple,
        inserts it after other messages in the inbox  store.
        When creating this message, its has_been_viewed status is set False
        :param from_number:
        :param time_arrived:
        :param text_of_SMS:
        :return:
        """
        has_been_viewed = False
        self.inbox.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """
        This method returns the number of sms messages in my inbox
        :return: inbox length
        """
        return len(self.inbox)

    def get_unread_indexes(self):
        """
        This method returns list of indexes of all not-yet-viewed SMS messages
        :return: indexes of all not-yet-viewed SMS messages
        """
        result = []
        for (i, v) in enumerate(self.inbox):
            if v[0] == False:
                result.append(i)
        return (result)

    def get_message(self, i):
        """
        This method return (from_number, time_arrived, text_of_sms) for message[i]
        Also change its state to "has been viewed"
        If there is no message at position i, return None
        :param i: index of message
        :return: (from_number, time_arrived, text_of_sms) for message[i]
        """
        sms = self.inbox[i]
        sms = (True,) + sms[1:]
        self.inbox[i] = sms
        return self.inbox[i][1:]

    def delete(self, i):
        """
        This method deletes the message at index i
        :param i: index i
        :return: message at index i
        """
        return self.inbox.pop(i)

    def clear(self):
        """
        This method deletes all messages from inbox
        """
        self.inbox = []

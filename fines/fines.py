from datetime import datetime

class Fine:
    def __init__(self, user_id, cost, date):
        self.user_id = user_id
        self.cost = cost
        self.date = date

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("user_id must be a positive integer.")
        self._user_id = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("cost must be a non-negative integer.")
        self._cost = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, datetime):
            # If value is a datetime object, convert it to a string in the desired format
            self._date = value.strftime('%Y-%m-%d')
        elif isinstance(value, str):
            # If value is a string, validate the format
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValueError("date must be a string in 'YYYY-MM-DD' format.")
            self._date = value
        else:
            raise TypeError("date must be a string in 'YYYY-MM-DD' format or a datetime object.")


    def __str__(self):
        return f"user_id = {self.user_id}\ncost = {self.cost}$\ndate = {self.date}\n"

    def __repr__(self):
        return f"Fine(user_id={self.user_id}, cost={self.cost}, date='{self.date}')"
class TallyCounter:
    
    def __init__(self):
        self.num_clicks = 0

    def click(self):
        self.num_clicks += 1

    def count(self):
        return self.num_clicks
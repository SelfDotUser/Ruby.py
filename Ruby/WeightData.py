class WeightData:
    def __init__(self, json: dict):
        try:
            self.weight = json['weight']
        except KeyError:
            self.weight = {}

        self.message = json['message']

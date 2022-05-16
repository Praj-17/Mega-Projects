class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
    def GetRawcard(self):
        return self.front, self.back
    def fronts(self):
        front, back = self.GetRawcard()
        front_color = list(front.split("_"))[1]
        front_type = list(front.split("_"))[0]
        return front_color, front_type
    def backs(self):
        front, back = self.GetRawcard()
        back_color = list(back.split("_"))[1]
        back_type = list(back.split("_"))[0]
        return back_color, back_type
    def GetCard(self):
        front_color, front_type = self.fronts()  
        back_color, back_type = self.backs()  
        self.front_color = front_color
        self.front_type = front_type
        self.back_color = back_color
        self.back_type = back_type
        card = {
            "front_color": front_color,
            "front_type": front_type,
            "back_color": back_color,
            "back_type": back_type
        }
        return card
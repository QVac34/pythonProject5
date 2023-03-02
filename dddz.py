class CPU:
    def __init__(self, intel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = intel
        self.ghz = 3

class GPU:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "GeForce RTX 4090"
class Performance(GPU, CPU):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.ghz)
iphone = Performance(intel ="i9 13900KF")
iphone.print_info()
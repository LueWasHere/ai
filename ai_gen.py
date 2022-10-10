import random
import pip

try:
    import keyboard as kbrd
except ModuleNotFoundError:
    pip.main(["install", "keyboard"])

class keyboard_ai:
    def __init__(self, keys, wants=None, times_to_type=100):
        self.keys = keys
        self.punish = 0.01
        self.grade = 0
        self.sub = []
        self.times_to_type = times_to_type
        if wants == None:
            self.wants = [random.uniform(0, 1.0) for i in range(len(keys))]
        else:
            self.wants = wants
    def train(self):
        sv = self.wants
        gtl = self.wants
        for i in range(self.times_to_type):
            gtl.sort(reverse=True)
            kbrd.press(self.keys[sv.index(gtl[0])])
            sv[sv.index(gtl[0])] -= self.punish
            gtl = sv
        self.human_grade()
    def human_grade(self):
        grade = ""
        while type(grade) != int:
            try:
                grade = int(input("Grade the ai output (0-100, 0 - horrible, 100 - perfect)"))
                if grade > 100 or grade < 0:
                    grade = ""
            except:
                grade = ""
        if grade > 60:
            self.punish = (grade/0.01)/2
            if self.sub == []:
                self.sub = [random.uniform(-1.0, 1.0)]
            for i in range(0, len(self.wants)-1):
                self.wants[i] += self.sub[i]
                if self.wants[i] > 1.0:
                    self.wants[i] = 1.0 
                elif self.wants[i] < -1.0:
                    self.wants[i] = -1.0
        elif grade == 100:
            print(self.wants)
            exit(1)
        else:
            self.punish = (grade/0.01)/2
            self.sub = [random.uniform(-1.0, 1.0)]
            for i in range(0, len(self.wants)-1):
                self.wants[i] += self.sub[i]
                if self.wants[i] > 1.0:
                    self.wants[i] = 1.0 
                elif self.wants[i] < -1.0:
                    self.wants[i] = -1.0
keyboard = keyboard_ai(['w', 'a', 's', 'd'])
print(keyboard.wants)
keyboard.train()
keyboard.train()
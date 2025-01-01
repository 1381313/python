class Soccer:
    
    def __init__(self, name, number, height, weight, clean_sheets=0, tackles=0, goals=0, assists=0):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.clean_sheets = clean_sheets
        self.tackles = tackles
        self.assists = assists
        self.goals = goals

    def player_first_name(self):
        
        return 'The player first name: ' + self.name

    def player_number(self):
        
        return f'The player {self.name} number is {self.number}'

    def player_stats(self):
       
        return (f'{self.name} has {self.clean_sheets} clean sheets, '
                f'{self.tackles} tackles, {self.goals} goals, '
                f'and {self.assists} assists.')


class Goalkeeper(Soccer):
    
    def __init__(self, name, number, height, weight, clean_sheets):
        super().__init__(name, number, height, weight, clean_sheets=clean_sheets)

    def goalkeeper_stats(self):
       
        return f'{self.name} has {self.clean_sheets} clean sheets.'


class Roaming(Soccer):
    def __init__(self, name, number, height, weight, tackles, goals=6, assists=5):
        super().__init__(name, number, height, weight, tackles=tackles, goals=goals, assists=assists)

    def defender_stats(self):
        
        return f'{self.name} has made {self.tackles} tackles this season.'


player_1 = Soccer('h.amiri', 7, 175, 60, clean_sheets=5, tackles=12,goals=13,assists=9)
player_2 = Goalkeeper('neuer', 17, 175, 90, clean_sheets=15)
player_3 = Roaming('ramos', 20, 180, 91, tackles=35,goals=4,assists=1)

print(player_1.player_first_name())
print(player_1.player_number())
print(player_1.player_stats())

print(player_2.goalkeeper_stats())
print(player_3.defender_stats())
print(player_3.player_stats())

from numpy.random import uniform, normal, choice

class Forageable():

    # These attributes may not be called by students
    distribution = None
    distribution_args = None

    def __init__(self) -> None:
        pass

    def forage(self):
        # return max(0, self.distribution(**self.distribution_args))
        pass

class Tree(Forageable):
    def __init__(self, mean, std) -> None:
        self.distribution = normal
        self.distribution_args = {'loc': mean, 'scale': std}
    
    @staticmethod
    def init_random():
        mean = normal(6.0, 1.0)
        std = max(0.1, normal(1.5, 0.5))
        return Tree(mean, std)

    def forage(self):
        return 'apples', max(0, self.distribution(**self.distribution_args))

class BerryBush(Forageable):
    def __init__(self, mean, std) -> None:
        self.distribution = normal
        self.distribution_args = {'loc': mean, 'scale': std}
        self.distribution_args_rain = {'loc': mean/2, 'scale': std}

    def forage(self):
        if ForageBot.is_raining:
            return 'berries', max(0, self.distribution(**self.distribution_args_rain))
        else:
            return 'berries', max(0, self.distribution(**self.distribution_args))
    
    @staticmethod
    def init_random():
        mean = normal(3.0, 1.0)
        std = max(0.1, normal(1.0, 0.5))
        return BerryBush(mean, std)

class ForageBot():

    # These attributes may not be called by students. Only use the functions.
    pre_survey = {
        'tree_one': Tree(3, 1),
        'tree_two': Tree(5, 1),
        'tree_three': Tree(8, 3),
        'tree_four': Tree(7, 1),
        'bush_one': BerryBush(3, 0.5)
    }
    foragables = [Tree, BerryBush]
    foragable_probabilities = [0.5, 0.5]
    is_raining = False
    rain_prob = 0.4
    day_count = 0
    limit = None
    earnings = 0
    apple_prices = [1, 4, 4, 1, 1, 1, 1]
    berry_prices = [3, 3, 3, 3, 3, 5, 5]

    def __init__(self) -> None:
        self.inventory = []

    def forage(self, target: Forageable, verbose=False):
        fruit, amount = target.forage()
        if verbose:
            print(f'The robot collected {amount:.02f}kg of {fruit}')
        self.inventory.append((fruit, amount, 4))
        self.nextDay()
        return amount
    
    def explore(self) -> Forageable:
        forageable_type = choice(self.foragables, 1, self.foragable_probabilities)[0]
        self.nextDay()
        return forageable_type.init_random()

    @staticmethod
    def is_it_raining():
        return ForageBot.is_raining
    
    @staticmethod
    def reset_days(limit=None):
        ForageBot.day_count = 0
        ForageBot.earnings = 0
        ForageBot.limit = limit

    @staticmethod
    def what_day_is_it():
        return ForageBot.day_count

    def nextDay(self):
        ForageBot.day_count += 1
        if ForageBot.limit != None and ForageBot.day_count >= ForageBot.limit:
            print(f'{ForageBot.day_count} days have passed! Your final score is €{ForageBot.earnings:.02f}. Your script should stop here.')
        ForageBot.is_raining = uniform(0,1) < ForageBot.rain_prob
        # Lists would be more efficient than tuples here, but I don't want to confuse anyone with a list of lists.
        new_inventory = []
        for item in self.inventory:
            item = (item[0], item[1], item[2]-1)
            if item[2] > 0:
                new_inventory.append(item)
        self.inventory = new_inventory

    def sell(self, verbose=False):
        money = 0
        weekday = self.day_count % 7
        for item in self.inventory:
            price = ForageBot.apple_prices[weekday] if item[0] == 'apples' else ForageBot.berry_prices[weekday]
            money += item[1] * price
        ForageBot.earnings += money
        self.inventory = []
        if verbose:
            print(f'You earned €{money:.02f} from selling your inventory. Your total is now €{ForageBot.earnings:.02f}')
        return money


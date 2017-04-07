# Aquarium:
# -----------
#
# The Cape Town aquarium is designing a new feature and asks you to help. There
# will be fish tanks of different sizes all arranged in a large circle. Each fish
# tank will only contain fish from a single species. If the same fish species are
# stocked in adjacent tanks then they will continually attempt to fight and
# eventually will die of stress.
#
# You will be given a list of fish species, and how much it costs to stock those
# fish per liter of water. You will also be given a list of the tanks and how many
# liters each tank is. Your job is to find which fish should be stocked in which
# tank to achieve minimum cost without incurring any stress on the fish.
#
# Don't forget that the tanks are in a circle, so the beginning and ending tanks
# also mustn't contain the same species either.
#
# >>> tanks = [10, 15, 200, 35, 18, 99, 99, 10]
# >>> fish = [('shark', 12.1), ('marlin', 8.1), ('sole', 9.1)]
# >>> print(aquarium(tanks, fish))

tanks = [10, 15, 200, 35, 18, 230, 99, 99, 10, 85, 67, 3, 54, 90, 21, 70, 80, 44, 5, 12, 1]
fish = [('shark', 12.1), ('marlin', 8.1), ('sole', 9.1)]
def aquarium(tanks, fish):
    global memoize
    species = []
    for i in fish:
        species.append(i[0])

    def Aquarium(interest, compare, species, fish, tanks, count):
        copy = species[:]
        copy.remove(interest)
        score_pad = []
        counter = count
        counter += 1
        chooses = []
        for k in copy:
            if counter == (len(tanks) - 1):
                value = 0
                choose = []
                if k == compare:
                    value = float('inf')
                    
            else:
                if (counter, k) in memoize:
                    value, choose = memoize[(counter, k)]
                else:
                    value, choose = Aquarium(k, compare, species, fish, tanks, counter)
            
            result = fish[species.index(k)][1] * tanks[counter]
            result += value
            score_pad.append(result)
            chooses.append(choose)
        
        result = min(score_pad)
        animal = chooses[score_pad.index(result)][:]
        animal.insert(0, copy[score_pad.index(result)])
        memoize[(counter - 1, interest)] = result, animal 
        return result, animal
                
        
    Result = []
    rank = float('inf')
    for i in species:
        memoize = {}
        a, b = Aquarium(i, i, species, fish, tanks, count = 0)
        a += (fish[species.index(i)][1] * tanks[0])
        b.insert(0, i)
        if a < rank:
            rank = a
            Result = b
       
    return 'The most minimum cost is', rank, 'with the ordering of', Result

print(aquarium(tanks, fish))

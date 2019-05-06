class Garden(object):
    mapping = {
        'V' : 'Violets',
        'R' : 'Radishes',
        'G' : 'Grass',
        'C' : 'Clover'
    }

    def __init__(self, diagram, students=[]):
        self.diagram = diagram
        self.students = students

    def plants(self, who):
        offset = 0

        # check to see whether the list is empty, or not empty
        if not self.students:
            first_initial = who[0].upper()
            offset = ord(first_initial) - ord('A')
        else:
            offset = sorted(self.students).index(who)

        plants_assigned = ''
        plants_assigned += (self.diagram.split()[0])[offset*2 : offset*2+2]
        plants_assigned += (self.diagram.split()[1])[offset*2 : offset*2+2]

        result = []
        for ch in plants_assigned:
            result.append(Garden.mapping[ch])
        return result

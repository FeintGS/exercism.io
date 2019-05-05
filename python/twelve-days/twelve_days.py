switch = {
        12: ("twelfth" , "twelve Drummers Drumming, "       ),
        11: ("eleventh", "eleven Pipers Piping, "           ),
        10: ("tenth"   , "ten Lords-a-Leaping, "            ),
        9:  ("ninth"   , "nine Ladies Dancing, "            ),
        8:  ("eighth"  , "eight Maids-a-Milking, "          ),
        7:  ("seventh" , "seven Swans-a-Swimming, "         ),
        6:  ("sixth"   , "six Geese-a-Laying, "             ),
        5:  ("fifth"   , "five Gold Rings, "                ),
        4:  ("fourth"  , "four Calling Birds, "             ),
        3:  ("third"   , "three French Hens, "              ),
        2:  ("second"  , "two Turtle Doves, "               ),
        1:  ("first"   , "and a Partridge in a Pear Tree."  )
}

def recite(start_verse, end_verse):
    result = []
    for i in range (start_verse, end_verse+1):
       result.append(build_verse(i))
    return result

def build_verse(verse):
    if verse == 1:
        return "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."

    result = f'On the {switch.get(verse)[0]} day of Christmas my true love gave to me: '
    for i in range(verse, 0, -1):
        result += switch.get(i)[1]
    return result

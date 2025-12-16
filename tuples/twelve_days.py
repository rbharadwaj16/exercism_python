def recite(start_verse, end_verse):


    ordinals = ("first", "second", "third", "fourth", "fifth", "sixth", 
                "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
    
    gifts = (
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    )
    
    result = []
    
    for day in range(start_verse, end_verse + 1):
        # Build the opening line
        ordinal = ordinals[day - 1]
        verse = f"On the {ordinal} day of Christmas my true love gave to me: "
        
        # Get gifts up to this day
        gifts_for_day = gifts[:day]
        
        # Reverse them
        day_gifts = list(reversed(gifts_for_day))
        
        # Add "and" before last gift if not day 1
        if day > 1:
            last_gift = day_gifts[-1]
            day_gifts[-1] = "and " + last_gift
        
        # Join all gifts with commas
        gifts_text = ", ".join(day_gifts)
        
        # Complete the verse
        verse = verse + gifts_text + "."
        
        # Add to result list
        result.append(verse)
    
    return result
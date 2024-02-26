###PLAYBOOK FOOTBALL
import time
from random import shuffle, choice
# Your type_out function
def type_out(text, delay=0.014):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def type_out_slow(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()    

def announce_touchdown(first_turn):
    if first_turn == 'rec':  # Ravens score a touchdown
        ravens_td = [
            "|   Al Michaels: And they break the plane! Touchdown, Ravens!",
            "|   Al Michaels: He's in! That's a Ravens touchdown!",
            "|   Al Michaels: It's official! Touchdown, RAVENS!",
            "|   Al Michaels: No doubt about it, that's a touchdown for the Ravens!",
            "|   Al Michaels: He crosses the goal line! Ravens score!",
            "|   Al Michaels: And the Ravens fly into the end zone!",
            "|   Al Michaels: They did it! Touchdown, Ravens!",
            "|   Al Michaels: Into the end zone! That's six for the Ravens!"
        ]
        return choice(ravens_td)
    else:  # Jets score a touchdown
        jets_td = [
            "|   Al Michaels: And he's in! Touchdown, Jets!",
            "|   Al Michaels: That's a score! Jets touchdown!",
            "|   Al Michaels: He's crossed the PLANE! That's a Jets touchdown!",
            "|   Al Michaels: Touchdown, Jets!",
            "|   Al Michaels: And the Jets are on the board with six!",
            "|   Al Michaels: That's a touchdown for the Jets!",
            "|   Al Michaels: They've done it! Jets score!",
            "|   Al Michaels: Into the end zone! Jets touchdown!"
        ]
        return choice(jets_td)

def introduce_offense(first_turn):
    if first_turn == 'rec':
        jets_intro = [
            "|   Al Michaels: Zach Wilson and the Jets offense, coming up...",
            "|   Al Michaels: And here comes the Jets' aerial attack, led by Zach Wilson...",
            "|   Al Michaels: The Jets offense takes the field. Zach Wilson at the helm...",
            "|   Al Michaels: Now it's time for the Jets to show what they've got on offense...",
            "|   Al Michaels: Wilson and his Jets' offense gearing up...",
            "|   Al Michaels: Zach Wilson strides onto the field, eyes focused...",
            "|   Al Michaels: The Jets offense, looking to make a statement here...",
            "|   Al Michaels: Zach Wilson and his Jets take the field, the crowd buzzing..."
        ]
        return choice(jets_intro)
    else:
        ravens_intro = [
            "|   Al Michaels: The Ravens powerful offense are up next...",
            "|   Al Michaels: Now it's the Ravens' turn, led  Lamar Jackson and Simon St-Laurent...",
            "|   Al Michaels: The Bulldozer and his Ravens offense take the field next...",
            "|   Al Michaels: Here come the Ravens, and listen to this crowd...",
            "|   Al Michaels: The Ravens offense, always a sight to behold, prepares for their drive...",
            "|   Al Michaels: Lamar Jackson leads the Ravens onto the field, crowd roaring...",
            "|   Al Michaels: The Ravens' offensive juggernaut is ready to roll...",
            "|   Al Michaels: Ravens take the field, and this crowd knows something big could happen..."
        ]
        return choice(ravens_intro)

def ravens_first_down_stadium_announcer():
    oneliners = [
        "|   ----> Ravens Move The Chains! ---->   ",
        "|   =====> Another Ravens First Down! =====>   ",
        "|   ++++> New Set of Downs for the Ravens! ++++>   ",
        "|   >>>>> The Drive Continues for Baltimore! <<<<<   ",
        "|   !!!!!> Ravens, First Down! !!!!>   ",
        "|   [1]  Ravens First Down! [1]   ",
        "|   $$$$> Cha-Ching! First Down, Baltimore! $$$$>   ",
        "|   --->  Fiiiiiiirst Dooown  Raaaaaaveeeennssssss! --->  ",
        "|   ----> Ravens Convert on Third! First Down! ---->   ",
        "|   =====> Ravens Move The Chains! =====> ",
        "|   [1] Ravens First Down [1]   "
    ]
    return choice(oneliners)

def first_down_oneliners():
    oneliners = [
        "|  ----> First Down! ---->   ",
        "|  ----> First Down! ---->   ",
        "|  [4] --> [3] --> [2] --> [1] --> First Down   ",
        "|  ~~~~~>  1 & 10   ~~~~~>   ",
        "|  ----> First Down! ---->   ",
        "|  ----> First Down! ---->   ",
        "|  ----> First Down! ---->   ",
        "|  =====> Move! Those! Chains! ===>   ",
        "|  ~~~~~> First and Ten! ~~~~~>  ",
        "|  ~~~~~> First and Ten! ~~~~~>   ",
        "|  >>>>> FIRST DOWN >>>>>>   ",
        "|  ----> fiiiiirst dooooown ---->   ",
        "|  =====> MOVE! THOSE! CHAINS! =====>   ",
        "|   [1] DOWN - [1] DOWN - [1] DOWN - [1] DOWN  ",
        "|  [4] --> [3] --> [2] --> [1] --> First Down   ",
        "|  ~~~~~>  1 & 10   ~~~~~>   ",
        "|  [4] --> [3] --> [2] --> [1] --> First Down   "
    ]
    return choice(oneliners)

from random import choice

def turnover_on_downs_commentary():
    comments = [
        ("|  Al Michaels: \"And that's a turnover on downs! Just couldn't convert.\"",
         "|  Chris Collinsworth: \"That's a tough break. They really needed that first down.\""),
        ("|  Al Michaels: \"Fourth down attempt is no good! They'll have to give up the ball.\"",
         "|  Chris Collinsworth: \"The defense held strong when it mattered most.\""),
        ("|  Al Michaels: \"And that's going to do it! Can't keep the drive alive.\"",
         "|  Chris Collinsworth: \"Huge stop by the defense there, Al.\""),
        ("|  Al Michaels: \"Oh, they're not going to like that. Turned it over on downs.\"",
         "|  Chris Collinsworth: \"That could be a game-changer, Al.\""),
        ("|  Al Michaels: \"Went for it and came up short. That's a turnover on downs.\"",
         "|  Chris Collinsworth: \"You have to admire the courage to go for it, but it just didn't pay off.\""),
        ("|  Al Michaels: \"Failed to convert on fourth down. What a stop!\"",
         "|  Chris Collinsworth: \"That's how you make a statement on defense.\""),
        ("|  Al Michaels: \"Oof, that's got to hurt. Turned the ball over on downs.\"",
         "|  Chris Collinsworth: \"Moments like this can really swing the momentum.\""),
        ("|  Al Michaels: \"Rolled the dice on fourth down and came up empty.\"",
         "|  Chris Collinsworth: \"High risk, high reward, but not this time.\""),
        ("|  Al Michaels: \"It's a turnover on downs! They'll have to give the ball back.\"",
         "|  Chris Collinsworth: \"They had a chance, but the defense was just too strong.\""),
        ("|  Al Michaels: \"Can't convert, and they'll turn it over on downs.\"",
         "|  Chris Collinsworth: \"That's a momentum killer right there.\"")
    ]
    return choice(comments)

def big_play_commentary(yards, suit):
    if suit in ['D', 'S']:  # Pass plays
        comments = [
            (f"Al Michaels: \"Lamar Jackson on the screen to Simon... he breaks a tackle... OH AND BURSTS UP FIELD FOR {yards}!!.\"", 
             "Chris Collinsworth: \"Are you kidding me?! He's not just a game-changer, He's a Franchise-changer!\""),
            ("Al Michaels: \"Jackson, deep down the field... and it's Incomplete.......... OH HE CAUGHT IT!!!\"", 
             f"Chris Collinsworth: \"My goodness, Al, That was perfect coverage by Gardner there but its still a {yards} yard gain!!!\""),
            (f"Al Michaels: \"Swing pass to St-Laurent who's got space and Speed... and it's a {yards}-yard gain!!\"", 
             "Chris Collinsworth: \"I mean, come ON! How does he get away with things like that?!\""),
            (f"Al Michaels: \"Jackson to OBJ, AND ITS A HUGE {yards} YARD COMPLETION!!.\"", 
             "Chris Collinsworth: \"Al, we're not worthy! We're not worthy!\""),
            (f"Al Michaels: \"JACKSON LETS IT FLY... AND ITS CAUGHT BY THE ROOKIE SPEEDSTER FOR {yards}!!\"", 
             "Chris Collinsworth: \"That's just sorcery, pure sorcery! Flowers is so fun to watch!\""),
            (f"Al Michaels: \"Jackson uncorks one... AND ITS CAUGHT FOR {yards} DOWN FIELD!\"", 
             "Chris Collinsworth: \"He just makes it look so effortless, doesn't he?\""),
            (f"Al Michaels: \"Jackson goes long... AND CONNECTS WITH BECKHAM!! {yards} YARDS!\"", 
             "Chris Collinsworth: \"What a display of athleticism by OBJ!\""),
            (f"Al Michaels: \"Deep pass by Jackson... and it's complete for {yards} yards.\"", 
             "Chris Collinsworth: \"He's rewriting the playbook one pass at a time!\""),
            (f"Al Michaels: \"Jackson throws deep... and that's good to Smith for {yards} yards.\"", 
             "Chris Collinsworth: \" Smith just sits right under the safety and waits for Lamar to spot him. Unstoppable!\"")
        ]
    else:  # Run plays
        comments = [
            (f"Al Michaels: \"Simon St-Laurent through the line... and he POWERS THROUGH FOR {yards}!\"", 
             "Chris Collinsworth: \"It's like watching a superhero in cleats!\""),
            (f"Al Michaels: \"St-Laurent finds an opening... OH MY GOD he LEVELS MOSLEY and rushes for {yards} yards!!\"", 
             "Chris Collinsworth: \"Ladies and gentlemen, fasten your seatbelts and don't get in the way of a Bulldozer...\""),
            (f"Al Michaels: \"Jackson keeps it... and he's off for {yards} yards.\"", 
             "Chris Collinsworth: \"Al, are we watching a football game or a magic show?!\""),
            (f"Al Michaels: \"St-Laurent with a cut... and he's loose for {yards} yards.\"", 
             "Chris Collinsworth: \"I've got goosebumps, Al. Actual goosebumps!\""),
            (f"Al Michaels: \"Flowers on the reverse... he turns the corner...HES GOT TONS OF ROOM!! Taken down after {yards} yards!!\"", 
             "Chris Collinsworth: \"This is just video game stuff! Unbelievable!\""),
            (f"Al Michaels: \"Simon St-Laurent breaks through... and he's gone for {yards} yards.\"", 
             "Chris Collinsworth: \"It's like he's got a turbo button!\""),
            (f"Al Michaels: \"St-Laurent, with the ball... and that's a {yards}-yard burst.\"", 
             "Chris Collinsworth: \"He's carving up this defense like a Thanksgiving turkey!\""),
            (f"Al Michaels: \"St-Laurent takes it... FINDS THE GAP AND BURSTS FOR {yards} YARDS!\"", 
             "Chris Collinsworth: \"He's a cheat code, Al. A human cheat code.\""),
            (f"Al Michaels: \"The handoff to St-Laurent... and he's off to the races for {yards} yards.\"", 
             "Chris Collinsworth: \"I can't believe what I'm seeing. This is extraordinary!\""),
            (f"Al Michaels: \"Simon St-Laurent gets the handoff... and that's a mammoth {yards}-yard run.\"", 
             "Chris Collinsworth: \"He's not human. He can't be!\"")
        ]
    
    return choice(comments)


def snap_count():
    comments = [
        # Existing Snap Counts
        ("Set Hutt... Hutt!"),
        ("Blue 42... Blue 42... Hutt!"),
        ("Al Michaels: 'The game clock getting low.... 4..3...2...' *Hutt*"),
        ("OMAHA OMAHA..... Set Hutt... HUTT.... HUTT!!!!!"),
        ("Set Hutt... Hutt!"),
        ("Set Hutt!"),
        ("Set Hutt... Hutt!"),
        ("Set Hutt... Hutt!"),
        ("Set Hutt... Hutt!"),
        ("Set Hutt... Hutt!"),
        ("Green 19, Green 19... Hutt!"),
        ("Kill, Kill, Kill... Hutt!"),
        ("Tango Charlie, Tango Charlie... Hutt!"),
        ("Black 5-0, Black 5-0... Hutt!"),
        ("Al Michaels: 'Clock ticking down... 3...2...1...' *Hutt!*"),
        ("Alert! Alert!... Hutt!"),
        ("Canary! Canary!... Hutt!"),
        ("Easy! Easy!... Hutt!"),
        ("*Hutt!*"),
        ("Turbo! Turbo! Set... Hutt!"),

        # New Combined-Style Snap Counts
        ("Green 19, Set Hutt... OMAHA... Hutt!"),
        ("Blue 42, Kill, Kill... Hutt!"),
        ("Al Michaels: 'Clock's ticking... 5...4...' *Tango Charlie, Hutt!*"),
        ("Black 5-0... Alert! Alert!... Hutt!"),
        ("Easy! Easy!... Set Hutt... Hutt!"),
        
        ("Turbo! Blue 42... Hutt!"),
        ("Kill, Kill... Canary! Hutt!"),
        ("Al Michaels: 'Down to the wire... 2...1...' *Set Hutt, Black 5-0... Hutt!*"),
        ("Alert! Alert!... Turbo!... Hutt!")
    ]
    return choice(comments)

def jets_field_goal_higher_value(current_position):  # Justin St-Laurent Field Goal Jets
    adjusted_position = current_position + 17  # Temporary variable for adjusted position


    comments = [
        (f"|  Al Michaels: \"Justin St-Laurent from {adjusted_position} yards... and he nails it!\"",
         "|  Chris Collinsworth: \"Like brother, like brother. He's just as clutch!\""),
        (f"|  Al Michaels: \"J. St-Laurent lines it up from {adjusted_position}... and it's perfect!\"",
         "|  Chris Collinsworth: \"He's showing his brother how it's done!\""),
        (f"|  Al Michaels: \"J. St-Laurent sets and kicks from {adjusted_position}... right down the middle!\"",
         "|  Chris Collinsworth: \"It runs in the family, Al.\""),
        (f"|  Al Michaels: \"J. St-Laurent's attempt from {adjusted_position}... and it's good!\"",
         "|  Chris Collinsworth: \"Like clockwork, just automatic.\""),
        (f"|  Al Michaels: \"St-Laurent from {adjusted_position} yards... and the Jets are on the board!\"",
         "|  Chris Collinsworth: \"He's a scoring machine.\""),
        (f"|  Al Michaels: \"And the kick from {adjusted_position} is up... and it's another gem!\"",
         "|  Chris Collinsworth: \"He's keeping the Jets in this one.\""),
        (f"|  Al Michaels: \"St-Laurent sets up for {adjusted_position} yards... and it's three more for the Jets!\"",
         "|  Chris Collinsworth: \"You can't underestimate the value of a good kicker.\""),
        (f"|  Al Michaels: \"St-Laurent from {adjusted_position}... and the crowd is silenced!\"",
         "|  Chris Collinsworth: \"He loves playing the villain.\""),
        (f"|  Al Michaels: \"St-Laurent for {adjusted_position} yards... and he delivers!\"",
         "|  Chris Collinsworth: \"As reliable as they come.\""),
        (f"|  Al Michaels: \"Here's St-Laurent from {adjusted_position}... and it's good!\"",
         "|  Chris Collinsworth: \"Precision, Al, pure precision.\""),
        (f"|  Al Michaels: \"J. St-Laurent sets, kicks from {adjusted_position}... and it's a beauty!\"",
         "|  Chris Collinsworth: \"Just another day at the office for him.\""),
        (f"|  Al Michaels: \"St-Laurent with a {adjusted_position}-yard attempt... and it's good!\"",
         "|  Chris Collinsworth: \"He's making a name for himself today.\""),
        (f"|  Al Michaels: \"From {adjusted_position} yards out, St-Laurent... drills it!\"",
         "|  Chris Collinsworth: \"He's a true competitor.\""),
        (f"|  Al Michaels: \"St-Laurent lines up for a {adjusted_position}-yard kick... and extends the Jets' lead!\"",
         "|  Chris Collinsworth: \"He's a game-changer, no doubt about it.\""),
        (f"|  Al Michaels: \"St-Laurent's kick from {adjusted_position} is up... and it's a bullseye!\"",
         "|  Chris Collinsworth: \"He's got nerves of steel.\""),
        (f"|  Al Michaels: \"Here's St-Laurent from {adjusted_position} yards... and he doesn't disappoint!\"",
         "|  Chris Collinsworth: \"He's got the leg of a champion.\""),
        (f"|  Al Michaels: \"St-Laurent with a {adjusted_position}-yard attempt... and it's as good as gold!\"",
         "|  Chris Collinsworth: \"He's got a leg like a howitzer.\""),
        (f"|  Al Michaels: \"And St-Laurent from {adjusted_position}... makes it look easy!\"",
         "|  Chris Collinsworth: \"Effortless, just effortless.\""),
        (f"|  Al Michaels: \"St-Laurent lines up for a {adjusted_position}-yard field goal... and it's money!\"",
         "|  Chris Collinsworth: \"He's worth every penny they pay him, Al.\""),
        (f"|  Al Michaels: \"St-Laurent's {adjusted_position}-yard attempt is up... and it's another one for the books!\"",
         "|  Chris Collinsworth: \"This guy is clutch.\"")
    ]
    return choice(comments)


def user_field_goal_higher_value(current_position):  # Justin Tucker Field Goal Ravens
    adjusted_position = current_position + 17  # Temporary variable for adjusted position

    comments = [
        (f"|  Al Michaels: \"Justin Tucker from {adjusted_position} yards... it's good!\"",
         "|  Chris Collinsworth: \"Tucker's leg is a national treasure, Al!\""),
        (f"|  Al Michaels: \"Tucker lines up from {adjusted_position}, the kick is up, and it splits the uprights!\"",
         "|  Chris Collinsworth: \"Automatic. That's the only word for Tucker!\""),
        # Added Lines
        (f"|  Al Michaels: \"Tucker aims, fires, and... {adjusted_position}-yarder is good!\"",
         "|  Chris Collinsworth: \"Is there anyone more reliable in the NFL?\""),
        (f"|  Al Michaels: \"Tucker from {adjusted_position} yards... You can put it on the board!\"",
         "|  Chris Collinsworth: \"Unbelievable consistency.\""),
        (f"|  Al Michaels: \"Here comes Tucker for a {adjusted_position}-yard attempt... Wow! Another one!\"",
         "|  Chris Collinsworth: \"What a weapon to have on your team.\""),
        (f"|  Al Michaels: \"Tucker from {adjusted_position}... and it's right down Main Street!\"",
         "|  Chris Collinsworth: \"Money. Every. Single. Time.\""),
        (f"|  Al Michaels: \"Tucker sets up from {adjusted_position} yards... and the Ravens add three more!\"",
         "|  Chris Collinsworth: \"This guy is a scoring machine.\""),
        (f"|  Al Michaels: \"From {adjusted_position} yards out, Tucker... drills it!\"",
         "|  Chris Collinsworth: \"He's a true pro's pro.\""),
        (f"|  Al Michaels: \"Tucker from {adjusted_position}... and the crowd goes wild!\"",
         "|  Chris Collinsworth: \"He's the hero Baltimore deserves.\""),
        (f"|  Al Michaels: \"Tucker sets, kicks from {adjusted_position}... and it's another masterpiece!\"",
         "|  Chris Collinsworth: \"He's painting a Picasso with his leg.\""),
        (f"|  Al Michaels: \"And Tucker from {adjusted_position}... as good as gold!\"",
         "|  Chris Collinsworth: \"He must have a GPS in that foot.\""),
        (f"|  Al Michaels: \"Tucker's kick from {adjusted_position} is up... and it's a beauty!\"",
         "|  Chris Collinsworth: \"He makes it look so easy.\""),
        (f"|  Al Michaels: \"Tucker lines up for a {adjusted_position}-yard kick... and the Ravens extend their lead!\"",
         "|  Chris Collinsworth: \"He's worth every penny they pay him, Al.\""),
        (f"|  Al Michaels: \"Here's Tucker from {adjusted_position} yards... and he delivers once again!\"",
         "|  Chris Collinsworth: \"He's got the leg of a champion.\""),
        (f"|  Al Michaels: \"Tucker from {adjusted_position} yards... and it's another one for the record books!\"",
         "|  Chris Collinsworth: \"Future Hall of Famer, no doubt.\""),
        (f"|  Al Michaels: \"Tucker with a {adjusted_position}-yard attempt... and it's good from downtown!\"",
         "|  Chris Collinsworth: \"I don't think this guy ever misses.\"")
    ]
    return choice(comments)

def gain_touchdown(yards, suit,):
    if suit in ['D', 'S']:  # Pass plays for touchdowns
        comments = [
            (f"Al Michaels: \"Lamar Jackson drops back, fires deep... Mark Andrews is open in the end zone! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"What a pitch and catch, just beautiful execution.\""),
            (f"Al Michaels: \"Jackson in the pocket, throws a dart to OBJ... He's got it! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"OBJ showing he's still got that magic.\""),
            (f"Al Michaels: \"Jackson finds Zay Flowers in the corner... TOUCHDOWN Ravens from {yards} yards out!\"",
             "Chris Collinsworth: \"Flowers continues to impress, the rookie has some serious skills.\""),
            (f"Al Michaels: \"Jackson with a laser to Torrey Smith... and he's in! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Smith's hands are just as reliable as they come.\""),
            (f"Al Michaels: \"Lamar fires it to The Bulldozer in the flat, who runs it in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Simon St-Laurent can do it all, can't he?\""),
            (f"Al Michaels: \"Jackson airs it out to OBJ for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"You can never count OBJ out, what a play.\""),
            (f"Al Michaels: \"Lamar Jackson, deep drop, fires it to Zay Flowers... He's got it! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"The rookie is just electric, Al.\""),
            (f"Al Michaels: \"Jackson to The Bulldozer, who breaks a tackle and gets in! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's why they call him The Bulldozer, just unstoppable.\""),
            (f"Al Michaels: \"Jackson connects with Mark Andrews in the end zone! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Andrews is just Mr. Reliable for Lamar.\""),
            (f"Al Michaels: \"Lamar Jackson with a bullet to Bateman... {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Veteran move by Bateman to find the open space.\""),
            (f"Al Michaels: \"Lamar Jackson scrambles, looks desperate... fires off balance to Mark Andrews! Caught in the end zone for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's a play only a few can make. Remarkable.\""),
            (f"Al Michaels: \"Jackson under pressure, rolls out, launches it to OBJ... One-handed catch! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"OBJ just defies gravity, doesn't he?\""),
            (f"Al Michaels: \"Bad snap! Jackson recovers, evades the sack, finds Zay Flowers in the back of the end zone... {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's a rookie making a veteran play right there.\""),
            (f"Al Michaels: \"Jackson to Bateman... Tipped! But Bateman catches it on the rebound for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"You've got to be kidding me, what concentration by the third year wide out from Minnesota.\""),
            (f"Al Michaels: \"Lamar in the shotgun, looks left, no one open... reverses field, throws across his body to The Bulldozer! Dives in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"St-Laurent shows off his athleticism, simply remarkable.\""),
            (f"Al Michaels: \"Jackson airs it out to OBJ, who's double covered... He jumps over both for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"OBJ is just a highlight reel in cleats.\""),
            (f"Al Michaels: \"Lamar back to pass, flushed out of the pocket, he's going to run... No, he throws last second to Zay Flowers! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Jackson had everyone fooled, even me!\""),
            (f"Al Michaels: \"Jackson looks, pumps, goes deep to The Bulldozer... who makes a spinning catch for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Simon St-Laurent is just a different breed.\""),
            (f"Al Michaels: \"Jackson with a quick slant to Mark Andrews who hurdles a falling Revis and gets in! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Andrews isn't just a possession receiver, folks.\""),
            (f"Al Michaels: \"Lamar drops back, throws a fade to Torrey Smith... who catches it with his fingertips for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's a catch not many can make. Incredible.\""),
            (f"Al Michaels: \"St-Laurent takes the snap in the wildcat, fakes the keep, and throws to a wide-open Mark Andrews for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Simon showing off his arm, too! What can't he do?\"")
        ]
        
    else:  # Run plays for touchdowns
        comments = [
            (f"Al Michaels: \"'The Bulldozer' takes the handoff, breaks free... {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Simon St-Laurent is just a force of nature.\""),
            (f"Al Michaels: \"Lamar Jackson keeps it himself, finds an opening... {yards}-yard TOUCHDOWN RUN!\"",
             "Chris Collinsworth: \"Lamar's speed is just a game changer.\""),
            (f"Al Michaels: \"The Bulldozer, with the carry... He's in! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"What power, what awareness, what a drive by this young superstar!\""),
            (f"Al Michaels: \"The Bulldozer takes the pitch, turns the corner... {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"A great change of pace and patience to let the guard pull by St-Laurent there.\""),
            (f"Al Michaels: \"The Bulldozer takes the handoff, finds a gap... TOUCHDOWN Ravens from {yards} yards out!\"",
             "Chris Collinsworth: \"He's not just a bulldozer, he's a freight train!\""),
            (f"Al Michaels: \"Jackson fakes the handoff, keeps it... and he's in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"The defense just can't account for his speed.\""),
            (f"Al Michaels: \"Handoff to St-Laurent, who powers his way in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"You just can't bring him down, Al.\""),
            (f"Al Michaels: \"St-Laurent with a quick cut and he's in! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"The Bulldozer showing he can be elusive too.\""),
            (f"Al Michaels: \"St-Laurent takes the toss, breaks a tackle... He's in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Simon's just got a nose for the end zone.\""),
            (f"Al Michaels: \"Lamar Jackson with a QB draw... He's got room! {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"It's like trying to catch smoke, Al.\""),
            (f"Al Michaels: \"'The Bulldozer' takes the handoff, gets stuffed at the line... but he keeps his legs moving! Breaks free for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's sheer willpower.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent with a wildcat snap, and takes it himself for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"Is there anything he can't do?\""),
            (f"Al Michaels: \" Lamar with the toss to the Bulldozer who has no space. It's a reverse! The Bulldozer hands it off to Zay Flowers who speeds in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"What a play call, they had everyone fooled.\""),
            ("Al Michaels: \"Lamar fakes the handoff to Mitchell and Flips it to St-Laurent on the shovel and HE HURDLES MOSLEY! Still going!! AND. HE. IS. IN!!!!\"",
             f"Chris Collinsworth: \"What did we just witness, Al? Mosley is 6'3\", 250 Pounds and St-Laurent clears him with space THEN goes for {yards} and the score.\""),
            (f"Al Michaels: \"St-Laurent takes the toss,  he's going to be tackled for a loss... but he pitches it back to Lamar! Jackson takes it in for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's just backyard football, Al.\""),
            (f"Al Michaels: \"Lamar with the QB draw, splits defenders, dives and flips into the end zone for a {yards}-yard TOUCHDOWN!\"",
             "Chris Collinsworth: \"That's just athleticism you can't teach.\"")
        ]
    return choice(comments)

def gain_yards_commentary(yards, suit): # Ravens yards gained
    if suit in ['D', 'S']:  # Pass plays
        comments = [
            # Existing lines
            (f"Al Michaels: \"Lamar Jackson drops back and fires a {yards}-yard bullet to the Bulldozer as he steps out of bounds!\"",
             "Chris Collinsworth: \"What an arm! That ball was right on the money.\""),
            (f"Al Michaels: \"Lamar Jackson Drops back... and finds Mark Andrews for {yards}!\"",
             "Chris Collinsworth: \"Andrews has such reliable hands. That was a great catch.\""),
            (f"Al Michaels: \"Jackson with a dart to OBJ for {yards} yards!\"",
             "Chris Collinsworth: \"OBJ still has it doesn't!\""),
            (f"Al Michaels: \"Lamar Jackson connects with Zay Flowers for {yards} yards!\"",
             "Chris Collinsworth: \"I tell you Al, That rookie has some wheels, doesn't he?\""),
            (f"Al Michaels: \"Jackson with a completion to OBJ, gaining {yards} yards!\"",
             "Chris Collinsworth: \"It can be that simple. Simple read and fire to open guy.\""),
            (f"Al Michaels: \"Lamar Jackson airs it out to Zay Flowers for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"Zay Flowers gets held off the line but still able to make the catch!\""),
            (f"Al Michaels: \"Lamar to the Bulldozer, HE MAKES A MAN MISS! {yards} yards. What an effort there by St-Laurent!\"",
             "Chris Collinsworth: \"St-Laurent can do it all, run, block, and catch.\""),
            (f"Al Michaels: \"Jackson to Andrews for {yards} yards!\"",
             "Chris Collinsworth: \"Andrews and Lamar have such a great connection.\""),
            (f"Al Michaels: \"Jackson drops back and hits Torrey Smith on the slant for a gain of {yards}!\"",
             "Chris Collinsworth: \"Smith's route running is just so crisp.\""),
            (f"Al Michaels: \"What a catch for Zay Flowers! The Rookie's incredible grab goes for {yards}!\"",
             "Chris Collinsworth: \"Flowers continues to impress. He's just so fast, Al.\""),
            (f"Al Michaels: \"Lamar drops back, finds The Bulldozer on a wheel route and off he goes for {yards} yards!\"",
             "Chris Collinsworth: \"Revis ALMOST gets Simon in the back field but he won't go down easy 1 on 1.\""),
            (f"Al Michaels: \"Jackson connects with Torrey Smith on for {yards} yards!\"",
             "Chris Collinsworth: \"Smith is just so reliable in clutch situations.\""),
            (f"Al Michaels: \"Lamar Jackson with a screen pass to Mitchell for {yards} yards!\"",
             "Chris Collinsworth: \"Keaton the Rookie UDFA knows how to get those Yards After Contact.\""),
            (f"Al Michaels: \"Zay Flowers beats Sauce off the line and gains {yards} yards!\"",
             "Chris Collinsworth: \"Flowers has that explosive first step and watch him burst out of his break.\""),
            (f"Al Michaels: \"Jackson finds St-Laurent in the flats on the quick out and he burst upfield for {yards}!\"",
             "Chris Collinsworth: \" What are you supposed to do there? How do you defend that? Simon is just so hard to bring down.\""),
            (f"Al Michaels: \"Lamar Jackson finds Torrey Smith for a {yards}-yard gain, with tight coverage from Revis!\"",
             "Chris Collinsworth: \"Revis was right there, but Smith just made an incredible catch.\""),
            (f"Al Michaels: \"Jackson threads the needle to Zay Flowers on a go route, beating Sauce Gardner for {yards} yards!\"",
             "Chris Collinsworth: \"Flowers just burned Gardner on that one. What a catch!\""),
            (f"Al Michaels: \"Lamar hits Simon 'The Bulldozer' St-Laurent on a hitch route for {yards} yards, with Quincy Williams in perfect position to make a play.\"",
             "Chris Collinsworth: \"Williams was in position, but Simon just plucked that ball out of the air.\""),
            (f"Al Michaels: \"Jackson drops back.. HERE COMES PRESSURE OFF THE EDGE, Lamar gets out and fires to St-Laurent on the wheel route for {yards} yards!\"",
             "Chris Collinsworth: \"Jackson made Williams miss THEN turned it into a big gain. Just Amazing stuff from Lamar.\""),
            (f"Al Michaels: \"Lamar Jackson fires a dart to Zay Flowers on the out route, picking up {yards} yards on Antonio Cromartie.\"",
             "Chris Collinsworth: \"Flowers is just too quick for Cromartie on that one.\""),
            (f"Al Michaels: \"Lamar Jackson with a shovel pass to 'The Bulldozer' for {yards} yards!\"",
             "Chris Collinsworth: \"Simon just powered through the defense like a hot knife through butter.\""),
            (f"Al Michaels: \"Lamar finds St-Laurent wide open on a seam route for a gain of {yards} yards!\"",
             "Chris Collinsworth: \"Simon just found that soft spot in the zone and exploited it.\""),
            (f"Al Michaels: \"Lamar with a quick slant to Zay Flowers for {yards} yards!\"",
             "Chris Collinsworth: \"Flowers just has that knack for getting open when you need him.\""),
            (f"Al Michaels: \"Jackson, No one open, finds Mitchell on the check down for {yards} yards!\"",
             "Chris Collinsworth: \"You can never underestimate the value of a reliable running back in the passing game.\""),
            (f"Al Michaels: \"Lamar Jackson with a fade route to Torrey Smith! That's {yards} yards!\"",
             "Chris Collinsworth: \"Wow, Smith just went up and got that ball at its highest point. Incredible.\""),
            (f"Al Michaels: \"Jackson with a screen to 'The Bulldozer' St-Laurent, and he rumbles for {yards} yards!\"",
             "Chris Collinsworth: \"Simon just makes defenders look silly trying to bring him down.\""),
            (f"Al Michaels: \"Lamar with a quick out to Zay Flowers who turns it upfield for {yards} yards!\"",
             "Chris Collinsworth: \"Flowers just has that elite speed to turn a small play into a big gain.\""),
            (f"Al Michaels: \"Jackson hits Mitchell on a swing pass and he turns it into a gain of {yards} yards!\"",
             "Chris Collinsworth: \"Keaton Mitchell, just so versatile. He can do it all.\""),
            (f"Al Michaels: \"Jackson finds 'The Bulldozer' St-Laurent on a drag route for {yards} yards!\"",
            "Chris Collinsworth: \"You just can't bring Simon down with arm tackles. You need the whole defense.\""),
            (f"Al Michaels: \"Lamar Jackson with a pinpoint back-shoulder throw to Rashad Bateman for {yards} yards!\"",
            "Chris Collinsworth: \"Bateman just has that veteran savvy to make those difficult catches look easy.\""),
            (f"Al Michaels: \"Lamar Jackson finds Mark Andrews  for {yards} yards through the air.\"",
             "Chris Collinsworth: \"Andrews' size and athleticism make him a matchup nightmare for defenses.\""),
            (f"Al Michaels: \"Jackson launches it deep to Odell Beckham Jr., who makes an acrobatic catch for {yards} yards!\"",
             "Chris Collinsworth: \"Beckham's catching ability is simply exceptional.\""),
            (f"Al Michaels: \"Lamar Jackson connects with Simon 'The Bulldozer' St-Laurent for a {yards}-yard gain, breaking tackles along the way!\"",
             "Chris Collinsworth: \"St-Laurent's determination and strength were on full display there.\""),
            (f"Al Michaels: \"Jackson throws a quick screen to Zay Flowers, who turns on the jets for {yards} yards!\"",
             "Chris Collinsworth: \"Flowers' speed is a game-changer.\""),
            (f"Al Michaels: \"Lamar Jackson finds Torrey Smith in the slot for a {yards} yard pickup, showcasing his route-running skills!\"",
             "Chris Collinsworth: \"Smith's precise routes make him a quarterback's best friend.\""),
            (f"Al Michaels: \"Jackson fires a missile to Odell Beckham Jr. on a slant route, gaining {yards} yards!\"",
             "Chris Collinsworth: \"Beckham's ability to create separation on routes is second to none.\""),
            (f"Al Michaels: \"Lamar Jackson connects with Simon 'The Bulldozer' St-Laurent on a crossing route, and he bulldozes his way for {yards} yards!\"",
             "Chris Collinsworth: \"St-Laurent is aptly named; he's like a wrecking ball on the field.\""),
            (f"Al Michaels: \"Jackson drops back, scans the field, and hits Mark Andrews in stride for a {yards}-yard completion!\"",
             "Chris Collinsworth: \"Andrews' reliability in the passing game is a huge asset for this offense.\""),
            (f"Al Michaels: \"Lamar Jackson delivers a perfect pass to Zay Flowers on a comeback route, gaining {yards} yards!\"",
             "Chris Collinsworth: \"Flowers' ability to create separation with his cuts is impressive.\""),
            (f"Al Michaels: \"Jackson finds Simon 'The Bulldozer' St-Laurent in the flat, and he rumbles for {yards} yards, dragging defenders with him!\"",
             "Chris Collinsworth: \"It takes a village to bring down St-Laurent.\""),
            (f"Al Michaels: \"Lamar Jackson fires a strike to Odell Beckham Jr. on an in-breaking route, picking up {yards} yards!\"",
             "Chris Collinsworth: \"Beckham's route-running precision is on full display today.\""),
            (f"Al Michaels: \"Jackson throws a quick slant to Rashad Bateman, who turns it into a {yards}-yard gain with his after-the-catch ability!\"",
             "Chris Collinsworth: \"Bateman knows how to create yards after the catch.\""),
            (f"Al Michaels: \"Lamar Jackson connects with Mark Andrews on a deep post route for a {yards}-yard gain, threading the needle!\"",
             "Chris Collinsworth: \"Andrews' catch radius is a quarterback's dream.\""),
            (f"Al Michaels: \"Jackson checks down to 'The Bulldozer' in the flats, and he plows through the Jets D! {yards} on the play!\"",
             "Chris Collinsworth: \"St-Laurent is unstoppable when he gets going.\""),

            (f"Al Michaels: \"Lamar Jackson connects with Torrey Smith for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"Smith is a dependable target for Jackson.\""),
            (f"Al Michaels: \"Jackson fires a pass to Mark Andrews, who picks up {yards} yards!\"",
             "Chris Collinsworth: \"He is a matchup nightmare for defenses.\""),
            (f"Al Michaels: \"Lamar Jackson finds Zay Flowers for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"Flowers' is a great story isn't he?.\""),
            (f"Al Michaels: \"Jackson connects with Simon 'The Bulldozer' St-Laurent for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"St-Laurent is tough to bring down after the catch.\""),
            (f"Al Michaels: \"Lamar Jackson with a precision pass to Odell Beckham Jr. for {yards} yards!\"",
             "Chris Collinsworth: \"Beckham Jr. showing off his route-running skills.\""),
            (f"Al Michaels: \"Jackson threads the needle to Torrey Smith, gaining {yards} yards!\"",
             "Chris Collinsworth: \"Smith's hands are as reliable as they come.\""),
            (f"Al Michaels: \"Lamar Jackson hits Mark Andrews in the seam for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"Andrews knows how to find the soft spots between the linebackers.\""),
            (f"Al Michaels: \"Jackson's pass to Zay Flowers goes for {yards} yards!\"",
             "Chris Collinsworth: \"Flowers' agility makes him a nightmare for defenders.\""),
            (f"Al Michaels: \"Lamar Jackson finds'The Bulldozer' on a crossing route for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"St-Laurent's physicality is on full display on that one.\""),
            (f"Al Michaels: \"Jackson delivers a strike to Odell Beckham Jr., picking up {yards} yards!\"",
             "Chris Collinsworth: \"Beckham Jr. with another highlight-reel catch.\""),
            (f"Al Michaels: \"Lamar Jackson connects with Torrey Smith for a {yards}-yard gain in tight coverage!\"",
             "Chris Collinsworth: \"Smith's concentration is off the charts.\""),
            (f"Al Michaels: \"Jackson's pass to Mark Andrews goes for {yards} yards, moving the chains!\"",
             "Chris Collinsworth: \"Andrews is a key target in crucial situations.\""),
            (f"Al Michaels: \"Lamar Jackson finds Zay Flowers on an out route, gaining {yards} yards!\"",
             "Chris Collinsworth: \"Flowers' footwork is exceptional.\""),
            (f"Al Michaels: \"Jackson fires a pass to Simon 'The Bulldozer' St-Laurent, who bulldozes his way for {yards} yards!\"",
             "Chris Collinsworth: \"St-Laurent is a force to be reckoned with.\"")
        ]

        
    else:  # Run plays
        comments = [
            # Existing lines
            (f"Al Michaels: \"'The Bulldozer' takes the handoff and powers through for {yards} yards\"",
            "Chris Collinsworth: \"You can't arm-tackle The Bulldozer!\""),
            (f"Al Michaels: \"Lamar Jackson drops back, good protection... he keeps it himself and rushes for {yards} yards!\"",
            "Chris Collinsworth: \"Jackson's speed is just incredible.\""),
            (f"Al Michaels: \"A quick handoff to St-Laurent gains {yards} yards!\"",
            "Chris Collinsworth: \"I tell you Al, Simon sure knows how to read his o-line. Watch him patiently let the play develop before attacking the gap.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent breaks a tackle and surges for {yards} yards!\"",
            "Chris Collinsworth: \"He's a one-man wrecking crew!\""),
            (f"Al Michaels: \"St-Laurent shakes off Qincy Williams and runs off for {yards} yards!\"",
            "Chris Collinsworth: \"His agility, strength AND speed is just out of this world.\""),
            (f"Al Michaels: \"St-Laurent takes the handoff and finds daylight for {yards} yards!\"",
            "Chris Collinsworth: \"He makes it look easy, Al.\""),
            (f"Al Michaels: \"Jackson drops back, here comes the blitz.... He keeps it! HES GOT SPACE! Gains {yards} yards!\"",
            "Chris Collinsworth: \"It's like trying to catch smoke with your bare hands.\""),
            (f"Al Michaels: \"The Bulldozer powers through the line for {yards} yards!\"",
            "Chris Collinsworth: \"He's not just a bulldozer, he's a steamroller!\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent with the carry for {yards} yards!\"",
            "Chris Collinsworth: \"He just floats when he plows through the defense.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the pitch and rumbles for {yards} yards!\"",
            "Chris Collinsworth: \"A great change of pace from Mitchell.\""),
            (f"Al Michaels: \"The Bulldozer breaks a tackle and powers his way for {yards} yards!\"",
            "Chris Collinsworth: \"You need a whole team to bring him down.\""),
            (f"Al Michaels: \"Keaton Mitchell with the run picking up {yards} yards!\"",
            "Chris Collinsworth: \"A hard-nosed run from Mitchell.\""),
            (f"Al Michaels: \"Simon St-Laurent takes a toss and is met by 3 Jet Def.... OH St-Laurent is still going!! He Breaks the tackles and gains {yards}!\"",
            "Chris Collinsworth: \"Wow. What. A. Run. What do you say after a play like that Al?\""),
            (f"Al Michaels: \"A draw play to The Bulldozer, and he gains {yards} yards!\"",
            "Chris Collinsworth: \"Perfect play call at the perfect time.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent in the wildcat, and he rushes for {yards} yards!\"",
            "Chris Collinsworth: \"The Bulldozer can do it all.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent takes a pitch from Lamar and picks up {yards} yards, out running Quincy Williams.\"",
            "Chris Collinsworth: \"Bulldozers aren't known for their speed. This guy is an F1 car in a Bulldozer Body.\""),
            (f"Al Michaels: \"Keaton Mitchell takes a handoff and powers through for {yards} yards, avoiding the blitzing Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams was in the backfield, but Mitchell just powered through.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent gets the ball on a toss and gains {yards} yards.\"",
             "Chris Collinsworth: \"Gardner had the angle but couldn't make the stop, St-Laurent is a nightmare 1 on 1.\""),
            (f"Al Michaels: \"St-Laurent takes a dive and picks up {yards} yards, breaking a tackle from Derrell Revis.\"",
            "Chris Collinsworth: \"A 'Bulldozer made a Hall of Famer miss. That's impressive.\""),
            (f"Al Michaels: \"The Bulldozer gets the handoff and powers through a tackle from Antonio Cromartie for {yards} yards.\"",
            "Chris Collinsworth: \"Cromartie is a good tackler, but Simon is just too strong.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent takes the inside handoff and bursts through the hole for {yards} yards!\"",
            "Chris Collinsworth: \"He found that crease and exploded through it.\""),
            (f"Al Michaels: \"Direct snap to Simon St-Laurent, and he plows forward for {yards} yards!\"",
            "Chris Collinsworth: \"The Bulldozer just can't be stopped.\""),
            (f"Al Michaels: \"St-Laurent with a cutback, dodges a tackler, and picks up {yards} yards!\"",
            "Chris Collinsworth: \"His vision is just unbelievable.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the counter play and rumbles for {yards} yards!\"",
            "Chris Collinsworth: \"Fantastic play design and execution.\""),
            (f"Al Michaels: \"Simon St-Laurent on the sweep, turns the corner, and gains {yards} yards!\"",
            "Chris Collinsworth: \"He's got the speed to go along with that power.\""),
            (f"Al Michaels: \"St-Laurent takes a delayed handoff and weaves through traffic for {yards} yards!\"",
            "Chris Collinsworth: \"Just when you think you've got him, he finds a way.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent on a zone read, keeps it and gains {yards} yards!\"",
            "Chris Collinsworth: \"That's what makes him so dangerous, his ability to read the defense.\""),
            (f"Al Michaels: \"Keaton Mitchell with a stiff arm and a gain of {yards} yards!\"",
            "Chris Collinsworth: \"That's a grown man's run right there.\""),
            (f"Al Michaels: \"St-Laurent lines up behind Jackson, takes the handoff, and blasts through for {yards} yards!\"",
            "Chris Collinsworth: \"Old school football, and it still works.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent breaks through the line and hurdles a defender for a gain of {yards} yards!\"",
            "Chris Collinsworth: \"He's not just a power back, he's got some finesse too.\""),
            (f"Al Michaels: \"'The Bulldozer' takes the handoff and powers through for {yards} yards!\"",
            "Chris Collinsworth: \"You can't arm-tackle The Bulldozer!\""),
            (f"Al Michaels: \"Lamar Jackson drops back, good protection... he keeps it himself and rushes for {yards} yards!\"",
            "Chris Collinsworth: \"Jackson's speed is just incredible.\""),
            (f"Al Michaels: \"A quick handoff to St-Laurent gains {yards} yards!\"",
            "Chris Collinsworth: \"I tell you Al, Simon sure knows how to read his o-line. Watch him patiently let the play develop before attacking the gap.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent breaks a tackle and surges for {yards} yards!\"",
            "Chris Collinsworth: \"He's a one-man wrecking crew!\""),
            (f"Al Michaels: \"St-Laurent shakes off Quincy Williams and runs off for {yards} yards!\"",
            "Chris Collinsworth: \"His agility, strength, AND speed are just out of this world.\""),
            (f"Al Michaels: \"St-Laurent takes the handoff and finds daylight for {yards} yards!\"",
            "Chris Collinsworth: \"He makes it look easy, Al.\""),
            (f"Al Michaels: \"Jackson drops back, here comes the blitz... He keeps it! HES GOT SPACE! Gains {yards} yards!\"",
            "Chris Collinsworth: \"It's like trying to catch smoke with your bare hands.\""),
            (f"Al Michaels: \"The Bulldozer powers through the line for {yards} yards!\"",
            "Chris Collinsworth: \"He's not just a bulldozer, he's a steamroller!\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent with the carry for {yards} yards!\"",
            "Chris Collinsworth: \"He just floats when he plows through the defense.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the pitch and rumbles for {yards} yards!\"",
            "Chris Collinsworth: \"A great change of pace from Mitchell.\""),
            (f"Al Michaels: \"The Bulldozer breaks a tackle and powers his way for {yards} yards!\"",
            "Chris Collinsworth: \"You need a whole team to bring him down.\""),
            (f"Al Michaels: \"Keaton Mitchell with the run picking up {yards} yards!\"",
            "Chris Collinsworth: \"A hard-nosed run from Mitchell.\""),
            (f"Al Michaels: \"Simon St-Laurent takes a toss and is met by Quinnen Williams... St-Laurent is still going!! Break the tackle and gains {yards} yards!\"",
            "Chris Collinsworth: \"Wow. What. A. Run. What do you say after a play like that Al?\""),
            (f"Al Michaels: \"A draw play to The Bulldozer, and he gains {yards} yards!\"",
            "Chris Collinsworth: \"Perfect play call at the perfect time.\""),
            (f"Al Michaels: \"Lamar Jackson fakes the handoff and keeps it himself, dancing around Revis for {yards} yards!\"",
            "Chris Collinsworth: \"Revis bit hard on that one, and Jackson made him look foolish...\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent takes the pitch, stiff-arms Antonio Cromartie, and gains {yards} yards!\"",
            "Chris Collinsworth: \"Cromartie tried to bring him down with an arm tackle, and it didn't work.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the handoff and runs through a tackle attempt by CJ Mosley for {yards} yards!\"",
            "Chris Collinsworth: \"Mosley had a shot, but Mitchell just shrugged him off.\"")
        ]
 
        
    return choice(comments)


def no_gain_commentary(suit): # Ravens 0 yards gained
    if suit in ['D', 'S']:  # Pass plays Ravens
        comments = [
            # Existing lines with Jets players added
            ("Al Michaels: \"Lamar Jackson's pass falls incomplete, great coverage by Derrell Revis.\"",
            "Chris Collinsworth: \"Revis Island is a tough place to make a catch.\""),
            ("Al Michaels: \"Jackson's pass is batted down at the line by Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams got his big paw on that one.\""),
            ("Al Michaels: \"The pass to Mark Andrews is broken up by Quincy Williams!\"",
            "Chris Collinsworth: \"Williams was all over that play.\""),
            ("Al Michaels: \"Jackson looks for OBJ, but the pass sails out of bounds. Pressure from Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams really forced Lamar into that bad throw.\""),
            ("Al Michaels: \"Lamar tries to hit the Bulldozer, but just out of reach for the star Running Back.\"",
            "Chris Collinsworth: \"Don't see many miss cues between those two.\""),
            ("Al Michaels: \"Jackson to Zay Flowers... Oh! Almost intercepted by Quincy Williams!\"",
            "Chris Collinsworth: \"Williams had a real shot at that one.\""),
            ("Al Michaels: \"Lamar looks for OBJ but it falls incomplete!\"",
            "Chris Collinsworth: \"You can't underestimate Revis, even for a second. Great Coverage there on Odell\""),
            ("Al Michaels: \"Jackson throws to the end zone... Broken up by Gardner!\"",
            "Chris Collinsworth: \"Look at Sauce just fly to the ball! He is making his presence felt today.\""),
            ("Al Michaels: \"Lamar Jackson targets Zay Flowers on the quick slant, but it's well-covered by Sauce Gardner.\"",
            "Chris Collinsworth: \"Gardner was all over him, Al.\""),
            ("Al Michaels: \"Zay and Odell out wide, Lamar drops back, looks for Flowers over the middle and Williams is there to make the play.\"",
            "Chris Collinsworth: \"Quincy read that play like a book.\""),
            ("Al Michaels: \" Lamar looks to Simon in the flats but Antonio Cromartie! meets him for no gain.\"",
            "Chris Collinsworth: \"Cromartie showed great instincts on that play.\""),
            ("Al Michaels: \"Jackson looks for Simon 'The Bulldozer' St-Laurent on the out, incomplete.\"",
            "Chris Collinsworth: \"Revis Island is still a no-fly zone, Al.\""),
            ("Al Michaels: \"Lamar tries to hit Zay Flowers on a deep post and hes got him wide open but it's broken up by Sauce Gardner.\"",
            "Chris Collinsworth: \"Gardner is making his presence felt tonight. Where on Earth did Sauce come from???\""),
            ("Al Michaels: \"Jackson's go route to Torrey Smith is just out of reach, great coverage by Antonio Cromartie.\"",
            "Chris Collinsworth: \"Cromartie used his speed to stay with Smith.\""),
            ("Al Michaels: \"Lamar looks for Simon on the screen, but gets nowhere. Well-defended by Quincy Williams.\"",
            "Chris Collinsworth: \"Quincy read that right away, watch him call screen and head right to St-Laurent.\""),
            (f"Al Michaels: \"Lamar Jackson aims for Zay Flowers, but the ball goes through his hands.\"",
            "Chris Collinsworth: \"Even the best have those moments. Tough break for Flowers.\""),
            (f"Al Michaels: \"Jackson's pass to Simon 'The Bulldozer' St-Laurent is just a bit too high.\"",
            "Chris Collinsworth: \"The Bulldozer is a tough target to miss, but that was a difficult throw.\""),
            (f"Al Michaels: \"Jackson looks for Torrey Smith in the endzone, but it's just out of reach.\"",
            "Chris Collinsworth: \"He had a step, just couldn't connect.\""),
            (f"Al Michaels: \"Pass intended for Mark Andrews is tipped at the line!\"",
            "Chris Collinsworth: \"Big defensive play there. That could've been a first down.\""),
            (f"Al Michaels: \"Lamar throws towards Keaton Mitchell, but it's knocked away by Sauce Gardner.\"",
            "Chris Collinsworth: \"Gardner read that play perfectly.\""),
            (f"Al Michaels: \"Jackson's deep ball to Zay Flowers is just a bit too long.\"",
            "Chris Collinsworth: \"He had him beat, just needed a touch less on that throw.\""),
            (f"Al Michaels: \"Lamar looks for Simon 'The Bulldozer' St-Laurent on the sideline, but the pass is out of bounds.\"",
            "Chris Collinsworth: \"That's a tough throw to make, especially under pressure.\""),
            (f"Al Michaels: \"Jackson's quick slant to Mark Andrews is deflected by Antonio Cromartie.\"",
            "Chris Collinsworth: \"Cromartie still has those quick reflexes.\""),
            (f"Al Michaels: \"Lamar tries to fit it into a tight window to Torrey Smith, but it's broken up by Derrell Revis.\"",
            "Chris Collinsworth: \"Revis isn't giving an inch today.\""),
            (f"Al Michaels: \"Jackson's pass to Simon 'The Bulldozer' St-Laurent is dropped. Looked like an easy catch.\"",
            "Chris Collinsworth: \"You won't see that often. That's a play Simon usually makes.\""),
            ("Al Michaels: \"Lamar Jackson's pass is well-defended by Derrell Revis, no room to make the catch.\"",
             "Chris Collinsworth: \"Revis is like a shadow out there, no separation for the receiver.\""),
            ("Al Michaels: \"Jackson's pass to Mark Andrews is just out of reach, incomplete.\"",
             "Chris Collinsworth: \"Andrews couldn't quite stretch for that one.\""),
            ("Al Michaels: \"The pass to OBJ is off the mark, incomplete. Lamar faced pressure on that one.\"",
             "Chris Collinsworth: \"Lamar had to get rid of it quickly, and it affected the throw.\""),
            ("Al Michaels: \"Lamar tries to hit 'The Bulldozer,' but the pass was too high for him to bring down.\"",
             "Chris Collinsworth: \"That was a tough catch to make, even for a big target like 'The Bulldozer.'\""),
            ("Al Michaels: \"Jackson to Zay Flowers... The pass was low and incomplete.\"",
             "Chris Collinsworth: \"Flowers couldn't scoop that one up.\""),
            ("Al Michaels: \"Lamar's pass is deflected at the line of scrimmage by Quinnen Williams.\"",
             "Chris Collinsworth: \"Williams got a hand on it to disrupt the throw.\""),
            ("Al Michaels: \"Jackson looks for OBJ, but the pass is swatted away by Quincy Williams.\"",
             "Chris Collinsworth: \"Williams timed that perfectly.\""),
            ("Al Michaels: \"Lamar attempts a deep throw, but it's overthrown and out of bounds.\"",
             "Chris Collinsworth: \"That pass had too much on it.\""),
            ("Al Michaels: \"Jackson's pass is well-covered by Sauce Gardner, and it falls incomplete.\"",
             "Chris Collinsworth: \"Gardner had that route locked down.\""),
            ("Al Michaels: \"Lamar looks for Zay Flowers on the quick slant, but the pass is deflected by Sauce Gardner.\"",
             "Chris Collinsworth: \"Gardner's quick reaction disrupted the play.\""),
            ("Al Michaels: \"Jackson targets OBJ, but the pass is broken up by Derrell Revis!\"",
             "Chris Collinsworth: \"Revis is showing why he's one of the best.\""),
            ("Al Michaels: \"Lamar throws under pressure and the pass is incomplete.\"",
             "Chris Collinsworth: \"Pressure from the Jets forced a quick throw.\""),
            ("Al Michaels: \"Jackson attempts a screen pass, but it's read perfectly by Quincy Williams.\"",
             "Chris Collinsworth: \"Williams was all over that screen play.\""),
            ("Al Michaels: \"Lamar's pass is well-defended by the Jets' secondary, and there's no room to complete it.\"",
             "Chris Collinsworth: \"The Jets' coverage was suffocating on that play.\""),
            ("Al Michaels: \"Jackson fires under duress, and the pass is off-target and incomplete.\"",
             "Chris Collinsworth: \"Lamar had to get rid of it quickly due to the pressure.\"")

        ]
 
        
    else:  # Run plays 
        comments = [
            # Existing lines with Jets players added
            ("Al Michaels: \"Simon 'The Bulldozer' St-Laurent is stuffed at the line by Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams just blew up that play.\""),
            ("Al Michaels: \"Lamar Jackson tries to scramble but is tackled by Quincy Williams.\"",
            "Chris Collinsworth: \"Williams had him in his sights.\""),
            ("Al Michaels: \"Keaton Mitchell is met in the backfield by Derrell Revis for no gain.\"",
            "Chris Collinsworth: \"Revis can do more than just cover, he can tackle too.\""),
            ("Al Michaels: \"Simon 'The Bulldozer' St-Laurent is wrapped up by Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams was having none of that.\""),
            ("Al Michaels: \"Lamar keeps it, but is corralled by Quincy Williams for no gain.\"",
            "Chris Collinsworth: \"They read that play perfectly.\""),
            ("Al Michaels: \"The Bulldozer tries to go outside but is taken down by Derrell Revis.\"",
            "Chris Collinsworth: \"Revis gets off the block so easily... The Ravens WR need to block out there Al.\""),
            ("Al Michaels: \"Jackson fakes the handoff but is brought down by Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams is just a force up front.\""),
            ("Al Michaels: \"Lamar hands off to St-Laurent, and he's  tackled by Both Williams'.\"",
            "Chris Collinsworth: \"Q. Williams' are both having a game today.\""),
            ("Al Michaels: \"'Ravens on the End-Around, Flowers is stuffed at the line by Quinnen Williams.\"",
            "Chris Collinsworth: \"Quinnen just dominated the line there THEN chases down the speedster. He really is a star in this Game.\""),
            ("Al Michaels: \"Keaton Mitchell takes the handoff but is met immediately by Williams.\"",
            "Chris Collinsworth: \"Quincy shot out of nowhere to make that stop.\""),
            ("Al Michaels: \"The Ravens try to run behind their pulling guard but is stuffed by Quinnen Williams.\"",
            "Chris Collinsworth: \"The Jets D line is making his presence felt in the middle.\""),
            ("Al Michaels: \"Keaton Mitchell attempts a draw play but gets nowhere, thanks to Derrell Revis.\"",
            "Chris Collinsworth: \"Revis can do it all, can't he?\""),
            ("Al Michaels: \"Mitchell tries to get outside on the pitch but is wrapped up by Cromartie.\"",
            "Chris Collinsworth: \"Cromartie showed great speed to close that down.\""),
            ("Al Michaels: \"Mitchell takes a toss but is met immediately by Sauce Gardner.\"",
            "Chris Collinsworth: \"The jets D just has a nose for the ball.\""),
            ("Al Michaels: \"Mitchell goes for a dive but is stopped by Quinnen AND Quincy Williams.\"",
            "Chris Collinsworth: \"Not much room to run there, Al.\""),
            (f"Al Michaels: \"Keaton Mitchell tries to find a hole but is met by a wall of defenders.\"",
            "Chris Collinsworth: \"No room to run there, Al.\""),
            (f"Al Michaels: \"St-Laurent gets the handoff but is tripped up behind the line by Sauce Gardner.\"",
            "Chris Collinsworth: \"Gardner saw that coming a mile away.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent tries to bounce it outside, but Antonio Cromartie is there to make the stop.\"",
            "Chris Collinsworth: \"Great read by Cromartie to contain the edge.\""),
            (f"Al Michaels: \"Lamar Jackson keeps it on the read-option but is wrapped up by Derrell Revis.\"",
            "Chris Collinsworth: \"Revis still has those instincts, doesn't he?\""),
            (f"Al Michaels: \"St-Laurent takes the pitch but is corralled in the backfield by Quinnen Williams.\"",
            "Chris Collinsworth: \"Williams just destroyed that play.\""),
            (f"Al Michaels: \"Keaton Mitchell gets the handoff and is immediately met by Quincy Williams.\"",
            "Chris Collinsworth: \"Williams was in the backfield in a hurry.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent tries to power through the middle, but he's swarmed by defenders.\"",
            "Chris Collinsworth: \"They knew who was getting the ball.\""),
            (f"Al Michaels: \"Lamar Jackson tries to sneak it but gets no push from the offensive line.\"",
            "Chris Collinsworth: \"The defensive line just won that battle.\""),
            (f"Al Michaels: \"St-Laurent gets the ball on a draw, but Sauce Gardner is there to stop him.\"",
            "Chris Collinsworth: \"Big play by Gardner.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent takes the handoff and is met immediately by Antonio Cromartie.\"",
            "Chris Collinsworth: \"Cromartie shot through like a missile.\""),
            ("Al Michaels: \"Simon 'The Bulldozer' St-Laurent is wrapped up at the line of scrimmage.\"",
            "Chris Collinsworth: \"The Jets' defense stood tall on that play.\""),
            ("Al Michaels: \"Lamar Jackson keeps it, but he's immediately brought down with no gain.\"",
            "Chris Collinsworth: \"The Jets' defense was ready for that option play.\""),
            ("Al Michaels: \"Keaton Mitchell tries to find a hole, but he's met by a wall of defenders for no gain.\"",
            "Chris Collinsworth: \"The Jets' defensive line is holding strong.\""),
            ("Al Michaels: \"Simon 'The Bulldozer' St-Laurent is stuffed in the backfield.\"",
            "Chris Collinsworth: \"The Jets' defenders penetrated the line and made the tackle.\""),
            ("Al Michaels: \"Lamar Jackson fakes the handoff but is tackled behind the line of scrimmage.\"",
            "Chris Collinsworth: \"The Jets' defense read that play perfectly.\""),
            ("Al Michaels: \"The handoff to St-Laurent goes nowhere as he's brought down for no gain.\"",
            "Chris Collinsworth: \"The Jets' defense swarmed to the ball.\""),
            ("Al Michaels: \"Jackson hands off, but there's no room to run as the Jets' defense clogs the lanes.\"",
            "Chris Collinsworth: \"The Jets' front seven is dominating the line of scrimmage.\""),
            ("Al Michaels: \"Simon St-Laurent tries to go outside, but the Jets' defenders close in quickly for no gain.\"",
            "Chris Collinsworth: \"The Jets' defense was disciplined on the edge.\""),
            ("Al Michaels: \"Lamar Jackson keeps it on the read option, but he's met by Quincy Williams with no gain.\"",
            "Chris Collinsworth: \"Williams made a great read and tackle.\""),
            ("Al Michaels: \"The Ravens attempt an end-around, but the Jets' defense is all over it, no gain on the play.\"",
            "Chris Collinsworth: \"The Jets sniffed that one out from the start.\""),
            ("Al Michaels: \"Keaton Mitchell takes the handoff, but he's immediately wrapped up by the Jets' defenders for no gain.\"",
            "Chris Collinsworth: \"No room to run there, the Jets' defense swarmed to the ball.\""),
            ("Al Michaels: \"Simon 'The Bulldozer' St-Laurent is hit at the line of scrimmage and brought down for no gain.\"",
            "Chris Collinsworth: \"The Jets' defenders were in the backfield in a flash.\""),
            ("Al Michaels: \"Lamar Jackson hands off, but the Jets' defense read the play and stopped it for no gain.\"",
            "Chris Collinsworth: \"The Jets' defenders were one step ahead.\""),
            ("Al Michaels: \"Simon St-Laurent tries to cut back, but the Jets' defenders are there to stop him for no gain.\"",
            "Chris Collinsworth: \"The Jets' defense stayed disciplined in pursuit.\""),
            ("Al Michaels: \"Lamar Jackson hands off, but the Jets' defense swarms to the ball and stops it for no gain.\"",
            "Chris Collinsworth: \"The Jets' defenders were relentless on that play.\"")
        ]
                          
        
    return choice(comments)




def loss_yards_commentary(yards, suit): # Ravens lose yards on the play
    if suit in ['D', 'S']:  # Pass plays
        comments = [
            # New lines featuring Jets players
            (f"Al Michaels: \"Lamar Jackson is swarmed by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Williams just bulldozed his way to the QB.\""),
            (f"Al Michaels: \"Jackson tries to escape, but Quincy Williams brings him down, losing {yards} yards.\"",
             "Chris Collinsworth: \"Quincy Williams was just relentless there.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Derrell Revis on a corner blitz! A loss of {yards} yards.\"",
             "Chris Collinsworth: \"Revis showing he's not just a cover guy.\""),
            (f"Al Michaels: \"Jackson's screen pass to The Bulldozer is snuffed out by Quinnen Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Williams read that play like a book.\""),
            (f"Al Michaels: \"Jackson is trapped in the pocket and taken down by Quincy Williams, losing {yards} yards.\"",
             "Chris Collinsworth: \"Jets D is having a standout performance today.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Williams is a game-changer, no doubt about it.\""),
            (f"Al Michaels: \"Jackson tries a screen pass to Keaton Mitchell, but it's blown up by Quincy Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"That's a big-time play from The Jets Defensive Line there...\""),
            (f"Al Michaels: \"Jackson's quick slant to Zay Flowers is sniffed out by Sauce Gardner, resulting in a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Gardner had that diagnosed from the get-go.\""),
            (f"Al Michaels: \"Lamar is pressured and throws it away, but it's intentional grounding! A loss of {yards} yards.\"",
             "Chris Collinsworth: \"That's a spot foul AND loss of down. That one hurts.\""),
            (f"Al Michaels: \"Jackson is flushed out of the pocket and gets tackled by Antonio Cromartie and loses {yards} yards.\"",
             "Chris Collinsworth: \"As soon as Lamar leaves the pocket, the Jets D swarm him. Great defensive play.\""),
            (f"Al Michaels: \"Lamar drops back but is and finds the Bulldozer who is wrapped up by CJ Mosley for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Mosley was just unblockable there. The Ex Raven, making his presence known.\""),
            (f"Al Michaels: \"Jackson tries a quick screen to Torrey Smith, but it's read by Micheal Carter II for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"You can't fool the Jets D like that, Al.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Williams just blew up that play.\""),
            (f"Al Michaels: \"Jackson's screen pass to Torrey Smith loses {yards} yards, thanks to a great read by Quincy Williams.\"",
             "Chris Collinsworth: \"Watch the effort by Williams to get all the way over there and make the TFL!\""),
            (f"Al Michaels: \"Jackson is flushed out of the pocket by Derrell Revis and loses {yards} yards.\"",
             "Chris Collinsworth: \"Ravens O-Line leaving Lamar with no time out there.\""),
            (f"Al Michaels: \"Lamar Jackson is caught in the backfield by Quincy Williams, losing {yards} yards!\"",
            "Chris Collinsworth: \"Williams' speed and pursuit were too much for Jackson.\""),
            (f"Al Michaels: \"Jackson tries to escape, but Jermaine Johnson brings him down for a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Johnson with the sack, he's been a menace in the backfield.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Derrell Revis on the corner blitz, losing {yards} yards.\"",
            "Chris Collinsworth: \"Revis timed that blitz perfectly.\""),
            (f"Al Michaels: \"Jackson is trapped in the pocket and taken down by Johnson for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"The Jets' defense is relentless today.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Quinnen Williams for a loss of {yards} yards! Williams is a force to be reckoned with.\"",
            "Chris Collinsworth: \"Williams is a game-changer in the trenches.\""),
            (f"Al Michaels: \"Jackson tries a screen pass to Keaton Mitchell, but it's blown up by Quincy Williams, resulting in a loss of {yards} yards.\"",
            "Chris Collinsworth: \"That's excellent recognition by Williams to sniff out the screen.\""),
            (f"Al Michaels: \"Lamar Jackson is brought down by Quincy Williams for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams made a textbook tackle there.\""),
            (f"Al Michaels: \"Jackson is taken down by Quinnen Williams, losing {yards} yards on the play.\"",
            "Chris Collinsworth: \"Quinnen Williams is a force to be reckoned with.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Derrell Revis, a loss of {yards} yards on the corner blitz!\"",
            "Chris Collinsworth: \"Revis still has that edge.\""),
            (f"Al Michaels: \"Jackson's pass to Mark Andrews is completed, but Quincy Williams was right there to bring him down behind the line for a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Williams with a quick reaction to stop that play.\""),
            (f"Al Michaels: \"Lamar Jackson is wrapped up by Quinnen Williams, losing {yards} yards on the play!\"",
            "Chris Collinsworth: \"Quinnen Williams showing his strength on that tackle.\""),
            (f"Al Michaels: \"Jackson is sacked by Quincy Williams, losing {yards} yards on the play.\"",
            "Chris Collinsworth: \"Williams is all over the field today.\""),
            (f"Al Michaels: \"Lamar Jackson's screen pass to 'The Bulldozer' is blown up by Quinnen Williams, resulting in a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Williams read that play perfectly.\""),
            (f"Al Michaels: \"Jackson is trapped in the pocket and taken down by Quincy Williams, a loss of {yards} yards on the play.\"",
            "Chris Collinsworth: \"Jets' defense is making a statement today.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Quinnen Williams for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams with another big play.\""),
            (f"Al Michaels: \"Jackson's screen pass to Keaton Mitchell is snuffed out by Quincy Williams, resulting in a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Great recognition by Williams on that play.\""),
            (f"Al Michaels: \"Lamar Jackson is brought down by Derrell Revis, losing {yards} yards on the corner blitz!\"",
            "Chris Collinsworth: \"Revis is a master of his craft.\""),
            (f"Al Michaels: \"Jackson tries to scramble, but Quincy Williams wraps him up for a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Williams is making plays all over the field.\""),
            (f"Al Michaels: \"Lamar Jackson's pass is completed, but Antonio Cromartie is there to tackle the receiver behind the line for a loss of {yards} yards.\"",
            "Chris Collinsworth: \"Cromartie closed in quickly to prevent any yards after catch.\""),
            (f"Al Michaels: \"Jackson is taken down by Jermaine Johnson, losing {yards} yards on the play.\"",
            "Chris Collinsworth: \"Jermaine Johnson with a crucial tackle.\""),
            (f"Al Michaels: \"Lamar Jackson is sacked by Quincy Williams, a loss of {yards} yards on the play.\"",
            "Chris Collinsworth: \"Williams is having a standout game today.\"")

        ]
    else:  # Run plays
        comments = [
            # New lines featuring Jets players
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent is wrapped up by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"The D line just manhandled the offensive line there.\""),
            (f"Al Michaels: \"Lamar Jackson tries to go outside but is corralled by Derrell Revis for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Revis is more than just a cover corner, he can tackle too.\""),
            (f"Al Michaels: \"St-Laurent takes the handoff but is met in the backfield by Quincy Williams, losing {yards} yards.\"",
             "Chris Collinsworth: \"QThese Jets Linebackers are heat-seeking missiles out there.\""),
            (f"Al Michaels: \"Lamar Jackson is caught from behind by Quinnen Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Williams' speed for a big man is astonishing.\""),
            (f"Al Michaels: \"The Bulldozer tries to power through, but he's stopped by Mosley for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Where is the Push from the Ravens O-Line? \""),
            (f"Al Michaels: \"Flowers on the end around and is met in the backfield by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Quinnen is just disruptive.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the pitch and is immediately tackled by Quincy Williams, losing {yards} yards.\"",
             "Chris Collinsworth: \"Jets were all over that play.\""),
            (f"Al Michaels: \"The Bulldozer tries a to run it up the middle but is stopped by Mosley for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"That hole closed immediately, giving Simon no room to run.\""),
            (f"Al Michaels: \"Mitchell takes the handoff and is swarmed by Sauce Gardner for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Sauce is adding some spice to this Jets defense.\""),
            (f"Al Michaels: \"Keaton Mitchell tries a power run but is met by Derrell Revis for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Revis isn't just a cover guy; he can tackle too.\""),
            (f"Al Michaels: \"St-Laurent takes a toss but is wrapped up by Quinnen Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Williams is having a monster game.\""),
            (f"Al Michaels: \"The Bulldozer goes for a draw but is snuffed out by Quincy Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"I mean St-Laurent has no help tonight.\""),
            (f"Al Michaels: \"Keaton Mitchell is tackled in the backfield by Quinnen Williams for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Williams just dominated the line there.\""),
            (f"Al Michaels: \"Keaton Mitchell tries a draw but is met by Quincy Williams for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Williams came out of nowhere.\""),
            (f"Al Michaels: \"The Bulldozer takes a toss but is wrapped up by Derrell Revis for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Revis may be a Hall of Famer in the secondary, but he can tackle too.\""),
            (f"Al Michaels: \"Mitchell is swarmed by Sauce Gardner in the backfield for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Gardner just shot the gap perfectly.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the check down is hit in the backfield by Antonio Cromartie for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Cromartie's still got those quick instincts.\""),
            (f"Al Michaels: \"Simon 'The Bulldozer' St-Laurent is wrapped up by Quinnen Williams for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams just bulldozed through the offensive line.\""),
            (f"Al Michaels: \"Lamar Jackson tries to go outside, but Derrell Revis wraps him up, losing {yards} yards on the play.\"",
            "Chris Collinsworth: \"Revis showing his tackling skills.\""),
            (f"Al Michaels: \"St-Laurent takes the handoff, but Quincy Williams meets him in the backfield, resulting in a loss of {yards} yards.\"",
            "Chris Collinsworth: \"The Jets' linebackers are flying around the field today.\""),
            (f"Al Michaels: \"Lamar Jackson is caught from behind by Quinnen Williams, losing {yards} yards on the play!\"",
            "Chris Collinsworth: \"Quinnen Williams' speed is impressive for a big man.\""),
            (f"Al Michaels: \"The Bulldozer tries to power through, but CJ Mosley stops him for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"The Ravens' offensive line needs to step up.\""),
            (f"Al Michaels: \"Flowers on the end around is met in the backfield by Quinnen Williams, losing {yards} yards!\"",
            "Chris Collinsworth: \"Quinnen Williams is disruptive in the backfield.\""),
            (f"Al Michaels: \"Keaton Mitchell takes the pitch and is immediately tackled by Quincy Williams, resulting in a loss of {yards} yards.\"",
            "Chris Collinsworth: \"The Jets' defense read that play perfectly.\""),
            (f"Al Michaels: \"The Bulldozer tries to run it up the middle, but CJ Mosley stops him for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"There's no room for St-Laurent to run.\""),
            (f"Al Michaels: \"Mitchell takes the handoff, but Sauce Gardner swarms him in the backfield, losing {yards} yards!\"",
            "Chris Collinsworth: \"Sauce Gardner adds some spice to the Jets' defense.\""),
            (f"Al Michaels: \"Keaton Mitchell tries a power run, but Derrell Revis brings him down for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Revis isn't just a cover corner; he can tackle too.\""),
            (f"Al Michaels: \"St-Laurent takes a toss, but Quinnen Williams wraps him up for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams is having a dominant performance today.\""),
            (f"Al Michaels: \"The Bulldozer goes for a draw, but Quincy Williams snuffs it out for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"St-Laurent is getting no help from his O-line tonight.\""),
            (f"Al Michaels: \"Keaton Mitchell is tackled in the backfield by Quinnen Williams for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams completely disrupted that play.\""),
            (f"Al Michaels: \"Keaton Mitchell tries a draw, but Quincy Williams tackles him for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Williams came out of nowhere to make that stop.\""),
            (f"Al Michaels: \"The Bulldozer takes a toss, but Derrell Revis wraps him up for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Revis, a Hall of Famer in the secondary, showing his tackling ability.\""),
            (f"Al Michaels: \"Mitchell is swarmed by Sauce Gardner in the backfield for a loss of {yards} yards!\"",
            "Chris Collinsworth: \"Gardner read that play perfectly.\"")
            
        ]
    return choice(comments)





def defense_no_gain_commentary(suit): # Jets gain no yards
    if suit in ['D', 'S']:  # Pass plays
        comments = [
            # Existing lines
            ("Al Michaels: \"Zach Wilson looks for Garrett Wilson, but the pass is batted down by Ed Reed!\"",
             "Chris Collinsworth: \"Ravens DBs read that play like a book, Al!\""),
            ("Al Michaels: \"Wilson drops back, but he's met immediately by Ray Lewis and throws it away!\"",
             "Chris Collinsworth: \"Ray Lewis just showed why he's a legend, forcing Wilson to throw it away!\""),
            ("Al Michaels: \"Wilson tries to connect with Allen Lazard, but Kyle Hamilton breaks it up!\"",
             "Chris Collinsworth: \"Hamilton's been a star since his rookie year for a reason.\""),
            ("Al Michaels: \"Zach Wilson looks for Breece Hall on the screen, but Roquan Smith sniffs it out!\"",
             "Chris Collinsworth: \"Smith read that play from a mile away.\""),
            ("Al Michaels: \"Wilson attempts to find Garrett Wilson, but the ball falls incomplete!\"",
             "Chris Collinsworth: \"Reed just knows where the ball is going to be, every time. Able to close on Wilson before he can secure the catch.\""),
            ("Al Michaels: \"Wilson throws towards Allen Lazard, but it's dropped!\"",
             "Chris Collinsworth: \"Lewis might be known for his run-stopping, but he can cover too. He was right there if Lazard held on.\""),
            ("Al Michaels: \"Wilson looks for Douglas DEEEEEEEP... INCOMPLETE!!!\"",
             "Chris Collinsworth: \"Douglas had Stephens beat off the line here but the ball is thrown slightly short...\""),
            ("Al Michaels: \"Zach Wilson targets Yasin Douglas, but it's well-covered by Humphrey!\"",
             "Chris Collinsworth: \"Wilson is struggling to get the ball to anyone tonight.\""),
            ("Al Michaels: \"Wilson' quick slant to Garrett Wilson is incomplete. Coverage by Kyle Hamilton.\"",
             "Chris Collinsworth: \"Hamilton has the length to disrupt those quick throws.\""),
            ("Al Michaels: \"Zach Wilson tries a hitch route to Allen Lazard, but Marcus Williams jumps the route and nearly intercepts it!\"",
             "Chris Collinsworth: \"Williams read Wilson like a book there...\""),
            ("Al Michaels: \"Wilson targets Yasin Douglas on an out route, but it fall incomplete!\"",
             "Chris Collinsworth: \"I tell you Al, Douglas creates a ton of space but Wilson just misses the throw.\""),
            ("Al Michaels: \"Wilson aims for Douglas on a The go, He airs it out! Incomplete... Hamilton gets his hand on it!\"",
             "Chris Collinsworth: \"Hamilton covered so much ground to make that play. He is  REAL star!\""),
            ("Al Michaels: \"Zach looks for Douglas on a post route, but it's disrupted by Marcus Williams.\"",
             "Chris Collinsworth: \"Williams has a real nose for the football.\""),
            ("Al Michaels: \"Wilson tries to hit Garrett Wilson on a go route, but it falls to the groud. Well-defended by Kyle Hamilton.\"",
             "Chris Collinsworth: \"Hamilton used his speed to keep up with Wilson there.\""),
            ("Al Michaels: \"Wilson attempts a deep pass, but Geno Stone is there for the interception!\"",
             "Chris Collinsworth: \"Stone read Wilson perfectly and came up with the pick!\""),
            ("Al Michaels: \"Zach Wilson targets Allen Lazard, but Patrick Queen is there on the coverage.\"",
             "Chris Collinsworth: \"Queen's coverage skills are exceptional; he's all over Lazard there!\""),
            ("Al Michaels: \"Wilson tries a quick throw, but David Odjabo gets a hand on it, disrupting the pass!\"",
             "Chris Collinsworth: \"Odjabo's athleticism is on full display with that deflection!\""),
            ("Al Michaels: \"Wilson attempts a screen pass, but Travis Jones sniffs it out and breaks up the play!\"",
             "Chris Collinsworth: \"Jones read that screen perfectly and blew it up!\""),
            ("Al Michaels: \"Zach Wilson looks deep for Yasin Douglas, but Geno Stone's coverage forces an incompletion!\"",
             "Chris Collinsworth: \"Stone's tight coverage made it impossible for Douglas to make the catch on a throw like that...\""),
            ("Al Michaels: \"Wilson targets Allen Lazard on a crossing route, but Patrick Queen is all over him, leading to an incompletion!\"",
             "Chris Collinsworth: \"Queen's speed and awareness were on full display there!\""),
            ("Al Michaels: \"Wilson tries to hit Garrett Wilson on a deep route, but David Odjabo pressures him, resulting in an incomplete pass!\"",
             "Chris Collinsworth: \"Odjabo's pass-rushing ability disrupted Wilson' timing on that throw!\""),
            ("Al Michaels: \"Zach Wilson attempts a quick slant to Douglas... Batted down by Travis Jones!\"",
             "Chris Collinsworth: \"Jones made himself a big obstacle there, forcing the incompletion!\""),
            ("Al Michaels: \"Wilson looks for Yasin Douglas on an out route, but Geno Stone's coverage is tight, leading to an incompletion!\"",
             "Chris Collinsworth: \"Stone didn't give Douglas an inch of space to make the catch!\""),
            ("Al Michaels: \"Wilson tries a wheel route to Garrett Wilson and he gets past stone and the throw is incomplete!\"",
             "Chris Collinsworth: \"It's times like these where Jets fans long for the Rodgers 4 snap glory run!\""),
            ("Al Michaels: \"Zach Wilson attempts a post route to Yasin Douglas, but David Odjabo pressures him, incomplete pass!\"",
             "Chris Collinsworth: \"Wilson Continues to struggle tonight with this Ravens Defence out there flying!\""),
            ("Al Michaels: \"Wilson goes deep to Garrett Wilson, but Geno Stone's coverage is superb, leading to an incompletion!\"",
             "Chris Collinsworth: \"Stone made sure Wilson had no chance to make that catch!\"")
        ]
        
    else:  # Run plays
        comments = [
            # Existing lines
            ("Al Michaels: \"Zach Wilson takes the snap and hands it off to Dalvin Cook, but he's met immediately by Ray Lewis at the line of scrimmage!\"",
             "Chris Collinsworth: \"Ray Lewis just showed why he's a legend, stopping Cook dead in his tracks!\""),
            ("Al Michaels: \"Breece Hall tries to bounce it outside, but he's wrapped up by Ed Reed for no gain!\"",
             "Chris Collinsworth: \"Reed's still got those tackling skills, doesn't he?\""),
            ("Al Michaels: \"Wilson hands off to Breece Hall, who is immediately met by Kyle Hamilton!\"",
             "Chris Collinsworth: \"Hamilton's tackling is as good as his coverage.\""),
            ("Al Michaels: \"Breece Hall takes the handoff, but is swallowed up by Ray Lewis!\"",
             "Chris Collinsworth: \"You can't run on Ray Lewis, plain and simple.\""),
            ("Al Michaels: \"Wilson gives it to Hall, but Roquan Smith is there to meet him at the line!\"",
             "Chris Collinsworth: \"Smith is a tackling machine, Al.\""),
            ("Al Michaels: \"Zach Wilson tries a QB sneak, but Ed Reed shuts it down!\"",
             "Chris Collinsworth: \"Reed can do it all, can't he?\""),
            ("Al Michaels: \"Breece Hall looks for a hole, but Kyle Hamilton fills it quickly!\"",
             "Chris Collinsworth: \"Hamilton's got a nose for the football, no doubt.\""),
            ("Al Michaels: \"Breece Hall takes a handoff but is met at the line by Roquan Smith!\"",
             "Chris Collinsworth: \"Smith is so quick to diagnose those run plays.\""),
            ("Al Michaels: \"Zach Wilson hands it off to Hall, but he's stuffed by Ray Lewis!\"",
             "Chris Collinsworth: \"Lewis is a one-man run-stopping machine.\""),
            ("Al Michaels: \"Breece Hall tries a power run but is swallowed up by Ed Reed.\"",
             "Chris Collinsworth: \"Reed's tackling is as good as his coverage.\""),
            ("Al Michaels: \"Hall goes for a draw, but it's sniffed out by Marlon Humphrey for no gain.\"",
             "Chris Collinsworth: \"Humphrey can do it all, can't he?\""),
            ("Al Michaels: \"Breece Hall takes a pitch but is immediately wrapped up by Marcus Williams.\"",
             "Chris Collinsworth: \"Williams is a force against the run.\""),
            ("Al Michaels: \"The Jets attempts a toss but Hall is met by Kyle Hamilton at the line.\"",
             "Chris Collinsworth: \"Hamilton's range is just incredible.\""),
            ("Al Michaels: \"Dalvin Cook tries a dive but is stuffed by Roquan Smith.\"",
             "Chris Collinsworth: \"Smith was in the backfield in a flash.\""),
            ("Al Michaels: \"Wilson hands off to Breece Hall, but David Odjabo penetrates the backfield and wraps him up for no gain!\"",
            "Chris Collinsworth: \"Odjabo's quickness off the line disrupted that play!\""),
            ("Al Michaels: \"Dalvin Cook tries to find a hole, but Patrick Queen fills it and stops him for no gain!\"",
            "Chris Collinsworth: \"Queen's instincts are on full display there, making the tackle!\""),
            ("Al Michaels: \"Zach Wilson attempts a quarterback draw, but Travis Jones stuffs him on the line of scrimmage!\"",
            "Chris Collinsworth: \"Jones wasn't fooled by that play at all!\""),
            ("Al Michaels: \"Breece Hall looks for running room, but Geno Stone flies in and wraps him up for no gain!\"",
            "Chris Collinsworth: \"Stone's speed and tackling ability were on display there!\""),
            ("Al Michaels: \"Wilson hands off to Cook, but Marcus Williams shoots the gap and meets him half way for no gain!\"",
            "Chris Collinsworth: \"Williams read that play perfectly and made the tackle!\""),
            ("Al Michaels: \"Dalvin Cook tries to cut outside, but Patrick Queen tracks him down and stops him for no gain!\"",
            "Chris Collinsworth: \"Queen's pursuit was outstanding on that play!\""),
            ("Al Michaels: \"Wilson keeps it on the read option, but Ed Reed is right there to bring him down for a minimal.....for no gain!\"",
            "Chris Collinsworth: \"Reed's football IQ is off the charts!\""),
            ("Al Michaels: \"Breece Hall takes the handoff, but Kyle Hamilton wraps him up no gain!\"",
            "Chris Collinsworth: \"Hamilton's athleticism was on full display with that tackle! He came down from the safety spot for the stop.\""),
            ("Al Michaels: \"Zach Wilson attempts a scramble, but Roquan Smith chases him down and prevents a big gain!\"",
            "Chris Collinsworth: \"Smith's speed allowed him to catch Wilson from behind!\"")
    ]
    return choice(comments)




def defense_positive_yards_commentary(yards, suit): # Jets gain Yards
    if suit in ['D', 'S']:  # Pass plays
        comments = [
            # Existing lines
            (f"Al Michaels: \"Zach Wilson takes the snap, fakes the handoff, and finds Garrett Wilson for a {yards}-yard gain!\"",
             "Chris Collinsworth: \"That play-action really sold the defense, giving Wilson plenty of room to make the catch.\""),
            (f"Al Michaels: \"Wilson drops back and hits Lazard for {yards} !\"",
             "Chris Collinsworth: \"Lazard's got some reliable hands out there.\""),
            (f"Al Michaels: \"Wilson finds Breece Hall in the flats, and he picks up {yards} yards!\"",
             "Chris Collinsworth: \"Hall can catch as well as he can run, a dual threat.\""),
            (f"Al Michaels: \"Zach Wilson to Garrett Wilson for another {yards}-yard gain.\"",
             "Chris Collinsworth: \"Wilson is becoming Wilson' go-to guy today.\""),
            (f"Al Michaels: \"Wilson throws a laser to Douglas for {yards} yards!\"",
             "Chris Collinsworth: \"Yasin has been stepping up big time this game.\""),
            (f"Al Michaels: \"Zach Wilson swings it out to Cook, and he scampers for {yards} yards.\"",
             "Chris Collinsworth: \"Cooks's elusiveness in open space is impressive.\""),
            (f"Al Michaels: \"Zach Wilson fires a quick slant to Yasin Douglas for a {yards}-yard gain, the tight coverage from Marlon Humphrey.\"",
             "Chris Collinsworth: \"Humphrey was right there, but Douglas just made a great play.\""),
            (f"Al Michaels: \"Wilson finds Douglas on the fade for {yards} yards, just out of reach for Kyle Hamilton.\"",
             "Chris Collinsworth: \"Hamilton was close, but Wilson' placement was impeccable.\""),
            (f"Al Michaels: \"Wilson hits Garrett Wilson for a gain of {yards} yards, beating Marcus Williams in coverage.\"",
             "Chris Collinsworth: \"Williams was in a tough spot there, great throw by Wilson.\""),
            (f"Al Michaels: \"Zach Wilson connects with Allen Lazard for {yards} yards.\"",
             "Chris Collinsworth: \"You don't often see someone get the better of Reed in Man Coverage often.\""),
            (f"Al Michaels: \"Wilson throws a to Yasin Douglas for {yards} yard. Coverage from Stephens on the play.\"",
             "Chris Collinsworth: \"Williams was in position, but that was just a perfect throw.\""),
            (f"Al Michaels: \"Wilson finds Breece Hall on the chip and go for {yards} yards, just out of reach for Roquan Smith.\"",
             "Chris Collinsworth: \"Smith almost had it, but Wilson placed it perfectly.\""),
            (f"Al Michaels: \"Zach Wilson hits Garrett Wilson on the double move, shaking off Marlon Humphrey for {yards} yards.\"",
             "Chris Collinsworth: \"Wilson showing off his route running skills there.\""),
            (f"Al Michaels: \"Wilson finds Douglas on a quick slant, beating Stone for {yards} yards.\"",
             "Chris Collinsworth: \"Stone will want that one back; he was just a step behind.\""),
            (f"Al Michaels: \"Wilson throws a dart to Yasin Douglas on the post for {yards}! What a catch!\"",
             "Chris Collinsworth: \"Douglas is making some key plays today.\""),
            (f"Al Michaels: \"Wilson fires to Garrett Wilson on an out route, picking up {yards} yards against Marcus Williams.\"",
             "Chris Collinsworth: \"Williams coming from the safety spot read that and was close, but Wilson' accuracy won the day.\""),
            (f"Al Michaels: \"Wilson connects with Lazard on a crossing route for {yards} yards!\"",
                "Chris Collinsworth: \"Lazard found the soft spot in the defense and capitalized.\""),
            (f"Al Michaels: \"Zach Wilson goes deep to Douglas for a {yards}-yard gain! What an arm!\"",
            "Chris Collinsworth: \"Wilson can make those deep throws look easy.\""),
            (f"Al Michaels: \"Wilson throws a screen pass to Breece Hall, and he takes it for {yards} yards behind some great blocking!\"",
            "Chris Collinsworth: \"That screen was executed perfectly, and Hall had the vision to follow his blockers.\""),
            (f"Al Michaels: \"Wilson hits Garrett Wilson on a comeback route for {yards} yards! Wilson's route running is on point.\"",
            "Chris Collinsworth: \"Wilson created separation with his route running there.\""),
            (f"Al Michaels: \"Zach Wilson with a quick release to Yasin Douglas for {yards} yards! The timing on that pass was impeccable.\"",
            "Chris Collinsworth: \"Wilson' quick release makes it tough for defenders to react.\""),
            (f"Al Michaels: \"Wilson finds Lazard on a screen pass, and he picks up {yards} yards after the catch!\"",
            "Chris Collinsworth: \"Lazard turned a short pass into a solid gain.\""),
            (f"Al Michaels: \"Wilson goes to Breece Hall on a swing pass, and he gains {yards} yards! Hall's versatility is a huge asset.\"",
            "Chris Collinsworth: \"Hall can make plays as a receiver too, showcasing his versatility.\""),
            (f"Al Michaels: \"Zach Wilson targets Garrett Wilson on a slant route for {yards} yards!\"",
            "Chris Collinsworth: \"Wilson's physicality helped him secure that catch in traffic.\""),
            (f"Al Michaels: \"Wilson connects with Yasin Douglas on a comeback route for {yards} yards! Douglas found the opening in the defense.\"",
            "Chris Collinsworth: \"Douglas ran a precise route to get open.\""),
            (f"Al Michaels: \"Wilson fires to Breece Hall on a wheel route, and he gains {yards} yards! A well-designed play!\"",
            "Chris Collinsworth: \"The play design fooled the defense, allowing Hall to get open.\"")
        ]
    else:  # Run plays
        comments = [
            # Existing lines
            (f"Al Michaels: \"Wilson hands it off to Breece Hall, who finds a seam and gains {yards} yards!\"",
             "Chris Collinsworth: \"Hall showed some great acceleration there, Al.\""),
            (f"Al Michaels: \"Breece Hall takes the handoff and muscles his way for {yards} yards.\"",
             "Chris Collinsworth: \"Hall is showing some power running today.\""),
            (f"Al Michaels: \"Wilson gives it to Hall, who bounces outside for {yards} yards!\"",
             "Chris Collinsworth: \"Hall has that speed to get to the edge.\""),
            (f"Al Michaels: \"Zach Wilson on the keeper! Picks up {yards} yards.\"",
             "Chris Collinsworth: \"Wilson can still move when he needs to.\""),
            (f"Al Michaels: \"Handoff to Breece Hall, and he slices through the defense for {yards} yards!\"",
             "Chris Collinsworth: \"Hall has a knack for finding those running lanes.\""),
            (f"Al Michaels: \"Wilson to Hall on the draw play, and he gains {yards} yards.\"",
             "Chris Collinsworth: \"A well-timed draw play can be so effective.\""),
            (f"Al Michaels: \"Breece Hall takes the handoff and gains {yards} yards before being brought down by Roquan Smith.\"",
             "Chris Collinsworth: \"Smith made a good stop, but not before Hall picked up some valuable yards.\""),
            (f"Al Michaels: \"Zach Wilson hands off to Hall, who finds a seam for {yards} yards, getting by Suggs.\"",
             "Chris Collinsworth: \"It's not often you see someone slip through Suggs' reach.\""),
            (f"Al Michaels: \"Breece Hall breaks a tackle from Ed Reed and gains {yards} yards.\"",
             "Chris Collinsworth: \"Reed usually wraps up better than that.\""),
            (f"Al Michaels: \"Hall takes a pitch from Wilson and picks up {yards} yards before being tackled by Marcus Williams.\"",
             "Chris Collinsworth: \"Williams made the stop, but Hall had already done the damage.\""),
            (f"Al Michaels: \"Breece Hall gets the handoff and finds a hole, gaining {yards} yards before being brought down by Kyle Hamilton.\"",
             "Chris Collinsworth: \"Hamilton made the play, but you can't ignore stellar that O-line effort to make that hole for Hall.\""),
            (f"Al Michaels: \"Hall takes a toss from Wilson and gains {yards} yards.\"",
             "Chris Collinsworth: \"Smith was in the backfield quickly but just missed the tackle.\""),
            (f"Al Michaels: \"Breece Hall slips through a tackle from Marlon Humphrey to pick up {yards} yards.\"",
             "Chris Collinsworth: \"Humphrey had him but just couldn't hold on.\""),
            (f"Al Michaels: \"Zach Wilson hands it off to Hall, who dodges a tackle from Ed Reed for a {yards}-yard gain.\"",
             "Chris Collinsworth: \"Reed almost had him in the backfield.\""),
            (f"Al Michaels: \"Breece Hall takes a handoff and makes Marcus Williams miss, picking up {yards} yards.\"",
             "Chris Collinsworth: \"Williams usually makes that tackle.\""),
            (f"Al Michaels: \"Hall gets the ball and finds room to run, gaining {yards} yards before being stopped by Kyle Hamilton.\"",
             "Chris Collinsworth: \"Hamilton saved a bigger gain there.\""),
            (f"Al Michaels: \"Wilson hands it off to Dalvin Cook, who bursts through the line and gains {yards} yards!\"",
            "Chris Collinsworth: \"Cook's speed and vision are on full display, Al.\""),
            (f"Al Michaels: \"Dalvin Cook takes the handoff and bulldozes his way for {yards} yards, breaking tackles along the way!\"",
            "Chris Collinsworth: \"Cook is a force to be reckoned with, Al.\""),
            (f"Al Michaels: \"Wilson gives it to Cook, and he makes a sharp cut to pick up {yards} yards!\"",
            "Chris Collinsworth: \"Cook's agility is a real asset on that run, Al.\""),
            (f"Al Michaels: \"Dalvin Cook takes the handoff, spins away from a defender, and gains {yards} yards! What a move!\"",
            "Chris Collinsworth: \"Cook's elusiveness is second to none, Al.\""),

            (f"Al Michaels: \"Handoff to Dalvin Cook, and he patiently waits for his blocks before picking up {yards} yards.\"",
            "Chris Collinsworth: \"Cook's patience pays off with a nice gain, Al.\""),
            (f"Al Michaels: \"Wilson hands it off to Cook, who follows his blockers and gains {yards} yards! Great vision!\"",
            "Chris Collinsworth: \"Cook's field awareness led to a big gain on that run, Al.\""),
            (f"Al Michaels: \"Dalvin Cook takes the pitch and sprints to the outside, gaining {yards} yards! Blazing speed!\"",
            "Chris Collinsworth: \"Cook turned on the jets and left the defense in the dust, Al.\""),
            (f"Al Michaels: \"Wilson gives it to Cook, and he powers through for {yards} yards, dragging defenders with him!\"",
            "Chris Collinsworth: \"Cook's determination is unmatched, Al.\""),
            (f"Al Michaels: \"Dalvin Cook takes the handoff and goes airborne to gain {yards} yards! What an acrobatic move!\"",
            "Chris Collinsworth: \"Cook's athleticism is off the charts, Al.\"")
        ]
    return choice(comments)


def defense_same_suit_higher_value(yards, suit): # Jets Lose Yards
    if suit in ['D', 'S']:  # Pass plays (Sacks)
        comments = [
            # New lines featuring Ravens players
            (f"Al Michaels: \"Zach Wilson is taken down by Ed Reed! A loss of {yards} yards.\"",
             "Chris Collinsworth: \"Reed still has that ability to change a game.\""),
            (f"Al Michaels: \"Wilson drops back, but he's sacked by Ray Lewis for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Ray Lewis showing he can do it all.\""),
            (f"Al Michaels: \"Zach Wilson is pressured and brought down by Roquan Smith! A loss of {yards} yards.\"",
             "Chris Collinsworth: \"Smith is just a blur out there.\""),
            (f"Al Michaels: \"Wilson is looking to pass, but Kyle Hamilton comes flying in for a sack! A loss of {yards} yards.\"",
             "Chris Collinsworth: \"Hamilton's playmaking ability is off the charts.\""),
            (f"Al Michaels: \"Zach Wilson is surrounded and taken down by Ed Reed, losing {yards} yards.\"",
             "Chris Collinsworth: \"Reed's veteran savvy really showed there.\""),
            # Additional lines
            (f"Al Michaels: \"Wilson under pressure from Geno Stone, and he's taken down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Stone's relentless pursuit paid off there, Al.\""),
            (f"Al Michaels: \"Wilson is swarmed by the Ravens' defense, with Patrick Queen leading the charge for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's speed and instincts were on full display, Al.\""),
            (f"Al Michaels: \"Zach Wilson goes down in the backfield as David Ojabo gets to him, resulting in a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Ojabo's pass-rushing skills were on display there, Al.\""),
            (f"Al Michaels: \"Wilson tries to escape the pressure, but Travis Jones brings him down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Jones is a force on the defensive line, Al.\""),
            (f"Al Michaels: \"Zach Wilson is sacked by a blitzing Patrick Queen, losing {yards} yards on the play!\"",
             "Chris Collinsworth: \"Queen's timing on that blitz was impeccable, Al.\""),
                         # Additional lines
            (f"Al Michaels: \"Wilson is under siege as Geno Stone gets to him for a sack, resulting in a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Stone's relentless pressure paid off, Al.\""),
            (f"Al Michaels: \"Wilson can't escape the grasp of Patrick Queen, going down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's speed is unmatched, Al.\""),
            (f"Al Michaels: \"Zach Wilson is buried by David Ojabo in the backfield, losing {yards} yards!\"",
             "Chris Collinsworth: \"Ojabo's pass-rushing ability was on full display there, Al.\""),
            (f"Al Michaels: \"Wilson tries to evade the rush, but Travis Jones brings him down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Jones is a force on the defensive line, Al.\""),
            (f"Al Michaels: \"Zach Wilson is caught in the chaos as Patrick Queen sacks him for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's relentless pursuit made the difference, Al.\"")
        ]
    else:  # Run plays
        comments = [
            # New lines featuring Ravens players
            (f"Al Michaels: \"Breece Hall is met in the backfield by Ray Lewis for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Lewis is just a wall against the run.\""),
            (f"Al Michaels: \"Wilson hands off to Hall, but Roquan Smith is there to drop him for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Smith is a disruptive force.\""),
            (f"Al Michaels: \"Breece Hall tries to cut back, but Ed Reed is right there for a loss of {yards} yards.\"",
             "Chris Collinsworth: \"Reed has a sixth sense for where the ball is going.\""),
            (f"Al Michaels: \"Zach Wilson on a QB draw, but he's swallowed up by Kyle Hamilton for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Hamilton was just waiting for that.\""),
            (f"Al Michaels: \"Hall takes the handoff but is met by Ray Lewis and Roquan Smith, losing {yards} yards.\"",
             "Chris Collinsworth: \"That's a linebacker duo you don't want to run into.\""),
            # Additional lines
            (f"Al Michaels: \"Dalvin Cook is wrapped up by Geno Stone in the backfield for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Stone's tackling skills were on full display there, Al.\""),
            (f"Al Michaels: \"Wilson hands it off to Hall, but Patrick Queen crashes in for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's pursuit was relentless, Al.\""),
            (f"Al Michaels: \"Breece Hall tries to find a hole, but David Ojabo is there to bring him down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Ojabo's strength made the difference on that play, Al.\""),
            (f"Al Michaels: \"Dalvin Cook is met by Travis Jones in the backfield, resulting in a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Jones is a disruptive force up front, Al.\""),
            (f"Al Michaels: \"Wilson hands it off to Hall, but Patrick Queen is there to stop him for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's instincts led to a big stop, Al.\""),
                # Additional lines
            (f"Al Michaels: \"Dalvin Cook is wrapped up by Geno Stone in the backfield for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Stone's tackling skills were on full display there, Al.\""),
            (f"Al Michaels: \"Wilson hands it off to Hall, but Patrick Queen crashes in for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's pursuit was relentless, Al.\""),
            (f"Al Michaels: \"Breece Hall tries to find a hole, but David Ojabo is there to bring him down for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Ojabo's strength made the difference on that play, Al.\""),
            (f"Al Michaels: \"Dalvin Cook is met by Travis Jones in the backfield, resulting in a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Jones is a disruptive force up front, Al.\""),
            (f"Al Michaels: \"Wilson hands it off to Hall, but Patrick Queen is there to stop him for a loss of {yards} yards!\"",
             "Chris Collinsworth: \"Queen's instincts led to a big stop, Al.\"")
        ]
    return choice(comments)




def sideline_commentary():
    comments = [
        # New lines with facts incorporated
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"We're at capacity tonight with 110,000 fans! Lac Bob Stadium is buzzing! Back to you, Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Simon and Justin St-Laurent are brothers and competitors. Though Simon has been stealing the spotlight with his MVP level looks and play, Al.\""),
      
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"It's a Hall of Famer showdown tonight with Ray Lewis, Ed Reed, and Derrell Revis showing they've still got it. Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Zay Flowers is proving why he was a 1st round pick. He is 13th of 14 siblings and then went on to break records at Boston College. Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Lamar Jackson and Simon St-Laurent are putting on a masterclass. We're looking at future 1st ballot Hall of Famers. Back to you, Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Quinnen and Quincy Williams are also brothers on the field tonight, and they're both making their presence felt. Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Both kickers, Justin St-Laurent and Justin Tucker, are showing why they'll likely be in the Hall of Fame someday. Back to you, Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"The atmosphere is so electric, you can almost feel the crowd's energy affecting the game. Al.\""),
        
        (f" > SIDE LINE UPDATE > |  Shea Timmins: \"Both Coaching Staff are very focused. They know that with so much talent on the field, every decision counts. Back to you, Al.\"")
    ]
    return choice(comments)




# Helper functions
def card_value(card):
    return {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card[:-1]]

def card_color(card):
    return {'D': 'Red', 'S': 'Red', 'R': 'Black', 'T': 'Black'}[card[-1]]


def calculate_yards_with_superstar(offense_card, defense_card, player_superstar_cards, computer_superstar_cards, is_player_on_offense):
    offense_value = card_value(offense_card)
    defense_value = card_value(defense_card)
    yards = 0
    superstar_used = "No Superstar Used"
    team_that_used_superstar = "None"

    # Determine the suits of the offense and defense cards
    offense_suit = offense_card[-1]
    defense_suit = defense_card[-1]
    
    # Check for offensive superstar card
    if (is_player_on_offense and offense_card in player_superstar_cards) or \
       (not is_player_on_offense and offense_card in computer_superstar_cards):
        if offense_suit != defense_suit:
            yards += offense_value  # Different suit, treated as different color
        else:
            yards -= (defense_value - offense_value)  # Same suit, follow Rule 2
        superstar_used = offense_card
        team_that_used_superstar = "The Ravens" if is_player_on_offense else "The Jets"

    # Check for defensive superstar card
    elif (is_player_on_offense and defense_card in computer_superstar_cards) or \
         (not is_player_on_offense and defense_card in player_superstar_cards):
        if offense_suit != defense_suit:
            yards -= defense_value  # Different suit, treated as different color
        else:
            yards += (offense_value - defense_value)  # Same suit, follow Rule 2
        superstar_used = defense_card
        team_that_used_superstar = "The Jets" if is_player_on_offense else "The Ravens"
    
    # Non-superstar cards

    
    # Non-superstar cards
    if superstar_used == "No Superstar Used":
        # Same suit (and same color by definition)
        if offense_suit == defense_suit:
            if offense_value < defense_value:
                yards -= (defense_value - offense_value)
            else:
                yards += 0  # No yards gained
        # Different suit but same color
        elif offense_suit in ['D', 'S'] and defense_suit in ['D', 'S'] or \
             offense_suit in ['R', 'T'] and defense_suit in ['R', 'T']:
            if offense_value >= defense_value:
                yards += (offense_value - defense_value)
            else:
                yards += 0  # No yards gained
        
        # Different color
        else:
            yards += offense_value

    if yards < -10:
        yards = -10
    
    return yards, superstar_used, team_that_used_superstar
# Importing Tkinter to build the new dashboard from scratch
import tkinter as tk

# Function to initialize the new dashboard
def initialize_dashboard():
    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Official Ravens Game Cast")
    
    # Create frames for better organization
    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP)
    
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM)
    
    score_box = tk.Text(top_frame, height=1, width=15, font=("Calibri", 14, "bold"))
    score_box.pack()
    score_box.insert(tk.END, "Ravens  |  Jets")
    
        # Commentary Box: Last Play Commentary (Initial set to "Game Start")
    cur_do_di = tk.Text(top_frame, height=3, width=20, font=("Calibri", 12,"italic"))
    cur_do_di.pack()
    cur_do_di.insert(tk.END, "1 & 10 from the 65 ")

    # Canvas for the football field representation with a white border
    canvas = tk.Canvas(top_frame, bg='green3', height=300, width=900, highlightthickness=6, highlightbackground="white")
    canvas.pack()

    # End zone in purple
    canvas.create_rectangle(0, 0, 100, 308, fill='purple4')
    
    # Yard lines (assuming each yard is 10 pixels)
    for i in range(100, 900, 50):  # Every 10 yards, skipping end zone
        canvas.create_line(i, 0, i, 308, fill='white', width=3)
    
    # Initial position marker (Blue line at 65-yard line / px = 750 = (yard line + 10) * 10 )
    position_marker = canvas.create_line(750, 0, 750, 308, fill="blue", width=4)
    
    # First down marker at the 55- yard line / px = 650 = (yardline +10) * 10 
    first_down_marker = canvas.create_line(650, 0, 650, 308, fill="yellow", width=4)
    
    # Field Goal Marker at the 42-yard line px = 520+ (yardline +10) * 10
    field_goal_marker = canvas.create_line(520, 0, 520, 308, fill="red2", width=3, dash=(4, 2))

    
    # Initialize 'yards gained' rectangle near the position marker
    yards_gained_rect = canvas.create_rectangle(750, 100, 775, 125, fill="purple4", outline="gold")

    
    # Commentary Box: Last Play Commentary (Initial set to "Game Start")
    last_com_box = tk.Text(bottom_frame, height=8, width=100, font=("Calibri"))
    last_com_box.pack()
    last_com_box.insert(tk.END, " Kick Off in Progress...")
    
    # Return the elements that will be updated during the game
    # Return the elements that will be updated during the game
    return root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box


# Function to update the dashboard elements based on the game state
def update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth):
    

    # Convert current_position and yards_to_go to pixels
    current_position_px = (current_position + 10) * 10
    first_down_position_px = (current_position - yards_to_go + 10) * 10

    # Update the position marker and first down marker
    canvas.coords(position_marker, current_position_px, 0, current_position_px, 308)
    canvas.coords(first_down_marker, first_down_position_px, 0, first_down_position_px, 308)
    # Update Score
    score_box.delete(1.0, tk.END)
    score_box.insert(tk.END, f"Ravens {player_score} | {computer_score} Jets")
    
    # Update Current Down and Distance
    cur_do_di.delete(1.0, tk.END)
    cur_do_di.insert(tk.END, f"{current_down} & {yards_to_go} From the {current_position}")
    
    last_com_box.delete(1.0, tk.END)
    last_com = f"Last Play: {yards_this_play} yards on the Play\n   \n{al_michaels}\n  \n{chris_collinsworth}"
    last_com_box.insert(tk.END, last_com)

    # Update the 'yards gained' rectangle
    yards_gained_px = yards_this_play * 10  # Convert to pixels


    # Determine the type of play based on card suit
    play_type_color = card_color(chosen_offense_card)

    # Choose the outline color of the rectangle based on the play type
    outline_color = 'black' if play_type_color == 'Black' else 'white'

    # Update the outline color if yards_this_play is negative
    if yards_this_play < 0:
        outline_color = 'red'

    # Set the fill color based on who is on offense
    fill_color = 'purple4' if first_turn == 'rec' else 'dark green'


# Update the rectangle coordinates and color
    canvas.coords(yards_gained_rect, current_position_px + yards_gained_px, 150, current_position_px, 175)
    canvas.itemconfig(yards_gained_rect, fill=fill_color, outline=outline_color, width=4)
    
    if current_position < 0:
        cur_do_di.insert(tk.END, "\n TOUCHDOWN!")
        
        # Again, reset all your canvas markers to their launch location
        canvas.coords(position_marker, 750, 0, 750, 308)  # Resetting to 65-yard line as an example
        canvas.coords(first_down_marker, 650, 0, 650, 308)  # Resetting to 55-yard line as an example
    
    if current_down == 5:
        cur_do_di.insert(tk.END, "\n Turn Over On Downs")

        last_com_box.delete(1.0, tk.END)
        last_com = f"Last Play: {yards_this_play} yards on the Play \n \n End Of Drive \n \n First Play of Next Drive Underway..."
        last_com_box.insert(tk.END, last_com)
        # Again, reset all your canvas markers to their launch location
        canvas.coords(position_marker, 750, 0, 750, 308)  # Resetting to 65-yard line as an example
        canvas.coords(first_down_marker, 650, 0, 650, 308)  # Resetting to 55-yard line as an example
    # Update the Tkinter window
    root.update()

# Initialize variables


suits = ['D', 'S', 'R', 'T']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{value}{suit}" for suit in suits for value in values]
shuffle(deck)

# Initialize the list to store used cards
used_cards = []

# Initialize empty lists for player_superstar_cards and computer_superstar_cards
player_superstar_cards = []
computer_superstar_cards = []

# Loop to ensure player_qb_card has a minimum value of 9
while True:
    candidate_card = deck.pop()  # Pop a card from the deck
    if card_value(candidate_card) > 10:  # Check if the card has a value of at least 9
        player_qb_card = candidate_card  # If yes, assign it as the player's QB card
        break
    else:
        used_cards.append(candidate_card)

# Extract the suit of the player's QB card
qb_suit = player_qb_card[-1]

# Add remaining face cards of the same suit as the QB card to player_superstar_cards
face_values = ['J', 'Q', 'K', 'A']
for value in face_values:
    if f"{value}{qb_suit}" != player_qb_card:
        player_superstar_cards.append(f"{value}{qb_suit}")
        deck.remove(f"{value}{qb_suit}")

# Deal additional Superstar cards for both players
for _ in range(6):
    while True:
        card = choice(deck)
        if card not in player_superstar_cards and card not in computer_superstar_cards:
            deck.remove(card)
            computer_superstar_cards.append(card)
            break

for _ in range(10 - len(player_superstar_cards)):  # Adjust the range to fill up to 10 cards
    while True:
        card = choice(deck)
        if card not in player_superstar_cards and card not in computer_superstar_cards:
            deck.remove(card)
            player_superstar_cards.append(card)
            break

                            #GAME STARTS HERE

type_out("   ______________________________________")             
print("   |                                    | ")
type_out("   |                      |   |         | ")
type_out("   |  PLAYBOOK            | o |  |_0_|  | ")
type_out("   |           FOOTBALL   |___|    |    |")
type_out("   |_By SSL_________________|_____/_\___|")
type_out("                                            ")
print("   ")
print(" ----------- General Rules ------------")
print("  ")
print("   - The offense will start. They will play their card first. The defense will then play a card to stop or minimize the offensive card if they can.")
print("  ")
print("   - The number of yards gained or lost depends on the cards played and the card value and suit of the defensive cards.")
print("  ")
print("   - This is a turn based turn. The defense plays after seeing the offensive card. ")
print("  ")
print("   - Points: 7 for a touchdown, 3 for a field goal, and 2 for a safety.")
print("  ")
print("   - You have four downs to gain 10 yards. If unsuccessful and within 42 yards, you have the option to kick a FG.")
print("  ")
print("   - Field Goal outcome = 'Highest Card Wins'  Ties result in a successful Field Goal.  ")
print("  ")
print("   - All Drives Start 65 yards from the defensive endzone, and 15 yards from your own.") 
print("  ")
print("   - At the end of the drive, the offense and defense switch sides and the game continues until the Point Limit is reached by either team.")
print("  ")
print("   - The 'Call of the Raven' can be used on offensive plays of the matching play type bonus of the card. If used it will be unavailable until you score a Touchdown.")
print("  ")
print("   - You and the Computer will get 10 'Special Play' cards you can use whenever they show up in your hand for guarenteed value.")
print(" ")
print("   - The Offense Cannot lose more than 10 Yards in one play. ")
print("      ")
print("      ")
input("  > Press Enter For Game Play Rules")
print("      ")
print("      ")
type_out(" ----------- Game Play Rules ------------")
print(" ")
print("   - Same Suit ( D, S, R, T ): Offense gains 0 yards. If defensive value is higher = offensive value - Defensive value = Yards lost.")
print("  ")
print("   - Same Play Type, Different Suit: Offensive value - Defensive Value. If defensive value is higher, Offense loses 0 yards.")
print("  ")
print("   - Different Play Type: Offense Gains Full Value of Card.") 
print("  ")
print("   - Turn order =  Offense Plays a card  --->  Defense Plays a Card  --->:   ")
print(" ")
print("       > EX:   JD  (11 yard Deep/ Play Action Pass Offense)   --->  8S  (8 yard, Short/ Shot Gun Pass Defense) ")
print("               Outcome =  +3 Yards. (Same Play Type, Different Suit)  ")
print(" ")
print("             ______________________________________________________________")
print("             |  PLAY TYPE |           PLAYBOOK    CARD   INDEX            | ")
print("             |____________|___________________(suit)______________________|")
print("             | PASS CARDS | D = DEEP/PLAY ACTION |   S = SHORT/ SHOT GUN  |")
print("             |- - - - - - |- - - - - - - - - - - | - - - - - - - - - - - -| ") 
print("             | RUN CARDS  | R = INSIDE RUN       |  T = TOSS/PITCH RUN    |")
print("             |____________|______________________|________________________| ")
print("             | Face Card  | J = 11  | Q  =  12   |  K  =  13  | A  =  14  | ")
print("             |__Values____|_________|____________|____________|___________| ")
print("   ")
print(" ")
print("   * BONUS CARD RULES * " )
print("  ")
print("   - Call of the Raven card value is added to the outcome of the Off & Def cards.")
print("  ")
print("   - Special Plays are worth their full value only")
print("  ")
print("       - On Offense: Only defensive cards of the same suit can lessen their strength. ")
print("  ")
print("       - On Defence: Playing them on the same suit as the offense's card will still be worth full value.")
print(" ")
print("        *HINT: Offence could then gain yards* ")
print("  ")
print("   - If both team use a Special Play, The Offense will retain full value and the defenses will 'wasted'.")
print("  ")
print(" ")
input("   > Press Enter For Game Set Up <  ")
print("      ")
print("      ")
type_out_slow("  ------- Game Set up ------- ")
print(" ")
game_limit = int(input("   + Set your Point Limit for the game: "))
print(" ")
computer_start_score = int(input("   + Set the Jet's starting score for higher difficulty ( 0 for full game ) : "))
print(" ")
first_turn = input("   + Would you like to go on Receive/Offence 'rec' or Differ/Defense* 'dif' ?' ").strip().lower()
# Initialize variables
player_score = 0
computer_score = computer_start_score
first_to = game_limit
print(" ")
print("  ")
type_out(" ------ PLAYBOOK FOOTBALL ------")
print("  ")
type_out("  ------- Game Info ------- ")
print(" ")
print(f"   + Jets {computer_score} | Ravens  0    <-- You")
print(" ")
print("   + Lac Bob Stadium ")
print("  ")
if first_turn == 'rec': 
    print("   + Ravens Receive ")
else:
    print("   + Jets Receive")
print(" ")
print(f"   + First Team to Reach {first_to} Wins")
print(" ")
print("  ")
input("   > Press enter to see you playbook <  ")
print("  ")
type_out("  ----- Ravens Playbook ----- ")
print("   ")
print(f"   + Call of the Raven: {player_qb_card} ")
print("             ")
print(f"   + Speacial Plays Playbook:", player_superstar_cards)
print(" ")
type_out(" ----------- Playbook FOOTBALL -----------")
print(" ")
print(" ")
print("                       |   |   ")
print("                       |   |       0  <- REF ")
print("                       |___|      /|\       ")
print("   ______________________|________/_\___________")
print("  |                                             |")
print("  |             PLAYBOOK  FOOTBALL              |  ")
print("  |_____________________________________________|   ")
print("  | _                                         _ |")
print("  | _                                         _ |")
input("  | _       > Press enter for Kick Off  <     _ |")                    
print("  | _                                         _ |")
print("  |_____________________________________________|   ")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  |_____________________________________________| ")
print("  | _                X QB                     _ |")
print("  | _                            X            _ |")
print("  | _     X  X    X X X.X X X       X         _ |")
print("  | _   O          O O  O  O        O         _ |")
print("  |_____________________________________________|   ")
print("  | _        O       O  O                     _ |")
print("  | _                         O               _ |")
print("  | _             O                           _ |")
print("  | _                                         _ |")
print("  |_____________________________________________|   ")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  | _                                         _ |")
print("  |____________________|___|____________________| ")
print("  |                    |   |                    |")
print("  |   RAVENS  RAVENS   |___|  RAVENS   RAVENS   |")
print("  |______________________|______________________|")
print(" ")
print("  ")
print("   ________________________")
print("   |-- LAC BOB STADIUM -- |  ")
print("   |______________________|")
print("   |   RAVENS  |   JETS   |")
type_out(f"   |     0     |    {computer_score} ")
print("   |___________|__________|")
print("   |--PLAYBOOK  FOOTBALL--|")
print("   |______________________|")
deck += used_cards
deck += player_superstar_cards + computer_superstar_cards
used_cards = []
shuffle(deck)
player_qb_used = False
switch_turn = False
root, canvas, position_marker, first_down_marker,score_box, cur_do_di, yards_gained_rect, last_com_box = initialize_dashboard()


#MAIN GAME LOOP STARTS HERE
while player_score < game_limit and computer_score < game_limit:

    if len(deck) < 8:
        # Ensure QB cards don't get back into the deck
        deck = [f"{value}{suit}" for suit in suits for value in values 
            if f"{value}{suit}" != player_qb_card 
            and f"{value}{suit}" not in player_hand  # Exclude cards in player's hand
            and f"{value}{suit}" not in computer_hand  # Exclude cards in computer's hand
            and f"{value}{suit}" not in player_superstar_cards
            and f"{value}{suit}" not in computer_superstar_cards]
        # Add back only those superstar cards that are not in anyone's hand
        deck += [card for card in player_superstar_cards if card not in player_hand]
        deck += [card for card in computer_superstar_cards if card not in computer_hand]
        # Add the superstar cards back into the deck
        

        # Add the used cards back into the deck
        deck += used_cards

        # Clear the list of used cards
        used_cards = []

        # Shuffle the deck
        shuffle(deck)

        sideline_comment = sideline_commentary()
        type_out_slow(sideline_comment)# Sideline commentary

    
    round_end = False
    player_hand = [deck.pop() for _ in range(4)]
    computer_hand = [deck.pop() for _ in range(4)]
    current_position = 65  # Starting at the 65-yard line
    current_down = 1
    yards_to_go = 10
    total_yards_gained = 0
    should_replenish_hand = False  # Initialize the flag
    superstar_in_hand = [card for card in player_hand if card in player_superstar_cards]

    
    
    #START OF THE ROUND DOWNS -
    while current_down < 6:

        if current_down == 5:
            print("|  ")
            current_position = 65
            yards_this_play=0
            
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
            round_end = True
            break

        
        print("____________________________________")
        print("|   ")
        print("|  |_0__ *WHISTLE*")
        print("|    |  ")
        print("|   / \ ")
        type_out(f"|  {current_down} & {yards_to_go} From the {current_position}")
        print("|  -------")
        # Display the user's hand
        print("| ")
        

        # Check for superstar cards in the user's hand
        superstar_in_hand = [card for card in player_hand if card in player_superstar_cards]

        # Display message if there is a superstar card in the hand
        if superstar_in_hand:
            print(f"|  + Special Play {superstar_in_hand} ")

        print(f"|  Playbook: {player_hand}")
        print("|  -------- ")
        
        
        # FOURTH DOWN FG LOGIC
        if current_down == 4 and current_position <= 42 : #Inside the 40 YARD LINE: #CURRENT DOWN IS FOUR


            #RAVENS FOURTH DOWN INSIDE THE 43
            if first_turn == 'rec': 
                
                decision = ""
                adjusted_position = current_position + 17  # Temporary variable for adjusted position
                while decision not in ["fg", "go"]:
                    type_out(f"|  > Ravens {player_score} | Jets {computer_score} >>> {current_down} & {yards_to_go} From the {current_position}")
                    decision = input(f"|    > Do you want to go for it or send Tucker out for a {adjusted_position}-yard FG attempt? (fg/go)").strip().lower()


                    # RAVENS FIELD GOAL LOGIC
                if decision == 'fg':
                    print("|")
                    print("|  Out comes Tucker and the FG unit...")
                    print("|  -------")
                    print(f"|  Your Card: {player_hand}")  # Display remaining cards
                    offense_card = input("|  The Kick is up....: ").strip().upper()
                    player_hand.remove(offense_card)
                    used_cards.append(offense_card)

                                # Computer (Jets) plays a defense card
                    defense_card = choice(computer_hand)
                    computer_hand.remove(defense_card)
                    used_cards.append(defense_card)

                    print("|")
                    print("|  -------")

                    if card_value(offense_card) >= card_value(defense_card):
                        type_out_slow("| ")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |  o  |")
                        type_out_slow("|     |_____|")
                        type_out_slow("|________|_______ ")
                        print("|")
                        print("|  |_0_|")
                        print("|    |  ")
                        print("|   / \ ")
                        print("|  -------")
                        print("|  ===============  ")
                        print(f"|  Jets Previous Play:{defense_card} ")
                        player_score += 3
                        commentary = user_field_goal_higher_value(current_position)
                        type_out(commentary[0])
                        type_out(commentary[1])
                        update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
                    else:
                        type_out_slow("| ")
                        type_out_slow("|      |     |")
                        type_out_slow("|      |     |")
                        type_out_slow("|      |     | o")
                        type_out_slow("|      |_____|")
                        type_out_slow("|_________|__________ ")
                        print("|")
                        type_out("|  He Missed!! We don't see that often from Justin Tucker.")
                        print("|  __0__")
                        print("|    |  ")
                        print("|   / \ ")
                        print("|  -------")
                        print("|  ===============  ")
                        print(f"|  Jets Previous Play:{defense_card} ")
                        update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
                    round_end = True
                    break

                else: #RAVENS GO FOR IT INSIDE THE 43
                
                    type_out("|  Looks like the Ravens are leaving Lamar and the offense on the field!")

                
                    while True:
                        chosen_offense_card = input("|  Call in your Offensive Play: ").strip().upper()
                        if chosen_offense_card in player_hand:
                            break
                        else:
                            print("|  We don't have that play ready...")


                    player_hand.remove(chosen_offense_card)
                                # Check if the offensive card's suit matches the QB card's suit, and if the QB card hasn't been used yet
                    if not player_qb_used and chosen_offense_card[-1] == player_qb_card[-1]:
                        use_qb = input("|  > Let you MVP Loose? (y/n): ").strip().lower()
                    else:
                        use_qb = 'n'
                                # Computer (Jets) plays a defense card
                    chosen_defense_card = choice(computer_hand)
                    computer_hand.remove(chosen_defense_card)
                    


                                # Before calling the function, determine who is on offense
                    is_player_on_offense = True

                    

                    yards_this_play, superstar_used, team_that_used_superstar = calculate_yards_with_superstar(
                        chosen_offense_card,
                        chosen_defense_card,
                        player_superstar_cards,
                        computer_superstar_cards,
                        is_player_on_offense
                    )


                
                        # Add commentary based on yards gained or lost
                    if yards_this_play > current_position:
                        al_michaels, chris_collinsworth = gain_touchdown(yards_this_play, chosen_offense_card[-1]) 
                    elif yards_this_play > 20:
                        al_michaels, chris_collinsworth = big_play_commentary(yards_this_play, chosen_offense_card[-1])
                    elif yards_this_play > 0:
                        al_michaels, chris_collinsworth = gain_yards_commentary(yards_this_play, chosen_offense_card[-1])
                    elif yards_this_play == 0:
                        al_michaels, chris_collinsworth = no_gain_commentary(chosen_offense_card[-1])
                    else:
                        al_michaels, chris_collinsworth = loss_yards_commentary(-yards_this_play, chosen_offense_card[-1])

                    snap = snap_count()
                    print("|  ")
                    print("|  ===============")
                    type_out_slow("|  "+ snap)
                    print("|  -------  ")
                    print("|  -------")
                    type_out_slow("|  "+ al_michaels)
                    print("|  -------  ")
                    type_out_slow("|  "+ chris_collinsworth)               
                    type_out("|  ===============")
                    type_out(f"|  Jets Last Play:  {chosen_defense_card} ")
                    if superstar_used != "No Superstar Used":
                        print("| ")
                        type_out(f"|  Special Play Used ( {superstar_used} ) by {team_that_used_superstar}")
                        
                    print("|  -------")    
                    print("|  ______________________")
                    print("|   ---->  --->  -->  ->                        ")
                    type_out(f"|   {yards_this_play} yards on the Play ")
                    print("|  ----------------------")
                    print("|")
                    
                        
                            
                        
                    #PLAY OUTCOME UPDATE
                    total_yards_gained += yards_this_play
                    used_cards.append(chosen_offense_card)
                    used_cards.append(chosen_defense_card)
                
                    current_position -= yards_this_play
                    
                    yards_to_go -= yards_this_play
                    update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)



        #TOUCHDOWN
                if current_position <= 0:
                            
                    print("|")
                    td_line = announce_touchdown(first_turn)
                    type_out_slow(td_line)
                    print("|")
                    print("|  |_0_|")
                    print("|    |  ")
                    print("|   / \ ")
                    print("|  -------  ")
                    print("|  ===============  ")
                    if first_turn == 'rec':
                        player_score += 7

                    if player_qb_used:
                    # Reset the QB card (MVP Bonus) so it can be used again.
                        player_qb_used = False
                        print("|  > MVP Bonus Returned")
                        round_end = True
                        break
                    update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
                    round_end = True
                    break 


                # FIRST DOWN
                if yards_to_go <= 0:
                    print("|  ")
                    oneliner = ravens_first_down_stadium_announcer()
                    type_out_slow(oneliner)
                    print("| ")    
   
                    yards_to_go = 10  # Reset yards needed for a first down                
                    current_down = 1  # Reset the current down
                    update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)

                    # Optionally, shuffle the deck and replenish both players' hands here if necessary
                    if len(deck) < 8:
        # Ensure QB cards don't get back into the deck
        # Before reshuffling, make sure to exclude cards currently in player's and computer's hands
                        deck = [f"{value}{suit}" for suit in suits for value in values 
                            if f"{value}{suit}" != player_qb_card 
                            and f"{value}{suit}" not in player_hand  # Exclude cards in player's hand
                            and f"{value}{suit}" not in computer_hand  # Exclude cards in computer's hand
                            and f"{value}{suit}" not in player_superstar_cards
                            and f"{value}{suit}" not in computer_superstar_cards]
                        # Add back only those superstar cards that are not in anyone's hand
                        deck += [card for card in player_superstar_cards if card not in player_hand]
                        deck += [card for card in computer_superstar_cards if card not in computer_hand]
                        deck += used_cards  # Add used cards back in
                        used_cards = []  # Clear the list of used cards
                        shuffle(deck)  # Shuffle the deck
                        sideline_comment = sideline_commentary()
                        type_out_slow(sideline_comment)# Sideline commentary
        # Replenish the hand to make sure each player has 4 cards
                    cards_needed = 4 - len(player_hand)
                    player_hand += [deck.pop() for _ in range(cards_needed)]

                    cards_needed = 4 - len(computer_hand)
                    computer_hand += [deck.pop() for _ in range(cards_needed)]

                    print("|")
                    continue
                else:
                    current_down += 1  # Move to the next down

                    #TURN OVER ON DOWNS        
                    if current_down > 4 and yards_to_go > 0:
                        print("|  ")
                        commentary = turnover_on_downs_commentary()
                        type_out_slow(commentary[0])
                        type_out_slow(commentary[1])
                        update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
                        round_end = True
                        break  # Exit the while loop for downs         
                    
                                          

                # JETS FOURTH DOWN LOGIC ON FOURTH DOWN INSIDE THE 40                      

            if first_turn == 'dif':
            # Computer automatically goes for a field goal if within 41 yards
                if current_position <= 41:
                    type_out_slow("|  Al Michaels: Justin St-Laurent and the FG unit are called in on fourth down for the Jets. ")
                    print("|  ") 
                    # The computer chooses an offense card.
                    chosen_offense_card = choice(computer_hand)
                    computer_hand.remove(chosen_offense_card)
                    # Prompt user to input a defense card
                    chosen_defense_card = input("|  Your defensive play: ").strip().upper()
                    
                    # Calculate whether the Field Goal is successful
                    if card_value(chosen_offense_card) >= card_value(chosen_defense_card):
                        print("| ")
                        type_out_slow(f"|  St-Laurent lines up. Snap is good, ball is down, Kick is....")
                        print("| ")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |  o  |")
                        type_out_slow("|     |_____|")
                        type_out_slow("|________|_______ ")
                        commentary = jets_field_goal_higher_value(current_position)
                        type_out(commentary[0])
                        type_out(commentary[1])
                        print("|")
                        print("|  |_0_|")
                        print("|    |  ")
                        print("|   / \ ")
                        print("|  ------- ")
                        print("|  ===============  ")
                        type_out(f"|  Jets Last Play:  {chosen_defense_card} ")
                        computer_score += 3
                        update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
                        round_end = True
                        break
                    else:
                        print("| ")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |     |")
                        type_out_slow("|     |_____|")
                        type_out_slow("|________|_______ ")
                        type_out_slow("|                  ")
                        type_out("|  OH MY GOD BULLDOZER JUMPS OVER THE LINEMEN AND CRUSHES JUSTIN OH MY I HOPE HES OK..........")
                        type_out("|")
                        type_out_slow("|  ____ <==> ____")
                        type_out_slow("|  \\___\\(**)/___/")
                        type_out_slow("|   \\___|  |___/ ") 
                        type_out_slow("|       >  <      ")
                        type_out_slow("|       |__|      ")
                        type_out_slow("|        vv       ")
                        print("|") 
                        print("|  __0__")
                        print("|    |  ")
                        print("|   / \ ")
                        print("|  -------")
                        print("|  ===============  ")
                        type_out(f"|  Jets Last Play:  {chosen_defense_card} ")
                    update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)    
                    round_end = True
                    break              
                    
                              
        # PLAY LOGIC                              
        if first_turn == 'rec':
            
            if not player_qb_used:
                print(f"|  MVP BONUS: {player_qb_card}")
                print("|  ")
                print("|  -------  ")
                

            # Validate offense card input
            while True:
                chosen_offense_card = input("|  Call in your Offensive Play: ").strip().upper()
                if chosen_offense_card in player_hand:
                    break
                else:
                    print("|  We don't have that play ready.")

            player_hand.remove(chosen_offense_card)
            if not player_qb_used and chosen_offense_card[-1] == player_qb_card[-1]:
                use_qb = input("|  > Do you Want run the Call of the Raven ? (y/n): ").strip().lower()
            else:
                use_qb = 'n'
               # Computer (Jets) plays a defense card
            chosen_defense_card = choice(computer_hand)
            computer_hand.remove(chosen_defense_card)
            

                    # Before calling the function, determine who is on offense
            is_player_on_offense = True

 # Check if the offensive card's suit matches the QB card's suit, and if the QB card hasn't been used yet
            

            yards_this_play, superstar_used, team_that_used_superstar = calculate_yards_with_superstar(
                chosen_offense_card,
                chosen_defense_card,
                player_superstar_cards,
                computer_superstar_cards,
                is_player_on_offense
            )


 # Apply the QB card bonus if it was used
            if use_qb == 'y':
                qb_bonus_yards = card_value(player_qb_card)  # Replace with whatever logic you want for the QB bonus
                print(f"|    Al: Looks Like the Ravens have something special Called up here!")
                yards_this_play += qb_bonus_yards
                player_qb_used = True  # Mark the QB card as used and effectively discard it for the rest of the game


            


            if yards_this_play > current_position:
                al_michaels, chris_collinsworth = gain_touchdown(yards_this_play, chosen_offense_card[-1]) 
            elif yards_this_play > 20:
                al_michaels, chris_collinsworth = big_play_commentary(yards_this_play, chosen_offense_card[-1])
            elif yards_this_play > 0:
                al_michaels, chris_collinsworth = gain_yards_commentary(yards_this_play, chosen_offense_card[-1])
            elif yards_this_play == 0:
                al_michaels, chris_collinsworth = no_gain_commentary(chosen_offense_card[-1])
            else:
                al_michaels, chris_collinsworth = loss_yards_commentary(-yards_this_play, chosen_offense_card[-1])

            snap = snap_count()
            print("|  ")
            print("|  ===============")
            type_out("|  "+ snap)
            print("|  -------  ")
            print("|  -------")
            type_out("|  "+ al_michaels)
            print("|  -------  ")
            type_out("|  "+ chris_collinsworth)               
            type_out("|  ===============")
            type_out(f"|  Jets Last Play:  {chosen_defense_card} ")
            if superstar_used != "No Superstar Used":
                print("| ")
                type_out(f"|  Special Play Used ( {superstar_used} ) by {team_that_used_superstar}")
                
         
            print("|  -------")    
            print("|  ______________________")
            print("|   ---->  --->  -->  ->                        ")
            type_out(f"|   {yards_this_play} yards on the Play ")
            print("|  ----------------------")
            print("|")
           

            total_yards_gained += yards_this_play
            used_cards.append(chosen_offense_card)
            used_cards.append(chosen_defense_card)

            current_position -= yards_this_play
            yards_to_go -= yards_this_play
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
 
        else:
           

            
 # The computer chooses an offense card.
            chosen_offense_card = choice(computer_hand)
            computer_hand.remove(chosen_offense_card)

# Extracting the suit from the chosen card. The suit is the last character of the string.
            suit_of_chosen_card = chosen_offense_card[-1]
            print(f"|  Jets Play Type: {suit_of_chosen_card} ")
            print("| ")
 # Prompt the player to choose a defense card.
            while True:
                chosen_defense_card = input("|  Call your play, Coach: ").strip().upper()
                print("|  -------")
                if chosen_defense_card in player_hand:
                    break
                else:
                    print("|  We can't call that play right now...")

            player_hand.remove(chosen_defense_card)

 # Before calling the function, determine who is on offense
            is_player_on_offense = False

# When calling the function
            yards_this_play, superstar_used, team_that_used_superstar = calculate_yards_with_superstar(
                chosen_offense_card,
                chosen_defense_card,
                player_superstar_cards,
                computer_superstar_cards,
                is_player_on_offense
            )
            # Add commentary based on yards gained or lost

            if yards_this_play > 0:
                al_michaels, chris_collinsworth = defense_positive_yards_commentary(yards_this_play, chosen_offense_card[-1])
            elif yards_this_play == 0:
                al_michaels, chris_collinsworth = defense_no_gain_commentary(chosen_offense_card[-1])
            else: 
                al_michaels, chris_collinsworth = defense_same_suit_higher_value(-yards_this_play, chosen_offense_card[-1])
            snap = snap_count()
            print("|  ============")
            type_out("|  "+ snap)
            print("|  -------  ")
            print("|  -------")
            type_out("|  "+ al_michaels)
            print("|  -------  ")
            type_out("|  "+ chris_collinsworth)
            type_out("|  ===============")
            type_out("|  Jets Last Play: "+ chosen_offense_card)
            if superstar_used != "No Superstar Used":
                print("| ")
                type_out(f"|  Special Play Used ( {superstar_used} ) by {team_that_used_superstar}")
            print("|  -------")    
            print("|  ______________________")
            print("|   ---->  --->  -->  ->                        ")
            type_out(f"|   {yards_this_play} yards on the Play ")
            print("|  ----------------------")
            print("|")
            
#PLAY OUTCOME UPDATE
            total_yards_gained += yards_this_play
            used_cards.append(chosen_offense_card)
            used_cards.append(chosen_defense_card)

            current_position -= yards_this_play
            yards_to_go -= yards_this_play
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
 
 #SAFETY        
        if total_yards_gained <= -15:  # Adjust this to whatever yard line you start on.
            
            type_out_slow("|  THEY GOT HIM IN HIS ENDZONE ITS A SAFETY!! Defense scores 2 points.")
            print("|")
            print("|   /0\ ") 
            print("|    |  ")
            print("|   / \ ")
            print("|  -------")
            print("|  ===============  ")
            if first_turn == 'rec':
                computer_score += 2
            else:
                player_score += 2
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
            round_end = True
            break

#TOUCHDOWN
        if current_position <= 0:
            print("|")
            td_line = announce_touchdown(first_turn)
            type_out_slow(td_line)
            print("|")
            print("|  |_0_|")
            print("|    |  ")
            print("|   / \ ")
            print("|  -------  ")
            print("|  ===============  ")
            if first_turn == 'rec':
                player_score += 7
                if player_qb_used:
                    # Reset the QB card (MVP Bonus) so it can be used again.
                    player_qb_used = False
                    print("|  > Call of the Raven Ready")
            else:
                computer_score += 7
                type_out("|  WHAT A DRIVE BY THE JETS OFFENSE WOW!!!")

                
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)            
            round_end = True
            break
        
        if yards_this_play > 0 or yards_this_play < 0: 
            should_replenish_hand = True

        # FIRST DOWN
        if yards_to_go <= 0:
            print("|  ")
            one_liner = first_down_oneliners()
            type_out(one_liner)
            print("| ")
            
        # Reset the game state for the next set of downs
            yards_to_go = 10  # Reset yards needed for a first down                
            current_down = 1  # Reset the current down
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
            # Optionally, shuffle the deck and replenish both players' hands here if necessary
            if len(deck) < 8:
# Ensure QB cards don't get back into the deck
# Before reshuffling, make sure to exclude cards currently in player's and computer's hands
                deck = [f"{value}{suit}" for suit in suits for value in values 
                    if f"{value}{suit}" != player_qb_card 
                    and f"{value}{suit}" not in player_hand  # Exclude cards in player's hand
                    and f"{value}{suit}" not in computer_hand  # Exclude cards in computer's hand
                    and f"{value}{suit}" not in player_superstar_cards
                    and f"{value}{suit}" not in computer_superstar_cards]

                # Add back only those superstar cards that are not in anyone's hand
                deck += [card for card in player_superstar_cards if card not in player_hand]
                deck += [card for card in computer_superstar_cards if card not in computer_hand]
                deck += used_cards  # Add used cards back in
                used_cards = []  # Clear the list of used cards
                shuffle(deck)  # Shuffle the deck
                sideline_comment = sideline_commentary()
                type_out_slow(sideline_comment)# Sideline commentary
# Replenish the hand to make sure each player has 4 cards
            cards_needed = 4 - len(player_hand)
            player_hand += [deck.pop() for _ in range(cards_needed)]

            cards_needed = 4 - len(computer_hand)
            computer_hand += [deck.pop() for _ in range(cards_needed)]

            print("|")
            
        else:
            current_down += 1  # Move to the next down
            update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
       
            #TURN OVER ON DOWNS        
            if current_down > 4 and yards_to_go > 0:
                print("|  ")
                commentary = turnover_on_downs_commentary()
                type_out(commentary[0])
                type_out(commentary[1])
                update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
       
        
    if yards_this_play > 0 or yards_this_play < 0: 
                    should_replenish_hand = True                             
#END OF ROUND SCORE UPDATE
    print("|   ________________________")
    print("|   |-- LAC BOB  STADIUM --|  ")
    print("|   |______________________|")
    print("|   |  RAVENS   |   JETS   | ")
    type_out(f"|        {player_score}           {computer_score}     ")
    print("|   |___________|__________|")
    print("|   |--PLAYBOOK  FOOTBALL--|")
    print("|   |______________________|") 
    print("|        |            | ")  
    print("|________|____________|________ ") 
    update_dashboard(root, canvas, position_marker, first_down_marker, score_box, cur_do_di, yards_gained_rect, last_com_box, current_position, yards_to_go, current_down, player_score, computer_score, chosen_offense_card, yards_this_play, al_michaels, chris_collinsworth)
    # Usage inside your loop
    print("|")
    intro_line = introduce_offense(first_turn)  
    type_out(intro_line)
    print("|")
    
#ROUND END = SWTICH ROLES    
    if round_end: 
        first_turn = 'dif' if first_turn == 'rec' else 'rec'


    root.update()
    

#END OF GAME

type_out("    Al Michaels: AND THERE IT IS FOLKS, THATS THE GAME!!")
type_out("                 Thank you all for tunning into this thrilling game between Your Ravens and the visiting Jets")
type_out("                 Hope to see you all again soon, Thanks for playing Playbook Football")
print("  ")
input("  > Press Enter to exit ... ")





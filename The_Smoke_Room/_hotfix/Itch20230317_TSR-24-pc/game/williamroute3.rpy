label williamroute3:
scene black with slow_dissolve
play music "sfx/sportcrowd.mp3" fadein 7.0
window hide
scene wilch3a with slow_dissolve
pause
stop music fadeout 2.0
play sound "sfx/sportcrowd2.mp3"
$ renpy.pause(3.7, hard=True)
scene wilch3b with dis
pause 3.5
stop sound
scene black
play background "sfx/desertmorning.ogg" fadein 15.0
pause 4.0
window show
play music "music/quiet.ogg" fadein 5.0
"Is it getting dark already?"

scene echodesertnight with slow_dissolve
"Nine fifteen P.M."

"Which means it’s really seven fifteen."

"...Seven fifteen here, anyway."

"This watch has never been wrong before."

"Maybe a bit too flashy for me..."

"But never too fast."

"Never too slow."

"It just keeps on going from one day to the next."

"It’s even water-proof!"

"That’s what my first boss said, anyway."

"WATERPROOF, BY GEORGIA!"

scene echoroadnight with slow_dissolve

"God, he was so proud of that."

"As if anybody gives a shit if a wrist watch is waterproof or not."

"I feel my muzzle split into a grin."

"But only for a bit."

"People get nervous when I smile."

"That’s not the case with Sam, though."

"People around here have come to expect a sort of coldness from him."

"So when he smiles it looks sweet enough to thaw winter."

"But he’s in a bad mood again."

"It has to be because of Nik."

"There’s still some frostiness between the two of them."

"It ain't usual to see Nik that distant from Sam."

"But then again,  Sam had been treating us like strangers for the last few weeks."

"At least I know he’s not lying to me anymore, now."

"But I guess what’s good enough for me ain't always enough for Nik."

"It’s a good thing that that weasel didn’t come with us."

"The both of us don’t need to be more on edge."

"I’m glad he said no when Nik suggested he stay at the office."

"Because he really {i}should{/i} say no."

"At least, if he has any shame."

"He already put Sam in danger."

"Twice."
"If his mouth leads a goddamn lynch mob to Sam or Nik and gets them killed, I might up and join the next one."

"That bullet already broke the skin on the Byrnes boy."
"..."
"But he put himself in the way."
"That fox wants approval too much."
"Maybe..."
"Goddamn it."
"That’s not important now."
"What is important is who placed the hit and if they’ll place another."
"Huxley Greene wouldn’t leave his wife over a grudge from a stranger."
"He’s too controlling."
"So where did he go... and what did he do with the gun?"
"I just need to move faster and think about what I already know."
"...Christ."
"It’s hard to focus on anything when I’m annoyed."
wi "\"Hey, Sam?\""
"I hear him padding behind me, but his breath is louder than his footsteps."
wi "\"Can we talk about what you said at the lake a little more?\""
"I hear his footsteps stop."
m "\"Which thing?\""
wi "\"Let’s keep walking.\""
m "\"Okay.\""
m "\"But which thing, William?\""
wi "\"The thing about needing more excitement.\""
wi "\"You’ve been thinkin’ about leaving town for a long time, haven’t you?\""
wi "\"Even before the night you told me about earlier.\""
m "\"...And if I have?\""
"His tone has an edge in it again."
wi "\"I’m just curious why.\""
wi "\"Things aren’t easier just because you go someplace else.\""
m "\"It ain't about things bein’ easy.\""
m "\"It’s just somethin’ about this place.\""
"He lowered his voice."
m "\"And the brothel.\""
m "\"Most folks I talk to there feel the same way.\""
m "\"Like this is a place you move to, you stay for a while, and then you keep on moving once you scrap together enough money.\""
m "\"Everybody’s just constantly coming and going.\""
m "\"Sometimes it feels like the whole goddamn city is a glorified train station and the only people who stay behind are the ones who lose their fare.\""
wi "\"Me and Nik aren’t stuck.\""
m "\"Nik will be gone the moment he finds gold.\""
"I think he deserves a little more credit than that."
m "\"And you’re out of a job the moment the public turns against you.\""
m "\"You plannin’ on keeping that badge forever?\""
m "\"Or did I miss you building houses on a day I wasn't paying enough attention?\""

m "\"Because if you ain't, you’re on your way out too as far as I’m concerned.\""
"What a mouth."
wi "\"There’s not a whole lot of competition for this job in this location, Sam.\""
wi "\"But you're right. If I’m out, I’m out.\""
wi "\"That being said--as far as I’m concerned, pessimism is only for losers.\""
m "\"Whatever, William.\""
play music "music/spiraling.ogg" fadeout 4.0 fadein 5.0
"So that’s it, then?"
"This is just a transitional period for you?"
"You probably planned to leave before you even arrived."
"I can’t completely blame you."
"My life has only ever been transitional too."
"Always coming."
"Always going."
scene white with slow_dissolve
scene chicagotrain with slow_dissolve
"From place to place, in one of the most transitional places in the country."
$renpy.sound.set_volume(0.2, delay=0.0, channel='sound')
play sound "sfx/l-train.mp3"
"I remember seeing hundreds of new faces I couldn’t recognize, every new day."
"Our lives shared briefly."
"Our time cut short chronically."
"Viciously."
"By the L-train."
play sound "sfx/l-train.mp3"
"By the streets."
"By the churches, the businesses, the people."
"You find yourself begging for the transitions to end."
"No matter who you are."
"Or what you do."
stop sound
"Or what you live."
"There’s always another train stop."
"Tick, tock, says the clock."
scene chicagostadium with slow_dissolve
"How much of my life have I spent, thinking it was another transition?"
play sound "sfx/baseballcrowd.mp3"
"How many baseball games did I end in my head early because I knew my team wasn’t going to win?"
"Too damn many."
hat "\"William?\""
"But it doesn’t matter if I’m here or there."
stop sound
scene black with slow_dissolve
scene chicagobar with slow_dissolve
hat "\"You have a thoughtful look on your face.\""
"Because the transitions?"
hat "\"I want to know what you’re thinking about.\""
"They never stop."
wi "\"I’m just enjoying my drink.\""
"Despite how much you want them to stop with you."
hat "\"You never enjoy your drink.\""
"Because they can’t."
wi "\"Today I am.\""
"Your life transitions still, no matter where in time your mind is stuck."
wi "\"I have something I have to tell you.\""
show sam talking dark2 with dissolve
stop music fadeout 3.0
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
m "\"Then what is it?\""
show sam dark2 with dis
"Sam?"
"What is he..."
show sam surprised dark2 with dis
m "\"Hello?\""
window hide
show sam surprised at center,nightbrown
show bg echoroadnight behind sam
with medium_dissolve
play music "music/long-nights.mp3" fadeout 4.0 fadein 5.0
window show
"We’re staring at the front door of the department."
"I could have sworn that we still had half a mile to walk before we got here."
wi "\"I think you should stay here for the night again.\""
show sam eyes talking with dissolve
m "\"That’s kind, but I have my own bed.\""
show sam eyes with dis
wi "\"I meant that I’d pay.\""
show sam surprised with dis
m "\"Oh.\""
show sam talking with dis
m "\"I’ll have to increase the rate to justify spending the night.\""
show sam with dis
wi "\"Done.\""
show sam surprised with dis
m "\"...I didn’t say how much yet.\""
wi "\"Better described indoors then, yeah?\""
show sam eyes talking with dis
m "\"...yeah...\""
show sam eyes with dis
"I finally manage to fish the goddamn keys out of my pocket and fit them in the lock."
show sam with dis
"I, ah, would feel more graceful if I weren’t bumping into the lock."
"Won’t be damned by how stiff my gait is when I’m inside."
scene black with fade
scene jailnight with dissolve
show sam surprised at center,prisonnight with dissolve
m "\"We sleeping near the jail again?\""
wi "\"No.\""
wi "\"My bedroom. Upstairs.\""
show sam smile with dis
m "\"Oh.\""
show sam talking with dis
m "\"I’ve never seen it.\""
show sam with dis
wi "\"It’s messy.\""
show sam laugh with hpunch
m "\"I don’t mind.\""
show sam smile with dissolve
wi "\"I do.\""
wi "\"But it can’t be helped.\""
scene black with fade
"When we climb the stairs and reach the foyer, the tobacco smell is cloying."
scene willapartmentnight with dissolve
show sam eyes talking at center,willroom1night with dis
m "\"How much do you smoke, William?\""
show sam eyes with dis
wi "\"That ain't my fault, though.\""
"At least not entirely."
"The place reeked of cigarettes before I moved in."
"Pipe smoke smells a hell of a lot sweeter."
show sam eyes talking with dis
m "\"I’ll get used to it.\""
show sam eyes with dis
m "\"You usually reek of somethin’ or other.\""
show sam with dis
wi "\"You’re no bed of flowers yourself when you get riled up.\""
show sam smile with dis
m "\"At least I use cologne.\""
wi "\"You mean perfume.\""
show sam talking with dis
m "\"I mean cologne, William.\""
show sam with dis
"Soap and water’s just fine."
"I open the cupboard and fetch a glass and the whiskey bottle."
wi "\"Need a drink before we start?\""
show sam talking with dis
m "\"Not much in the mood to drink.\""
show sam with dis
wi "\"Suit yourself.\""
"I pour myself a shot and wash it down."
"The burn wakes me up a bit."
"The pressure in my pants is starting to hurt."
wi "\"My bedroom.\""
scene black with fade
stop music fadeout 3.0
"I jerk my head and he follows me down the hall."
scene willbedroomlight with dissolve
show sam eyes talking at center,willroom2night with dis
m "\"We don’t have to rush if I’m gonna be here all night, you know.\""
show sam eyes with dis
"I’m rushing?"
show sam with dis
wi "\"Guess I’m just used to having somewhere else to be.\""
wi "\"And there aren’t as many windows in my room.\""
"I feel the heat rise from my body when I start to strip."
"I can smell Sam’s perfume when he follows my lead, but there’s still the trace of his own scent underneath."

"We both take a seat on my bed, and the tension in the air between us is a bit thick."
wi "\"You uh... gonna get on your knees again soon?\""
show sam talking with dis
m "\"Could do.\""
show sam smile with dis
m "\"But I figured we could try something else since this is the first time you’ve had more than an hour with me.\""
"The heat is rushing between my legs."
wi "\"Like putting me inside you?\""
show sam talking with dis
m "\"You have a condom?\""
show sam smile with dis
"He’s making me too damn embarrassed."
wi "\"You think I have that sort of thing just lying around?\""
show sam talking with dis
m "\"Dumb question I guess.\""
show sam smile with dis
"He put his hand between my lap."
show sam talking with dis
m "\"I’m the only one who really touches this, aren’t I?\""
show sam smile with dis
wi "\"...’m fine with that.\""
"He slipped his hand under the tent in my trousers and touched me."
"And squeezed."
"It was a slow, slimy sound."
show sam eyes talking with dis
m "\"It’s a miracle you don’t have to buy many slacks.\""
show sam eyes with dis
m "\"Seems like you ought to have ruined them by now.\""
show sam smile with dis
wi "\"It’s your fault.\""
show sam talking with dis
m "\"Nah.\""
show sam smile with dis
"He curled his digits and stroked me once."
show sam talking with dis
m "\"This is all you.\""
show sam smile with dis
wi "\"And how do you know that?\""
show sam eyes talking with dis
m "\"Because you’re the one who brought up burying it in me.\""
"Huh."
show sam smile with dis
"I guess it slipped off my tongue."
wi "\"Might be just the alcohol talking.\""
show sam talking with dis
m "\"Then I guess you don’t want to be inside me.\""
show sam with dis
wi "\"I didn’t say that.\""
show sam talking with dis
m "\"So what do you want?\""
show sam smile with dis
"I exhale."
"I don’t want to deal with awkward small talk."
"If we’re gonna talk like this, I guess we’re gonna talk for real."
show sam shocked with vpunch
wi "\"How much shame do you feel when a man finishes in you?\""
show sam surprised with dissolve
"Sam stopped stroking me."
show sam with dis
"He glared."
show sam talking with dis
m "\"Why do you want to know?\""
show sam with dis
wi "\"I just want to know what goes through your head when you do all this.\""
wi "\"Maybe so I can better understand myself.\""
wi "\"So let’s talk about it... man to man.\""
show sam surprised with dis
"His glare turned into a surprised look."
show sam talking with dis
m "\"Never thought I’d be talking about this with you.\""
show sam surprised with dis
wi "\"Well, me neither, so fair.\""
"...but I need to know."
show sam eyes with dis
m "\"I always feel a little foul after doing the deed, but the build up is heaven.\""
show sam eyes talking with dis
m "\"And the need comes often.\""
show sam eyes with dis
wi "\"Does the shame ever feel good?\""
show sam surprised with dis
m "\"What makes you ask that?\""
wi "\"For me, I think the pain and the pleasure start to blur sometimes.\""
wi "\"The depravity, I mean.\""
show sam eyes with dis
wi "\"You ever feel like the more somebody tells us what’s right or wrong, the more satisfying it feels to just give them the finger?\""
wi "\"Especially because we know it feels good, and it’s not hurting nobody?\""
show sam eyes talking with dis
m "\"I understand.\""
show sam eyes with dis
show sam eyes talking with dis
m "\"That’s how I feel every time I break one of your laws.\""
show sam eyes with dis
"That’s not how the government works."
wi "\"They ain't my goddamn laws, Sam.\""
show sam eyes talking with dis
m "\"Whatever you say, William.\""
show sam eyes with dis
show sam talking with dis
m "\"But I want to understand more of what you mean.\""
show sam with dis
show sam talking with dis
m "\"About shame and pleasure blurring.\""
show sam with dis
"Oh."
"Shit."
"Maybe I told him too much."
wi "\"I don’t think you want to go through that, Sam.\""
show sam surprised with dis
m "\"Well, maybe I already do... to some extent.\""
show sam eyes talking with dis
m "\"Help me explore that, a bit.\""
show sam eyes with dis
wi "\"You said you don’t have condoms.\""
show sam laugh with dissolve
"He let out a short laugh."
show sam talking with dissolve
m "\"You don’t have any bumps on your cock and you fuck nobody.\""
show sam with dis
show sam talking with dis
m "\"I think I’ll be fine.\""
show sam surprised with dis
"His eyes shift away and he puts on a sheepish expression."
show sam talking with dis
m "\"...Your stove work?\""
show sam surprised with dis
wi "\"Yeah. There’s wood in the living room.\""
show sam talking with dis
m "\"What about rags?\""
show sam surprised with dis
show sam talking with dis
m "\"I need to make sure I’m clean.\""
show sam surprised with dis
"Christ on a cracker."
"What debonair bullshit did I walk myself into now?"
wi "\"Cloth scraps are under the sink.\""
hide sam with dissolve
"He’s already rushing out of the bedroom."
"I sigh, feeling my shaft twitch in my pants."
"That one... always has to make himself immaculate, doesn’t he?"
"Can we just go, Sam?"
"..."
"Goddamn it."
"I read a small piece of literature on the city’s zoning laws to kill my erection while I hear pots and pans banging in the kitchen along with some swears."
"He’s lucky the sink works here."
"I wait for nearly 10 minutes before I hear some sloshing around and a cloth being wrung."
show sam eyes s at center,willroom2night with dissolve
"And five more minutes before he’s finally back in the room."
wi "\"Was all that really necessary?\""
show sam talking s with dis
m "\"I assure you. It was for what we’re about to do.\""
show sam s with dis
wi "\"Fine. I won’t make a fuss, then.\""
"He took a seat next to me, and I hooked my arm around his waist."
"His hand was on my thigh again."
show sam talking s with dis
m "\"Talk me through what it’s like when I touch you.\""
show sam smile s with dis
"Jesus."
"This is hard."
wi "\"Feels like I’m touching a friend in a way I shouldn’t be touching them.\""
wi "\"And there’s a pit in my stomach.\""
wi "\"Like anybody could open the door at any moment and shout so loud that it makes my ears ring.\""
show sam talking s with dis
m "\"That scare you?\""
show sam smile s with dis
wi "\"Should.\""
wi "\"But somehow, the look of disgust on their faces makes me want to rip off your pants and smile back while they watch, and they can’t do anything about it.\""
show sam talking s with dis
m "\"They can’t do a damn thing if they ain't real.\""
show sam smile s with dis
wi "\"And they have to deal with me making your big damn dick swell up in your trousers while the smell fills the room.\""
show sam eyes s with dis
m "\"The way you describe this stuff sticks with me...\""
m "\"...even though you make it sound a little foul.\""

show sam surprised s with dis
wi "\"Men are foul, Sam.\""
"I stick my tongue down his throat and he’s all too receptive."
"He savors it, but I pull away with a soft smack."
wi "\"Filthy, even.\""
show sam eyes s with dis
"I give more tongue."
"He sucks on it again. Like he’s nursing on it."
"Then I pull off again."
wi "\"I think I’m at peace with that, at least.\""
"His chest is heaving and his throat is starting to rumble."
show sam eyes talking s with dis
m "\"Is that why you can’t keep your hands off me?\""
show sam eyes s with dis
show sam eyes talking s with dis
m "\"Because you know it’s dirty?\""
show sam eyes s with dis
"I feel my heartbeat in my shaft, pulsing with angry spurts of warm liquid."
wi "\"Because I want to empty into you more than I want to make another life with this.\""
wi "\"And I want the energy from that life to change you from the inside out.\""
show sam eyes talking s with dis
m "\"...change me, how?\""
show sam eyes s with dis
"Maybe I’m going too far."
show sam s with dis
wi "\"Do you really want me to?\""
show sam talking s with dis
m "\"I think I do.\""
show sam s with dis
"I don’t think I can tell you."
"I just have to show you."
show sam surprised s with dis
wi "\"Okay.\""
"I stand up and I start to take the rest of my clothes off."
"My pants. My garters. My undergarments."
"A bit of me drips to the floor."
"I’ll clean it up later."
wi "\"First thing I’ll ask is... what else do you have to prep for to make yourself comfy enough for this?\""
"I cup my paw and bring it over my cock, forcing one slow thrust through it."
show sam smile s with dis
m "\"I hope you don’t mind but I saw you had some oil in the kitchen.\""
"He uncorked the stopper, poured some of the slick contents in his paw, and smeared it on me."
show sam talking s with dis
m "\"We’ll have to use more when we’re ready, but that’s a good start.\""
show sam smile s with dis
"I pick up my underwear and put them on the bed."
"Then I take a handkerchief out of the drawer."
"I fetch a bit of rope, too."
show sam surprised s with dis
"He looks a little worried when I show him that."
"I feel guilt for what I’m about to do."
wi "\"Are you sure you want me to keep going?\""
show sam eyes s with dis
show sam surprised s with dis
show sam eyes s with dis
show sam surprised s with dis
"He pauses this time."
"I think he’s still relaxed, but I can see that he’s still hard with his pants on."
#New
show sam s with dis
"That’s good."
show sam talking s with dis
m "\"I meant it when I said it.\""
show sam surprised s with dis
wi "\"Then put your wrists behind your back.\""
"My heartbeat is pounding in my throat."
"Is this what you feel like all the time, Sam?"
show sam s with dis
"But he obeys me."
"Good boy."
show sam eyes s with dis
wi "\"I’m going to put these ropes on your wrists to make you feel trapped.\""
"I shuffle up behind him, dangling a line of pre while I approach him."
show sam s with dis
"The ropes aren’t as soft as they probably should be."
"He might get burns if he struggles too hard, but his fur is pretty thick."
wi "\"They’re going on now.\""
show sam annoyed talking s with dis
m "\"Just do it...\""
show sam smile s with dis
wi "\"Alright. Goddamn...\""
"I loop them around as he holds still for me."
show sam s with dis
"I tied it in a way that I know he can’t get out of."
wi "\"Comfortable?\""
show sam talking s with dis
m "\"As much as I can be with rope around my wrists.\""
show sam s with dis
wi "\"Okay.\""
wi "\"I wanted you to feel trapped while you’re hard.\""
wi "\"Do you?\""
show sam eyes talking s with dis
m "\"Aside from the rope, not really.\""
show sam s with dis
wi "\"I think I’m gonna loosen you up.\""
show sam smile s with dis
"Sam hummed."
show sam talking s with dis
m "\"You know how?\""
show sam smile s with dis
"He thinks I’ve never teased an asshole before."
"That’s cute."
wi "\"Course I know how. Lift those legs...\""
"He struggles to adjust himself properly without the use of his arms for leverage."
"I get some of that oil onto my middle finger until I can see it shine."
show sam talking s with dis
m "\"I don’t really need a finger, you know.\""
show sam s with dis
wi "\"Relax. It loosens the muscles.\""
wi "\"Makes going in a hell of a lot more comfortable for both of us.\""
hide sam with dissolve
show sam surprised d at center,willroom2night with dissolve
"He lies back and lifts his legs in the air, looking a little uncomfortable."
"Ugh."
show sam d with dis
wi "\"Don’t worry. I won’t be a priss about it.\""
"I pour some of the oil in my hands and rub it between my digits."
"Then I go to the bed and sit on my knees and grab him by the ankles, lifting them up in the air."
hide sam with dissolve
scene wilcg5 with slow_dissolve
"I’ve never been this close to his balls before."
"And beneath them?"
"He can brag about wearing perfume as much as he wants, but that smell is all him."
"Even lower I see that pale ring of muscle."
"I prod at it with my middle digit."
"The fur on his legs stand up when I do."
"Then I slide against it, curling into a hook for an easy opening."
wi "\"...and there it goes.\""
"He sucks on his teeth as the pressure gives way, and I slide on into him."
"And he groans."
wi "\"Now I’ll pull out slow.\""
"It’s easy enough to slip out of him."
"He sighs, like he’s steeling himself for something."
wi "\"Going back in.\""
"I go up to the knuckle and he grits his teeth."
wi "\"I just have to keep this up and it’ll tire you out.\""
wi "\"And you won’t clench when I’m sliding in.\""
"The next time my finger goes in I curl upward."
"He looks back at me with something close to panic in his eyes as his length is the one going stiff now."
wi "\"I guess I found your special spot too, huh?\""
m "\"I didn’t think you’d know about that.\""
wi "\"Course I do.\""
wi "\"I knew there had to be another reason why men put things up there.\""
wi "\"Some even get addicted to it.\""
"Every curl just makes him bigger."
wi "\"You think of yourself as one of those people, Sam?\""
"I don’t need to hear him say yes or no, really."
"He loves being a slut."
"Can smell it on him and see it in his eyes."
"And I’ve made him really big."
m "\"I don’t really think much on it.\""
wi "\"Then don’t think.\""
wi "\"Your body already knows what it wants, don’t it?\""
m "\"Yeah.\""
wi "\"So what does it want right now, Sam?\""
"He grunts and pushes back against me as best as he can and his tip starts to leak, too."
m "\"The real deal.\""
"I have to watch him for a bit."
"His chest is heaving."
"He’s leaking uncontrollably."
"He reeks with need."
"I envy him."
"Maybe he’s starting to understand."
"Then I slide away and grab him by the arm."
wi "\"Stand up.\""
"He complies, and sprays from his tip fall to the floor."
"I grab my undergarments on the bed and pick them up."
wi "\"Open your mouth.\""
m "\"Why--\""
"That’s all I need to stuff it in."
wi "\"Because a bandana alone isn’t enough to act like a gag.\""
"And you’ll only be able to focus on how I taste when I do all these things to you."
"I wrap the scarf around his head."
wi "\"This will help you remember not to spit anything out while you yell.\""
"I bend him over the bed."
"Then I hook my finger in his ass again."
"I wiggle it to make him yell-- as much as he can with the dampened rag."
wi "\"It’s good that you’re yelling.\""
wi "\"You can do it as much as you like and nobody will hear it.\""
"I grab the length of my cock to the opening of his rear and slide my tip against it."
wi "\"I think our bodies were meant to scream, sometimes.\""
"My tip is pressing beneath his tail right now."
"I can feel the muscles about to give way."
wi "\"Don’t yell that you want it.\""
wi "\"Yell out because you want it.\""
scene wilcg4 with slow_dissolve
"And when he shifts, and I start to sink in, he does what I say."
"I hilt my cock in his pert cheeks until I feel my balls touch his, and then I roll my hips."
"I go in and out, just like my finger did, and it don’t take long for the both of us to feel too warm."
"So I slip on out and roll him over, feeling how heavy he is."
wi "\"We’re like prisoners in these bodies, Sam.\""
wi "\"Doesn’t matter what the heart or the mind really wants.\""
"His fat, monster of a cock is just drumming against his belly, now."
"Like he’s hurting for a release."
"But I can’t let him have that yet if he wants to understand."
wi "\"Our instinct drives us toward a particular direction.\""
"I grab his ankles and lift them again."
"Then I walk forward again, letting gravity and his legs bear my weight as I sink into him another time, deeper than before."
"Sweat rolls down my back as I move in him."
wi "\"See? It’s always about control.\""
"I roll my hips into him, inside of him."
"Then I clamp my mouth over his neck and bite into his scruff."
"I feel him writhe under me, and I can’t help but smile."
wi "\"The control your own body has over you.\""
"Faster."
wi "\"The control others have over your needs and your feelings.\""
"Harder."
wi "\"And you. Just have. To take it.\""
"He cries out when I lap his nipples too beneath the fur, making his head thrash left and right."
"Please him like I would a woman, though every cell in my body knows he isn’t."
"And doesn’t want him to be."
"Because I see him jab the air every time I dip in deep."
"I look down between his legs, deeper into his prick's drooling eye, sinking as more of my body weight shifts over him."
scene willbedroomlight with dissolve
"Reminding me what my instinct demands."

menu willbedchoice:
    "..."
    "Take care of that, Cocksucker.":
        $ SW_Points +=1
        "Well... fuck that idea, I ain't gonna suck it."

        "But goddamn is this the slimiest he’s ever made himself."

        "And if it goes like that too much longer, it might turn blue."

        "Well..."

        "He’s a good boy, though."

        "And I’ve touched my own, plenty."

        "And besides..."

        wi "\"Bit fucked up when it’s somebody else who decides what your body can do, ain't it?\""
        "I smear my paw over the pre on his prick and then rub it on his nose."
        wi "\"You have no control over that.\""
        "The stickiness is so fucking loud when I start to stroke him."
        wi "\"As good as that feels, it’s still terrifying.\""
        "The more I make his prick shine, the more of a mess the tip makes."
        wi "\"So the two can start to blend.\""
        "I wipe the excess on his abs and the rest of it around his length and balls."
        wi "\"You get it now?\""
        "His eyes close shut and the muffled scream is lengthy this time."
        "Wait a minute, is he already..."
        wi "\"Shit!\""
        "He’s blasting off like a cannon and it’s too late to move my hands."
        "There’s already more than three bursts of it coating my paw, the rest hiting him beneath the chin."
        "The smell is pungent, and it’s familiar enough to my own that I..."
        "Feel the pressure in my balls pull back."
        "And jolts fire off in my body."
        wi "\"Shiiiiit!\""
        "I’m finishing in him, filling him up, without even any protection..."
        "And that makes me bury myself deeper."
        "Like I’m stuck in him."
        "And we can be trapped here together in this... well, this mess."
        "...the hell did he do to my paw?"
        show handwil cum at center,willroom2night with dissolve
        "Christ."
        hide handwil with dissolve
        "There aren’t any rags in the kitchen."
        "His eyes flick to his gag impatiently, so I untie the bandana."
        "I cringe a bit as I stain it."
        "He pushes my underwear out of his mouth with his tongue and lets it slop to the floor, then starts taking deep breaths."
        m "\"Mind letting me loose, William?\""
        wi "\"Once I figure out where I can wipe my hand.\""
        m "\"You could always lick it clean.\""
        wi "\"Hell no.\""
        scene willapartmentnight with dissolve
        "I go out to fetch some newspaper from the living room."
        "It’s not perfect, but it’ll do for the moment."
        show handwil ohno at center,willroom1night with dissolve
        "Shit, there’s terrible opinions sticking to my hand now."
        scene willbedroomlight with dissolve
        "My paws are as clean as they're gonna get, so I undo the bonds of rope behind his hands and pull the coils off of his wrist."
        wi "\"Sorry.\""
        "That’s all I can really say about this."
        "I really did go too damn far, this time."
        "But then Sam hooks his arms around my neck and pulls me in."
        m "\"Don’t be.\""
        "And he makes me taste myself on his tongue."
        "Making me remember what I used to do between my legs in private when I bent over far enough."



    "He’ll be able to use his own hands once I’m done with this.":
        "I close my eyes and think about my own dick more than his."
        "And I picture it firing off, louder than any pistol, hotter than any bullet."
        "Putting this embarrassing act to a close."
        "And I feel myself pumping into him, as clarity and relaxation wash over me."
        "Then I pull out of him and undo his bonds."
        "He doesn’t bother to take off the gag before he finished himself off."
        "I look away to give him some decency, but I can still hear him finish."

scene black with slow_dissolve
stop background fadeout 3.0
"...Christ, that was exhausting."
"What the hell got into me last night?"
play sound "sfx/knock.ogg"
"Somebody’s banging on the door to the office downstairs."
scene willbedroomnight with slow_dissolve
stop sound
play music "music/typical day.ogg" fadeout 4.0 fadein 5.0
"It’s morning?"
"Shit."
"I don’t remember us falling asleep."
"But we did so much I must’ve conked out."
"Sam is on his side with his back to me and his tail resting between my legs."
"I check my watch."
"It’s almost seven A.M. there, so five A.M..."
"Shit."
"I touch my temples and rub."
"Then I shake his shoulder."
wi "\"Time to wake up, sunshine.\""
m "\"Already am.\""
"What the..."
"I stop shaking."
wi "\"And when did you get up?\""
m "\"Can’t be sure.\""
m "\"Feels like hours ago.\""
wi "\"You get enough shut-eye?\""
m "\"Enough. Yeah.\""
m "\"Say... William?\""
"He still hasn’t turned around yet."
"He’s looking up the walls."
m "\"Are the walls in this building hollow?\""
"Bit of a queer thing to say."
"...especially first thing in the morning."
wi "\"Sounds don’t get out too well, so they’re insulated with somethin’.\""
wi "\"Why do you ask?\""
show sam sad n night with dissolve
"He turned around, still looking up."
show sam sad talking n night with dis
m "\"Heard things crawling around.\""
show sam sad n night with dis
show sam sad talking n night with dis
m "\"Sometimes it sounded like somethin’ was gonna break out.\""
show sam sad n night with dis
"Sometimes I have to wonder if his head is completely okay."
"That Jack fellah really fucked him up."
show sam n night with dis
wi "\"...See any cracks in the walls, then?\""
show sam talking n night with dis
m "\"No.\""
show sam n night with dis
show sam sad talking n night with dis
m "\"At least, I don’t think so.\""
show sam n night with dis
wi "\"Then tell me if you do. \""
show sam sad n night with dis
"I glide my hand over his shoulder but take it back as he sits up."
"His back is hunched and his head is hanging low."
"He could probably use some water."
play sound "sfx/knock.ogg"
show sam surprised n night with dis
"Jesus."
"That banging’s just getting louder."
stop sound
"It better not be Todd."
"I peek through the shutters and guard the sunlight from my eyesight."
"It’s him."
"I’ve told him a dozen times where the spare key to the office is."
"Though it’s not like I can complain."
"I just slept in and got caught with my pants down, so to speak."
"...let’s fix that."
"I get dressed as quickly as I can."
"Then I remember that I was going to get Sam some water."
"...Todd can wait a little longer."
scene willapartmentnight with dissolve
"I fetch a glass in the living room, fill it up, then bring it to him."
scene willbedroomnight
show sam n night
with dissolve
wi "\"Drink. Some fluid will help you wake up.\""
play sound "sfx/knock.ogg"
show sam surprised n night with dis
pause
show sam surprised talking n night with dis
m "\"Who’s makin’ that fuss outside?\""
show sam surprised n night with dis
wi "\"It’s just Todd.\""
stop sound
show sam talking n night with dis
m "\"Sounds urgent.\""
show sam n night with dis
"It’s probably not."
"Because if it were urgent he’d remember where I put the spare key."
wi "\"Might be.\""
show sam annoyed n night with dis
wi "\"But I’m not letting you out of my sight until you finish that glass of water.\""
"He glares, then tips his head back to chug it."
"A bit cheeky, but if it gets the job done..."
show sam annoyed talking n night with dis
m "\"There. All done.\""
show sam annoyed n night with dis
show sam eyes smile n night with dis
show sam annoyed n night with dis
"He pushes the covers off and plants his feet on the floor a little stiffly, then blinks."
"His eyes aren’t rolling back or drifting out of focus, and his pupils aren’t contracting and dilating, so that’s a relief."
show sam annoyed talking n night with dis
m "\"You done staring me down, Sheriff?\""
show sam annoyed n night with dis
"Is he really going to judge me for staring as if asking if somebody’s walls are hollow or not is normal?"
play sound "sfx/knock.ogg"
"That’s the kind of stuff that makes me worry about you, Sam."
show sam n night with dis
wi "\"No need. My gaze had its fill of you last night.\""
stop sound
show sam talking n night with dis
m "\"Must have been hard for you.\""
show sam n night with dis
play sound "sfx/knock.ogg"
"Todd’s still banging on the door."
show sam talking n night with dis
m "\"You gonna get that?\""
stop sound
show sam n night with dis
wi "\"Not until you’re dressed and ready to go downstairs.\""
show sam eyes talking n night with dis
m "\"I’ll be quick about that.\""
show sam eyes smile n night with dis
hide sam with dissolve
pause 0.45
show sam s night with dissolve
"He steps over his undergarments and drawers on the floor and tugs the fabric up his legs."
wi "\"So you’re the one volunteering to get the door, then?\""
show sam eyes s night with dis
"He waddles towards the shades and tilts his head."
play sound "sfx/knock.ogg"
pause
show sam talking s night with dis
m "\"Nah.\""
show sam annoyed s night with dis
stop sound
wi "\"Then hurry up. I have to lock the door behind me.\""
show sam annoyed night with dissolve
"He’s mumbling about eating his ass under his breath, as if I can’t hear him while he snatches his shirt, tucks it in, and then hooks his suspenders over his shoulders."
scene black with fade
stop music fadeout 3.0
"Finally he’s ready to go, and I lock the door on the way out."
scene jailnight with dissolve
play sound "sfx/knock.ogg"
pause
"Todd’s still pounding on the door like a mad man."
stop sound
wi "\"Hold your goddamn horses, I’m coming.\""
scene black with fade
"I let him finish his flurry of blows before turning the knob, letting the door creak open."
scene echoroadnight with dissolve
show tod talking at center,nightbrown with dissolve
to "\"Well there you are, sheriff.\""
show tod with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"He looks a bit of a mess."
show tod surprised with dis
wi "\"Did you forget about the key, Todd?\""
show tod sad with dis
to "\"Oh, right.\""
show tod arms happy with dissolve
to "\"Well that ain't important right now.\""
show tod surprised with dissolve
to "\"I needed to tell you that I met Huxley Greene.\""
"Well, that’s good news at least."
wi "\"Oh, yeah? And what sort of state was he in.\""
show tod sad with dis
to "\"Well, none too good, considering he didn’t have a head.\""
"What?!"
show tod surprised with dis
wi "\"You mean he’s dead?\""
show tod talking with dis
to "\"Well that’s what the wallet in his pocket said, but I brought his body just to make sure.\""
show tod surprised with dis
"I grabbed his shoulder to move him aside and see the carcass-sized pillow case."
wi "\"You dragged this all the way here?!\""
show tod talking with dis
to "\"I figured you would like to look at him before the bugs and buzzards got the rest of him.\""
show tod surprised with dis
"I lift my shirt up over my nose and crouch down, then lift the sheets off of the body."
"It’s frozen, so the smell isn’t as bad as it could be, but there are pieces of fur and flesh missing."
"Those are definitely his clothes, though-- I’d recognize Marcy’s stitchwork anywhere."
"And hard to mistake the thick, bald rat tail that looks more like a pale worm than anything else."
wi "\"Yeah. That’s probably him.\""
wi "\"Let’s haul him inside.\""
show tod annoyed with dis
to "\"Yes sir.\""
scene black with fade
"Todd carries one side and I carry the other into that open jail cell we had used the other night for the same purpose."
scene echoroadnight with slow_dissolve
show tod surprised at center,nightbrown with dissolve
"I check outside again to see if we’ve dropped anything, but there’s nothing much to look at."
wi "\"I would have thought this man was lying low or hopped a train out of town.\""
wi "\"But something like this in a place like here?\""
wi "\"It’s just yet another thing that don’t make much sense.\""
show tod sad with dis
to "\"Well... you know what they say...\""
show tod talking with dis
to "\"When it’s your time, it’s your time.\""
show tod surprised with dis
wi "\"Who’s they exactly?\""
show tod arms happy with dissolve
to "\"Some Jesuits down the street.\""
wi "\"The man had his head ripped off. He didn’t die of old age.\""
show tod surprised with dissolve
to "\"Well I already know that.\""
wi "\"I mean that if he’s been dead for, let’s be honest, what looks like at least a few days...\""
wi "\"Then he would have had to be real quick about issuing a hit on Mr. Tibbits.\""
wi "\"...See what I’m saying?\""
show tod eyes happy with dis
show tod surprised with dis
"Todd blinks at me."
"Come on, you can put it together."
show tod talking with dis
to "\"Are you saying he just hated what he couldn’t understand?\""
show tod with dis
wi "\"...I’m saying he might not have placed the hit, Todd.\""
show tod sad with dis
to "\"If not him, then who?\""
show tod surprised with dis
wi "\"Now that’s a great question, Todd.\""
$ renpy.notify("Notebook updated.")
$ quick_menu = False
$ quick_menu_will = True
$ unlocked_journal_pages += 1
$ willnote = True
wi "\"This is why I always bring my notebook with me when I'm keeping track of my thoughts.\""
$ renpy.notify("Notebook updated.")
$ unlocked_journal_pages += 1
$ current_journal_page = 1
wi "\"You ought to start picking up the practice yourself.\""
wi "\"Now what do you say we do what we should have done in the first place and pay Mr. Tibbits a visit?\""
hide tod with dissolve

"I turn and see the red of Sam’s eye staring from my office."
show sam at center,nightbrown with dissolve
wi "\"We’ll be back soon. Keep the interior locked.\""
show sam eyes talking with dis
m "\"...Okay.\""
show sam eyes with dis
hide sam with dissolve
"He disappeared behind the window and we heard the heavy lock of the door click."
wi "\"Shouldn’t be long.\""
show tod at center,nightbrown with dissolve
"I don’t know if that’s true, but he is just next door."
show tod surprised with dis
to "\"So wait. What’s Sam doing in there at this hour?\""
wi "\"Debriefing.\""
"Technically not wrong."
show tod happy arms with dissolve
to "\"Gee. I guess he does work late hours, doesn’t he?\""
wi "\"He works hard.\""
show tod eyes happy with dissolve
to "\"And there’s no shame in that.\""
show tod surprised with dissolve
wi "\"I didn’t exactly say that, Todd.\""
show tod talking with dis
to "\"I just mean that I think he must have to do all sorts of really difficult things.\""
show tod sad with dis
"I give him a look."
show tod surprised with dis
wi "\"You think about those things a lot, Todd?\""
show tod talking with dis
to "\"No.\""
show tod surprised with dis
hide tod with dissolve
"He doesn’t say anything else for the rest of the walk."
"When we reach the door to Mr. Tibbits’ apartment, some things immediately don’t make sense."
wi "\"This lock is scratched to hell and back.\""
"I swivel the knob to see if it’s still locked, but it’s completely loose."
cl "\"I told you once and I’ll tell you again that you aren’t welcome here!\""
cl "\"I’ll have you know that if you knock down that door the authorities will be here in an instant!\""
wi "\"It's just us, Mr. Tibbits.\""
cl "\"Oh, thank goodness!\""
"I hear some of the furniture move around and something rattles against the door."
"The door pops open and the twitchy little man takes a step back."
cl "\"Please come in. I’ll put on some tea.\""
scene cliffroom with slow_dissolve
show cli at left,cliffroomnight:
    xzoom -1
show tod talking at right,cliffroomnight
with dissolve
to "\"What kind?\""
show tod
show cli talking
with dis
cl "\"Black with a bit of bergamot, surely!\""
show cli with dis
wi "\"That won’t be necessary Mr. Tibbits, but do what makes you feel comfortable.\""
wi "\"Just get straight to the point and tell us what the hell is going on up here.\""
show cli doubt with dis
cl "\"Well I had thought it was patently obvious that I am frightened, sheriff.\""
wi "\"Don’t be cute. Frightened of who?\""
show cli frustrated with dissolve
cl "\"Of that brute and bully who calls himself Reed!\""
show cli eyes talking with dissolve
$ unlocked_journal_pages += 1
$ current_journal_page = 2
$ renpy.notify("Notebook updated.")
cl "\"That wolf came clawing at my door tonight and broke the lock!\""
show tod sad
show cli eyes
with dis
to "\"That’s terrible!\""
show tod surprised with dis
show cli angry with vpunch
cl "\"That’s not the half of it!\""
show cli sad with dissolve
cl "\"He would have been upon me if I hadn't barricaded the door with all of the furniture I could put together in this ramshackle apartment!\""
wi "\"So you know it was him for sure?\""
show cli doubt with dissolve
play sound "sfx/match.mp3"
"The stoat was filling his kettle and striking a match beneath the wood stove."
show cli eyes talking with dis
cl "\"I’d know that greasy grey fur and those dumpy little ears anywhere.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"And if I were blind, there’d of course be the smell.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"You know, mustelids get all sorts of earfuls about how we put off an offensive odor simply for our ordinary body scents.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"But canines have a particular kind of reek to them that’s unmistakable.\""

show cli blush eyes closed with dis
"He stopped all of a sudden, a bit flushed in the ears."
show tod talking with dis
to "\"Well he’s right about that, William.\""
show tod with dis
"I do not give one iota of a fuck about this conversation."
show cli doubt with dis
wi "\"Mr. Tibbits? Please focus. I’ll check into Reed.\""
show cli frustrated with dissolve
cl "\"That’s splendid, but I won’t feel a moment’s peace with that mad man on the loose.\""
wi "\"I’d like you to stay at the station for a while.\""
show cli doubt with dissolve
cl "\"You think I’d feel safer inside of a prison cell?!\""
wi "\"Nobody said nothin’ about any prison cells.\""
show tod happy arms with dissolve
to "\"William has a comfy couch in his office. Heck, I’ve slept there plenty of times.\""
show tod surprised with dissolve
show cli talking with dis
cl "\"Not on taxpayer dollars, I hope.\""
show cli doubt with dis
"Todd looks like he just got hit in the face with a shovel."
"There’s no way he’d be able to handle somebody like Cliff on his own."
wi "\"Let’s talk about the other things to do to keep you safe.\""
"He turned to look at me as he was filling metal capsules with dry leaf and flower bundles."
show cli eyes talking with dis
cl "\"Such as?\""
show cli eyes with dis
wi "\"It’s common protocol to investigate a victim a little closer after they’ve been attacked. \""
wi "\"Helps us piece together a few things.\""
"He places three teacups on his little table."
show cli happy with dis
cl "\"I think you’ll find I’m an open book, so ask away.\""
wi "\"Let’s start with who you think might want you dead.\""
show cli doubt with dis
cl "\"Seems rather obvious, doesn’t it?\""
wi "\"Just tell me who you think it is.\""
show cli eyes talking with dis
cl "\"Huxley and Reed, without a doubt?\""
show cli eyes with dis
wi "\"Okay.\""
"I watch his expression as he puts down his little teacups onto the table."
wi "\"But who else?\""
show cli doubt with dis
"His lip curls and he looks sideways."
show cli eyes with dis
"...which probably means that he was thinking about it before I asked him."
show cli eyes talking with dis
cl "\"Perhaps somebody who doesn’t want me here.\""
show cli eyes with dis
"Now we’re getting somewhere."
wi "\"But why go through all the trouble to use violence to stop your academic endeavor?\""
"I lean in a little bit closer."
wi "\"I hear plenty of stories about how cutthroat a field academia is without even needing any bloodshed.\""
show cli doubt with dis
play sound "sfx/kettle.mp3"
"The kettle whistles."
show cli eyes talking with dis
cl "\"A moment!\""
show cli eyes with dis
hide cli with dissolve
stop sound fadeout 2.0
"I can tell that he’s relieved by this distraction."
show cli happy at left,cliffroomnight with dissolve:
    xzoom -1
cl "\"Sugar and cream?\""
show tod eyes happy with dis:
to "\"Sugar and cream!\""
show cli doubt with dis
show tod with dis
wi "\"So who do you think might use violence against you, Cliff?\""
wi "\"Because they don’t want you here?\""
show cli eyes with dis
"He pours his own cup of tea first, then Todd’s, then mine."
show cli talking with dis
cl "\"Perhaps some greedy businessmen who don’t see eye to eye with my benefactor.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"I doubt I’d know their names.\""
show cli eyes with dis
wi "\"So who is the benefactor that brought you to Echo?\""
show cli doubt with dis
cl "\"The same man who drew you here, from what I understand.\""
wi "\"Name him, please.\""
show cli eyes talking with dis
cl "\"Sorry, but that’s confidential.\""
show cli eyes with dis
wi "\"Mr. Tibbits.\""
wi "\"Just because I asked you nicely doesn’t mean you can withhold that information.\""
wi "\"This is basic information pertinent to whether or not your worker’s permit can be deemed valid.\""
show cli sad with dissolve
cl "\"Well bend my arm, why don’t you?\""
wi "\"The name, Tibbits...\""
show cli doubt with dissolve
cl "\"Very well!\""
show cli talking with dis
$ unlocked_journal_pages += 1
$ current_journal_page = 3
$ renpy.notify("Notebook updated.")
cl "\"It’s Mr. Hendricks, of course.\""
show cli with dis
"I’m not surprised at all."
"This is exactly the kind of clown shit that would have his name all over it."
"But I want to rely on as few assumptions as possible."
wi "\"Could I see your official paperwork?\""
show cli eyes talking with dis
cl "\"I don’t see how that’s relevant to anything, but of course.\""
show cli eyes with dis
"He picks up the satchel by his feet, unlatches it, then plucks a gray folder from it and passes it to me."
"I thumb through it."
"It states his full name, Clifford Tibbits  and his job title, consultant, in gold letters. Health information follows."
wi "\"This is beautiful stationery.\""
show cli happy with dis
cl "\"Thank you!\""
"I hand it back to him."
wi "\"Government issue type face is bare-bones and clinical. This is a CGCS form, not an official government verification.\""
show cli shocked with vpunch
show tod surprised with dis
cl "\"I’m afraid that my work permit is still moving through the post.\""
show cli sad with dissolve
cl "\"If I’m lucky it should arrive in a week or two, and you’ll have your paperwork then.\""
"As far as I can tell, everything this man has told me has been truthful."
"But I can tell that his cards still aren’t all on the table."
show cli doubt with dissolve
wi "\"What’s something official you have that can prove you are who you say you are?\""
show cli talking with dis
cl "\"Would travel tickets suffice, Mr. Adler?\""
show cli with dis
wi "\"It’s better than nothing.\""
show cli doubt with dis
cl "\"Well it’s the last thing that I have.\""
"He slides me a ticket."
"It states a passage for one person on an ocean liner. A Cornelis van Houwelinck."
wi "\"Your ticket, Mr. Tibbits.\""
show cli talking with dis
cl "\"That’s mine.\""
show cli doubt with dis
wi "\"This is a ticket for a man named Cornelis.\""
show cli down with dis
"He looks down."
show cli blush eyes right with dis
$ current_journal_page = 4
$ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
cl "\"And that’s my, ah, birth name.\""
show cli doubt with dis
cl "\"I don’t believe it is criminal to have an alias, is it Sheriff Adler?\""
wi "\"Not really, no.\""
show cli eyes with dis
cl "\"Lots of people do it.\""
show cli eyes talking with dis
cl "\"Especially when they’re writing books.\""
show cli eyes with dis
show cli talking with dis
cl "\"It’s a bit romantic to be able to choose your own name, isn’t it?\""
show cli blush eyes right with dis
cl "\"All you have to do is pick your mother’s maiden name as your own and suddenly you can turn yourself into a sports writer rather than a romance author.\""
show cli blush eyes left with dis
cl "\"You can become anything you want, really.\""
show cli blush eyes closed with dis
"But there’s a difference between calling yourself something new and living out a good part of your life as that something."
"You might not want to be what you choose to become."
"A life isn’t a pen name, or a book cover, or a change of scenery."
"It’s everything you are."
"...my wrist watch sounds too damn loud again."
wi "\"It’s just a bit concerning, what with everything that’s happened around you, is all.\""
show cli doubt with dis
cl "\"Oh, and that’s my fault, is it?\""
"The weasel sips his tea."
show cli eyes talking with dis
cl "\"You bit off more than you can chew when you took this job, didn’t you?\""
show cli shocked
show tod yell
with vpunch
to "\"Hey!\""
show cli doubt with dis
show tod annoyed with dis
to "\"Why are you being so unneighborly with us?\""
show cli eyes with dis
"The stoat gestures broadly to his wrecked living room."
show cli frustrated with dissolve
cl "\"Because I’m a little bit frightened right now, Mr. Bronson.\""
show cli doubt with dissolve
cl "\"I think we want the same things though, right, Sheriff?\""
show cli talking with dis
cl "\"I help you unmask some of the monsters trying to murder me, and I just keep telling you the truth like I always have.\""
show cli happy with dis
cl "\"But just let me hold onto the idea of what I want to be a little longer, and let me keep using that new name.\""
"So there it all is, then."
stop music fadeout 3.0
wi "\"I can recognize a fair deal when I see one.\""
show cli doubt with dis
"I hold out my paw to him."
show cli eyes with dis
play music "music/toddtheme.ogg" fadein 5.0
"He clasps it cautiously."
show cli with dis
wi "\"You gonna stay at the station then, or what?\""
show cli talking with dis
cl "\"...Let me go wake Mr. Byrnes first and I’ll be on my way shortly.\""
show cli with dis
wi "\"Byrnes is here?\""
show cli sad with dissolve
cl "\"He has work early.\""
show cli doubt with dissolve
cl "\"I didn’t want to wake him.\""
wi "\"I thought you said you were attacked?\""
show cli eyes talking with dis
cl "\"You think I can’t riposte Mr. Adler?\""
show cli happy with dissolve
cl "\"I told you that I can take care of myself.\""
show cli eyes talking with dis
cl "\"Mr. Byrnes was running a fever, and he’s practically naked at the moment.\""
show cli with dis
wi "\"...I’ll give y’all some space then.\""
show cli happy with dissolve
cl "\"Very good. I shant be long.\""


scene black with fade
scene echoroadnight with slow_dissolve
"We waited a while outdoors until we see a very weary looking Murdoch emerge from the apartment."
"He looks from side to side, rubbing his snout before making his way toward the direction of his father’s store."
show mur eyes night with dissolve
"He staggers a bit, but he makes his way there."
hide mur with dissolve
show cli happy night with dissolve
"Mr. Tibbits leaves the apartment five minutes later with a heavily stuffed bag and follows us to the station."
scene black with fade
stop background
scene officeday with slow_dissolve
"I feel like I’m in the calm of a hurricane before the storm comes."
"I think I was right about disaster following this weasel, but I don’t think he’s the only one stirring up trouble by far."
"Considering the way Huxley died, and with Cliff having ties to James, I’m almost certain now that the rat didn’t place the hit on the stoat."
"But if that’s the case, then how did he get the gun?"
"And if Cliff is telling the truth, then why was Reed trying to break into his apartment?"
"Did they plan the hit together and then something happened to Mr. Greene before he lost the gun?"
"Maybe."
"I’ll have to have a chat with Reed again before I have any reason to believe he has that much spite."
"Because as of now, that still don’t make much sense to me."
"I’d pin down Reed as a guy willing to get his own hands dirty."
"Or to start shit when he’s bored."
"He could definitely beat a man to death in broad daylight if he were mad and drunk enough."
"But plotting a murder while sober?"
"I just can’t see it."
"If the two of them already jumped this weasel in broad daylight then what’s the point of giving a kid a traceable gun to take care of him in secret?"
"Maybe they just fucked it up."
"Simple as that."
"Case closed."
"...but then how did he get his goddamn head severed?"
"I have more than a few things to consider now."
"I could go to the mayor and have a little chat about how things are going."
"...Any time, really. He spends most of his time in his office doing nothing when there isn’t a ribbon to cut or a speech to unload."
"And he has no real jurisdiction over me."
"Or I could go to the Stag that Nik and the Byrnes boy keep bringing up from time to time."
"It’s the biggest men’s club in town."
"And more importantly, I know that the mining union tends to congregate there."
"Perhaps the suggestion to go wouldn’t be a waste of time after all."
"Tricky thing is... wherever I go first will take all day."
"If I want Nik’s help at the Stag, it will have to be at night."
"But if I want a more private audience with the mayor, and I don’t WANT Nik there at the Stag with me, I should maybe go to the Stag first."
$ current_journal_page = 5
$ unlocked_journal_pages += 2
$ renpy.notify("Notebook updated.")
"Regardless, I shouldn’t stall."

menu willinvestigation1:
    "Where am I going first?"
    "City Hall.":
        jump cityhallday

    "The Stag.":
        jump stagday

label cityhallday:
$ CITYHALLDAY_Points +=1
label cityhallnight:
wi "\"Alright, I’m off to see mayor Testerman.\""
wi "\"Are you still able to keep watch over everything while I’m gone, Todd?\""
show tod arms happy at right,prisonday with dissolve
to "\"Sure thing!\""
show tod talking with dissolve
to "\"Did I hear that you’re paying old Franz another visit?\""
show tod with dis
show tod talking with dis
to "\"Why, that’s basically an honor.\""
show tod with dis
wi "\"Not really.\""
wi "\"He just wants to ask me whether or not the city is close to a state of emergency.\""
show tod arms happy with dissolve
to "\"That sounds like him alright.\""
show tod eyes happy with dissolve
to "\"Old Franz always looks out for us.\""
show tod talking with dis
to "\"Seems like only yesterday when I was a pup that he gave old woman Willoughby his own jacket on Easter Sunday.\""
show tod with dis
show tod talking with dis
to "\"I remember how she said her feet turned so cold!\""
show tod with dis
show tod talking with dis
to "\"And when the doctors paid her a house call, they said she nearly died!\""
show tod with dis
show tod talking with dis
to "\"But she dreamed about Franz.\""
show tod surprised with dis
to "\"In her dreams he was an angel, William!\""
show tod talking with dis
to "\"And he brought her back from the cold while she was asleep.\""
show tod with dis
wi "\"So you’re saying that he did the bare minimum that most people would do for an old woman, and then took credit for saving her life?\""
show tod eyes happy with dis
to "\"Well, the Lord works in mysterious ways, William.\""
show tod arms happy with dissolve
to "\"I think you could argue that he pretty much did save her life, no matter how you look at it.\""
"This poor man."
wi "\"That’s nice, Todd.\""
show tod eyes happy with dissolve
to "\"Lots o’ things are nice when you just stop to think about 'em.\""
show sam annoyed talking at left,prisonday with dissolve:
    xzoom -1
show tod surprised with dis
m "\"{i}...These things hast thou done, and I kept silence; thou thoughtest that I was altogether such an one as thyself: but I will reprove thee, and set them in order before thine eyes.{/i}\""

show sam annoyed with dis
"Sam is staring down at a pocket Bible."
"He looks angry."
show sam annoyed talking with dis
m "\"{i}Now consider this, ye that forget God, lest I tear you in pieces, and there be none to deliver.{/i}\""
show sam annoyed with dis
show sam annoyed talking with dis
m "\"Psalm fifty. Twenty-one, twenty-two.\""
show sam annoyed with dis
"He shuts the pages between his paws with a crisp snap."
show tod talking with dis
to "\"You just sounded like a genuine preacher man, Sam.\""
show tod with dis
show sam annoyed talking with dis
m "\"Well, I’m not.\""
show sam annoyed with dis
show sam annoyed talking with dis
m "\"I just thought it was an important thing to share.\""
show sam with dis
show tod talking with dis
to "\"I’ll admit I need to brush up on my old testament, but the way you said that made me feel I was sweating in the pews.\""
show tod with dis
show tod talking with dis
to "\"You ever read any of the Book of Mormon?\""
show tod with dis
show sam eyes with dis
show cli doubt at center,prisonday with dissolve
"Sam still looks a bit mad, and now Cliff looks uncomfortable."
wi "\"Well, I’ll leave this thrilling theological conversation to the both of you.\""
stop music fadeout 3.0
wi "\"...Bye!\""


if  CITYHALLNIGHT_Points > 0:
    scene echoroadnight with slow_dissolve
    $ BG_Light =1
else:
    scene echobackalley with dissolve
    $ BG_Light =0
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"Sam sure is invested in the bible."
"You’d think he sucked off enough men to be put off by all the bitching about adultery, but he keeps getting wrapped up in all the metaphysics."
"I know why he’s mad at Todd."
"Todd believes in a loving, affectionate God."
"Sam believes in a wrathful God."
"It’s like he wants there to be something real that he can be afraid of."
"Alright... I think that’s enough Church for me today."

if  CITYHALLNIGHT_Points > 0:
    scene townhallnight with dissolve
else:
    scene townhallday with dissolve
"Downtown is always so wide open when I go there."
"The wind picks up between the tall buildings and makes the wooden shutters rattle."
"It’s the closest reminder of my city."

"Other than the bars after dark."

"Bars always have the same sticky smell, no matter where you are in the world."

"I expected to run into Judge Miller or the clerk Chrissy Smalls, or somebody filing for their liquor license."
if BG_Light == 0:
    show ree with dissolve
else:
    show ree night with dissolve
"But what I see instead is Reed Morris."
play music "music/tension.mp3" fadeout 4.0 fadein 5.0
wi "\"You stop right there Reed!\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Oh God fucking DAMN it.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"I have some questions for you.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"I don’t have time for your flea-bitten ass today.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"That’s not how this works.\""
wi "\"Keep your hands where I can see them and don’t make a scene.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Why? Am I under arrest for the fiftieth fucking time?\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"I guess it depends.\""

wi "\"It’ll be just like old times! We’re used to each other by now!\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"You gonna feel me up like a fucking faggot and strip me of my rights again?\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"You’re the one who’s thinking that, not me.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Go ruin somebody else’s day, you ugly son of a bitch.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Cut the shit.\""

wi "\"Did you break into Mr. Tibbits’ apartment last night or not?\""
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
"He looks guilty."
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"There’s a whole lot more to it than that.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"So you’re not even trying to lie about it?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"That fucking fruit did something to Huxley.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"I goddamn KNOW that he did.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"And what if he didn’t, Reed?\""

wi "\"You just went off and beat his door down like a goddamn lunatic?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"He started some shit, he got his ass beat, and he took revenge on my friend!\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"And I’m sure as hell not gonna trust your shady ass to lift a finger over it, because you don’t even like me in the first place.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"I need you to stop talking for a few minutes and start listening.\""
stop music fadeout 3.0
wi "\"Some kid tried to shoot up my office two nights ago using {i}Huxley’s{/i} pistol.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
re "\"His revolver?\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"He pawned it. Anybody coulda bought it.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Not a fifteen year old without a job and no parents.\""

wi "\"Sales records indicate he bought it back.\""
if  CITYHALLDAY_Points > 0:
    $ unlocked_journal_pages += 3
$ current_journal_page = 7
$ renpy.notify("Notebook updated.")
$ huxley1 = _("According to Reed, Huxley's gun was pawned. Sales records indicate Huxley repurchased it.")
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
"Now he’s sweating."
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"That’s a hell of a lot of evidence that could implicate the two of you for attempted murder, damaging government property, and endangering the life of two officers.\""

wi "\"Hell, that’s more than enough to string you up!\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"We didn’t do NONE of that.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"I don’t think you did either you dumb asshole.\""
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
"He blinks and looks confused."

wi "\"Breaking and entering is unacceptable, and you will pay for that crime in time.\""
wi "\"But just talk to me for a bit, and I'll have it so you won’t have to spend the rest of the day in jail.\""

if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Okay. Shoot.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Why did he pawn the gun in the first place?\""

if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re  "\"...He was having money troubles.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"And why’s that?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis

$ renpy.notify("Notebook updated.")
$ current_journal_page = 9
$ huxley3 = _("Huxley was an alcoholic who needed more money for his drinking habit. I wonder where he was getting the cash?")
re "\"A man with troubles has gotta drink.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"A little too much maybe?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"That’s rich, based on what I hear about you.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"I can afford my drinks, Reed.\""
wi "\"What made him live beyond his means?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"He has problems.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
"Had problems, but I don’t think you can handle that yet."

wi "\"Yeah, I know. I saw what his {i}problems{/i} did to Marcy.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"What, you think she doesn’t like it that way, too?\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
"His greasy fur bends into a slow, cracked smile and his eyes wrinkle."

"His moldy cotton smell reminds me of how my father smelled at his wake, and it makes me want to puke up bile."
if BG_Light == 0:
    show ree eyes talking with dis
else:
    show ree eyes talking night with dis
re "\"...But now that I think about it, he was actin’... different, lately.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Different how?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Longer hours at the bank.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"Sounded paranoid.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Of Mister Tibbits?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"No, Tibbits just made him laugh.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"He wasn’t scared at all of that mouthy little fairy.\""
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
"Now something’s troubling him, like he’s starting to get it."
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"He kept talking about buying back that pistol, like he was gonna need it to defend himself soon, but I thought he hadn’t yet.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"And this was after you both had your quarrel with Mr. Tibbits?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"No, this was happening before.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"So who would have had an eye on the gun?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
$ renpy.notify("Notebook updated.")
$ current_journal_page = 8
$ huxley2 = _("Marcy may know what happened to the gun.")

re "\"Marcy would know where he hid it. He always kept it close to her.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
"Of course he did."

wi "\"So maybe a chat with Marcy would have been a little smarter than tearing down Mr. Tibbits’ apartment then, huh?\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"...May I go now?\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"Sure. But I don’t want to see you 100 yards within that stoat or we’re gonna have ourselves a more punctual problem.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"I don’t give a damn if he didn’t take the gun.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"But if Marcy says that he did take it, I’ll kill him.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
wi "\"To ask somebody to shoot at him?\""
if BG_Light == 0:
    show ree eyes talking with dis
else:
    show ree eyes talking night with dis
re "\"...Maybe.\""
if BG_Light == 0:
    show ree eyes with dis
else:
    show ree eyes night with dis
wi "\"Brilliant. That would make a whole lot of sense.\""
if BG_Light == 0:
    show ree talking with dis
else:
    show ree talking night with dis
re "\"I’ll find out soon enough anyway.\""
if BG_Light == 0:
    show ree with dis
else:
    show ree night with dis
"He turns away and walks stiffly into the alley."
hide ree with dissolve
wi "\"Don’t think I won’t come looking for you later when it’s time to pay repair costs for that apartment!\""

"He flips me the bird."

"What a living waste of space if ever I saw one."

"But at least I know who to visit later."

"Marcy Greene might be the key to all of this after all, even if her husband played no part in trying to kill somebody."

"Maybe Huxley thinks he was acting paranoid when he bought back the gun."

"But considering his current state... it sounds like he was right to be afraid."

"But who’s strong enough to rip a head clean off of a body?"

"That’s just another question for later."

scene townhallinterior with dissolve

play music "music/byrneshouse.mp3" fadeout 4.0 fadein 5.0

"Town hall is predictably empty on a Monday."

"Most town meetings are on Saturdays, and that’s also when people tend to pick up their licenses."

"Krissy isn’t at reception right now, but I’ve been through these halls so much I won’t need to wait for her."

show jam happy with dissolve

jam "\"Well goodness gracious, if it isn’t my favorite public servant.\""
show jam with dis
if CITYHALLDAY_Points > 0:
    $ current_journal_page = 10
    $ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
"So that’s why Franz called today."

wi "\"Shaking the mayor down for favors again?\""
show jam eyes with dis
jam "\"Well, what else is a mayor good for, anyway?\""
show jam talking with dis
jam "\"He’s very grateful to have more things to do.\""
show jam with dis
show jam eyes with dis
jam "\"Besides, baring fangs is more your line of work, is it not?\""
show jam with dis
wi "\"Only when I have to.\""
show jam happy with dis
jam "\"Of course, of course.\""
show jam talking with dis
jam "\"You’ve had ample time to practice burying your guilt.\""
show jam with dis
wi "\"I’m not talking to you because I want to make merry and exchange quips.\""

wi "\"I know something that could help you and I’m willing to trade information.\""
show jam happy with dis
jam "\"Well why didn’t you say so?!\""
show jam talking with dis
jam "\"And here I thought you were just talking to me to pout about the ex-wife.\""
show jam with dis
wi "\"Oh, we’ll be having a talk about that too.\""
show jam talking with dis
jam "\"Then why not move this conversation to the city library?\""
show jam with dis
show jam happy with dis
jam "\"It’s the perfect place for sharing information for men with noble character.\""
show jam with dis
wi "\"I still have to talk to the mayor.\""
show jam eyes with dis
"James rolled his eyes."
show jam talking with dis
jam "\"He’s always available.\""
show jam with dis
wi "\"And so are you?\""
show jam happy with dis
jam "\"Now there’s a private fantasy!\""
show jam talking with dis
jam "\"Since you have such a great sense of humor, I’ll make sure to dally at the library so that you can catch me there.\""
show jam eyes with dis
jam "\"Feel free to speak with the mayor first if you insist.\""
show jam talking with dis
jam "\"Until then, Sheriff.\""
show jam with dis
hide jam with dissolve
stop music fadeout 3.0
"I could follow up on James's offer."
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"But then again, I’m already here."

menu williamchallmenu:
    "What should I do right now?"
    "Talk to the Mayor." if willchall1interview == False:
        "Let’s get this over with, then."

        scene mayoroffice with dissolve
        "I step into Testerman’s office."

        "The big rat is pecking away at his typewriter, but he stands up when he sees me."
        show fra sweat talking with dis
        fr "\"Well it’s about time, Adler!\""
        show fra sweat with dis
        wi "\"There were some road bumps on the way, but I’m here.\""
        show fra sweat talking with dis
        fr "\"Hendricks is threatening to cut all sorts of donation money if we don’t set this right, fast.\""
        show fra sweat with dis
        "I start laughing."
        show fra glare talking with dis
        fr "\"What in the Lord’s name is funny about that?\""
        show fra glare with dis
        wi "\"Let’s start with the essentials.\""
        wi "\"The mining operation continues to place blame on CGCS management for the death of this particular miner.\""
        wi "\"Tension is calm on the surface but resentment brews below.\""
        show fra with dis
        wi "\"Deputy Bronson found another dead body last night.\""
        show fra sweat with dis
        "His expression changes from one of anxiety to a look of sheer panic?"
        show fra sweat talking with dis
        fr "\"Another miner?!\""
        show fra sweat with dis
        wi "\"No.\""
        wi "\"This one’s a banker.\""
        show fra eyes with dis
        "I see relief wash over him."
        show fra talking with dis
        fr "\"So this wasn’t related to the other case, then?\""
        show fra with dis
        wi "\"A man is still dead, Mr. Testerman.\""
        show fra eyes with dis
        "He starts mumbling to himself."
        show fra eyes talking with dis
        fr "\"Well, sometimes it can’t be helped.\""
        show fra eyes with dis
        show fra eyes talking with dis
        fr "\"Men take all sorts of risks to make it out here, and not everybody can.\""
        show fra eyes with dis
        show fra eyes talking with dis
        fr "\"There are fights, and freak accidents, and hasty decisions accompanying immoral acts.\""
        show fra sweat with dis
        wi "\"His head was ripped off.\""
        show fra sweat talking with dis
        fr "\"Oh. So probably an animal.\""
        show fra with dis
        wi "\"Could be.\""
        show fra talking with dis
        fr "\"Now I feel a lot better.\""
        show fra with dis
        wi "\"Are you sure that you should?\""
        wi "\"I didn’t say that this was an animal for certain.\""
        show fra sweat talking with dis
        fr "\"Do any of your discoveries call for a state of emergency evacuation?\""
        show fra sweat with dis
        wi "\"I wouldn’t say so.\""
        wi "\"Unless this death isn’t an isolated incident.\""
        wi "\"I have reasonable suspicion to think that it could be linked to a targeted attack on one of the CGCS employees.\""
        show fra glare talking with dis
        fr "\"But you just have suspicions.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"Not proof.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"That’s what you said, right?\""
        show fra glare with dis
        wi "\"That would be right.\""
        wi "\"But odds are--\""
        show fra sweat talking with dis
        fr "\"I think it would be kind not to sensationalize a tragedy.\""
        show fra sweat with dis
        "He looks into my eyes as if he’s looking for approval for what he’s about to say."
        show fra sweat talking with dis
        fr "\"Wouldn’t it?\""
        show fra sweat with dis
        wi "\"I think that should always be a priority.\""
        wi "\"But what I’m telling you is that whatever this is, it probably ain't over, and it probably ain't isolated from CGCS affairs.\""
        wi "\"So you might want to prepare a statement ahead of time if things go to hell in a handbasket and you don’t want to be caught with your britches down.\""
        show fra talking with dis
        fr "\"I think I would prefer to be optimistic about the future Mr. Adler.\""
        show fra with dis
        show fra talking with dis
        fr "\"Just keep me informed about the present, please?\""
        show fra with dis
        wi "\"Okay then!\""
        wi "\"There are presently some signs of very clear scandals at that company that will make their way to the surface soon.\""
        show fra glare talking with dis
        fr "\"That {i}company{/i} is our town’s life-blood, Adler!\""
        show fra glare with dis
        wi "\"Well, that’s fine, but ignoring it won’t make it all go away.\""
        show fra glare talking with dis
        fr "\"But isn’t it your job to prevent a state of panic?\""
        show fra glare with dis
        wi "\"I’m saying that if all these problems go back to CGCS management, then the panic is just going to keep coming back like clockwork.\""
        show fra eyes talking with dis
        fr "\"But you still need proof before you can bandy about these claims.\""
        show fra eyes with dis
        "I swear to God this man is as thick as pig shit."
        show fra glare with dis
        wi "\"I didn’t make claims.\""
        wi "\"I shared suspicions.\""
        show fra sweat with dis
        wi "\"Let me make something very clear to you, Franz Testerman.\""
        wi "\"I don’t work for you.\""
        wi "\"But if you ask me for help and aren’t willing to take it, there’s not much I can do for you.\""
        wi "\"I do think this could lead to a public crisis.\""
        wi "\"So I think you should prepare for that.\""
        show fra glare talking with dis
        fr "\"And I’ll tell {i}you{/i} something, Mr. Adler!\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"I will say it once, I will say it a hundred times over.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"I must see the evidence before I am swayed to act!\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"Why is that so hard for you to accept?\""
        show fra glare with dis
        "The more I look into this man’s eyes, the more I know he has no interest in evidence."
        "He’ll see what he wants to see when he needs it to be true."
        wi "\"Do you already have a contingency plan in place for evacuating a population of over six thousand, then?\""
        show fra eyes with dis
        fr "\"There’s precedents in place if such a need arrives.\""
        show fra sweat with dis
        wi "\"And you’ve practiced them?\""
        show fra sweat talking with dis
        fr "\"Once again, I will not disrupt daily routines on the basis of an assertion!\""
        show fra sweat with dis
        "Alright, this is going nowhere."
        wi "\"Then let’s conclude this meeting.\""
        "I turn around and put my hand on the knob."
        show fra sweat talking with vpunch
        fr "\"Wait...\""
        show fra sweat with dis
        wi "\"Yes?\""
        show fra sweat talking with dis
        fr "\"Do you really think things are that bad?\""
        show fra sweat with dis
        wi "\"Yes.\""
        show fra sweat with dis
        "He wipes his brow with a kerchief."
        show fra eyes talking with dis
        fr "\"I could... review the evacuation plans.\""
        show fra sweat with dis
        show fra sweat talking with dis
        fr "\"But quietly, and without getting the public involved.\""
        show fra sweat with dis
        show fra sweat talking with dis
        fr "\"But just as a backup plan! I still have no intention of officiating an evacuation.\""
        show fra eyes with dis
        "That’s what I’ve been saying, Testerman."

        wi "\"That’s better than nothing.\""
        wi "\"I have to go now.\""
        show fra talking with dis
        fr "\"...You’ll keep me updated, then?\""
        show fra sweat with dis
        wi "\"I’ll call if it’s important.\""
        hide fra with dissolve
        "What a headache."
        $ willchall1interview = True
        jump williamchallmenu
    "Talk to James." if willchall2interview == False:
        "Information shared among noble souls?"
        "And here I thought we were a couple of bastards."
        if  CITYHALLNIGHT_Points > 0:
            scene townhallnight with dissolve
        else:
            scene townhallday with dissolve
        "At least I can understand that."
        "Pitiful."
        if  CITYHALLNIGHT_Points > 0:
            scene echolibraryinteriornight with dissolve
        else:
            scene echolibraryinteriorday with dissolve

        "The library is big, but it’s pretty underutilized."
        "Because, well, let’s face it... not a whole lot of people here like to read."
        "Which I don’t entirely get, considering how little there is to do."
        if BG_Light == 0:
            show jam eyes at center,sunset with dissolve
        else:
            show jam eyes night with dissolve
        "It doesn’t take me long to find him."
        "He’s reading a newer book by the looks of it."
        "{i}Dubliners{/i}, by James Joyce."
        "His bodyguards were sitting in a corner, flipping through magazines."
        wi "\"Let’s keep this quick.\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Don’t act so suburban, Mr. Adler, there’s a treasure trove of knowledge all around you. \""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Enjoy yourself.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"Not interested.\""
        wi "\"You really did bring Hattie here.\""
        wi "\"Why?\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        jam "\"My, my. You’re so accusatory.\""
        wi "\"That’s because I’m accusing you of something.\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"You’re wrong to, you know.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        "He flipped a page to the beginning of another short story."
        "{i}Araby{/i}."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"She’s the one who reached out to me, not the other way around.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"I only did for her what I did for you.\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"She just needed some money to stay on her feet to orient herself in someplace new.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"How generous of you.\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        jam "\"I am generous.\""
        wi "\"When it’s inconvenient for me. Sure.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"Why’d you tell her where I live?\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Now that, I can’t talk about.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"Did your generosity suddenly run dry?\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"No. I mean I simply don’t know.\""
        wi "\"Horse shit.\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        jam "\"Why would I need to lie?\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"I genuinely don’t know, and that’s going to put you in the most amusing little tizzy.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"But how about granting me some of {i}your{/i} generosity now?\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Share.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"I guess you’ll have to ask yourself why somebody would try to assassinate one of your business associates.\""
        "He lifted an eyebrow."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Which?\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"Little fellah who goes by the name Clifford Tibbits.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        "He hummed."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Well that’s no good at all.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"He’s such a card... and much more fun than you.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"What kind of cad would put their hands on such a delightful boy?\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"I’ll have to keep a much closer eye on him from now on.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"I could help you with that.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"Your stalwart sense of justice really is invigorating.\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        jam "\"I always knew deep down that you liked me.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        "It takes a lot of willpower not to rip that book out of his hands and beat him with it."
        wi "\"So help me understand.\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Well, let’s see.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"As is typical of your older workhorses, too many of them tend to keep very old-fashioned ideas.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"They might not approve of a foreigner in a higher ranking consultation position.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Particularly the men closest to my most important business partner, Mr. Briggs.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"And do you have the names of these men?\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"Not really.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"There’s simply too many, and they’re all very closed-minded.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"But it shouldn’t be too complicated to pick them out of a crowd.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"They tend to smell like raw earth, after all.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        "He snaps his book shut."
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        if CITYHALLDAY_Points > 0:
            $ current_journal_page = 11
            $ unlocked_journal_pages += 1
            $ renpy.notify("Notebook updated.")
        jam "\"If it wasn’t one of them, then I’m out of ideas.\""
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Then again, that one does have a bleeding heart.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"I wouldn’t be surprised if he spilled his guts out to some savage and they took it the wrong way.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        wi "\"You stop speaking.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        wi "\"Now.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"Oh don’t be so sensitive, Adler.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"I’m not a monster.\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"And I don’t begrudge you for the primal blood on your mother’s side.\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        jam "\"In fact, I think you’re the best of two worlds.\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        jam "\"The raw and the refined.\""
        "I see a pebble on the table."
        "I pick it up, then flick it at his cheek."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Oh, what the fuck?\""
        if BG_Light == 0:
            show jam with dis
        else:
            show jam night with dis
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Am I bleeding?!\""
        if BG_Light == 0:
            show jam eyes with dis
        else:
            show jam eyes night with dis
        "Oh damn."
        "He is."
        "Hope it stings, you son of a bitch."
        "His guards rush over but he puts up his hand to make them stop."
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        "He smiles real big at me."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"And that’s exactly what I’m talking about!\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        "He waves at me with his bloody hand."
        if BG_Light == 0:
            show jam talking with dis
        else:
            show jam talking night with dis
        jam "\"Until next time.\""
        if BG_Light == 0:
            show jam happy with dis
        else:
            show jam happy night with dis
        wi "\"Always an affable time.\""
        hide jam with dissolve
        "It doesn’t take too long for James and his men to clear out of the library."
        $ renpy.notify("Notebook updated.")
        $ current_journal_page = 10
        $ jamestext = _("Made James bleed. Was funny.")
        $ jamesimage = "wn8"
        "I never much cared for Joyce."

        if  CITYHALLNIGHT_Points > 0:
            $ PORINT_Points +=1
            "I hear somebody else stir behind the library stacks."
            wi "\"Who’s there?\""
            wi "\"Come on out and show yourself.\""
            show por talking night with dissolve
            pounk "\"It’s only me.\""
            show por night with dis
            "I hear a thin, cheery voice."
            wi "\"Who the hell’s me?\""
            show por eyes talking night with dis
            pounk "\"The librarian.\""
            show por eyes night with dis
            "Oh."
            show por night with dis
            "That makes sense."
            "Now I feel silly."
            wi "\"My apologies. I didn’t think I’d hear anybody there.\""
            show por talking night with dis
            po "\"Porter Moore.\""
            show por eyes night with dis
            po "\"But don’t bother apologizing.\""
            show por talking night with dis
            po "\"After all, I did happen to hear a good chunk of your conversation.\""
            show por night with dis
            wi "\"Fair game in a public library.\""
            wi "\"We are supposed to be quiet in them, after all.\""
            show por eyes night with dis
            po "\"I’m afraid I must insist!\""
            show por talking night with dis
            po "\"You are looking for reliable information, aren’t you?\""
            show por night with dis
            wi "\"Well, what would you know?\""
            show por talking night with dis
            po "\"I know that you collect information from the prostitutes at the Hip in exchange for a loose adherence to the law.\""
            show por night with dis
            show por talking night with dis
            po "\"But other than that, not much about you, I’m afraid.\""
            show por night with dis
            wi "\"Alright, who the hell are you?\""
            show por talking night with dis
            po "\"I already told you.\""
            show por night with dis
            show por talking night with dis
            po "\"I’m just a librarian.\""
            show por night with dis
            show por talking night with dis
            po "\"You’d trade information with the co-owner of CGCS but not with me?\""
            show por night with dis
            show por talking night with dis
            po "\"Now that feels unfair.\""
            show por night with dis
            show por talking night with dis
            po "\"At least allow me to give you something free as a token of good will...\""
            show por night with dis
            wi "\"Alright then.\""
            wi "\"What do you got?\""
            show por smug talking night with dis
            po "\"James has a voracious sexual appetite.\""
            show por night with dis
            show por talking night with dis
            po "\"You’ll find that he sleeps with many of the workers at the Hip to satisfy his curiosities.\""
            show por night with dis
            show por talking night with dis
            po "\"One of them is loyal to him now, and will tell you nothing useful.\""
            show por night with dis
            show por talking night with dis
            po "\"They will be an active hindrance to you.\""
            show por night with dis
            show por smug talking night with dis
            po "\"Would you like to know their name?\""
            show por smug night with dis
            wi "\"Sure. Why not?\""
            show por talking night with dis
            po "\"Now that’ll cost you something.\""
            show por night with dis
            wi "\"Oh, does it now?\""
            show por talking night with dis
            po "\"You can pay me money, or you can pay me in information.\""
            show por night with dis
            wi "\"How much?\""
            show por talking night with dis
            po "\"Fifty dollars.\""
            show por night with dis
            wi "\"I think I see.\""
            show por talking night with dis
            po "\"Is the price too high?\""
            show por night with dis
            wi "\"Not necessarily.\""
            show por surprised night with dis
            wi "\"But I understand what diminishing returns are.\""
            wi "\"My secrets are more valuable when I’m the source.\""
            wi "\"And that will go farther than putting it up in your information market.\""
            show por smug talking night with dis
            po "\"Well done.\""
            show por smug night with dis
            show por serious talking night with dis
            po "\"Just don’t compete with me or you might regret it.\""
            show por serious night with dis
            wi "\"I assure you. We’re in different businesses.\""
            show por night with dis
            hide por with dissolve
            $ renpy.notify("Notebook updated.")
            $ current_journal_page = 6
            $ chnighttext = _("Apparently, at least one person who works at the hip is leaking information to James.")
            "He flashed me a smile and walked away."
        else:
            "Where's Baroness Orczy when you need her?"
        "So there are people who'd have a motive to hurt Mr. Tibbits."
        $ willchall2interview = True
        jump williamchallmenu




label endofwillchallinterviews1:
"I think I’ve learned all that I could."
"That’s just about enough of this place for now."

if CITYHALLNIGHT_Points > 0:
    "Time to go."
    scene black with fade
    jump hipinvestigation
else:
    scene black with fade
    jump samstation

label stagday:
$ STAGDAY_Points +=1
label stagnight:
wi "\"Todd! Watch over the station while I head to The Stag.\""
show tod surprised at right,prisonday with dis
to "\"Oh!\""
show tod talking with dis
to "\"So are ya finally gonna learn how to dance, Sheriff?\""
show tod with dis
wi "\"This isn’t for fun, Todd. I’m going to scope the place out and ask some questions.\""
wi "\"And I already know how to dance.\""
show tod eyes happy with dis
to "\"I guess I shouldn’t be surprised. You do know an awful lot.\""
show tod with dis
show sam smile at left,prisonday with dissolve:
    xzoom -1
m "\"Why don’t you show him how, Sheriff?\""
show sam talking at left,prisonday with dis:
    xzoom -1
m "\"He seems eager.\""
show sam smile at left,prisonday with dis:
    xzoom -1
"Oh shut the hell up Sam."
show sam surprised at left,prisonday:
    xzoom -1
show tod surprised
show cli eyes talking at center,prisonday

cl "\"I’ve been told I can be very eager.\"" with vpunch
show cli happy with dis
show sam surprised with dis
show tod surprised with dis
cl "\"Numerous times.\""
show sam talking  at left,prisonday with dis:
    xzoom -1
m "\"Nah. This is something I think the Sheriff should do.\""
show sam smile  at left,prisonday with dis:
    xzoom -1
"Smarmy shit."
wi "\"You’re the expert on moving your legs. You do it.\""
show tod talking with dis
to "\"Sam’s a dancer?\""
show tod with dis
show sam eyes talking  at left,prisonday with dis:
    xzoom -1
m "\"Uh... no?\""
show sam eyes at left,prisonday:
    xzoom -1
show cli talking with dis
cl "\"Oh, nonsense. Everybody’s a dancer when they find the right rhythm.\""
show cli with dis
show cli happy with dissolve
cl "\"Now let’s find some music or make some ourselves.\""
show sam surprised at left,prisonday with dis:
    xzoom -1
wi "\"Have fun, Sam!\""
stop music fadeout 3.0



if  STAGNIGHT_Points > 0:
    scene echoroadnight with slow_dissolve

else:
    scene echobackalley with slow_dissolve
"I guess it’s time to finally make my way to this club."
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"I know the directions, roughly."

"Which means I’m gonna be walking for a while."

if  STAGNIGHT_Points > 0:
    scene stagtrailnight with slow_dissolve

else:
    scene mineroad with slow_dissolve

"For one of the busiest places in town, it sure is out of the goddamn way of everything."

"Though, considering the kinds of things that go down there, I suppose that’s part of the point."

if  STAGNIGHT_Points > 0:
    scene stagexteriornight with slow_dissolve
else:
    scene stag with slow_dissolve

"It looks like a massive barn."

"But it doesn’t smell like one."

"I know what a bar smells like."

"The wide double doors are held open by a big rock, so it doesn’t look like this place is closed often."

if  STAGNIGHT_Points > 0:
    "There’s a big figure in the distance lumbering toward me."
    wi "\"That you, Nik?\""
    show nik talking night with dissolve
    ni "\"If you wanted to go for a drink we should have invited all the others.\""
    show nik night with dis
    show nik talking night with dis
    ni "\"I am sure they would love to see how drunk I could get you.\""
    show nik smile night with dis
    wi "\"The last thing I want is a scene here.\""
    wi "\"Could you help me fit in?\""
    wi "\"Maybe get cozy with some of the regulars?\""
    show nik talking night with dis
    ni "\"Well do not wear the badge obviously.\""
    show nik night with dis
    wi "\"I already took it off Nik.\""
    show nik disappointed night with dissolve
    ni "\"Pah! It is dark.\""
    show nik talking night with dissolve
    ni "\"Just put in an effort to have a good time and people will talk without asking.\""
    show nik smile night with dis
    wi "\"I’m on a time crunch, Nik.\""
    wi "\"There are other places I still have to be.\""
    show nik disappointed night with dissolve
    ni "\"Very well, very well.\""
    show nik night with dissolve
    "He beckons toward the front door."
    show nik sidelook night with dissolve
    ni "\"Shall we, then?\""
    stop music fadeout 3.0
    "I nod and sigh."
    play music "music/stag1.mp3" fadeout 4.0 fadein 5.0
    wi "\"After you.\""
else:
    "I hope this is worth it."

if  STAGNIGHT_Points > 0:
    scene stagnight with dissolve
    $ BG_Light =1
else:
    scene stag with dissolve
    $ BG_Light =0


if STAGNIGHT_Points > 0:
    "It’s packed so dense I can hardly move."
else:
    "There’s barely a crowd right now."
    $ current_journal_page = 5
    $ unlocked_journal_pages += 5
    $ renpy.notify("Notebook updated.")
menu williamstagmenu:
    "Where should I look right now?"
    "Check the upper beams" if willstag1interview == False:
        if  STAGNIGHT_Points > 0:
            scene stagloftnight with dissolve
            $ BG_Light =1
        else:
            scene stagloft with dissolve
            $ BG_Light =0
        if willstag1interview2 == False and STAGNIGHT_Points > 0:
            show nik talking light1 with dis
            ni "\"Move to the ladder and we can escape the crowd.\""
            show nik light1 with dis
            show nik talking light1 with dis
            ni "\"I know some people we could talk to.\""
            show nik light1 with dis
            hide nik with dissolve
        else:
            "There's got to be somebody useful to talk to nearby."
        if willstag1interview2 == False:
            "It might be easier to scope out the place if I look from a higher position."
            "Might as well climb up the ladder and see what I’ve got to work with."
        else:
            "God it's getting stuffy up here."

        label loftjump:

        if willstag1interview2 == False:
            "There’s a severe looking fellow in eastern clothing sitting by the rails by himself."
            "He looks like a sable."
        else:
            "Now then..."

        if willstag1interview2 == False and STAGNIGHT_Points > 0:
            wi "\"Say, Nik...\""
            wi "\"Do you know any folks in these parts who’s be comfortable to share what they know with me?\""
            wi "\"Maybe somebody a little less cagey.\""
            show nik happy light1 with dissolve
            ni "\"This is a spirited place, Will. Especially after a few drinks.\""
            show nik smile light1 with dissolve
            ni "\"But I know some good union men who will share what they know if they believe in the cause.\""
            show nik talking light1 with dis
            ni "\"Over there, for example.\""
            show nik light1 with dis
            show nik talking light1 with vpunch
            ni "\"Oiy!\""
            show nik light1 with dis
            hide nik with dissolve
        else:
            jump willstagmenu2


        menu willstagmenu2:
            "Who should I approach?"
            "Talk to the sable." if willstag1interview2 == False:
                $ willstag1interview2 = True
                if BG_Light == 0:
                    show cha dark4 with dissolve
                elif BG_Light == 1:
                    show cha light1 with dissolve
                else:
                    show cha stagback with dissolve
                "He might think that he was minding his business, but I caught him staring multiple times."
                "Which either means he’s curious about me or he wants me to leave."
                "Let’s find out which."
                wi "\"Mind if I take a seat?\""
                if BG_Light == 0:
                    show cha eyes dark4 with dis
                elif BG_Light == 1:
                    show cha eyes light1 with dis
                else:
                    show cha eyes stagback with dis
                "He dabs his pen in the ink again, and keeps writing."
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"If you insist, though I will be involved in my work.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                wi "\"What sort of work?\""
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"Translation.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                wi "\"You kept giving me looks, so you know who I am, don’t you?\""
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"Difficult not to.\""
                if BG_Light == 0:
                    show cha smile dark4 with dis
                elif BG_Light == 1:
                    show cha smile light1 with dis
                else:
                    show cha smile stagback with dis
                wi "\"Well I promise I’m not here to give you a hard time.\""
                wi "\"I just hoped that the good people here could help me understand a little more about James Hendricks and his relationship with his employees.\""
                wi "\"I have reason to believe that somebody might be trying to hurt his employees, and some folks are already hurt.\""
                if BG_Light == 0:
                    show cha eyes talking dark4 with dis
                elif BG_Light == 1:
                    show cha eyes talking light1 with dis
                else:
                    show cha eyes talking stagback with dis
                unkch "\"I no longer work there, so I would not know.\""
                if BG_Light == 0:
                    show cha eyes dark4 with dis
                elif BG_Light == 1:
                    show cha eyes light1 with dis
                else:
                    show cha eyes stagback with dis
                wi "\"But do you know anything that might support the claim that Mr. Hendricks is putting his own employees in danger?\""
                "The sable looks like he’s thinking."
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"I can tell you something general.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                wi "\"Anything helps.\""
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"Mr. Hendricks, very blatantly, has favored employees.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"However, so does Mr. Briggs.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                $ renpy.notify("Notebook updated.")
                $ current_journal_page = 11
                $ changtext = _("{s}Could a CGCS employee placed a hit on Cliff, or was it somebody else?{/s} Seems like the CGCS employees loyal to the company don't even get along. Some favor James. Some favor Briggs.")
                unkch "\"There was very little overlap in those two groups, and it traditionally bred resentment.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                unkch "\"But that’s all I can tell you.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                wi "\"Thanks. You’ve been very helpful. Mr... what was your name again?\""
                if BG_Light == 0:
                    show cha talking dark4 with dis
                elif BG_Light == 1:
                    show cha talking light1 with dis
                else:
                    show cha talking stagback with dis
                chji "\"Call me Ji Ba.\""
                if BG_Light == 0:
                    show cha dark4 with dis
                elif BG_Light == 1:
                    show cha light1 with dis
                else:
                    show cha stagback with dis
                "I try to pronounce it, but it’s a bit of a mouthful."
                wi "\"Thank you, Mr. Ji Ba.\""
                if BG_Light == 0:
                    show cha smile dark4 with dis
                elif BG_Light == 1:
                    show cha smile light1 with dis
                else:
                    show cha smile stagback with dis
                chji "\"Oh, call for me any time.\""
                hide cha with dissolve
                "Strange fellah."
                if willstag1interview2 == True and willstag2interview2 == True:
                    $ willstag1interview = True
                    jump williamstagmenu
                else:
                    "Shame about his hand."
                    $ willstag1interview = True
                    if STAGNIGHT_Points > 0:
                        jump willstagmenu2
                    else:
                        jump williamstagmenu
                if STAGNIGHT_Points > 0:
                    jump williamstagmenu
                else:
                    $ willstag1interview = True
                jump willstagmenu2
            "Talk to the miners." if willstag2interview2 == False and STAGNIGHT_Points > 0:
                play music "music/stag2.mp3" fadeout 4.0 fadein 5.0
                scene stagloftbacknight with dissolve
                $ BG_Light =2
                $ MININT_Points +=1
                show nik stagback with dissolve
                "Nik keeps nudging me towards a round table where a few men are talking."
                show nik talking stagback with dis
                ni "\"Dimitri, Paul, Felipe.\""
                show nik stagback with dis
                hide nik with dissolve
                show dim coat stagback
                show pau stagback at left:
                    xzoom -1
                show fel stagback at right
                with dissolve
                "He pointed to the bear, the wolverine, and the jackrabbit respectively."
                ni "\"Say hello to sheriff Adler.\""
                show pau angry talking stagback with dis
                pa "\"Sheriff, you say?\""
                show pau angry stagback with dis
                show dim coat smile talking stagback with dis
                di "\"We’d be happy to speak with him.\""
                show dim coat smile stagback
                show fel talking stagback
                with dis
                fe "\"Would we?\""
                show fel stagback with dis
                ni "\"He is working on more than a few dangerous cases.\""
                show pau angry talking stagback with dis
                pa "\"So what?\""
                show pau angry stagback with dis
                ni "\"One of the men involved shot at me.\""
                show pau surprised stagback with dis
                pa "\"Oh.\""
                show pau eyes smile stagback with dis
                pa "\"Well that changes things.\""
                show pau talking stagback with dis
                pa "\"You hurt?\""
                show pau stagback with dis
                ni "\"Not yet, thankfully, but for how long?\""
                ni "\"Who can say...\""
                show pau eyes smile talking stagback with dis
                pa "\"Just tell us what you need already, damn it...\""
                show pau eyes smile stagback
                show dim coat smile talking stagback
                with dis
                di "\"I’m glad you changed your tune Paul.\""
                show dim coat smile stagback with dis
                show dim coat talking stagback with dis
                di "\"Now what might we help you with?\""
                show dim coat stagback with dis
                wi "\"I know it’s not exactly a secret that your folks aren’t happy with the management at CGCS.\""
                show pau angry talking stagback with dis
                pa "\"I don’t give a damn about the management, I just want more pay.\""
                show pau angry stagback with dis
                show fel talking stagback with dis
                fe "\"The management could also be better.\""
                show fel stagback
                show dim coat eyes smile talking stagback
                with dis
                di "\"Our chapter isn’t exactly united on every front, but frustrations are certainly at an all time high.\""
                show dim coat eyes stagback with dis
                wi "\"Know anybody frustrated to assassinate one of James’s higher ranking employees?\""
                show pau talking stagback with dis
                pa "\"If you’re here to sniff around for information about James, the stag won’t do you much good.\""
                show pau stagback with dis
                show pau talking stagback with dis
                pa "\"The hip is more his speed.\""
                show pau stagback with dis
                wi "\"In what way?\""
                show pau eyes smile talking stagback with dis
                pa "\"The carnal way.\""
                show pau eyes smile stagback with dis
                wi "\"Noted.\""
                show pau eyes smile talking stagback with dis
                pa "\"I hear that man gets stuck in women more times than Taft got stuck in the presidential bathtub...\""
                show pau eyes smile stagback with dis
                "Is he trying to make me vomit?"
                wi "\"That paints a picture alright.\""
                wi "\"Anything else you can tell me?\""
                show dim coat talking stagback with dis
                di "\"I think he doesn’t seem to like the barkeep much?\""
                show dim coat stagback with dis
                show dim coat talking stagback with dis
                $ renpy.notify("Notebook updated.")
                $ current_journal_page = 6
                $ stagnighttext = _("Harlan gets into fights with James? He usually keeps things professional.")
                di "\"Sounded like he gets in fights with him enough.\""
                show dim coat stagback with dis
                show pau talking stagback with dis
                pa "\"Not enough to get him banned from the establishment, apparently.\""
                show pau stagback with dis
                show fel eyes talking stagback with dis
                fe "\"Well we all know what he’s like.\""
                show fel eyes stagback with dis
                "You’re a life-saver, Nik."
                wi "\"I think I might have enough here gentleman.\""
                wi "\"It’s been a pleasure.\""
                show dim coat talking stagback with dis
                di "\"Why don’t you stay for a little while longer?\""
                show dim coat stagback with dis
                show dim coat smile talking stagback with dis
                di "\"I’m sure we have other mutual interests we could discuss other than James three.\""
                show dim coat stagback with dis
                wi "\"I'm on a time crunch, I’m afraid, but I think that’s not a bad idea once this case is under control.\""
                show dim coat smile talking stagback with dis
                di "\"I’ll hold you to that.\""
                show dim coat smile stagback with dis
                wi "\"People usually do.\""
                hide fel
                hide pau
                hide dim
                with dissolve
                "There’s a bar and a dance floor downstairs."
                "There could be somebody down there with loose lips from all the alcohol."
                if willstag1interview2 == True:
                    $ willstag1interview = True
                    $ willstag2interview2 = True
                    jump williamstagmenu
                else:
                    $ willstag2interview2 = True
                    jump willstagmenu2
        label endofwillstaginterviews2:
    "Check out the bar." if willstag3interview == False:
        if  STAGNIGHT_Points > 0:
            scene stagnight with dissolve
            $ BG_Light =1
        else:
            scene stag with dissolve
            $ BG_Light =0

        "I see an opening to fit into the bar, so I sit on one of the bar stools right now so I don’t miss my chance."
        "The bartender strolls over slowly."
        "Barkeep" "\"What will it be?\""
        wi "\"Just a scotch on the rocks.\""
        if STAGNIGHT_Points > 0:
            "Barkeep" "\"Comin’ right up...\""
        else:
            "Barkeep" "\"Ain't it a bit early for that?\""
            wi "\"You want me to just order a water instead?\""
        "The barkeep turns his head towards me and squints at me."
        "Barkeep" "\"Hey, I know you.\""
        "Oh boy. Here comes trouble."
        "Barkeep" "\"You’re Sheriff Adler.\""
        "I hear some adjustments in the seats next to me."
        wi "\"Right now I’m just thirsty, thanks.\""
        "Barkeep" "\"How come you’re not wearing your badge?\""
        wi "\"Because I don’t tend to need it for folks to know who I am.\""
        wi "\"And I’m on a case.\""
        wi "\"Are you saying you have time to talk with me?\""
        "Barkeep" "\"Your drink will be right up.\""
        "He hurries away and I can feel the breath leaving my lungs."
        "That’s what I thought."
        "That was a scene that didn’t need to be one."
        "Some folks clear the seats beside me."
        "A big Sonoran wolf stares at me through the space they left behind."
        if BG_Light == 0:
            show kan smile at center,stagday with dissolve
        else:
            show kan smile light1 with dissolve
        "He stands up, saunters over with a bit of a swagger, then takes the seat next to me."
        if BG_Light == 0:
            show kan eyes smug with dis
        else:
            show kan eyes smug light1 with dis
        kaunk  "\"Bit hard out there for a law man, ain't it?\""
        wi "\"Hard out there for most people.\""
        wi "\"Patronizing me won’t get you far.\""
        if BG_Light == 0:
            show kan smug with dis
        else:
            show kan smug light1 with dis
        kaunk  "\"Easy there, tough guy.\""
        if BG_Light == 0:
            show kan smug talking with dis
        else:
            show kan smug talking light1 with dis
        kaunk  "\"Who says I’m looking to get anywhere?\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        "He leans in and strokes the edge of his  beer glass with an index finger."
        wi "\"Your posture. Your tone. Your gaze.\""
        wi "\"You like to play games.\""
        if BG_Light == 0:
            show kan eyes smug with dis
        else:
            show kan eyes smug light1 with dis
        kaunk  "\"What’s so wrong with a game or two?\""
        if BG_Light == 0:
            show kan talking with dis
        else:
            show kan talking light1 with dis
        ka "\"Kane’s the name.\""
        if BG_Light == 0:
            show kan smile with dis
        else:
            show kan smile light1 with dis
        "I feel a groan rumble out of my throat."
        wi "\"That don’t even rhyme.\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        ka "\"You callin’ me a poet?\""
        if BG_Light == 0:
            show kan sneer talking with dis
        else:
            show kan sneer talking light1 with dis
        ka "\"Careful now. I could take offense to that.\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        "I sip a little deeper and don’t mind the burn."
        wi "\"If you want to waste your own time, go ahead, but there’s not a whole lot of scotch in this glass.\""
        if BG_Light == 0:
            show kan eyes talking with dis
        else:
            show kan eyes talking light1 with dis
        ka "\"Truth be told, I just like to think your scars are interesting.\""
        if BG_Light == 0:
            show kan eyes smug with dis
        else:
            show kan eyes smug light1 with dis
        wi "\"Be careful about what you call interesting.\""
        if BG_Light == 0:
            show kan smug with dis
        else:
            show kan smug light1 with dis
        ka "\"Can I know how you got ‘em?\""
        wi "\"The swipe to the face was me getting too close to a thug after knocking a gun out of his hand.\""
        wi "\"Sliced me to ribbons.\""
        if BG_Light == 0:
            show kan smug talking with dis
        else:
            show kan smug talking light1 with dis
        ka "\"And what about the chunk out of your ear?\""
        if BG_Light == 0:
            show kan smile with dis
        else:
            show kan smile light1 with dis
        wi "\"That was just a bit of good old-fashioned torture.\""
        if BG_Light == 0:
            show kan talking with dis
        else:
            show kan talking light1 with dis
        ka "\"You say that pretty casual-like.\""
        if BG_Light == 0:
            show kan with dis
        else:
            show kan light1 with dis
        wi "\"I was trained for it.\""
        if BG_Light == 0:
            show kan sneer talking with dis
        else:
            show kan sneer talking light1 with dis
        ka "\"It’s good that you know how to bounce back.\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        wi "\"Most men don’t get far if they don’t.\""
        if BG_Light == 0:
            show kan smug with dis
        else:
            show kan smug light1 with dis
        ka "\"Too true.\""
        if BG_Light == 0:
            show kan smug talking with dis
        else:
            show kan smug talking light1 with dis
        ka "\"Say, do you like to brawl, sheriff?\""
        if BG_Light == 0:
            show kan smile with dis
        else:
            show kan smile light1 with dis
        wi "\"Why, you want to find out?\""
        if BG_Light == 0:
            show kan sneer talking with dis
        else:
            show kan sneer talking light1 with dis
        ka "\"Would you fight me if I gave you a kiss?\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        wi "\"That’s real cute.\""

        ka "\"Who’s joking?\""
        if BG_Light == 0:
            show kan wink with dis
        else:
            show kan wink light1 with dis
        if BG_Light == 0:
            show kan smile with dis
        else:
            show kan smile light1 with dis
        "The hell is with this guy."
        wi "\"Thanks, but I don’t have the time.\""
        if BG_Light == 0:
            show kan smug with dis
        else:
            show kan smug light1 with dis
        ka "\"Pity.\""
        if BG_Light == 0:
            show kan smug talking with dis
        else:
            show kan smug talking light1 with dis
        ka "\"Hard to find folks anywhere who can push as hard as they give.\""
        if BG_Light == 0:
            show kan smug with dis
        else:
            show kan smug light1 with dis
        wi "\"I suppose that’s true.\""
        wi "\"But I’ve finished my drink.\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        ka "\"Find me some other time if you want to get physical, law man.\""
        if BG_Light == 0:
            show kan sneer talking with dis
        else:
            show kan sneer talking light1 with dis
        ka "\"Just for a bit of fun.\""
        if BG_Light == 0:
            show kan sneer with dis
        else:
            show kan sneer light1 with dis
        wi "\"...I’m flattered.\""
        hide kan with dissolve
        "I feel his eyes on my back as I rise out of my seat."
        "Good thing I can see him in the mirror across the room if he tries any sudden moves."
        $ willstag3interview = True
        jump williamstagmenu
label endofwillchallinterviews2:
"That's probably all I'm gonna get out of people right now."
"I think I’m done here."

if STAGNIGHT_Points > 0:
    play music "music/stag1.mp3" fadeout 4.0 fadein 5.0
    wi "\"Thanks for all the help, Nik, but I don’t think there’s a whole lot left for me to learn here.\""
    wi "\"You want to come back to the station with me?\""
    if BG_Light == 1:
        show nik sad light1 with dissolve
    else:
        show nik sad stagback with dissolve
    ni "\"Sam will still be there, won’t he?\""
    "He sounds resentful."
    wi "\"Possibly, unless one of his little friends called him back to the brothel for chores.\""
    if BG_Light == 1:
        show nik sidelook light1 with dissolve
    else:
        show nik sidelook stagback with dissolve
    ni "\"I think I’ll stay here a little while longer.\""
    wi "\"Did something happen between the two of you?\""
    if BG_Light == 1:
        show nik talking light1 with dissolve
    else:
        show nik talking stagback with dissolve
    ni "\"He lied to us for weeks, Will.\""
    if BG_Light == 1:
        show nik light1 with dissolve
    else:
        show nik stagback with dissolve
    wi "\"He had his reasons, didn’t he?\""
    if BG_Light == 1:
        show nik disappointed light1 with dissolve
    else:
        show nik disappointed stagback with dissolve
    ni "\"For you? Absolutely.\""
    if BG_Light == 1:
        show nik sidelook light1 with dissolve
    else:
        show nik sidelook stagback with dissolve
    ni "\"But me?\""
    if BG_Light == 1:
        show nik talking light1 with dissolve
    else:
        show nik talking stagback with dissolve
    ni "\"I expected more trust.\""
    if BG_Light == 1:
        show nik light1 with dis
    else:
        show nik stagback with dis
    wi "\"He told us eventually, didn’t he?\""
    if BG_Light == 1:
        show nik angry light1 with vpunch
    else:
        show nik angry stagback with vpunch
    ni "\"He told {i}you{/i}.\""
    wi "\"I think that’s because he had given up.\""
    if BG_Light == 1:
        show nik sidelook light1 with dissolve
    else:
        show nik sidelook stagback with dissolve
    wi "\"He seemed ready for the worst.\""
    if BG_Light == 1:
        show nik talking light1 with dissolve
    else:
        show nik talking stagback with dissolve
    ni "\"But he should know that he can come to me for anything.\""
    if BG_Light == 1:
        show nik light1 with dis
    else:
        show nik stagback with dis
    wi "\"And I think he would have if he were in a better state of mind.\""
    wi "\"Maybe you should take some comfort in that?\""
    if BG_Light == 1:
        show nik sidelook light1 with dissolve
    else:
        show nik sidelook stagback with dissolve
    ni "\"Maybe.\""
    wi "\"So are you in a better state, now?\""
    if BG_Light == 1:
        show nik disappointed light1 with dissolve
    else:
        show nik disappointed stagback with dissolve
    ni "\"No.\""
    if BG_Light == 1:
        show nik talking light1 with dissolve
    else:
        show nik talking stagback with dissolve
    ni "\"But you’re right.\""
    if BG_Light == 1:
        show nik light1 with dis
    else:
        show nik stagback with dis
    if BG_Light == 1:
        show nik talking light1 with dis
    else:
        show nik talking stagback with dis
    ni "\"So I will be, eventually.\""
    if BG_Light == 1:
        show nik sidelook light1 with dissolve
    else:
        show nik sidelook stagback with dissolve
    "He shifts the weight from the left foot to his right and looks over at the bar."
    if BG_Light == 1:
        show nik eyes light1 with dissolve
    else:
        show nik eyes stagback with dissolve
    ni "\"Goodnight.\""
    if BG_Light == 1:
        show nik light1 with dis
    else:
        show nik stagback with dis
    wi "\"Until next time.\""
    hide nik with dissolve
    "I hope he means what he says."
else:
    "I’m tired of the smell of sweat and rye whisky."

    "That seems like all I can learn from here at the moment."

if STAGNIGHT_Points > 0:
    "Time to go."
    stop music fadeout 5.0
    jump hipinvestigation
else:
    "I think it’s about time to head back to the station."
    jump samstation

pause 0.5
label samstation:
scene white with fade
scene black with slow_dissolve
scene officeday with slow_dissolve
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
window show
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
"William’s been away for a while."
"It’s hard not to think about that whole experience last night."
"How he described the body fighting against the mind."
"And our bodies being cages."
"...and how we come to love and hate our cages at the same time."
"Paul says, {i}For the mind that is set on the flesh is hostile to God, for it does not submit to God's law; indeed, it cannot.{/i}"

"Never much cared for Paul."
"He didn’t even know Jesus."
"And he doesn’t have much interest in living through the struggle of sin."
"His advice is, more or less, {i}just don’t have it.{/i}"
"Which makes me think he lied a lot."
"To make people only hate their cages."
"To revel in death. To revel in breaking out of them as soon as we can."
"To rush into someplace they don’t know."
"Blind faith, or eternal death."
"...that doesn’t sound like Jesus at all."
"{i}If he sins against you seven times in one day, and each time he comes to you saying, 'I repent,' you must forgive him.{/i}"
"{i}Not seven times. But seventy-seven times.{/i}"
"Jesus believed that sin and redemption were a journey."
"Paul didn’t seem to want to walk at all, so to speak."
show cli angry at left,prisonday:
    xzoom -1
with vpunch
cl "\"Who in blazes does this?\""
show cli doubt with dissolve
show tod talking at right,prisonday with dissolve
to "\"I think he has a lot of special jazz numbers that he worries about getting scratched or taken.\""
show tod with dis
"There’s not been a whole lot to do for those two once they found out Will locks his record cabinet."
show cli talking with dis
cl "\"Surely he could leave something cheap out.\""
show cli doubt with dis
cl "\"At the very least a holiday jingle or two?\""
show tod sad with dis
to "\"I wouldn’t say the sheriff is much of a Noel type.\""
show cli shocked
show tod surprised
with vpunch
play sound "sfx/softknock.ogg"
"They both flinch when somebody knocks at the door."
show cli doubt
show tod annoyed
with dis
m "\"Is Will finally back?\""
show tod talking with dis
to "\"Naw, he has his own key, so it wouldn’t make much sense for him to be knocking.\""
show tod with dis
show tod talking with dis
to "\"Back in a jiffy.\""
hide tod with dissolve
show cli talking with dis
cl "\"...bit of an odd expression.\""
show cli happy with dis
cl "\"Samuel, would you happen to know the increment of time that constitutes a jiffy?\""
m "\"Don’t know.\""
m "\"It’s just an expression people say.\""
show cli talking with dis
cl "\"I’ve heard people use it before at my university, but it’s much more prevalent here.\""
show cli with dis
show cli talking with dis
cl "\"How fun.\""
show cli with dis
show tod talking at right,prisonday with dis
to "\"Sam, you have a lady friend at the door.\""
show tod with dis
"He lowered his voice."
show tod eyes happy with dis
to "\"And she smells real nice.\""
show tod surprised with dis
to "\"Like apples.\""
show cyn a at center,prisonday with dissolve
"Cynthia walks on up to us through the doorway."
"She looks more dolled up than usual."
m "\"Cynthia?\""
show cyn talking a with dis
cy "\"Good afternoon Sam.\""
show cli eyes talking with dis
show cyn a with dis
cl "\"Hello miss Cynthia.\""
show cli eyes with dis
show cyn surprised a with dis
cy "\"Oh.\""
show cyn happy a with dis
cy "\"You took me by surprise.\""
show cyn talking a with dis
cy "\"Good afternoon, Mr. Tibbits.\""
show cli talking with dis
show cyn a with dis
cl "\"You look absolutely radiant today!\""
show cli with dis
show cyn talking a with dis
cy "\"Thank you!\""
show cyn a with dis
show cyn talking a with dis
cy "\"Now I don’t mean to be curt, but might I have some privacy with Mr. Ayers?\""
show cyn a with dis
show cli happy with dis
cl "\"Well of cou--\""
show cli shocked with dis
show tod yell with vpunch
to "\"You heard the lady! Now move out!\""
hide cli
hide tod
with dissolve
"Todd practically tackles Cliff out of the office, leaving Cynthia alone with me."
"Christ Todd, if this was somebody else it could have been a problem."
show cyn serious a with dis
cy "\"It’s been a few days.\""
m "\"Yeah, I suppose it has.\""
m "\"I guess I kind of lost track.\""
hide cyn with dissolve
"She walks over to Will’s desk and starts rifling through his drawers."
m "\"Whoa, whoa, whoa!\""
m "\"What are you doing?\""
show cyn talking a at center,prisonday with dissolve
cy "\"Learning.\""
hide cyn with dissolve
m "\"That’s illegal, Cynthia.\""
show cyn happy a at center,prisonday with dissolve
cy "\"Tremendous.\""
hide cyn with dissolve
"She pulls out a notebook, flips through a few pages, and rips them out."
m "\"Lord have mercy, what are you up to?\""
show cyn serious a at center,prisonday with dissolve
cy "\"Just taking a few things about me and some friends that he has, that’s all.\""
show cyn angry a with dis
cy "\"I don’t see the big deal.\""
m "\"He’s gonna know you took them.\""
show cyn serious a with dis
cy "\"Then I’ll just lie.\""
show cyn talking a with dis
cy "\"He shouldn’t have this stuff in the first place.\""
show cyn a with dis
m "\"He’s working on a case for Christ’s sake.\""
m "\"You might screw something up.\""
show cyn angry a with dis
cy "\"If he wants to record this information then he can ask these girls for it to their faces himself.\""
show cyn serious a with dis
cy "\"That sound good?\""
m "\"Whatever.\""
show cyn angry a with dis
cy "\"Is he using you to spy on people?\""
m "\"He hasn’t asked.\""
show cyn serious a with dis
cy "\"Make sure he doesn’t.\""
"I roll my neck."
m "\"If he does then that’s my call to make, isn’t it?\""
"She puts the journal back as neatly as she found it."
show cyn angry a with dis
cy "\"I’m warning you, Sam.\""
show cyn serious a with dis
cy "\"Folks in our line of work are the first to get blamed when shit hits the fan.\""
show cyn eyes a with dis
cy "\"Happens to friends in Coalville. And in Payton. It’s definitely happened before here, too.\""
show cyn serious a with dis
m "\"Wouldn’t he have done that to me already if he was gonna do it?\""
show cyn surprised a with dis
cy "\"I never said I think he dislikes you Sam.\""
"She flaps the pages she tore out of the book loudly, then she stuffs them into her purse."
show cyn angry a with dis
cy "\"I just can’t ignore what he is, and I don’t think you should either.\""
show cyn serious a with dis
cy "\"Just find a way to protect yourself, even if you don’t have to use it.\""
show cyn happy a with dis
cy "\"And come back to work tonight, we miss you.\""
show cyn a with dis
m "\"Alright, alright, I’ll go in.\""
show cyn fear a with dis
play sound "sfx/dooropen.mp3"
"We hear the front door open."
show cyn serious a with dis
"I feel my throat drop into my stomach when I hear William’s voice."
show wil talking at right,prisonday with dissolve
wi "\"I’m back Sam.\""
show wil with dis
show wil shocked with dissolve
"I look back and forth from him to Cynthia and she just crosses her arms."
show wil sideeyes with dissolve
wi "\"And Cynthia too?\""
show cyn talking a with dis
cy "\"Didn’t think I’d be dropping by here either, but if it’s the only way to see Sam for days then I guess it’s all I can do.\""
show cyn a with dis
"She adjusted her purse and walked past Will into the doorway."
show cyn happy a with dis
cy "\"Enjoy the rest of your afternoon, gentleman.\""
show cyn a with dis
show cyn talking a with dis
cy "\"You know where to find me.\""
show cyn a with dis
hide cyn a with dissolve
"Will watches her leave."
show wil surprised at center with dissolve
wi "\"The hell was going on in here?\""
m "\"She’s mad that I’m not at the brothel enough.\""
show wil talking with dissolve
wi "\"Perfect timing, then.\""
show wil with dis
"He took some money out of his pocket and put it in my hand."
show wil embarrassed with dissolve
wi "\"For last night.\""
show wil talking with dissolve
wi "\"Should be enough to get them off your back for a while, right?\""
show wil smile with dis
m "\"It won’t hurt.\""
m "\"But I think she wants to see me more.\""
show wil eyes with dis
"Will shrugged."
show wil talking with dis
wi "\"Then maybe she should start paying.\""
show wil smile with dis
m "\"Hilarious.\""
show wil talking with dis
wi "\"I brought you something to eat.\""
show wil with dis
m "\"What? More beans?\""
"It’s... a sandwich."
"A really nice looking one."
m "\"Is that smoked Salmon?\""
show wil talking with dis
wi "\"There’s a nice place downtown that was open.\""
show wil smile with dis
m "\"Did you get anything for yourself?\""
show wil eyes with dis
stop music fadeout 3.0
wi "\"I ate on the way.\""
hide wil
scene black with fade
play music "music/toddtheme.ogg" fadeout 4.0 fadein 5.0
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"I'm glad Sam likes the sandwich."
$ current_journal_page = 12
$ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
"...Cats are supposed to like salmon, right?"
scene officeday with slow_dissolve


if STAGDAY_Points > 0:
    $ CITYHALLNIGHT_Points +=1
    jump cityhallnight
else:
    $ STAGNIGHT_Points +=1
    jump stagnight

label hipinvestigation:

scene echoroadnight with dissolve
stop music fadeout 3.0
play background "sfx/desertmorning.ogg" fadein 3.0
"Everywhere I’ve been today seems to be pointing me in the same direction."
$ current_journal_page = 14
$ unlocked_journal_pages += 2
$ renpy.notify("Notebook updated.")
"The Hip."
"Dora’s carved out a sizable space in this podunk."
"The CGCS put Echo on the map economically, but the brothel is the only thing in town that attracts genuine celebrities."
stop background fadeout 3.0
scene black with fade
scene saloon2 with slow_dissolve
"Not everybody might be able to afford the Hip daily."
"But everybody’s been there at least once."
"And it’s not just the prostitutes who love the madam."
"Mormons and Meseta; Marxists and capitalists; atheists and protestants; suffragettes and satirists; bull moose boys and yes-men conservatives."
"They might not break bread together, but they mingle in and out, day and night, under the uneasy solidarity of sex and socialization."
"It’s one AM there, so it’s eleven PM here."
scene white with dissolve
"I walk up the stairs and go through the double doors."
scene powderroom with slow_dissolve
play music "music/powderroom.ogg" fadeout 4.0 fadein 5.0
"The powder room is fully active."
"The first person I look for is the person I don’t want to see."
"And I don’t see her, for now."
"But I have no idea how long I’ll have."
"I might have time to interview only one person."

show cyn a with dissolve
"Cynthia is flitting to and from nearly every single male in the room, starting conversations."
wi "\"Evening, Cynthia.\""
show cyn serious a with dis
"She gives me a look."
show cyn talking a with dis
cy "\"Evening, Adler.\""
show cyn a with dis
wi "\"Saw you coming back from the station today.\""
show cyn talking a with dis
cy "\"And?\""
show cyn serious a with dis
wi "\"Just wondering what it’s all about.\""
wi "\"You left in a bit of a hurry when you saw me walk through the door.\""
show cyn talking a with dis
cy "\"It’s hard to have a conversation with Sam when you’re monopolizing him.\""
show cyn serious a with dis
"The hell?"
wi "\"That’s crazy talk.\""
show cyn angry a with dis
cy "\"Is it now?\""
show cyn talking a with dis
cy "\"I’ve barely see him at work now that he’s running around town with you.\""
show cyn serious a with dis
wi "\"He’s a free agent.\""
show cyn happy a with dis
cy "\"Funny how you’re saying that.\""
show cyn serious a with dis
cy "\"You know he told me, don’t you?\""
"He did {i}what{/i}!?"
show cyn angry a with dis
cy "\"It seems like that scares you.\""
wi "\"Because it does.\""
show cyn serious a with dis
cy "\"Now why’s that, exactly?\""
"I lower my voice to a whisper."
wi "\"Because it could get him into deep trouble.\""
show cyn happy a with dis
cy "\"Or maybe you’re just scared that I’ll convince him that you’re taking advantage of his fear.\""
show cyn serious a with dis
"What the hell has gotten into her?"
wi "\"You tell that story to anybody with loose lips and you’ll damn him, woman.\""
show cyn happy a with dis
cy "\"You really think the word of one Meseta hooker is more trustworthy than the big shot Sheriff?\""
show cyn serious a with dis
cy "\"I thought you were supposed to be smart, Adler.\""
"God, she gets really squeaky when she’s mad."
show cyn angry a with dis
cy "\"If you use him like you use the rest of this brothel and then leave him to rot, you'll take some damage.\""
"She's never been this brazen with me before."
show cyn serious a with dis
wi "\"I’m not doing any of that.\""
show cyn serious a with dis
cy "\"Are you kidding me?\""
show cyn angry a with dis
cy "\"His habits are completely different now.\""
show cyn talking a with dis
cy "\"I don’t believe for a second that you aren’t influencing him to stay with you.\""
show cyn serious a with dis
wi "\"Calm yourself.\""
wi "\"I’m just trying to teach him to protect himself for once in his life.\""
wi "\"What he does with that is up to him.\""
wi "\"But he’s not safe being on his own, yet.\""
wi "\"There are things going on that you don’t know about.\""
show cyn eyes a with dis
"She holds up a digit."
show cyn serious a with dis
cy "\"I’ll give you one chance Adler.\""
show cyn angry a with dis
cy "\"One.\""
show cyn serious a with dis
cy "\"If you fuck him up, I promise I will find some way to make you pay.\""
wi "\"One chance is all I need.\""
show cyn angry a with dis
cy "\"Don’t you dare make me regret this.\""
hide cyn with dissolve
$ renpy.notify("Notebook updated.")
$ current_journal_page = 12
$ cynthiatext = _("Maybe Cynthia does too.")
"I take a deep breath as she walks away."
"Shit."
"I wonder who pissed in her grits this morning."
"I’ve got to shake this off."
"I’m here for a reason besides Sam tonight."
"Too many people pointed me in this direction for me to ignore that."
"The first strange thing I see is Harlan, serving drinks."
"Dora is on the couch, watching me ever since I entered the room."
"The only other person who’d be easy to access is Ethel, sitting along on the couch."

menu hipinvestigation1:
    "Now, who would be the most useful to talk to?"
    "Talk to Dora.":
        $ DORINT_Points +=1
        show dor cig talking with dissolve
        md "\"Back so soon, Sheriff?\""
        show dor cig with dis
        wi "\"Duty calls, ma’am.\""
        wi "\"Your office?\""
        show dor cig profile thinking with dissolve
        md "\"Very well.\""
        hide dor with dissolve
        "She puts out her cigarette in her glass and Harlan doesn’t have to be asked to attend to it at once."
        scene doraofficenight with dissolve
        show dor cig profile squint at center,saloon with dissolve
        "Once we’re alone in her office, she gives me her classic glare."
        show dor cig profile talking with dis
        md "\"Could you please do me the favor of keeping this meeting short?\""
        show dor cig profile thinking with dis
        md "\"It’s the start of the week, and it’s already been a long day.\""
        show dor cig profile squint with dis
        wi "\"Any information your girls collect on James would be useful to have.\""
        show dor cig amused with dissolve
        md "\"Good heavens.\""
        show dor cig talking with dis
        md "\"Is this just another dick waving contest between you two?\""
        show dor cig with dis
        wi "\"Ma’am, no.\""
        wi "\"I have reason to believe somebody is targeting him by targeting one of his valued employees.\""
        show dor cig talking with dis
        md "\"Well there’s not a whole lot to know about him that you don’t know already, is there?\""
        show dor cig profile thinking with dissolve
        md "\"He fucks a lot of my girls and wants to bed Samuel, too.\""
        wi "\"And you’re still blocking that, right?\""
        show dor cig profile talking with dis
        md "\"I prioritize him last, but he’s persistent, so he’s bound to get a booking one of these days.\""
        show dor cig profile with dis
        show dor cig profile talking with dis
        md "\"I won’t be surprised when he becomes brazen enough to ask Sam himself.\""
        show dor cig profile squint with dis
        md "\"Why do you care so much about that anyway?\""
        wi "\"I don’t.\""
        wi "\"I just think it’s funny.\""
        show dor cig talking with dissolve
        md "\"Well you better keep up with the price tag if you think it’s so funny.\""
        show dor cig with dis
        wi "\"I pay well in advance, don’t I?\""
        show dor cig talking with dis
        md "\"You slip up sometimes.\""
        show dor cig with dis
        show dor cig talking with dis
        md "\"But regardless of that, I’m sorry that I don’t know much more unless you want very niche specifics, and even then, I couldn’t promise to know.\""
        show dor cig worried with dis
        md "\"The man’s tiresome.\""
        show dor cig talking with dis
        md "\"Is there anything else?\""
        show dor cig with dis
        "Well, shit."
        "I’ve got nothin’."
        wi "\"I think that’s it for now.\""
        show dor cig talking with dis
        md "\"Then let’s return to the powder room, shall we?\""
        show dor cig with dis
        scene powderroom with dissolve
        "I can never read that woman well."
        "When I get back to the powder room, I check my watch."
        jump hattie

    "Talk to Harlan.":
        show har
        show dor cig at left
        with dissolve
        wi "\"Harlan Perkins, might I have a word?\""
        show har eyebrows
        show dor cig profile
        with dissolve
        "He looks to Dora, who swirls the contents of her glass, then he looks back to me."
        show har eyes with dis
        ha "\"If we must, Sheriff Adler.\""
        show har talking with dis
        ha "\"I do have a job to do, and we’re on the clock.\""
        show har eyes with dis
        wi "\"I’ll try not to keep you long.\""
        wi "\"Might we use your office, ma’am?\""
        show har angry with dis
        ha "\"Is that necessary?\""
        show dor cig profile thinking with dis
        md "\"Go ahead.\""
        show dor cig profile talking with dis
        md "\"The last thing we need is the both of you putting a damper on the atmosphere.\""
        show dor cig profile thinking with dis
        wi "\"Much appreciated.\""
        show har angrier with dis
        ha "\"....\""
        scene doraofficenight with dissolve
        "I lead the way to Dora’s office, and I close the door behind us."
        show har talking at center,saloon with dis
        ha "\"Now what’s the meaning of this?\""
        show har with dis
        "I shrug and put up my hands."
        wi "\"No need to be so defensive, Mr. Perkins.\""
        wi "\"I’m on a case, and it might be helpful if you could answer a few of my questions.\""
        show har talking with dis
        ha "\"Might a man feel indignant when he’s shaken down by the law?\""
        show har annoyed with dis
        wi "\"That’s not the situation Mr. Perkins.\""
        wi "\"I’m asking you questions all peaceful-like.\""
        wi "\"Helping me helps you if there’s trouble in our community.\""
        show har talking with dis
        ha "\"And I’m trouble now, is that it?\""
        show har annoyed with dis
        "He sure is dancing around anything that I ask him."
        "He throws out a hell of a lot of questions to statements I don’t make."
        "That alone is a bit suspicious."
        if  MININT_Points > 0:
            $ HARINT_Points +=1
            wi "\"I hear you don’t get along with Mr. Hendricks so much.\""
            wi "\"That true?\""
            show har angry with dis
            ha "\"He stands on the shoulders of giants and makes problems for better men.\""
            "Huh."
            "He didn’t even bother to deflect that one."
            "It came out a little more heated than I expected."
            wi "\"What sorts of problems?\""
            show har angrier with dis
            ha "\"He brings the wrong sort of people into town.\""
            "That’s true."
            "He brought in me, for example."
            show har talking with dis
            ha "\"We need sturdy, practical men, not dreamers and idealists.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Men who can rear a family and keep their noses to the grind.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Those kinds of men are the backbones of society, and we serve them.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Men like you, for instance.\""
            show har angrier with dis
            show har talking with dis
            ha "\"You’re more familiar with a pistol in your hand than a cocktail glass.\""
            show har annoyed with dis
            wi "\"You’re making me swoon, Mr. Perkins.\""
            "But you’re digging yourself an impressive hole."
            wi "\"Do you know anybody else who might share these views on the type of riff-raff James drags into town?\""
            show har smug with dis
            ha "\"Far more folks than you’d think.\""
            "So you aren’t naming names, you have a grudge against James and the people he hires, and you have constant contact with Dora."
            $ current_journal_page = 13
            $ renpy.notify("Notebook updated.")
            $ harlantext = _("Harlan has a grudge against James and has regular access to most of Dora's information.")
            "That’s very interesting."
        else:
            "But then again most people don’t like James."
        wi "\"How would you describe your relationship with Mr. Hendricks?\""
        show har smug with dis
        ha "\"I serve him drinks and redirect his drudgery when he flummoxes patrons in the bar area.\""
        wi "\"And does that create a lot of problems in the bar?\""
        "The hare uncrosses his arms."
        show har unamused with dis
        ha "\"When the other patrons like him, they love him.\""
        show har unamused talking with dis
        ha "\"It’s the staff he tends to flummox.\""
        show har unamused with dis
        wi "\"Have you ever seen his business partners come into the saloon together?\""
        wi "\"Maybe for a drink, or a company lunch?\""
        show har talking with dis
        ha "\"They do, from time to time.\""
        show har with dis
        wi "\"And do any of them seem to dislike one another?\""
        show har talking with dis
        ha "\"He tends to keep them isolated, so they don’t really know each other.\""
        show har with dis
        "By the way I phrased that question, I didn’t expect him to know anything."
        "But he did."
        "Huh."
        wi "\"I think that’s all I have to ask for now, Mr. Perkins.\""
        show har talking with dis
        ha "\"Was it so urgent that I had to be pulled away on the clock?\""
        show har with dis
        wi "\"Urgent enough by my standards.\""
        wi "\"Thank you for your time.\""
        show har talking with dis
        ha "\"It’s precious, so don’t squander it.\""
        show har with dis
        wi "\"Let’s return to the powder room then, shall we?\""
        hide har with dissolve
        scene powderroom with slow_dissolve
        "When I get back to the powder room, I check my watch."
        jump hattie

    "Talk to Ethel.":
        show eth with dissolve
        wi "\"Evening, ma’am.\""
        show eth talking with dis
        et "\"Are you talking to little old me?\""
        show eth with dis
        wi "\"I’m not talking to anybody else, am I?\""
        show eth talking with dis
        et "\"You’ve got a big mouth.\""
        show eth with dis
        show eth talking smug with dis
        et "\"I wonder if that applies the rest of you?\""
        show eth with dis
        "Whoa."
        "She’s laying it on a bit thick, ain't she?"
        wi "\"I’m not interested in your cunt, ma’am.\""
        show eth talking sus with dis
        et "\"Oh wait a minute.\""
        show eth with dis
        show eth talking shock with dis
        et "\"You’re the fucking Sheriff, aren’t you?\""
        show eth talking sus with dis
        et "\"Oh God fucking damn it, of course you are.\""
        show eth talking frown with dis
        et "\"What the hell do you want?\""
        show eth frown with dis
        wi "\"I want to ask some questions is all.\""
        show eth talking sideeye frown with dis
        et "\"Then hand over some money, this isn’t a charity.\""
        show eth frown with dis
        wi "\"Easy enough.\""
        "I hand her a few dollars."
        "But she still isn’t pleased."
        show eth talking frown with dis
        et "\"What, you think that’s all I’m worth.\""
        show eth frown with dis
        wi "\"I’m not exactly paying by the hour now, am I?\""
        if  PORINT_Points > 0:
            $ ETHINT_Points +=1
            wi "\"Be careful about how you proceed though.\""
            wi "\"You probably want to act calm and lower your voice.\""
            show eth talking sideeye frown with dis
            et "\"And why should I?\""
            show eth frown with dis
            wi "\"Because the law in this city discovers lots of things.\""
            "I lean forward."
            show eth talking shock with dis
            wi "\"And if it turned out you had a bad habit of breaching confidentiality of your coworkers’ clients...\""
            "I look over in the direction of the madam."
            wi "\"Your employer might not take so kindly to that.\""
            "She looks really uncomfortable now."
            $ current_journal_page = 14
            $ renpy.notify("Notebook updated.")
            $ etheltext = _("Ethel reacted to a hollow threat of exposure. She's probably the one leaking information to James.")
            "It looks like what the librarian said was true."
        else:
            show eth smug with dis
            "She just gives me another shitty smirk."
        wi "\"What can you tell me about James Hendricks?\""
        show eth talking smug with dis
        et "\"Oh, I can tell you plenty.\""
        show eth with dis
        show eth talking smug with dis
        et "\"He’s good, and he pays well.\""
        show eth with dis
        show eth talking smug with dis
        et "\"And he can definitely manage to make me climax.\""
        show eth smug with dis
        wi "\"That’s not the sort of information that I’m looking for, ma’am?\""
        show eth frown with dis
        et "\"And why not?\""
        show eth talking frown with dis
        et "\"I bet you’re one of those sorts who finishes and then rolls over and falls asleep.\""
        show eth with dis
        show eth talking smug with dis
        et "\"I’d still take your money though.\""
        show eth with dis
        show eth talking smug with dis
        et "\"Less work for me if you’re asleep.\""
        show eth smug with dis
        "They’re not paying me enough for this."
        wi "\"Anything else?\""
        show eth talking smug
        et "\"Well, he gives my cunt a fantastic cleaning.\""
        show eth smug with dis
        wi "\"Charming.\""
        show eth talking sideeye with dis
        et "\"Oh, I’m sorry, were you suddenly expecting me to become a prude?\""
        show eth with dis
        show eth talking smug with dis
        et "\"We’re in a brothel, Sheriff.\""
        show eth with dis
        show eth talking smug with dis
        et "\"Or are you just getting shy because you haven’t tried it?\""
        show eth with dis
        wi "\"I’m not much interested in discussing that, ma’am.\""
        show eth talking smug with dis
        et "\"You know, I always suspect a man might be a fairy until they can prove they’re not afraid to go down south.\""
        show eth smug with dis
        wi "\"Probably true.\""
        show eth talking smug with dis
        et "\"So you do have a pulse, after all.\""
        show eth smug with dis
        "I’m starting to wish that I didn’t."
        show eth talking smug with dis
        et "\"I was starting to think I was talking to a man made out of ice.\""
        show eth smug with dis
        show eth talking smug with dis
        et "\"But deep down, there’s always something that gets you men hot.\""
        show eth smug with dis
        "I look her straight in the eye."
        show eth with dis
        wi "\"I know you think you’re slick, ma’am, but this was sloppy.\""
        show eth eyes with dis
        show eth with dis
        show eth eyes with dis
        show eth with dis
        "She’s blinking at me."
        wi "\"Clean yourself up.\""
        show eth frown with dis
        "She starts to shake and then puts out her cigarette."
        show eth talking shock with vpunch
        et "\"Hurry back to your station so you can masturbate, pig.\""
        hide eth with dissolve
        "Then she gets up and stomps off."
        "I can’t help but chuckle."
        "I wish I could tell her that I jerk off plenty."
        "It’s free--and besides. Men know how to make it feel good better than women can, anyway."
        "We’re the ones who know what a cock feels like, after all."
        "I check my watch."
        jump hattie
    "Talk to Cynthia.":
        $ CYNINT_Points +=1
        wi "\"Just one more thing, Cynthia.\""
        show cyn serious a with dissolve
        "She turns on the balls of her heels and stares me down."
        show cyn talking a with dis
        cy "\"What?\""
        show cyn serious a with dis
        wi "\"If you really do care about Sam and the people in this town, I could use your help with my current case.\""
        show cyn angry a with dis
        cy "\"I’m not interested in any of your crackdowns.\""
        show cyn serious a with dis
        "Luckily the room is still crowded enough to drown out our voices."
        wi "\"It’s murder, Cynthia.\""
        show cyn surprised a with dis
        "She lowers her voice too."
        show cyn fear a with dis
        cy "\"...Another?\""
        "I nod."
        wi "\"Can you tell me anything... and I mean anything about James Hendricks?\""
        show cyn serious a with dis
        cy "\"Well, I hate the man’s guts.\""
        show cyn talking a with dis
        cy "\"He buys up Meseta land as quick as he can for much lower than its value and then families have to turn to the reservation.\""
        show cyn serious a with dis
        wi "\"So it’s personal for you.\""
        show cyn angry a with dis
        cy "\"I dedicated a long time ago that I’d rather sell my body than let another man like that take away my freedom.\""
        show cyn serious a with dis
        cy "\"He’s a client I will never take.\""
        wi "\"I saw earlier that you had Mr. Tibbits as a client.\""
        wi "\"Did he ever talk Hendricks or his business partners?\""
        wi "\"Or maybe he named some folks who don’t like ‘em?\""
        show cyn eyes a with dis
        cy "\"Not really, aside from the men who hurt him earlier.\""
        show cyn serious a with dis
        cy "\"He asked me more about my life than he talked about himself.\""
        show cyn talking a with dis
        cy "\"And then he asked if I could braid some of his fur.\""
        show cyn happy a with dis
        cy "\"Then, he asked it was a special Meseta braid, but I was just honest and told him it’s how Lucy makes challah bread.\""
        "Yikes."
        show cyn serious a with dis
        cy "\"Oh, don’t give me that look.\""
        show cyn happy a with dis
        cy "\"He’s just another man.\""
        show cyn talking a with dis
        cy "\"Most of you have the bad habit of becoming overfamiliar too soon.\""
        show cyn a with dis
        show cyn happy a with dis
        cy "\"It doesn’t bother me that much because I never let it go too far.\""
        show cyn serious a with dis
        wi "\"Well, I guess that’s all that comes to mind.\""
        wi "\"Thank you for your time.\""
        hide cyn with dissolve
        "I check my watch."
        jump hattie

label hattie:
"Shit, it's already been half an hour."
"I can keep coming back here every so often for reports."
stop music fadeout 3.0
"But for now, I think I’ve lingered here long enough."
scene saloon2 with dissolve
"The safest thing I can do right now is look for Sam."
"He talks to the girls, and I don’t have to be out in the open to reach him."
"If he’s not with a client he’s going to be by himself."
scene smokeroomdark with slow_dissolve
"Odd thing is, his door is open when I get to his room."
wi "\"Samuel?\""
"Nobody answers, which is strange."
"Sometimes he stalks the bar at night when nobody’s there anymore."
"Nik found him drunk there once... after downing a whole glass of absinthe."
"He won’t make that mistake again."
scene saloon2 with slow_dissolve
"As I go down the stairs and turn the corner, I hear somebody rattling around."
hat "\"Back so soon, Will?\""
play music "music/reminiscence.ogg" fadeout 4.0 fadein 3.0
"Shit."
show hat eyes at center,saloon with dissolve
"I see Hattie step out from behind the counter."
"I don’t even want to see her, but there she is."
show hat with dis
show bg chicagobar behind hat with slow_dissolve
"Still as bright as spun gold as she was back there."
"But just a bit more frayed around the edges."
show hat talking with dis
hat "\"Are you ready to talk yet, or are you just going to yell some more like a big old baby?\""
show hat smile with dis
wi "\"Ain't much to talk about, is there?\""
wi "\"You’re in danger here.\""
show hat angry talking with dis
$renpy.sound.set_volume(0.2, delay=0.0, channel='sound')
hat "\"I keep getting told that I’m in danger everywhere, Will.\""
show hat angry with dis
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.mp3"
show hat angry talking with dis
hat "\"If not here, then it’s the city.\""
show hat angry with dis
show bg chicagobar behind hat with dissolve
show hat angry talking with dis
stop sound fadeout 3.0
hat "\"If not there, then it’s any city in the north.\""
show hat angry with dis
show hat angry talking with dis
hat "\"Fact of the matter is, the whole wide world’s a pretty dangerous place for a single mother.\""
show hat angry with dis
wi "\"You had a support system there.\""
wi "\"There were people who would protect you and Andy.\""
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.mp3"
show hat angry talking with dis
hat "\"It was cramped and dirty.\""
show hat angry with dis
show hat angry talking with dis
hat "\"And it was expensive, Will.\""
show hat angry with dis
wi "\"I would have sent you money if you asked.\""
show hat talking with dis
hat "\"Maybe I didn’t want your money.\""
show hat with dis
wi "\"If not mine, then whose?\""
stop sound fadeout 3.0
show bg saloon2 behind hat with dissolve
show hat eyes with dis
"She pulls a lighter and a cigarette from her pocket."
"She’s trembling as she struggles to light it."
"She always did have frail hands."
show hat angry talking with dis
hat "\"I’m paying my own way from now on.\""
show hat angry with dis
show hat angry talking with dis
hat "\"Besides, Andy’s past the age for alimony.\""
show hat with dis
show hat talking with dis
hat "\"Mr. Hendricks needs a house cook.\""
show hat with dis
show hat talking with dis
hat "\"I already took the position.\""
show hat with dis
wi "\"Don’t do it.\""
wi "\"The man’s a two-faced pervert.\""
show hat talking with dis
hat "\"Aren’t you too?\""
show hat eyes with dis
show bg chicagobar behind hat with dissolve
"She takes a drag on her cigarette."
wi "\"No.\""
show bg saloon2 behind hat with dissolve
wi "\"I told you the truth.\""
show hat shock with dis
wi "\"It would have been wrong to stay together that way.\""

show bg chicagobar behind hat with slow_dissolve
show hat shock talking with dis
hat "\"We built a life together and you put a child in me.\""
show hat shock with dis
show hat angry talking with dis
hat "\"I’m sorry I couldn’t be the woman you wanted me to be.\""
show hat angry with dis
"All these years and she still doesn’t get it."
show hat eyes with dis
wi "\"I cared about you a lot.\""
show hat smile with dis
wi "\"And you still look good.\""
show hat talking with dis
hat "\"So then what was the goddamn problem, Will?\""
show hat with dis
show bg saloon2 behind hat with slow_dissolve
wi "\"It’s useless to retread this.\""
show hat talking with dis
hat "\"So then we won’t.\""
show hat with dis
wi "\"Hendricks told me you reached out to him.\""
show hat with dis
wi "\"Is that true?\""
show hat talking with dis
hat "\"Only after I had already arrived.\""
show hat with dis
wi "\"You moved here before speaking with Hendricks?\""
show hat talking with dis
hat "\"In truth, the reason I’m here is because I’m worried about Andy.\""
show hat eyes with dis
wi "\"Why worry about him?\""
show hat angry talking with dis
hat "\"He wants to join the army, Will.\""
show hat angry with dis
wi "\"What’s so wrong with that?\""
wi "\"I served my country in my own way.\""
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.mp3"
show hat angry talking with dis
hat "\"And look where that got us.\""
show hat angry with dis
wi "\"My job had nothing to do with what happened to us. You’re just going to have to trust me on that.\""
show hat angry talking with dis
hat "\"I just don’t think it’s a good idea for him to go into the military what with what’s happening in the world right now.\""
stop sound
show hat angry with dis
show bg chicagostadium behind hat with dissolve
show hat angry talking with dis
play sound "sfx/baseballcrowd.mp3"
hat "\"He needs a strong male influence in his life to set him straight.\""
show hat angry with dis
wi "\"Then you definitely don’t want me involved.\""
wi "\"I’d probably encourage him to go.\""
show hat angry talking with dis
hat "\"And why the hell would you do that?\""
show hat angry with dis
wi "\"If the draft comes around he might not have a choice.\""
stop sound
wi "\"Better to get a head start on an officer position than getting dragged in as a foot soldier with everybody else, right?\""
show hat eyes talking with dis
show bg chicagobar behind hat with dissolve
hat "\"I don’t want to think about that possibility.\""
show hat eyes with dis
show bg saloon2 behind hat with dissolve
wi "\"We might have to.\""
show hat shock with dis
"She drops her cigarette into a glass of water."
show hat shock talking with dis
hat "\"Shit!\""
show hat eyes with dis
"I pluck one from my pocket and hand it to her."
"She takes it."
"Then I light it for her."
show hat talking with dis
stop music fadeout 3.0
hat "\"I don’t want to lose him how I lost you.\""
show hat with dis
show bg chicagobar behind hat with slow_dissolve
wi "\"I told you before.\""
if  SW_Points > 2:
    show bg saloon2 behind hat with slow_dissolve
    play music "music/williamtheme.ogg" fadeout 4.0 fadein 5.0
    wi "\"You didn’t lose me Hattie.\""
    wi "\"I was never yours in the first place.\""
    show hat angry talking with dissolve
    hat "\"...that supposed to make me feel better, or somethin’?\""
    show hat angry with dis
    wi "\"It’s just the truth.\""
    wi "\"I’m sorry there isn’t any rhyme or reason to it.\""
else:
    play music "music/spiraling.ogg" fadeout 4.0 fadein 5.0
    wi "\"Everything I did was done to keep us safe.\""
show hat eyes with dis
"She exhales."
show hat eyes talking with dis
hat "\"I’ve been having all sorts of bad feelings, Will.\""
show hat eyes with dis
wi "\"Bad how?\""
show hat talking with dis
hat "\"Feelings like I’m being watched.\""
show hat with dis
show hat talking with dis
hat "\"Or that there’s always somebody waiting around the corner for me.\""
show hat with dis
show hat talking with dis
hat "\"Like those months when we were stalked.\""
show hat with dis
show hat talking with dis
hat "\"It’s like they’re back again.\""
show hat eyes with dis
show hat eyes talking with dis
hat "\"Or more like they never stopped.\""
show hat eyes with dis
"I’ve been feeling the same way."
"But I don’t know if it’s helpful or not to tell her that right now."
wi "\"How did you know how to contact Mr. Hendricks?\""
show hat talking with dis
hat "\"A letter.\""
show hat with dis
wi "\"What was the return address?\""
show hat talking with dis
hat "\"...Didn’t have one.\""
show hat with dis
wi "\"Do you still have it?\""
show hat eyes with dis
"She lowers her paw into the purse at the side and unclasps the copper buckle."
"Then she slips her hand inside."
"She pulls out an envelope with a sliced opening and hands it to me."
"I pull out the letter and read it."
"Some photographs are taped to it, too."
wi "\"What is this?\""
show hat talking with dis
hat "\"That one is the inside of my apartment.\""
show hat with dis
show hat talking with dis
hat "\"The inside of my bedroom, when I’m asleep.\""
show hat with dis
"Some how... some way..."
"James made this happen."
wi "\"...I’ll kill that man.\""
show hat talking with dis
hat "\"But wouldn’t leaving his own phone number incriminate himself?\""
show hat eyes with dis
wi "\"I don’t think he sent the letter.\""
wi "\"But I bet it’s his fault, some way, some how.\""

show hat talking with dis
hat "\"Can you just look after our son if something happens to me, Will?\""
show hat with dis
show hat talking with dis
hat "\"That’s all I’m asking.\""
show hat with dis
wi "\"...That’s a big ask, Hattie.\""
show hat shock talking with vpunch
hat "\"Please!\""
show hat shock with dis
stop music fadeout 3.0
wi "\"...I’ve got to go.\""
show hat eyes with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
wi "\"Call me at the station if you don’t feel safe.\""
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
scene echoroadnight with dissolve
"She’s saying something as I go out the back door of the saloon, but I block it out."
"I can’t be mad at her if she was coerced into coming here."
"But I know there were other places she could go and other people she could go to."
show andy angry talking at center,nightbrown with dissolve
an "\"I thought I saw you stalking around out here.\""
show andy angry with dis
wi "\"Good eyes, good ears.\""
wi "\"I’m not surprised.\""
"Guess I ought to learn how to tread even lighter around here from now on."
show andy angry talking with dis
an "\"Save your breath.\""
show andy angry with dis
show andy angry talking with dis
an "\"It’s your fucking fault we’re out here in the middle of the goddamn desert now.\""
show andy angry with dis
"Lord have mercy."
"Where to start?"
show andy with dis
wi "\"First of all... groom your whiskers better.\""
show andy shock with dis
wi "\"They’re gonna look like shit until your mid-twenties.\""
show andy angry talking with dis
an "\"Oh, fuck off.\""
show andy angry with dis
wi "\"Second, what your mom does is her business.\""
wi "\"I know that you work.\""
show andy talking with dis
an "\"Somebody has to stay with her and support her.\""
show andy with dis
show andy talking with dis
an "\"It’s not you.\""
show andy with dis
"He still thinks he can pull this out on me."
wi "\"That so?\""
show andy shock with dis
wi "\"What’s this I hear about you runnin’ off to the military then?\""
show andy angry talking with dis
an "\"Don’t use that tone on me like you’re my pa.\""
show andy with dis
wi "\"Well, I am.\""
wi "\"But if that’s not good enough for you then just think of me as a concerned third party.\""
show andy talking with dis
an "\"You don’t know what concern even is.\""
show andy with dis
wi "\"Cut the crap, Andy.\""
wi "\"You signing up or not?\""
show andy talking with dis
an "\"A man’s meant to know what to do with a gun in his hands.\""
show andy smile with dis
"I feel more of my breath escape me."
show andy shock with dis
wi "\"You’d do better knowing how to trim first, Andy.\""
show andy angry talking with dis
an "\"I told you to cut that out!\""
show andy angry with dis
wi "\"If you really want to enlist, then you should do it.\""
show andy with dis
wi "\"Better to regret a choice you made yourself than to regret a choice somebody else made for you.\""
show andy eyes with dis
wi "\"It hurts a lot less.\""
show andy eyes talking with dis
an "\"Will you promise to keep ma safe if I do?\""
show andy eyes with dis
if  SW_Points > 2:
    "... I’m not gonna lie here."
    show andy shock with dis
    wi "\"No.\""
    show andy angry talking with vpunch
    an "\"The hell do you mean, no?\""
    show andy angry with dis
    wi "\"Exactly what I said.\""
    wi "\"This place isn’t safe and I told her not to come.\""
else:
    wi "\"I always have, haven't I?\""
    show andy talking with dis
    an "\"And what if you can't this time?\""
    show andy with dis
    wi "\"I expect they'd have to get the drop on me good then, wouldn't they?\""
    "He doesn't look like he's listening to me."
show andy angry talking with dis
an "\"I’ll protect her then.\""
show andy angry with dis
show andy angry talking with dis
an "\"I’ll do it with my own two hands.\""
show andy angry with dis
show andy angry talking with dis
an "\"It’s more than you’ve ever done.\""
show andy angry with dis
wi "\"You have no idea what I’ve been through to protect your mom and you probably never will.\""
show andy shock with dis
wi "\"Now you listen and listen good.\""
show andy with dis
wi "\"There are people here who absolutely will murder you and your mother if you let them get close.\""
wi "\"She said that she’s here for... other reasons, but she was coerced without a doubt.\""
wi "\"If you really care about her then you’ll buy her a ticket out of town.\""
show andy eyes talking with dis
an "\"That’s not gonna work.\""
show andy eyes with dis
wi "\"She’ll do whatever you say if you don’t enlist.\""
show andy talking with dis
an "\"It’s okay, Will.\""
show andy with dis
show andy smile with dis
an "\"I’m a warrior.\""
show andy with dis
wi "\"You are nothing of the sort.\""
wi "\"Now go inside before I beat your ass. It’s not safe after dark.\""
show andy talking with dis
an "\"...Pussy.\""
show andy with dis
wi "\"The fuck you just say?\""
show andy angry with vpunch
an "\"PUSSY!\""
hide andy with dis
"He slams the door."
"Well god damn."
"That boy is in over his head."
"Maybe the military would do him some good."
show sam shocked at center,nightbrown with vpunch
label williamroute3a:
m "\"...Will?\""
show sam surprised with dissolve
wi "\"Sam!\""
show sam talking with dis
m "\"What are you doing here right now?\""
show sam surprised with dis
wi "\"Just catching up on old business.\""
show sam talking with dis
m "\"Fair enough.\""
show sam surprised with dis
show sam talking with dis
m "\"I’m the one who lives here, though, so stop lookin’ at me like I’m suspicious.\""
show sam surprised with dis
wi "\"I’m not suspicious.\""
"At least not of you."
show sam with dis
wi "\"That was my kid back there.\""
show sam talking with dis
m "\"Seemed prickly.\""
show sam with dis
show sam talking with dis
m "\"Hardly surprising I s’pose.\""
show sam with dis
show sam talking with dis
m "\"You see the Mrs. too?\""
show sam with dis
wi "\"Ex-Mrs., but yes.\""
show sam surprised with dis
wi "\"More to the point, whenever they’re closeby, there’s no telling who else is.\""
wi "\"Let’s get back to the station.\""
wi "\"Quickly.\""
scene black with slow_dissolve
play sound "sfx/knock.ogg"
pause 1.2
to "\"Hold on to your horses...\""
scene echoroadnight
show wil eyes at right,nightbrown
with slow_dissolve
play sound "sfx/dooropen.mp3"
show tod sigh a at left,nightbrown with dissolve:
    xzoom -1
"Todd’s tired face pokes past the slip of the opening in the door."
show wil surprised at nightbrown with dis
"His fur is a bit mussed and his shirt is extra wrinkled."
stop sound
show wil talking with dis
wi "\"You alright Todd?\""
show wil with dis
show tod surprised a with dis
to "\"Well, ah...\""
to "\"Sir yes sir!\""
show tod sigh a with dis
to "\"Nothing a bit of hot soup and a few laps around town won’t fix.\""
show tod surprised a with dis
m "\"Runnin’ at this hour?\""
"Wouldn’t he trip over his tail?"
show wil talking with dis
wi "\"Seems like you’re trying to go awful quick.\""
show wil with dis
show tod eyes happy a with dis
to "\"A good night’s sleep keeps me spry, sir!\""
show tod talking a with dis
to "\"I need to check in with my folks soon anyway.\""
show wil talking with dis
show tod surprised a with dis
wi "\"You’re leaving like Clifford isn’t in there behind you.\""
show wil with dis
to "\"Oh.\""
show tod sad a with dis
show wil surprised with dis
to "\"Well that’s because he isn’t!\""
show wil talking with dis
wi "\"What do you mean, he isn’t?\""
show wil surprised with dis
show tod surprised a with dis
to "\"He said he was ready to leave.\""
show wil frustrated with dissolve
wi "\"You were supposed to be watching him.\""
wi "\"It was for his own safety.\""
show tod sad a with dis
to "\"Well he wasn’t under arrest now, was he?\""
show wil talking with dissolve
wi "\"No, but that’s not the point.\""
show wil with dis
show tod surprised a with dis
to "\"Well I ran out of things to distract him with, and I didn’t feel good about makin’ him stay.\""
show tod sigh a with dis
show wil surprised with dis
to "\"But I really oughta get some rest sheriff.\""
to "\"These shorter naps ain’t cuttin’ it.\""
hide tod with dissolve
"The otter hops down the stoop and waddles across the street with a distracted look on his face."
show wil talking with dis
wi "\"Todd, wait!\""
show wil surprised with dis
show tod surprised a at left,nightbrown with dissolve:
    xzoom -1
to "\"Sir?\""
show wil talking with dis
wi "\"Before you go, I need to ask.\""
show wil with dis
show wil talking with dis
wi "\"Whereabouts did you first find Huxley’s body?\""
show wil with dis
show tod sad a with dis
"He scratches the back of his head, as if trying to remember."
show tod talking a with dis
to "\"In a ditch on the side of the road, coming back the direction from Payton.\""
show wil eyes with dis
show tod a with dis
show tod talking a with dis
to "\"About a fifteen minute’s walk east from the station.\""
show tod a with dis
show wil eyes talking with dis
wi "\"Close enough to plenty of houses with an icebox then.\""
show wil eyes with dis
show wil talking with dis
wi "\"Was anybody near the body?\""
show wil with dis
show tod surprised a with dis
$ update_unlocked_pages(1, 15)
$ renpy.notify("Notebook updated.")
to "\"Sir no sir!\""
show tod talking a with dis
to "\"The road was clear.\""
show tod annoyed a with dis
show wil talking with dis
wi "\"He must have been dumped.\""
show wil with dis
show tod talking a with dis
to "\"By a wagon?\""
show tod annoyed a with dis
show wil talking with dis
wi "\"Something like that.\""
show tod eyes happy a with dis
show wil eyes with dis
to "\"Well, I was glad to be of help!\""
show wil eyes talking with dis
hide tod
with dissolve
wi "\"Well you could also let me know--\""
show wil surprised with dis
"But he was already gone."
show wil frustrated with dissolve
"William exhales."
m "\"He looked distracted.\""
show wil eyes talking with dissolve
wi "\"It comes and goes in waves.\""
show wil eyes with dis
show wil talking with dis
wi "\"But he’s been clumsier with just about everything the last few days.\""
show wil with dis
m "\"What do you think the sudden exit was about?\""
show wil eyes talking with dis
wi "\"No doubt somethin’ irritating.\""
show wil eyes with dis
show wil talking with dis
wi "\"Bound to find out soon though.\""
show wil eyes with dis
wi "\"I always do.\""
scene black with dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
scene jailnight with dissolve
show wil at center,prisonnight with dissolve
"The inside of the prison is a lot less dusty than we left it, which would explain the filth on Todd's shirt."
show wil surprised with dis
"Will’s eyebrow lifts as he examines the floor, resting his paws on his hips."
hide wil with dissolve
"Then he walks past the door to his office, stops, then walks backwards, cocking his head as he turns it, pursing his lips as he squints."
show wil frustrated at center,prisonnight with dissolve
wi "\"Oh for the love of...\""
scene officenight with dissolve
"I walk in through the door to see what he’s fussing about."
"The scattered papers look cleaner, and stacked neatly."
"His office is remarkably clean."
"The papers are stacked, the stamps are organized, and there aren’t any stray sheets of paper lying around."
show wil frustrated at center,prisonnight with dissolve
wi "\"I told Todd not to mess with anything.\""
m "\"But ain’t everything better organized this way?\""
show wil talking with dissolve
wi "\"I already had an organized system.\""
show wil with dis
show wil talking with dis
wi "\"Now I just won’t be able to find anything for days.\""
show wil frustrated with dissolve
wi "\"Great.\""
"I see a note of patterned stationery placed on the table."
"It has a mint scent to it."
show wil eyes talking with dissolve
wi "\"What else did he leave...\""
show wil eyes with dis
"There’s fancy lettering in ink."
show wil with dis
m "\"It says something.\""
show wil talking with dis
wi "\"Says what?\""
show wil surprised with dis
m "\"{i}I do so love a desk with a shine,{/i}\""
m "\"{i}And I do so love the scent of pine,{/i}\""
m "\"{i}For a sheriff of reputable achievance,{/i}\""
m "\"{i}To address every public grievance,{/i}\""
m "\"{i}Whilst not buried ‘neath papers, supine!{/i}\""
m "\"Big words.\""
show wil talking with dis
wi "\"Big ego.\""
show wil frustrated with dissolve
wi "\"Insolent bastard.\""
show wil eyes talking with dissolve
wi "\"Should have known better than to leave Todd alone with somebody that pushy.\""
show wil with dis
m "\"Nice of them to clean up for you though.\""
m "\"’Cause I ain’t doing that.\""
show wil talking with dis
wi "\"Didn’t ask you to.\""
show wil with dis
show wil talking with dis
wi "\"But if complete strangers are organizing my personal documents, then they have more than enough opportunities to steal information.\""
show wil with dis
show wil talking with dis
wi "\"I have to at least check to see if everything’s here, now.\""
show wil with dis
m "\"Yeah. All hell’s gonna break loose when people find out who’s pissing in the watering trough.\""
"I pocket my paws and start walking to the direction of the front door."
show wil talking with dis
wi "\"Or maybe where Nik saw you walking back a month ago.\""
show wil with dis
"I swivel on my heel."
m "\"...You wrote that down?\""
show wil eyes talking with dis
wi "\"You’re lucky I burned it.\""
show wil with dis
show wil talking with dis
wi "\"There’s all sorts of information in my notes, Sam.\""
show wil with dis
show wil talking with dis
wi "\"They’re not for just anybody to look at.\""
show wil with dis
m "\"We don’t know if they even looked at anything.\""
show wil talking with dis
wi "\"You’re right.\""
show wil eyes with dis
wi "\"We don’t know.\""
show wil with dis
m "\"I’m worried enough about what is, not what might be.\""
show wil talking with dis
wi "\"Not askin’ you to be worried.\""
show wil with dis
show wil talking with dis
wi "\"Just to prepare for ugly possibilities whenever something like this happens.\""
show wil with dis
m "\"I think you’re on edge.\""
m "\"Do you really need to go and drag me back here just to scare me about Cliff looking at your papers?\""
m "\"Or did you find out somethin’ important in the last 3 hours?\""
show wil talking with dis
wi "\"Found out my ex-wife is working for Mr. Hendricks.\""
show wil with dis
m "\"Bet that stings, but so what?\""
show wil sideeyes with dissolve
wi "\"She showed me a photograph somebody took of her while she’s been sleeping.\""
wi "\"It was her apartment back at the city...\""
wi "\"Which means it’s almost certainly a mobster.\""
"I click my tongue."
m "\"Didn’t you think it was mobsters back at the tunnel?\""
show wil eyes talking with dissolve
wi "\"I don’t know what I heard back there, but a photograph’s a photograph.\""
show wil eyes with dis
wi "\"And I don’t think she’s lying to me.\""
show wil with dis
m "\"So what?\""
m "\"You think Hendricks is responsible for that?\""
show wil talking with dis
wi "\"Could be.\""
show wil with dis
show wil talking with dis
wi "\"I never talked much with him about my wife.\""
show wil surprised with dis
m "\"Or anybody, for that matter.\""
show wil eyes with dis
"His lips tightens and he nods."
show wil eyes talking with dis
wi "\"So somebody I’m not close to had to tell him about her.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"That means he has contacts who can supply him with information that isn’t easy to get.\""
show wil eyes with dis
show wil talking with dis
wi "\"The closeness of his contacts is the question.\""
show wil with dis
show wil talking with dis
wi "\"Either he’s paying somebody a pretty penny for knowledge, or he’s making deals with long-founded partnerships.\""
show wil with dis
m "\"Any idea which?\""
show wil with dis
show wil talking with dis
wi "\"Certainly the former since the man is loaded.\""
show wil with dis
show wil talking with dis
wi "\"But as for the latter, I don’t know how many bridges his father or his grandfather burned.\""
show wil sideeyes with dissolve
wi "\"There’s a lot of nasty rumors still dogging them from what I hear around town.\""
show wil with dissolve
m "\"Nasty, how?\""
show wil talking with dis
wi "\"The stories I hear go something like this...\""
show wil with dis
show wil talking with dis
wi "\"Over fifty years ago, James’ grandfather, James the first, hired a Meseta manservant who he had a good social relationship with.\""
show wil with dis
show wil eyes talking with dis
wi "\"Over the course of that partnership, said manservant allegedly murdered over two dozen children, Meseta and settlers alike, and only some of the bodies were recovered.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"The man was lynched by the town before there was a trial.\""
show wil eyes with dis
show wil talking with dis
wi "\"People also tend to say that James was very reluctant about this series of events, leaving the manor and the mine to his son, James the second.\""
show wil with dis
m "\"So why’s there so much pressure on Hendricks if it was the servant’s fault?\""
show wil talking with dis
wi "\"Some people say James the first was too concerned with his beloved homestead getting associated with the actions of a serial killer and he was too slow to act.\""
show wil with dis
show wil talking with dis
wi "\"Others say the killer was James the first’s lover.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"But folks around here always try to say that deviant behavior all leads to the same end, so I don’t know how much stock I can put into that version of events.\""
show wil with dis
show wil talking with dis
wi "\"Either way, those events cast a shadow on that family despite James the second’s success with the co-ownership of the mine, and James the first’s success with the food industry by the coast.\""
show wil with dis
m "\"I don’t see what his problems would be finding out what he needs if he has money.\""
show wil talking with dis
wi "\"Well, money can get you a lot of things from people who need money.\""
show wil with dis
show wil talking with dis
wi "\"But when it comes to deals and interactions between families who have had money for generations, well, that’s when money only goes so far.\""
show wil with dis
show wil eyes talking with dis
wi "\"If James is responsible for directing Hattie here, then his family might still have some of those old connections.\""
show wil sideeyes with dissolve
wi "\"But if he didn’t, then somebody else is responsible for what happened to her apartment.\""
wi "\"And if somebody had the ability to find her up north, they certainly have the ability to keep tabs on her here.\""
wi "\"And me too.\""
show wil with dissolve
m "\"...You think that has something to do with everything that’s been going on in Echo?\""
show wil talking with dis
wi "\"Maybe not everything.\""
show wil with dis
show wil talking with dis
wi "\"But somebody wants to keep me busy.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Preoccupied at the very least.\""
show wil with dis
m "\"Seems like their plan’s working.\""
m "\"I’m guessing you didn’t pick up any leads again.\""
show wil smile with dis
wi "\"Good news!\""
show wil eyes smile with dis
wi "\"You’re wrong.\""
m "\"Oh yeah?\""

if HARINT_Points > 0:
    show wil talking with dis
    wi "\"That barkeeper at the Hip is a real creep.\""
    show wil with dis
    m "\"Harlan?\""
    m "\"He’s just intimidating, and hard to approach.\""
    m "\"Sort of like somebody else I know.\""
    show wil talking with dis
    wi "\"Hates James’ guts.\""
    show wil with dis
    m "\"So do you.\""
    show wil talking with dis
    wi "\"Has something against Mr. Tibbits too.\""
    show wil with dis
    m "\"So do you.\""
    show wil frustrated with dissolve
    wi "\"You a parrot or something now, Sam?\""
    show wil with dissolve
    m "\"I’m just trying to see where you’re going with this.\""
    show wil talking with dis
    wi "\"He has the means and a motive to want to hurt Mr. Tibbits.\""
    show wil with dis
    show wil talking with dis
    wi "\"He doesn’t want James to do well here.\""
    show wil with dis
    m "\"So what are you going to do about it?\""
    show wil eyes talking with dis
    wi "\"Keep a close tab on him for certain.\""
    show wil eyes with dis
    show wil talking with dis
    wi "\"I also found out Huxley’s gun was pawned and then repurchased.\""
elif ETHINT_Points > 0:
    show wil talking with dis
    wi "\"Your friend Ethel is a snake.\""
    show wil surprised with dis
    m "\"She’s a salamander.\""
    show wil frustrated with dissolve
    wi "\"I mean figuratively.\""
    show wil talking with dissolve
    wi "\"She’s selling brothel information to James.\""
    show wil with dis
    m "\"Are you kidding me?\""
    m "\"She bursts into my room all of the time.\""
    show wil eyes talking with dis
    wi "\"So you should have known ahead of time.\""
    show wil eyes with dis
    m "\"I was always suspicious, sure.\""
    show wil with dis
    m "\"But if you tell the madam she’ll be fired for sure.\""
    show wil talking with dis
    wi "\"So what?\""
    show wil with dis
    m "\"She’ll have no place to go.\""
    show wil talking with dis
    wi "\"None of you will if everybody leaves once they find out all of their personal information is compromised.\""
    show wil with dis
    m "\"Maybe we can resolve this without anybody finding out.\""
    show wil eyes with dis
    wi "\"Maybe.\""
    show wil eyes talking with dis
    wi "\"I’ll see what I can do.\""
    show wil with dis
    show wil talking with dis
    wi "\"I also found out Huxley’s gun was pawned and then repurchased.\""
else:
    show wil smile with dis
    wi "\"Why yes indeedy, Sam.\""
    show wil talking with dis
    wi "\"I found out Huxley’s gun was pawned and then repurchased.\""
show wil with dis
m "\"So how’s that helpful?\""
show wil talking with dis
wi "\"Because it was bought real close to the days it went into somebody else’s hands.\""
show wil with dis
show wil talking with dis
wi "\"His drinking buddy, Reed, didn’t know he was missin’ at the time, so he couldn’t have taken the gun to his usual haunts.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"So he left the house with the gun, or he didn’t, and Marcy was around to see what happened to it.\""
show wil eyes with dis
show wil talking with dis
wi "\"She’d at the very least know if somebody broke into her home.\""
show wil with dis
m "\"So you’re going back to Marcy’s in the morning?\""
show wil smile with dis
wi "\"Yep.\""
show wil talking with dis
wi "\"Come with me again.\""
show wil with dis
m "\"Why?\""
show wil talking with dis
wi "\"Because you notice some things that I miss.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"And I need to bounce ideas off of somebody other than Todd.\""
show wil with dis
m "\"If Todd’s not useful, why don’t just you fire him?\""
show wil talking with dis
wi "\"Because he’s good with people.\""
show wil with dis
show wil talking with dis
wi "\"And he’s been a deputy longer than I’ve been a sheriff.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Locals wouldn’t be happy.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"He served under the former Sheriff.\""
show wil eyes with dis
m "\"Shouldn’t he have been the sheriff after the old guy left?\""
show wil eyes talking with dis
wi "\"Usually that’s how these things go, but that didn’t happen.\""
show wil eyes with dis
wi "\"Might be because he was too young.\""
show wil sideeyes with dis
wi "\"The prior sheriff’s leave was... sudden, but the city hall sent out a scouting campaign, paraded me around town to talk about my experiences, then held the election.\""
show wil eyes talking with dis
wi "\"The rest is history.\""
show wil with dis
m "\"You came off a lot more strict back then.\""
show wil eyes talking with dis
wi "\"Because I was.\""
show wil with dis
show wil talking with dis
wi "\"I wasn’t used to six o’clock meaning six fifteen whenever anybody makes plans around here.\""
show wil with dis
show wil talking with dis
wi "\"But I’ve found that the nature of a place changes you more than you’d like to change it.\""
show wil with dis
show wil talking with dis
wi "\"It breaks you when you’re stiff, so you can choose to bend.\""
show wil with dis
m "\"I’m sorry us hicks have disgraced you so.\""
show wil smile with dis
wi "\"I meant no harm by it.\""
show wil eyes with dis
wi "\"Had to bend for the big city too.\""
show wil eyes talking with dis
wi "\"Hard sometimes to take my mind off how where you’re from in the past is just as much a part of who you are as where you live now in the present.\""
show wil with dis
m "\"Is that just a fancy way of saying the past will catch up with you?\""
show wil sideeyes with dissolve
wi "\"More like the past is always here.\""
"He looks like he wants to say something, but won’t allow that for himself."
show wil eyes with dissolve
"But then he takes a seat in his chair, sitting on it backwards while he drapes his arm over the back and holds his wrist."
show wil talking with dis
wi "\"Stay the night again, Sam.\""
show wil with dis
m "\"You need me to take care of you again already?\""
show wil talking with dis
wi "\"Just to sleep.\""
show wil with dis
show wil talking with dis
wi "\"Might as well since it would save you the walk in the morning.\""
show wil eyes with dis
"His leg begins to bounce like he can’t sit still."
m "\"You’re still paying, right?\""
show wil smile with dis
wi "\"What, you think I’m cheap?\""
"I pull back the curtains to see if I see anybody moving around outside."
"The street looks pretty dead."
m "\"Just making sure.\""
"He spins in his chair, almost like a kid."
show wil eyes talking with dis
wi "\"I’m wounded, Sam.\""
show wil eyes smile with dis
m "\"I’ll get you a bandage in the morning if I remember.\""
show wil talking with dis
wi "\"You comfortable sleeping in my bed again?\""
show wil with dis
m "\"Well I already done it once.\""
show wil talking with dis
wi "\"Just making sure.\""
show wil with dis
show wil talking with dis
wi "\"It’s no trouble putting together a pallet for you.\""
show wil with dis
m "\"I said it’s fine.\""
show wil smile with dis
"He smirks a bit."
show wil surprised with dis
m "\"Did I just see you wag?\""
show wil eyes talking with dis
wi "\"Coyotes don’t wag, Sam.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"You saw me use my tail to keep balance, yes.\""
show wil eyes with dis
"Bullshit."
stop music fadeout 5.0
scene black with slow_dissolve
play background "sfx/crickets.ogg" fadein 5.0
scene bg willbedroomnight with slow_dissolve
"William’s arm holds me by the waist while I sleep."
"I can tell he’s asleep by the way his chest is rising."
"Usually I worry about getting too hot, but I often forget how cold it can get until it’s dark again."
"I sit in silence, wondering if I’m going to hear those noises again."
"Scratches inside the walls."
"I try to listen for them, but there’s nothing."
"That’s when I realized how tired I am."
"Sleep takes me."
$renpy.sound.set_volume(0.3, delay=0.0, channel='sound')
$renpy.sound.set_volume(0.3, delay=0.0, channel='music')
stop background fadeout 5.0
scene black with slow_dissolve
pause 1.5
play sound "sfx/knock.ogg"
pause 1.2
"Fuck."
stop sound
scene bg willbedroom with slow_dissolve
play music ("music/a-moment-of-solace.mp3")
"I throw the thin sheet off of me."
play sound "sfx/knock.ogg"
scene bg willapartment
show wil eyes p at left
with dissolve
"William is sitting by his desk, smoking his pipe as he ignores the beatings against the door."
m "\"That’s not Todd again is it?\""
stop sound
show wil eyes talking p with dis
wi "\"I can tell it is by the way he knocks on the door.\""
show wil eyes p with dis
m "\"Does he do that every morning?\""
show wil talking p with dis
play sound "sfx/knock.ogg"
wi "\"Only when I don’t beat him to the lock.\""
show wil p with dis
m "\"Why don’t you just...\""
stop sound
m "\"Give him a key?\""
show wil talking p with dis
wi "\"I told you before that he ought to know where the spare is hidden.\""
show wil p with dis
m "\"I mean one of those dangly ones on a chain?\""
m "\"For his belt?\""
show wil talking p with dis
play sound "sfx/knock.ogg"
wi "\"For his belt...\""
show wil p with dis
stop sound
m "\"Maybe.\""
show wil talking p with dis
wi "\"You know...\""
show wil eyes p with dis
show wil eyes talking p with dis
wi "\"I stay in bed longer when my temperature’s higher.\""
show wil eyes smile p with dis
wi "\"So it’s technically your fault he’s out there bangin’.\""
show wil eyes p with dis
"He shakes a tin of instant coffee into his mug and starts downing it before it’s completely dissolved."
m "\"You gonna add any sugar or honey to that?\""
play sound "sfx/knock.ogg"
show wil p with dis
"His glance flicks to me, then he tips the mug higher, downing it as fast as possible."
"The empty mug clatters to the table as he lets it sit."
stop sound
show wil talking p with dis
$renpy.sound.set_volume(0.5, delay=0.0, channel='sound')
wi "\"You want any?\""
show wil p with dis
m "\"Nah.\""
play sound "sfx/knock.ogg"
"The banging gets louder while William yawns into one paw and gestures towards the window with his mug."
show wil eyes talking p with dis
wi "\"You get used to it, you know.\""
stop sound
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
show wil eyes p with dis
m "\"Let’s let him in already.\""
hide wil with dissolve
scene black with dissolve
play sound "sfx/knock.ogg"
"We dress ourselves and get to the bottom of the stairs."
scene officeday
show wil at right,prisonday
with dissolve
play sound "sfx/dooropen.mp3"
"I’m the one who opens up the door."
stop sound
show tod arms happy at center,prisonday behind wil with dissolve
to "\"Well it’s about time!\""
show tod surprised with dissolve
to "\"Oh howdy, Sam!\""
m "\"Hello.\""
show tod talking with dis
to "\"You got here earlier than me two times in a row?\""
show tod with dis
m "\"I slept here.\""
show tod eyes happy with dis
to "\"Now there’s a relief.\""
to "\"I was about to whup myself for slackin’ more than the volunteer!\""
show tod with dis
show wil talking with dis
wi "\"No need for any of that.\""
show wil with dis
show wil talking with dis
wi "\"But I will need you in top form today.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Can you do that for me, Todd?\""
show wil with dis
show tod eyes happy with dis
to "\"Sir yes sir.\""
show tod with dis
show wil talking with dis
wi "\"Good.\""
show wil with dis
show wil talking with dis
wi "\"We’re visiting Marcy Greene again today.\""
show wil with dis
show wil talking with dis
wi "\"I’ve got a keen suspicion that she’s going to know what happened to her husband’s gun the day that he went missing.\""
show wil with dis
show wil talking with dis
wi "\"But even if she knows, she might not tell us.\""
show wil sideeyes with dissolve
wi "\"That gun is crucial to the progress of our case, ‘cause it’s connected to the deaths of at least two people, the attempt of a life on a third, and injuring a fourth.\""
show wil with dissolve
show tod eyes happy with dis
to "\"Well, Marcy’s real nice.\""
to "\"I’m sure she’s gonna help us.\""
show wil eyes with dis
show tod surprised with dis
m "\"She still doesn’t know her husband’s dead, does she?\""
show wil eyes talking with dis
wi "\"Not unless she helped do it.\""
show wil with dis
show tod sad with dis
to "\"You think little old Marcy would do such a thing?!\""
show tod surprised with dis
show wil talking with dis
wi "\"Not really, but we can’t rule anything out too early.\""
show wil with dis
show wil talking with dis
wi "\"She’s certainly a suspect, unlikely as it may be.\""
show wil with dis
show tod sad with dis
to "\"But what would make you suspect such a thing?\""
show wil talking with dis
wi "\"Clear evidence of domestic abuse, for one.\""
show wil with dis
show wil talking with dis
wi "\"I found out from his buddy Reed that he was a heavy drinker.\""
show wil sideeyes with dissolve
wi "\"I also found out from the madam of the Hip that he’d brag about controlling her.\""
show wil talking with dissolve
show tod sad with dis
wi "\"Keeping her in line, so to speak.\""
show wil with dis
show wil talking with dis
wi "\"The last time we were there, it looked to me like she was stuck in place...\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Like he had made her depend on him as a part of her routine.\""
show wil eyes with dis
show wil talking with dis
wi "\"Depend on him for so long that she couldn’t live an ordinary life without him.\""
show wil with dis
m "\"Why would she hurt him if she relied on him?\""
show wil talking with dis
wi "\"Sometimes desperate people still need an out.\""
show wil with dis
show wil talking with dis
wi "\"Take into account that she flinches when you speak to her.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Baggy clothes are good for hiding bruises.\""
show wil eyes with dis
show wil talking with dis
wi "\"I don’t know the extent of what he was doin’ to her, but I have a pretty good idea about what this situation looked like.\""
show wil with dis
show wil talking with dis
wi "\"If he went too far, she could have fought for her life.\""
show wil with dis
show tod sigh with dis
to "\"Sir...\""
to "\"With talk like that, you’re really makin’ it seem like she did kill ‘im.\""
show tod sad with dis
show wil talking with dis
wi "\"Except there’s still the matter of the gun, deputy Bronson.\""
show wil with dis
show wil talking
show tod surprised
with dis
wi "\"If it didn’t go missing with him, why didn’t she use it on him?\""
show wil with dis
show wil talking with dis
wi "\"And if she had used it on him, why would she try to throw it away or give it to somebody else?\""
show wil sideeyes with dissolve
wi "\"She doesn’t strike me as a schemer.\""
show wil with dissolve
m "\"So, the gun...\""
show wil with dis
show wil talking
show tod
with dis
wi "\"I think if we can find out what happened to the gun, we can get a little bit closer to finding out who was involved in the death of Huxley Greene, as well as who was responsible for a hit on Mr. Tibbits.\""
show wil with dis
show wil talking with dis
wi "\"And she’s the only one who might know.\""
show wil with dis
show tod talking with dis
to "\"So what are y’all waiting for?\""
show tod with dis
show wil talking with dis
stop music fadeout 5.0
wi "\"You ready to go, Todd?\""
show wil with dis
show tod surprised with dis
to "\"Ready as I’ll ever be, I suppose.\""

scene black with slow_dissolve
$renpy.sound.set_volume(1.0, delay=4.0, channel='music')
scene bg greenecottage with slow_dissolve
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"When we come upon Marcy’s cottage, it’s close to the state it was in a few days ago."
"Except there isn’t that pastry kind of smell anymore, with cinnamon and baked butter."
"It doesn’t smell much like anything."
"Just a bit of overturned earth and dust."
show sam at left:
    xzoom -1
show tod at right
with dissolve
wi "\"Marcy?\""
play sound "sfx/softknock.ogg"
"My knuckles rap against her door."
wi "\"It’s the sheriff.\""
stop sound
wi "\"I want to to talk to you again.\""
play sound "sfx/dooropen.mp3"
"I hear something hobbling around on the opposite side of the door and then it creaks open."
play music "music/mellowpiano.ogg"
show mar dazed with dissolve
show sam surprised
show tod surprised
with dis
"The vacant gaze of Mrs. Greene stares back at us."
stop sound
mar "\"You’re here again?\""
wi "\"Yes, Marcy.\""
wi "\"We need your help again.\""
show mar eyes with dis
mar "\"Have you found him?\""
"I can’t tell her yet."
wi "\"The investigation is underway.\""
show mar eyes talking with dis
mar "\"Come on in, then.\""
show mar eyes with dis
scene bg greenecottageinterior dark with dissolve
show mar at center,house1 with dissolve
show sam surprised at left,house1 :
    xzoom -1
show tod surprised at right,house1
with dissolve
"The state of her house is darker and dingier compared to our last visit."
"There’s so many more dolls."
"All dirty and dingy too."
"I can see clusters of half-filled teacups scattered about the house; some still with fluid in them, catching flies and bugs and specks of grime."
"Yarn has been tacked to the ceiling, like spandrels."
"I think the idea is that it’s supposed to look like the inside of a big-top."
"But the way the banners move makes me think it looks more like the insides of something alive."
wi "\"Thank you for seeing us again, Marcy.\""
wi "\"Truly.\""
show mar talking with dis
show tod sad with dis
mar "\"I just want to see him again.\""
show mar with dis
wi "\"My records indicate that Mr. Greene owned a firearm, pawned, and then repurchased within days of his disappearance.\""
wi "\"This firearm to be exact.\""
show mar dazed with dis
"I put the gun on the table and her eyes go blank."
wi "\"He had this the day he went missing, didn’t he?\""
"She lifts her thumb and sticks out her finger, mouthing gun noises as she points it at me."
show mar eyes talking with dis
mar "\"He’s a good shooter.\""
show mar dazed eyes with dis
mar "\"Rodeo Romeo.\""
mar "\"Gonna take me away.\""
mar "\"Rodeo Romeo.\""
mar "\"Gonna save the day.\""
mar "\"Rodeo Romeo.\""
mar "\"Got time to play.\""
wi "\"What are you singing?\""
show mar smile eyes with dis
"She wheezed first, and then giggled."
show mar smile with dis
mar "\"Our song.\""
wi "\"Marcy...\""
wi "\"Are you dodging my question?\""
show mar with dis
"She pouted."
show mar eyes talking with dis
mar "\"Yes...\""
show mar eyes with dis
wi "\"And why is that?\""
show mar with dis
"She leaned away."
show mar talking with dis
mar "\"Bet you think I’m slow, don’t ya?\""
show mar with dis
wi "\"What?\""
show mar eyes talking with dis
mar "\"He ain’t never coming back, ain’t he?\""
show mar eyes with dis
"Maybe you did kill him."
show mar with dis
wi "\"Now why would you say something like that?\""
show mar talking with dis
mar "\"’Cause the dollies don’t lie.\""
show mar with dis
show mar talking with dis
mar "\"They always tell the truth.\""
show mar with dis
wi "\"Your dollies aren’t alive, Marcy...\""
wi "\"They can’t tell you anything.\""
show mar talking with dis
mar "\"If they can tell the truth, they why can’t you?\""
show mar with dis
show tod sigh
to "\"You’re right Mrs Greene, he’s not comin’ back!\""
show tod surprised
show sam
with vpunch
wi "\"Todd!\""
show mar talking with dis
mar "\"I knew.\""
show mar  with dis
show mar talking with dis
mar "\"I knew the whole time he ain’t comin’ back.\""
show mar with dis
show tod sigh with dis
to "\"But there’s other people out there who need your help!\""
show mar talking with dis
show tod surprised with dis
mar "\"I knew.\""
show mar with dis
show sam talking with dis
m "\"Ma’am...\""
show sam with dis
show sam talking with dis
m "\"We just need to talk to you about the gun!\""
show sam with dis
show mar eyes with dis
"She closes her eyes and starts whispering to herself."
show mar eyes talking with dis
show sam surprised
show tod sad
with dis
mar "\"I knew, I knew, I knew, I knew.\""
show mar eyes with dis
wi "\"Marcy...\""
wi "\"Could we have permission to search your house and the property?\""
show mar dazed with dis
mar "\"...Hmm?\""
wi "\"I can get permission from somebody else if you tell me no, but I don’t want to go through all the trouble.\""
show mar dazed eyes with dis
mar "\"Not like anything matters anymore anyway.\""
wi "\"...I’ll take that as a yes.\""
show mar dazed with dis
wi "\"Again, if you remember anything about this gun, or where it was stored, or who your husband was going to visit the last time you saw him, it could save lives.\""
show mar dazed eyes with dis
mar "\"I knew. I knew. I knew, I knew, I knew.\""
"She keeps repeating the phrase, like it’s a psalm."
hide tod
hide sam
with dissolve
scene black with slow_dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
scene bg greenecottage at sunset with slow_dissolve
play sound ("sfx/doorshut.ogg")
show tod sad at right,sunset
show wil eyes at center,sunset
with dissolve
"The door shuts behind us on our way out of the cottage and the window gets shuttered."
"I could hear soft wailing from the inside."
m "\"...I’m afraid of that woman.\""
stop sound
show wil sideeyes with dissolve
wi "\"She’s traumatized, Sam.\""
show wil frustrated with dissolve
wi "\"And now more so because deputy Bronson couldn’t keep his fuckin’ mouth shut for just a little while longer.\""
show tod surprised with dis
to "\"Well I don’t think you should have lied to her...\""
show wil talking
show tod sad
with vpunch
wi "\"I thought I had explained to you that she’s a suspect?!\""
show wil with dis
show wil eyes talking with dis
wi "\"Now if she’s got something to hide then we’ll never get it out of her willingly.\""
show wil eyes with dis
stop music fadeout 9.0
m "\"So now what do we do?\""
show wil frustrated with dissolve
wi "\"Scout the property and wait for her to calm down.\""
m "\"And how long is that gonna take?\""
show wil with dissolve
show wil eyes with dissolve
wi "\"Could be a few hours, could be a few days.\""
show wil talking with dis
wi "\"Now we just gotta hope for the best that she’s isn’t guilty and that she’ll be in the right mind to cooperate in the future.\""
show wil with dis
show wil talking with dis
wi "\"Until then we ought to look around.\""
show wil eyes with dissolve
show wil eyes talking with dis
show tod surprised with dis
wi "\"Why don’t you and Todd search the grounds surrounding the house while I search the road.\""
show wil with dissolve
m "\"What should we be looking for?\""
show wil talking with dis
wi "\"Trash, or wheel marks, or scraps of clothing.\""
wi "\"I don't think we'll find anything, but something is better than nothing.\""
show wil with dis
show wil talking
show tod
with dis
wi "\"You could start with her shed.\""
show wil with dissolve
show wil talking with dis
wi "\"She probably has more outdoor storage around here and that’s worth checking too.\""
show wil with dis
"I scratch the back of my head."
m "\"You know, this ain’t my job, Will.\""
show wil talking with dis
wi "\"I know, but it's close where I'll be for the next few days, and I think it would be best for you to keep by.\""
show wil with dis
m "\"I get that, but I have other things that I could be doing right now.\""
show wil with dis
wi "\"Like I said before, I don't think we're going to find anything.\""
show wil talking with dis
wi "\"I know it's been a long day.\""
wi "\"If y'all don't find anything in a few hours, you and Todd can head off home or back to the office.\""
show wil sideeyes with dissolve
wi "\"I need some time to myself to think about how we’re going about this again.\""
show wil with dissolve
m "\"Alright\""
m "\"Guess I’m with you for the next few hours, Mr. Bronson.\""
show tod talking with dis
to "\"Looks like I’ll get to show you the ropes for a spell!\""
show tod with dis
show wil talking with dis
wi "\"Let’s try to meet back in front of the house in a few hours.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Hopefully no more than two at most.\""
show wil eyes with dis
hide wil with dissolve
"Will trots off down the dusty road, disappearing as he turns past an outcropping of rocks."
m "\"So, how are we supposed to go about this again?\""
show tod talking with dis
to "\"We can start with a general sweep of the perimeter.\""
show tod with dis
show tod talking with dis
to "\"Just think about it like it’s a nice walk.\""
show tod with dis
m "\"Ain’t there more to it than that?\""
show tod talking with dis
to "\"I think it’s best to get a general impression before we get bogged down by any details.\""
show tod eyes happy with dis
to "\"Just keep your eyes and ears open and enjoy yourself.\""
show tod with dis
play background ("sfx/birds.ogg") fadein 8.0
scene bg greeneshed with dissolve
"The Greenes’ property is a lot bigger than I thought it would be, though I suppose it makes sense they’d have more room per how far away from down town they are."
"It takes us about a ten minute hike before we see any trace of anything at all down the dirt road."
"We can see Emma in the distance through a copse of trees, and there are a few shallow creeks and ditches full of smooth pebbles around."
show tod at right,sunset with dissolve
m "\"Just how big is the Greene property?\""
show tod talking with dis
to "\"Fifty acres, roughly.\""
show tod with dis
"That's a huge amount of land for the little cabin to sit on."
"Up ahead, I see a ramshackle building under a thick pine tree that looks like it might be a tool shed, considering it ain’t that big."
show tod at right,sunset
m "\"Think it’s locked?\""
show tod talking with dis
to "\"I’d reckon so.\""
show tod sigh with dis
to "\"Mr. Greene always did get touchy about people stayin’ away from his things.\""
show tod with dis
m "\"Let’s just try.\""
"We walk past pots of succulents here and there, next to squatting ornaments of cast-iron imps, and gnomes, and angels, all with pudgy baby faces."
"There’s a thick padlock over a horseshoe-shaped bar shoved into very thin, very rickety wood."

show tod eyes happy with dis
to "\"Take a look at this puppy.\""
show tod with dis
"He pulls out a pocket knife and pulls out its sides, showing off a set of oddly shaped blade ends."
show tod talking with dis
to "\"I bet if I can fiddle with this for about half an hour and get the right feel, I just might be able to get us inside.\""
show tod surprised with dis
play sound ("sfx/padlock.ogg")
"I jiggle the u-shaped bar and it comes clean out of the wood with the lock falling to the ground."
show tod sigh with dis
to "\"Well, yeah, that was a good idea too.\""
stop sound
play sound "sfx/doorcreakopen.mp3"
"The door creaks as we walk inside the dusty shed."
stop sound
$renpy.sound.set_volume(0.2, delay=0.1, channel='background')
scene bg greeneshedinterior with dissolve

show tod dark3 at right with dissolve
"Specks of light play off the surface of rusty tools on their racks, and the cobwebs in the corners of the room glimmer."
m "\"You see anything out of the ordinary?\""
show tod talking dark3 with dis
to  "\"There’s a hoe, a shovel, a can of oil...\""
show tod annoyed dark3 with dis
to "\"A well-used bin with some pine needles on the bottom, a few cans of paint...\""
show tod sigh dark3 with dis
to "\"Nothing much out of the ordinary.\""
show tod talking dark3 with dis
to "\"I guess we can put the lock and the door handle back into place.\""
show tod dark3 with dis
m "\"Shouldn’t we look a little longer?\""
show tod sigh dark3 with dis
to "\"I guess we could, but I think we’ve seen everything.\""
show tod dark3 with dis
m "\"Right...\""
m "\"But we’ve been here less than a few minutes.\""
m "\"We probably missed something.\""
show tod talking dark3 with dis
to "\"Sure, but there’s still a whole lot of land to cover.\""
show tod sigh dark3 with dis
to "\"Sometimes there ain’t a whole lot beneath the surface, you know?\""
show tod annoyed dark3 with dis
m "\"I’d think it depends.\""
show tod surprised dark3 with dis
m "\"Maybe you’re not trying as hard as you could be because you knew ‘em.\""
show tod annoyed dark3 with dis
to "\"Know who exactly?\""
show tod dark3 with dis
m "\"Well, you’ve know Mrs. Greene for a while, right?\""
show tod talking dark3 with dis
to "\"’Course I do.\""
show tod eyes happy dark3 with dis
to "\"My uncle works for the bank, so my family always exchanged gifts with the Greenes.\""
show tod dark3 with dis
m "\"For some reason I thought your uncle owned a barber shop.\""
show tod talking dark3 with dis
to "\"No, that’s my other uncle, Amos Bronson.\""
show tod dark3 with dis
m "\"How many uncles you got?\""
show tod talking dark3 with dis
to "\"Seven I think, but four of ‘em live up in Camp Rosa so I only see them at the reunion.\""
show tod dark3 with dis
m "\"And how many kids they got?\""
show tod eyes happy dark3 with dis
to "\"They all got at least three but some of ‘em have up to seven.\""
show tod dark3 with dis
m "\"That’s too many.\""
show tod eyes happy dark3 with dis
to "\"Ain’t no such thing when it comes to family!\""
to "\"More family just means more to love!\""
show tod dark3 with dis
m "\"But how do y’all keep track of each other?\""
show tod talking dark3 with dis
to "\"Same way as everybody else does, I suppose.\""
show tod dark3 with dis
show tod talking dark3 with dis
to "\"Writin’. Keepin’ picture albums, swappin’ gossip and makin’ memories when we can.\""
show tod dark3 with dis
show tod talking dark3 with dis
to "\"And the local family sees one another every Sunday.\""
show tod dark3 with dis
m "\"Sounds busy.\""
show tod talking dark3 with dis
to "\"When do you see your family?\""
show tod surprised dark3 with dis
m "\"I don’t.\""
show tod talking dark3 with dis
to "\"How come?\""
show tod surprised dark3 with dis
m "\"Don’t like ‘em.\""
show tod sigh dark3 with dis
to "\"Well, what for?\""
show tod annoyed dark3 with dis
m "\"They had a lot of ideas about what I should be doing, I suppose.\""
m "\"Which trade I should learn.\""
m "\"How often I should be available for them.\""
m "\"They broke the law a lot.\""
show tod talking dark3 with dis
to "\"Doin’ what?\""
show tod annoyed dark3 with dis
m "\"Nothing too big.\""
m "\"Mostly moonshine.\""
m "\"Sometimes even riskier stuff.\""
show tod sigh dark3 with dis
to "\"Bonafide smugglers, huh?\""
show tod annoyed dark3 with dis
m "\"I wasn’t proud of them.\""
m "\"But if they knew me now I guess they wouldn’t be proud of me, neither.\""
m "\"And I guess I was scared I’d go down with them one day.\""
show tod talking dark3 with dis
to "\"Think they’re in jail by now?\""
show tod surprised dark3 with dis
m "\"Who knows if they’re even alive.\""
m "\"I wouldn’t shed any tears for ‘em.\""
m "\"Lord knows they wouldn’t shed none for me.\""
show tod sad dark3 with dis
to "\"That’s so sad.\""
show tod surprised dark3 with dis
m "\"I think it’s simple.\""
m "\"And fair.\""
m "\"I didn’t agree to be born to those people.\""
show tod sad dark3 with dis
to "\"I just don’t like to see a family neglecting one another.\""
show tod sigh dark3 with dis
to "\"Family is supposed to help each other.\""
show tod talking dark3 with dis
to "\"If not to one another’s dishes at the Sunday potluck, then at least when they’re in trouble.\""
show tod annoyed dark3 with dis
m "\"Your family ever try to make you wash your mouth out with bleach if you swore.\""
show tod surprised dark3 with dis
to "\"Of course not!\""
show tod sigh dark3 with dis
to "\"And we don’t swear at one another because we respect each other.\""
show tod dark3 with dis
m "\"That must be nice.\""
m "\"How often did your family visit the Greene’s?\""
show tod talking dark3 with dis
to "\"I’ve been over there more times than I can remember.\""
show tod eyes happy dark3 with dis
to "\"Since I was a baby, I reckon!\""
hide tod with dissolve
"I know Todd said he wanted to leave but I make sure to turn over ever shovel, every can, every piece of junk I can find."
"Todd just awkwardly stands by the door, looking out of it as if he won't leave until I go with him."
"When he figures out I'm determined to be thorough, he sags a bit and starts helping me sort through the junk."
"After a decent while we sort through more paint cans than I can count."
"I check under the slats in the floorboard."
"One of them goes back in quick-like when I see an angry looking black scorpion skittering towards the direction of my arm."
"I wipe my brow with the back of my arm and keep looking."
"Todd looks at me back with that wide stare."
show tod dark3 with dissolve
m "\"Find anything yet?\""
show tod sigh dark3 with dis
"He shakes his head."
m "\"Well, we've got just a few more things to look through.\""
show tod dark3 with dis
m "\"Do you know if Marcy owned the house before Huxley?\""
show tod talking dark3 with dis
to "\"Oh, no, they’ve been together my whole life.\""
show tod dark3 with dis
m "\"You know, Mrs. Greene doesn’t look that old.\""
show tod sigh dark3 with dis
to "\"Well it’s rude to ask a lady her age, Mr. Ayers.\""
show tod dark3 with dis
m "\"So you never did?\""
show tod eyes happy dark3 with dis
to "\"No siree-bob.\""
show tod dark3 with dis
m "\"Huh.\""
show tod surprised dark3 with dis
m "\"You seem tense around women in general.\""
show tod annoyed dark3 with dis
to "\"No I don’t.\""
"You can’t just tell somebody that they didn’t experience an observation, Todd."
m "\"What I mean is that you tense up when it comes to asking even basic questions of a woman.\""
m "\"But when you talked with me at the sheriff’s office a few days ago, you got real personal.\""
show tod surprised dark3 with dis
to "\"I didn’t mean to!\""
show tod sigh dark3 with dis
to "\"I just thought you were used to hearin’ about stuff like that from people.\""
show tod dark3 with dis
m "\"I’m not angry.\""
m "\"I just think it’s funny.\""
show tod annoyed dark3 with dis
to "\"And I just think it’s important to respect women, okay?\""
show tod sigh dark3 with dis
to "\"There’s all sorts of bad people out here here who’d jump at the opportunity to dishonor them.\""
show tod surprised dark3 with dis
m "\"People like Mr. Greene?\""
show tod annoyed dark3 with dis
to "\"Now wait just a minute...\""
to "\"I never said any of that, now.\""
m "\"You didn’t seem very upset when you showed us Mr. Greene’s body, though?\""
show tod angry dark3 with dis
to "\"You trying to imply something?\""
show tod annoyed dark3 with dis
m "\"Not much else besides you clearly didn’t like ‘em.\""
m "\"Marks me as queer considerin’ you knew him since you were a baby.\""
show tod angry dark3 with dis
to "\"Well it can be hard to make a fuss over bad people when they kick the bucket.\""
show tod annoyed dark3 with dis
m "\"You think those rumors William was saying about Huxley were true?\""
show tod angry dark3 with dis
to "\"Probably worse, but I don’t like to think about it.\""
show tod sigh dark3 with dis
to "\"Mrs. Greene seemed happy enough so I just helped when I could.\""
show tod sad dark3 with dis
to "\"She isn’t so good with chores.\""
m "\"I can see that.\""
m "\"I just wanted you to know that most women aren’t like Marcy.\""
show tod surprised dark3 with dis
m "\"You treat ‘em like special linens and they’ll be offput by the disrespect.\""
m "\"If you’re not willing to get a little personal with somebody once in a while they’ll think you aren’t interested.\""
m "\"And if you’re always more personal with men than women, well...\""
m "\"You’ll probably find yourself in bed with a man sooner than a woman.\""
show tod annoyed dark3 with dis
to "\"Now don’t you go making any presumptions about me, y’hear?\""
m "\"I don’t think it’s presumptuous to say most people get lonely.\""
show tod surprised dark3 with dis
m "\"I could tell what you were doing in Will’s attic.\""
m "\"You mentioned Mr. Tibbits before you did.\""
show tod annoyed dark3 with dis
m "\"I’ve gotta ask an honest question if you’ll humor me.\""
show tod talking dark3 with dis
to "\"Ain’t nobody else out here, so fine.\""
show tod surprised dark3 with dis
m "\"...Were you thinking about some she-otter, or were you thinking about him?\""
show tod sigh dark3 with dis
to "\"Neither actually.\""
m "\"Then who?\""
show tod surprised dark3 with dis
to "\"Those thoughts ain’t pure.\""
m "\"The company you’re in ain’t exactly pure.\""
to "\"Ah...\""
show tod sigh dark3 with dis
to "\"You’re definitely sleepin’ with Mr. Adler, then, ain’t you?\""
m "\"I thought you knew.\""
show tod surprised dark3 with dis
to "\"Well, ah, I pretty much figured.\""
show tod annoyed dark3 with dis
to "\"It's just a lot to take in when I start to really think about it.\""
to "\"I respect Mr. Adler a lot.\""
to "\"He’s sort of like another father to me.\""
show tod surprised dark3 with dis
to "\"Sort of like one who tells you all sorts of stuff you’re not supposed to know.\""
m "\"So what?\""
show tod sigh dark3 with dis
to "\"So, uh...\""
show tod surprised dark3 with dis
to "\"It’s kind of awkward picturing you doing things for him.\""
"He pauses, stammering a bit, like he's trying to spit something out."
show tod sigh dark3 with dis
to "\"Mostly because I know he's not supposed to.\""
show tod talking dark3 with dis
to "\"And also because I think it’s easy to see why he’d want you to.\""
"Now there's a confession."
"I knew there was something funny about this one when I worked him up to spankin' himself off at the Sheriff's office."
"But something's put him in an earnest mood."
"Maybe the all the anxiety's loosened his tongue a bout."
"I heard before from Cynthia that otters get squeaky when they're scared, and also when they're in a mood."
"Maybe Todd's the kind to mix those two emotions up."
show tod surprised dark3 with dis
m "\"You saying I make you stiff, Mr. Bronson?\""
to "\"Well I try not to get stiff at all, Mr. Ayers.\""
show tod sigh dark3 with dis
to "\"Thoughts lead to actions.\""
to "\"And if I do something like that, I know I ain’t ever gettin’ into heaven unless I marry, and who knows if I’ll ever have the chance.\""
show tod surprised dark3 with dis
m "\"You really think all that’s true?\""
to "\"That’s what my family taught me.\""
show tod surprised dark3 with dis
m "\"How specific did they get?\""
show tod annoyed dark3 with dis
to "\"Mr. Ayers...\""
to "\"Nobody ever goes into the details about things like that.\""
show tod surprised dark3 with dis
m "\"So what you’re saying is you don’t know how far is wrong?\""
show tod annoyed dark3 with dis
to "\"I think I have a pretty good idea.\""
show tod surprised dark3 with dis
m "\"Seed’s gotta go somewhere if it’s not going in a wife, right?\""
show tod sigh dark3 with dis
to "\"It’s a violation of something we call the law of chastity.\""
show tod surprised dark3 with dis
m "\"But you’ve finished in your paw before, right?\""
show tod sad dark3 with dis
"His ears droop."
to "\"I’m not proud of all that.\""
show tod sigh dark3 with dis
to "\"Sometimes it comes out and you can’t help it.\""
show tod sad dark3 with dis
m "\"So you’re already breaking the rules, ain’t you?\""
show tod sigh dark3 with dis
to "\"That path to chastity is a road any man can walk, even after they stray.\""
m "\"So why not stray and walk the path later?\""
show tod annoyed dark3 with dis
to "\"Mr. Ayers...\""
m "\"There’s plenty you can do with another man that ain’t quite close to christenin’ your wedding bed.\""
m "\"Sometimes it’s just a matter of helpin’ each other get the stuff out.\""
show tod sigh dark3 with dis
to "\"How far could we go if I wanted to stop?\""
m "\"As far as you want if we’re quick about it.\""
show tod sad dark3 with dis
to "\"I don’t know if I'd feel right doing something like that in Marcy’s shed.\""
show tod surprised dark3 with dis
m "\"A few minutes ago it sounded like you didn’t want to do anything at all.\""
"There’s that ottery smell in the air again."
"Pretty certain he does want to."
show tod sigh dark3 with dis
to "\"Can it be outside?\""
m "\"Out in the open?\""
show tod talking dark3 with dis
to "\"Feels less disrespectful to indugle in  earthly pleasures out in nature.\""
to "\"Plus, there’s coverage behind the shed.\""
to "\"And ain’t nobody comes this way.\""
show tod sigh dark3 with dis
to "\"You, ah, really wanna do this?\""
m "\"Do you?\""
show tod dark3 with dis
"I'm asking him and myself both the question at the same time."
"I don’t know."
"Another steady customer seems too good to turn up."
"And we already know William is preoccupied in a different direction."
show tod surprised dark3 with dis
m "\"How about I just give you a taste of the experience?\""
m "\"We can do something quick and easy and then you can vist me later...\""
m "\"...with money.\""
show tod sigh dark3 with dis
to "\"Well how quick is quick?\""
show tod surprised dark3 with dis
m "\"Take your shirt off and follow me outside.\""
hide tod with dissolve
pause 0.2
show tod surprised p dark3 at right with dissolve
pause 0.2
$renpy.sound.set_volume(1.0, delay=1.0, channel='background')
scene bg greeneshed with dissolve
show tod p at center,sunset with dissolve
"We get to the back of the shed, and while it’s not perfectly concealed, I still get the feeling that we’re very much alone, and will be for a long time."
m "\"After we start, no finishing.\""
show tod talking p with dis
to "\"...Why not?\""
show tod p with dis
m "\"Because it has a smell to it.\""
show tod surprised p with dis
m "\"William don’t need an explanation for that, does he?\""
m "\"’Cause if he asks for the truth, I’m just gonna tell him.\""
to "\"Oh God no.\""
m "\"Saying the lord’s name in vain already?\""
"I tsk."
show tod sigh p with dis
"I touch him through his pants."
show tod arms sigh p with dissolve
"He’s stiff."
"Bigger than I thought he’d be too."
"Then I give him a squeeze through the slacks."
show tod surprised p with dissolve
m "\"Keep these on if we’re going to have to cover up quick if somebody comes our way.\""
show tod sigh p with dis
to "\"D-don’t remind me.\""
show tod surprised p with dis
"I set down a sheet covering a crate and lie it on the dirt."
m "\"Now lie on your back.\""
"He looks left, then he looks right, then bends his knees, scooting backwards."
hide tod with dissolve
"His chest rises as he looks up at me."
"I sink down on my knees, looming over him."
window hide
pause 0.5
scene bg wilcg6a with slow_dissolve
pause 1.0
window show
m "\"What’s the matter?\""
m "\"Scared?\""
"He shuffles a bit, and licks his whiskers."
to "\"Well not of you, no.\""
"I dip my hands down his pants and fish him out."
"God damn, he’s leaking."
"I bow down my head and smirk."
"Then I fish out my own cock and his eyes widen."
"I bring it as close as I can to his cock without touching it."
m "\"Well maybe you should be?\""
to "\"I don’t...\""
m "\"Want to stop yet?\""
to "\"I don’t know.\""
"I scoot in, leaning in closer over him, and hold his wrist down with my paw."
"He isn’t struggling."
m "\"If you don’t want to admit that you like it, you can just blame it on me, you know.\""
"I press us together and he lets out a squeak of surprise."
"His tongue is slipping out of his mouth, and his cock is throbbing with his pulse beneath mine."
window hide
pause 0.5
scene bg wilcg6b with slow_dissolve
pause 1.0
window show
"We're practically stuck to one another now between the two of because of our pre, and his cock is making sounds each time it pulls away."
m "\"Gonna ask you again...\""
"I punctuate it with slow, deliberate rub, squeezing us together, producing a sloppy sort of sound that’s always much louder than you think it should be."
m "\"Do you want me to stop yet?\""
play sound ("sfx/branch2.ogg")
scene black
stop background fadeout 3.0
"A twig snaps."
scene bg greeneshed:
    zoom 1.03
    truecenter
play sound ("sfx/tumble.ogg")
show tod surprised2 p at right,sunset
with hpunch
"We slide off of one another like we’re the opposite ends of a magnet."
"Fuck, fuck, fuck!"
stop sound
play music ("music/bedhorror.mp3")
"I look around."
"I don’t see nobody."
play sound ("sfx/belt.ogg")
show tod surprised p with dissolve
"I look at Todd, who’s flailing with the ends of his belt like it’s two heads of fighting snakes."
"I snatch my shirt from off of a beam and toss it on myself and crouch behind a crate."
stop sound
"He mouths ‘don’t leave me!’ and I try to mouth back ‘you’re just one person, it’s fine!’"
hide tod with dissolve
play sound ("sfx/foreststep.ogg")
"More pine nettles crunch as we can hear somebody coming back out of the bush."
show mar dazed eyes at halfleft,sunset with dissolve
stop sound
"What’s not so surprising is that it’s Marcy."
"But what is surprising is the blood running down her legs."
play sound ("sfx/wsplash.ogg")
show blood08:
    zoom 1.03
    truecenter
"And then we hear something splash on the ground." with vpunch
window hide
pause 1.0
stop music fadeout 4.0
scene black with slow_dissolve
stop sound
play background ("music/cicadas.mp3") fadein 5.0
scene bg echoforest at sunset with slow_dissolve:
    zoom 1.03
    truecenter
window show
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"I still can’t believe Todd spilled the beans on Huxley."
"If Marcy falls through, or we can’t find any evidence of where the gun went, we’re out of leads and probably out of time."

"I’m pretty sick of carrying around this pistol."
"Usually a weapon alone wouldn’t connect this many people."
"If I were the sort to believe in curses, I’d have this thing melted down after the conclusion of this investigation."
"I’d leave that up to Marcy, but she’s not looking too good."
"I come to the part of the road that’s a three way juncture."
"East to downtown, west to Payton, south to the railway tracks."

"If there were a road directly north, I’d be at Hendricks manor."
"Sooner or later, I’m going to have to investigate there."
"Even if she’s gonna be there."
"I wonder what sort of game he’s playing with her."
"Did he put her there to keep me away, or did he put her there because he knew I’d be too stubborn to resist an investigation?"
play sound ("sfx/gravelwalk.ogg")
"Up ahead I see something bright sticking up out some of the rocks."
"It’s a discarded gum wrapper."
stop sound
"Tutti-frutti, huh?"
"I don’t recall ever seeing Marcy chewing much gum."
"And Huxley was usually too busy with a bottle."
$ update_unlocked_pages(1, 16)
$ renpy.notify("Notebook updated.")
"This doesn’t look old."
"Makes you wonder who’s been putting this stuff in their mouths."
kaunk "\"Afternoon, lawman.\""
play sound "sfx/branch.mp3"
play music "music/foreman.mp3"
show kan smile at center,sunsetkane with vpunch
"I take a big step backwards."
stop sound
wi "\"Christ on a cracker!\""
wi "\"Ain’t you a sneak.\""
show kan wink with dis
ka "\"Wouldn’t be satisfied with myself if I wasn’t.\""
show kan smile with dis
wi "\"That’s enough tom-foolery.\""
wi "\"This path’s somethin’ of a detour from the main roads.\""
show kan with dis
wi "\"What’s a fellah like you doing all the way out here?\""
show kan talking with dis
ka "\"Truth be told, I was looking for ya.\""
show kan with dis
wi "\"Looking for me?\""
wi "\"And how did you know I was going to be here?\""
show kan smug with dis
ka "\"Trailed ya.\""
show kan smile with dis
wi "\"Trailed me?\""
wi "\"Bit suspicious to admit that, yeah?\""
show kan eyes sneer with dis
ka "\"More than a bit! But I’m impatient.\""
show kan smile with dis
show kan talking with dis
ka "\"Why come there’s such a lack of bounties posted up in this area?\""
show kan smug with dis
ka "\"A man’s gotta eat, as well as wet his whistle.\""
show kan with dis
wi "\"You look plenty well-fed to me.\""
wi "\"And I regret to inform you that we’re a bit of a podunk.\""
wi "\"Not a whole lot of high profile criminals to apprehend around here, so not much need for any bounties.\""
show kan smug with dis
ka "\"That tale’s a little bit different from the ones I hear.\""
show kan smile with dis
"He plucks a piece of grass off of the side of the road and twirls it between his claws."
show kan talking with dis
ka "\"Your families selling off houses.\""
show kan with dis
show kan talking with dis
ka "\"Your coal workers all up in arms.\""
show kan with dis
show kan talking with dis
ka "\"And now a banker’s turned up dead for sure?\""
show kan smile with dis
wi "\"Eavesdropping on us, were you?\""
show kan eyes talking with dis
ka "\"Troubling times, Mr. Adler.\""
show kan smile with dis
wi "\"What do you want, stranger?\""
show kan talking with dis
ka "\"I think you missed the part where I told you that I’m very food-motivated, sheriff.\""
show kan smug with dis
ka "\"You give me a bounty and I’ll be happy to deliver a head.\""
show kan smile with dis
wi "\"Fuck off.\""
show kan eyes sneer with dis
ka "\"Two heads within a day, and they can even be alive if you’re one of those bleedin’ heart types.\""
show kan with dis
wi "\"Only thing that’s bleedin’ is my stomach from the ulcer you gave me.\""
wi "\"Scram.\""
show kan talking with dis
ka "\"Oh come on now, don’t be such a poor sport.\""
show kan eyes with dis
show kan eyes talking with dis
ka "\"I know how much y’all rely on bounty hunters, so there’s no need to be so prideful.\""
show kan eyes with dis
show kan talking with dis
ka "\"I’ve helped plenty of lawmen in the course of my career.\""
show kan with dis
wi "\"And how many of ‘em are dead or scandalized now?\""
show kan wink with dis
ka "\"Only the ugly ones.\""
show kan smile with dis
wi "\"Charmers don’t last long around here.\""
show kan sneer with dis
ka "\"Who says I plan to stick around that long?\""
show kan smug with dis
ka "\"I just need a few names, a few pictures, and a fatter wallet, and I’ll be merrily out of your fur.\""
show kan with dis
wi "\"I’ll let you know names once I have some.\""
show kan eyes sneer with dis
"He whistles."
show kan sneer with dis
ka "\"I didn’t take a man with that many scars for bein’ a slacker.\""
show kan with dis
wi "\"I’ll take an extra nap today and think of you.\""
show kan talking with dis
ka "\"You can’t be dumb enough to turn down help when it’s sitting in front of you.\""
show kan with dis
show kan talking with dis
ka "\"You’re stumbling around. I’m hungry.\""
show kan eyes with dis
show kan eyes talking with dis
ka "\"And bored.\""
show kan eyes with dis
show kan talking with dis
ka "\"Let’s come to an understanding?\""
show kan with dis
wi "\"I need information more than I need a maniac pumping lead into suspects right now.\""
show kan smug with dis
ka "\"That’s always part of the job.\""
show kan with dis
wi "\"No killing, no violence.\""
wi "\"Do we have an understanding?\""
show kan eyes talking with dis
ka "\"Unfortunately.\""
show kan with dis
wi "\"Okay then.\""
"I unclench my fist and show him what’s inside."
wi "\"This your gum wrapper?\""
show kan eyes with dis
show kan with dis
"He blinks at the pack I hold up for him, more than a little derisively."
show kan talking with dis
ka "\"Sure ain’t.\""
show kan with dis
wi "\"That’s all I’ve got to go off of right now.\""
show kan eyes with dis
ka "\"You’ve gotta be funnin’ me.\""
show kan with dis
wi "\"Do I look much like the funny sort to you?\""
show kan talking with dis
ka "\"Fine.\""
show kan eyes with dis
show kan eyes talking with dis
ka "\"I can work with that.\""
show kan eyes with dis
show kan talking with dis
ka "\"What’s my rate?\""
show kan with dis
wi "\"An eagle if you tell me something useful.\""
show kan eyes smug with dis
"He whistles."
show kan smug with dis
ka "\"Not a bad start for just a little word of mouth.\""
show kan talking with dis
ka "\"I’m not bullshitting you, you know.\""
show kan smile with dis
show kan wink with dis
ka "\"I’m good.\""
show kan smile with dis
wi "\"Guess we’ll see.\""
hide kan with dissolve
stop music fadeout 7.0
$ update_unlocked_pages(1, 17)
$ renpy.notify("Notebook updated.")
play sound ("sfx/gravelwalk.ogg")
"I walk away, leaving him to the weeds and the creek as I push past infant pine trees back in the direction of the house."
play sound ("sfx/crunch.ogg")
"But I hear a small crunch where I thought I’d hear nettles."
"I look below my feet and it can tell that what I’m stepping on isn’t any plant debris."
stop sound
"It looks like a small tube with a spool on the end."
"Weird place for something like this to be."
$ update_unlocked_pages(1, 18)
$ renpy.notify("Notebook updated.")
"Probably worth noting."
"Once I’m done sketching it and put it in my pocket, I take a look at my watch."
"It’s 6 PM there, so it’s 4 PM here."
"Time to head back."
window hide
pause 0.5
stop background fadeout 6.0
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
scene black with slow_dissolve
play music "music/horrorpiano.ogg" fadein 3.0
play ambient ("sfx/wind2.ogg") fadein 3.0
play ambient2 ("sfx/crows.ogg") fadein 3.0 volume 0.2
scene bg greeneshed:
    zoom 1.03
    truecenter
#show mar eyes at halfleft
with slow_dissolve
show mar eyes talking at halfleft,sunset with dis3
pause 0.5
window show
"Marcy Greene inhales slowly, then lets out a shriek that goes well beyond the boundaries of her property, into Lake Emma."
show mar eyes with dis
"I can’t tell if she’s screaming at us or from pain."
show mar with dis
play sound ("sfx/tumble.ogg")
show tod surprised p at right,sunset with dissolve
"Todd crab walks several feet away before scrambling to his feet, chest heaving."
stop sound
#show mar eyes with dissolve
show mar eyes talking with dis3
"Marcy crouches, squeezes her eyes shut, looks into the sky, and yowls."
show mar eyes with dissolve
hide tod with dissolve
pause 0.5
show tod surprised at right,sunset with dissolve
"Birds above us caw as they disperse."
show tod sad with dis
to "\"M-ma’am...\""
show tod surprised with dis
to "\"Are you okay?!\""
"I look at Todd because I can’t believe he just asked that, and he looks at me in a daze."
show blood01 with dis3
window show
"She cries out, sinking to the ground on her knees as a pool of something dark expands below her."
hide blood01
hide mar
m "\"Oh, shit!\"" with vpunch
show tod sad with dis
to "\"That’s...\""
"I only realize right now what’s happening."
show wil talking at left,sunset
show tod surprised
wi "\"What the HELL do y’all think you’re doing!\"" with vpunch
show wil surprised with dis
m "\"She’s in labor!\""
show wil shocked with dissolve
wi "\"The fuck you mean she’s in labor?!\""
m "\"I don’t think I stuttered!\""
show wil frustrated with dis3
"Will lets out a slew of curse words."
show wil talking at left with dis3
show tod sad with dis3
wi "\"Todd, go inside her house and get her a clean sheet.\""
show wil with dis
show tod surprised with dis
to "\"I, uh, um... ok!\""
hide tod with dis3
#sfx
"He runs a little stiffly as his thick tail trots behind him."
hide wil with dis3
pause 0.5
show wil eyes at left,sunset
show mar eyes at halfleft,sunset
with dissolve
"Will holds Mrs. Greene, who’s shaking violently."
show wil eyes talking with dis
wi "\"Deep breaths, M-ma’am...\""
show wil with dis
show wil talking with dis
wi "\"Help me move her, Sam\""
show wil with dis
"I try to get her under one of the pine trees with the most shade, but the coppery smell of blood is making me dizzy."
show blood02 with dissolve
"She’s leaving thin, splattery trails as she moves."
hide blood02 with dissolve
show wil eyes at right,sunset
show mar eyes at center
with dis3
m "\"Do you have a midwife?\""
show mar with dissolve
pause 0.3
show mar eyes with dissolve
"She looks at me, like she’s lost, and shakes her head and starts crying again."
#sfx
show tod surprised at left,sunset with dissolve
"I hear Todd’s footsteps as he races back with what looks like the tablecloth."
hide mar with dissolve
show wil with dis
"I check beneath her dress and gag from the sour smell."
"Her undergarments are soaked."
m "\"We have to get these off of her.\""
show tod sigh with dis
to "\"C-can, we do that, M-ma’am...?\""
show tod surprised with dis
"She nods, still shaking."
show tod annoyed with dis
"Todd looks at me like I’m the one who needs to do it."
show tod surprised with dis
"I shake my head and jerk it towards her, giving him the hardest stare I might’ve given somebody in my life."
show tod sad with dis
to "\"Okay.\""
show tod sigh with dis
to "\"Alright.\""
hide tod with dissolve
show wil eyes with dis
"Todd crouches, grimacing from the smell as he puts his paws below."
"I hear the undergarments squelch as he pulls them down, sticking slightly to the skin."
show wil with dis
"I can tell from the marks on the side of her leg she has an infection."
show wil sideeyes with dis3
wi "\"Don’t try to push too hard.\""
show tod surprised at left,sunset
show wil
with dis3
"She shakes her head, tears still welling out of her eyes."
show tod talking with dis
to "\"It’s okay Mrs. Greene!\""
show tod eyes happy with dis
to "\"You’re gonna be a mommy!\""
show tod surprised with dis
"The rat starts wailing again."
play sound ("sfx/wsplash.ogg")
show blood03:
    zoom 1.03
    truecenter
"More blood splashes to the ground." with vpunch
hide blood03 with dis2
pause 1.0
show tod eyes happy with dis
to "\"I think I see a head!\""
show tod surprised with dis
"Mrs. Greene screams again."
show tod talking with dis
to "\"I definitely see a head!\""
show tod with dis
"Will hold Mrs. Greene’s hand and she squeezes it."
show tod eyes happy with dis
to "\"Now there’s a body!\""
show wil talking with dis
show tod surprised with dis
wi "\"Hold it while it comes out.\""
show wil with dis
hide tod with dissolve
to "\"I am, I am!\""
show wil talking with dis
wi "\"Make sure the cord isn’t wrapped around its neck.\""
show wil with dis
to "\"Is that not supposed to happen?\""
show wil eyes talking with dis
wi "\"The baby can get strangled on it if you’re not careful.\""
show wil with dis
to "\"It’s sliding out pretty easy now.\""
show blood05 with dis3
"I can see it too."
"It’s bloody and hairless with chunks of pus coating the body, and encased in a thin film of mucus."
"But it’s small."
"Very small."
hide blood05 with dis3
to "\"Do we need to cut the cord?\""
show wil eyes talking with dis
wi "\"No need.\""
show wil eyes with dis
show wil talking with dis
wi "\"It’s good to let the blood flow through the cord and the rest comes out later.\""
show wil eyes with dis
m "\"It usually detaches by itself.\""
show wil with dis
to "\"How do you know that?\""
m "\"Because I’ve seen this happen enough at work.\""
show tod surprised at left,sunset with dissolve
"But something’s wrong."
"Will knows it too."
"There aren’t any sounds."
"Will looks stone-faced and Todd looks scared."
"I just cover my mouth, unable to look away from the scene of Mrs. Greene trembling while the sour-smelling thing attached by a fleshy cord below her legs doesn’t breathe."
show wil frustrated with dissolve
pause 0.5
show wil with dissolve
"Will hangs his head and pinches his nose and then looks at me."
show tod sad with dis
show wil talking with dis
wi "\"We need to keep her awake.\""
show wil with dis
show wil talking with dis
wi "\"She’s lost a lot of blood.\""
show wil surprised with dis3
mar "\"I knew they were dead.\""
mar "\"I knew it I knew it I knew it.\""
m "\"You don’t have to worry about that now, Mrs. Greene.\""
show wil eyes with dis
mar "\"But it’s all my fault.\""
m "\"It’s not.\""
show wil with dis
m "\"This thing happens all the time.\""
m "\"Trust me, I see it happen all the time.\""
mar "\"But it is though.\""
mar "\"If it would have lived, he would have taken it.\""
show wil surprised with dis
wi "\"...What?\""
mar "\"Taken it like he took me.\""
show tod surprised with dis
m "\"Mrs. Greene?!\""
mar "\"If he was dead then I could have had this one.\""
m "\"But now there won’t be another one.\""
mar "\"Forever again, for never again, for never again.\""
"Her eyelids flutter before they close."
m "\"Stay with me Mrs. Greene.\""
show wil talking with dis
show tod annoyed with dis
wi "\"Todd, go get her something to drink.\""
hide tod
show wil sideeyes
with dis3
wi "\"Sit with her and keep talking, Sam.\""
show wil talking with dis3
wi "\"I’m going to go boil some water.\""
show wil eyes with dis
hide wil with dis3
"He didn’t look back at us when he stood up, and as his tawny tail swayed behind him, prickling."
"I shake her shoulder to try to wake her up again."
window hide
scene black with medium_dissolve
#stop ambient fadeout 5.0
stop ambient2 fadeout 5.0
scene bg greenekitchen at sunset with medium_dissolve
window show
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"For the love of God, what is wrong with this place?"
"I stumble around the kitchen that’s cluttered with half-filled cups and soiled dishes, looking around for the biggest pot I can find."
play sound "sfx/doorcreakopen.mp3"
"I open the cupboard to see what we have to work with."
stop sound
"Mostly sealed jars of perishables."
"And a jar of something else."
"I’ve seen this root before."
$ update_unlocked_pages(1, 19)
$ renpy.notify("Notebook updated.")
"...Did she really think this was a better fate for them than living with her husband?"
"I’m afraid to think about the things Huxley Greene might have been doing that I didn’t know about."
"But there’s no time for that now."
"There’s a big enough pot below her stove."
show tod surprised at right,sunset with dis3
"Todd knows exactly where the cups are."
show tod sigh with dis
"He finds a large jug of water in a pantry and turns the knob to let it flow."
show tod annoyed with dis
play sound "sfx/tea.mp3"
"I turn on her sink and let the water begin to flow."
hide tod with dis3
"Todd runs out with the cup in his hand."
stop sound
"I’m surprised but thankful that she has a gas stove, so I don’t have to light a fire or stoke any coals to get started."
"I have to find a place where Marcy can lie down."
"Her couch is so covered with these damn dolls that she has no place to sit."
"Upsetting her further will just add stress."
"I go to her bedroom."
scene bg greenebedroom with dissolve
"Thankfully it’s a little less cluttered than her living room."
"But her bed..."
"More dolls?"
"No, that’s just one big lump beneath the sheets."
"I don’t know if I can take it if it’s a big doll that looks like Huxley."
"Thankfully it isn’t."
"It’s... I think she mentioned it’s her grandma’s burial shroud."
"She shouldn’t be sleeping with this."
"It’s covered in mold."
"No wonder she’s sick."
"I start to push it off the bed but it has a weird feel to it."
play sound "sfx/nope.ogg"
"It lands wetly on the ground and makes a noise that makes me want to gag."
$ update_unlocked_pages(1, 20)
$ renpy.notify("Notebook updated.")
"This bed is unsanitary."
stop sound
"She can’t sleep here."
"Living room it is, then."
scene bg greenecottageinterior dark with dissolve
"I remove each and every one of those dolls from the couch and place them on the only surface left, which is the table."
show sam sad at center,house1
show tod sad at right,house1
show mar eyes at centerright,house1
with dis3
"Sam and Todd bring her in and she’s holding a pink-stained sheet, wrapped up in swaddle."
show sam with dis
wi "\"Here, here!\""
hide sam
hide tod
hide mar
show sam at left,house1:
    xzoom -1
show tod sad at right,house1
show mar eyes at center,house1
with dis3
"I direct them to the couch."
"Marcy is still dripping from the legs."
show mar eyes talking with dis
mar "\"Bedroom.\""
show mar with dis
wi "\"No Marcy, it’s not clean.\""
"She holds up the sheet."
show mar talking with dis
show sam surprised
show tod surprised
with dis
mar "\"I want to put her with the others.\""
show mar with dis
"With the others?!"
"Oh, God..."
show mar eyes
show tod sigh
with dissolve
hide tod with dis3
"Todd takes it for her and disappears into the bedroom."
show mar eyes talking with dis
mar "\"Thank you.\""
show mar eyes smile with dis3
mar "\"Always such a good boy.\""
show mar eyes with dis
show sam sad with dis
"Sam leans into me, whispering in my ear."
show sam sad talking with dis
m "\"The afterbirth wasn’t whole when it came out.\""
show sam eyes with dis
"I feel the ‘Fuck’ roll out of me like it’s a gasp."
show sam with dis
wi "\"Marcy, who’s your doctor?\""
show mar eyes talking with dis
mar "\"Medicine?\""
show mar dazed eyes with dis
mar "\"I’ve had my fill of medicine.\""
show mar eyes with dis
wi "\"We already know everything so there’s no need to hide anything from us anymore.\""
wi "\"You’re very sick, and you need help.\""
show tod surprised at right,house1 with dis3
show mar with dis3
stop music fadeout 8.0
"Todd comes out of the room looking a little queasy."
to "\"I put her on the bed.\""
show mar eyes with dis
"Marcy whimpers again."
"Okay, that’s enough."
wi "\"Let’s talk in the kitchen.\""
"They both follow me."
hide sam
hide tod
with dissolve
scene bg greenekitchen at sunset with dissolve:
    zoom 1.03
    truecenter
show tod sad at right,sunset
show sam sad at left,sunset:
    xzoom -1
with dissolve
play music ("music/contemplation.ogg") fadein 5.0
wi "\"Okay, this is really bad.\""
show sam with dis
wi "\"Just having access to some ice would be enough to reduce her swelling.\""
show tod surprised with dis
to "\"But I know she has an icebox.\""
wi "\"...You do?\""
show tod sad with dis
to "\"...She used to make tarts.\""
show tod sigh with dis
to "\"The kind with frozen fruits.\""
show tod surprised with dis
wi "\"Think real hard, Todd.\""
show tod annoyed with dis
wi "\"Where did she used to go before she’d make those desserts?\""
show tod talking with dis
to "\"Well, here, in the kitchen.\""
show tod with dis
show tod talking with dis
to "\"But it was always Mr. Greene who’d get the fruit.\""
play sound "sfx/thud7.ogg"
show tod surprised
show sam surprised
with vpunch
"I jump in the air and listen."
show sam
show tod annoyed
with dis
wi "\"These boards sound hollow to y’all?\""
stop sound
show tod talking with dis
to "\"They do.\""
show tod annoyed
show sam eyes
with dis
wi "\"Help me move the table.\""
hide tod
hide sam
with dissolve
play sound ("sfx/tablemove.ogg")
"All three of us give it a good shove, letting the dolls fall off as we move them."
"There’s a rug beneath the floor that matches the color of the wood pretty well."
stop sound
"I bend down and give it a tug."
show tod annoyed at right,sunset
show sam at left,sunset:
    xzoom -1
with dissolve
show tod talking with dis
to "\"Well I’ll be...\""
show tod with dis
show tod talking with dis
to "\"To think that was here the whole time?\""
show tod annoyed with dis
wi "\"I think we might have found where they keep the ice.\""
show tod talking with dis
to "\"Is it locked?\""
show tod annoyed with dis
show sam eyes with dis
wi "\"Not securely.\""
show sam with dis
"I point at the hinges."
wi "\"Doesn’t look like the kind of lock designed to keep anybody out.\""
wi "\"More like the kind of lock that keeps you out long enough to get caught trying to break in.\""
play sound ("sfx/doorrattle.mp3")
"I shake the lock and chains to show off how noisy the setup is."
show tod surprised with dis
"Todd flinches."
stop sound
"I grab the hammer I saw under one of the counters earlier and hold it against a hinge."
wi "\"I think I have more than enough excuses to do this by now...\""
play sound ("sfx/bonebreak.mp3")
"The top of the planks crunch as the hinges come off."
show tod sad with dis
to "\"Well wait, what if you don’t find an icebox down there?\""
show tod surprised with dis
show sam eyes with dis
wi "\"Then I’ll make some repairs and issue my apology.\""
play sound ("sfx/bonebreak.mp3")
show sam with dis
"I position the hammer again, putting my body weight down on it until I hear the crunch."
play sound ("sfx/impact1.mp3")
"The trapdoor made of planks flips out easily from the top, rattling."
stop sound
wi "\"I guess Mr. Greene thought he was slick.\""
show tod sigh with dis
show sam annoyed with dis
to "\"It worked on me.\""
"Yeah, that’s not that surprising."
show tod annoyed with dis
wi "\"Mostly because you don’t tend to expect something as eccentric as this from a banker.\""
scene black with dissolve
"We climb down an iron set of stairs that wobbles as we move beneath it."
"It’s dank and dirty down here."
"There’s plenty of cobwebs, and I’m sure I saw a few things crawling around the floor out of the corners of my eye."
play sound ("sfx/stringswitch.ogg")
scene bg greenebasement with dis
"I see a dangling lightbulb and pull the string."
stop sound
"There’s not much down here but a tall, black chest, and a wooden crib, painted white."
show sam at halfright,basement1
show tod annoyed at right,basement1
with dissolve
show tod talking with dis
to "\"Well what’s somethin’ like that doing down here?\""
show tod annoyed with dis
"I slide my fingers along it, expecting to find grime or dust from being in storage."
wi "\"It’s clean.\""
"There’s a doll here too."
show tod sigh with dis
to "\"This looks expensive.\""
show tod sad with dis
show sam eyes with dis
$ update_unlocked_pages(1, 21)
$ renpy.notify("Notebook updated.")
wi "\"It’s definitely not like the other ones we’ve seen around the house.\""
show sam with dis
wi "\"What’s in the icebox, Todd?\""
show tod surprised with dis
to "\"Well, ah...\""
to "\"Ice.\""
wi "\"And?\""
show tod sigh with dis
to "\"Huckleberries.\""
show tod surprised with dis
"I follow him to it."
"And he opens it."
"The ice box is separated into different sorts of shelves."
show tod sigh with dis
to "\"Hey William?\""
wi "\"Yes Todd?\""
show tod annoyed with dis
show sam eyes with dis
to "\"That really doesn’t look big enough to store a body.\""
"I can’t disagree with him here."
show sam with dis
"There’s far less down here than I would have expected."
"If Huxley had plans for this space, it looks like he never got down to them."
show sam talking with dis
m "\"Is this another dead end?\""
show sam with dis
wi "\"I sure hope not.\""
"The two of them stare at me as if they’re waiting for what to do next."
"And their close proximity in such a cramped space makes something new dawn on me."
wi "\"Now don’t take this personal...\""
show sam surprised blush
show tod surprised
with dis
wi "\"But did y’all roll around in the hay together or something?\""
wi "\"You both smell really strong right now.\""
show tod sad
show sam eyes
with dis
"They both look away."
show sam eyes talking with dis
m "\"We’re both really stressed, Will.\""
show sam annoyed with dis
show sam annoyed talking with dis
m "\"I think we should talk about the doll.\""
show sam annoyed with dis
"Todd is unusually silent."
show tod sigh with dis
to "\"Y-yeah, and the crib.\""
show tod sad with dis
$ update_unlocked_pages(1, 22)
$ renpy.notify("Notebook updated.")
wi "\"Okay...fine.\""
"I’ll pick this up later at a better time."
show sam with dis
show tod surprised with dis
wi "\"So... the crib and this doll...\""
show tod annoyed with dis
wi "\"Todd, are you sure you never saw Marcy go down the to cellar?\""
show tod sigh with dis
to "\"Cross my heart.\""
show tod annoyed with dis
show sam annoyed with dis
wi "\"Huxley doesn’t mark me as a fellow who’d play with dolls.\""
show sam annoyed talking with dis
m "\"Hell no he wouldn’t.\""
show sam annoyed with dis
show tod sigh with dis
to "\"So why is this down here?\""
show tod annoyed with dis
wi "\"Why don’t we go find out...\""
"We climb up the stairs and head back to Marcy’s kitchen."
hide sam
hide tod
with dissolve
scene bg greenekitchen at sunset with dissolve
show tod annoyed at right,sunset
show sam at left,sunset:
    xzoom -1
with dissolve
wi "\"Say... Sam?\""
wi "\"Dora knows doctors, right?\""
show sam talking with dis
m "\"People who are close enough, yeah.\""
show sam with dis
wi "\"Would she help in this case?\""
show sam talking with dis
m "\"I suspect she would.\""
show sam with dis
wi "\"She’d respond better to you than she would to me.\""
show sam eyes talking with dis
m "\"...Right.\""
show sam eyes with dis
show sam talking with dis
m "\"I could go get help?\""
show sam with dis
wi "\"I think it would be a good idea to go fetch her.\""
wi "\"Be careful about who else you bring.\""
show tod sad with dis
wi "\"If a licensed doctor saw any of this it wouldn’t be good for her.\""
show sam talking with dis
m "\"Yeah, okay.\""
show sam with dis
hide sam with dissolve
"Sam pokes around the hall of the kitchen with his head, giving Marcy another cautious look before disappearing out the front door."
scene bg greenecottageinterior dark
show mar dazed at center,house1
with dissolve
show tod sad at right,house1 with dissolve
"Me and Todd head back to the living room."
"She’s staring up at the ceiling, holding her paw up, feeling one of the yarn streamers tacked to her walls, letting it slip through her digits, coiling them up."
wi "\"Marcy.\""
"She doesn’t respond to my voice."
wi "\"Mrs. Greene?\""
show tod sigh with dis
to "\"Is it okay if we give you this?\""
show tod sad with dis
show mar smile with dis3
"Her eyes widened as her mouth broke into a smile."
mar "\"Penelope...\""
mar "\"I bet you thought I had forgotten all about you.\""
wi "\"Is Penelope the doll’s name?\""
show mar eyes smile with dis3
mar "\"No.\""
show mar smile with dis3
mar "\"That was my sister.\""
show mar eyes with dis3
mar "\"The doll is hers.\""
show mar with dis3
wi "\"Did she give it to you for safe keeping?\""
wi "\"It doesn’t look cheap.\""
show mar talking with dis3
mar "\"Because it wasn’t.\""
show mar with dis3
show mar talking with dis3
mar "\"I stole it because I was jealous.\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"But I was going to give it back.\""
show mar eyes with dis3
show mar eyes talking with dis3
$ marcydolltext = _("It used to belong to Marcy's sister.")
$ current_journal_page = 21
$ renpy.notify("Notebook updated.")
mar "\"I just never got the chance to.\""
show mar eyes with dis3
"None of us dare ask why."
show mar with dis3
wi "\"Why do you think Mr. Greene had this locked in the cellar?\""
show mar talking with dis3
mar "\"Because he knew I wanted it.\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"He’d know if I’d try to mess with the chains.\""
show mar with dis3
wi "\"But why would he put it down there?\""
show mar eyes talking with dis3
mar "\"Same reason he always did.\""
show mar eyes smile with dis3
mar "\"He knew little girls like dollies.\""
show mar smile with dis3
"She takes a look at the porcelain and gives it a kiss on the cheek."
show mar talking with dis3
mar "\"In the dark, and the quiet, it’s safe and warm.\""
show mar with dis3
show mar talking with dis3
mar "\"Sometimes you have to lose yourself in the coziness.\""
show mar with dis3
show mar talking with dis3
mar "\"And the idea of not moving anymore isn’t so bad.\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"Because you’re pretty as a picture and not quite so cheap.\""
show mar eyes with dis3
wi "\"Mrs. Greene...\""
show mar with dis3
wi "\"What does this have to do with anything?\""
show mar talking with dis3
mar "\"I’m just repeating what he said before he took me away from everybody I knew.\""
show mar with dis3
show mar talking with dis3
mar "\"I think I understand now that he just liked to hurt me.\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"Not because I think it made him happy...\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"But because it made him feel more alive.\""
show mar eyes with dis3
show mar eyes talking with dis3
mar "\"Made him feel more alive than me as he took more from me, all the while saying he was doing me the greatest favor.\""
show mar with dis3
show mar talking with dis3
mar "\"Well I just want you all to know that he wasn’t doing that.\""
show mar dazed with dis3
mar "\"I just think...\""
mar "\"I just think--\""
play sound ("sfx/wsplash.ogg")
show blood04:
    zoom 1.03
    truecenter
"We flinch as she goes crosseyed and retches loudly." with vpunch
"Red vomit shoots into the dark water we cleaned her with."
hide blood04
show mar eyes
show tod surprised
with dissolve
"I don’t know if she’s going to be okay or if she’s got much time left."
show tod sad with dis
wi "\"Mrs. Greene, don’t push yourself.\""
show mar dazed with dis3
mar "\"But I... want. To.\""
mar "\"Won’t let him hurt people no more.\""
show mar dazed eyes with dis3
mar "\"Not even... dead...\""
wi "\"Mrs. Greene!\""
mar "\"He had the gun.\""
mar "\"Went in the carriage.\""
mar "\"Red... fox...\""
wi "\"Red...\""
show tod surprised with dis
to "\"Fox?\""
"...That’s what I needed."
hide mar with dissolve
"She vomits again, brighter red this time, and her breath quickens."
wi "\"Todd, I want you to stay with her while Sam brings help.\""
show tod sad with dis
to "\"Y-yes sir.\""
stop music fadeout 5.0
scene bg greenecottage at sunset with dissolve
"Once I leave the cloying smell of that house behind, the tension in my shoulders loosen up."
window hide
pause 0.5
stop ambient fadeout 6.0
scene black with medium_dissolve
pause 1.0
play music ("music/quiet.ogg") fadein 1.0
scene bg generalexterior at sunset with medium_dissolve
window show
"The general store is probably closing up by now."
"I can usually find Mr. Byrnes and his son there after hours."
"As I walk on over I mull over the things I’m going to say, and how I’m going to approach this."
play sound ("sfx/softknock.ogg")
"I knock on the front door with the back of my wrist."
stop sound
show ral frown c at center,sunset with dissolve
"Ralph greets me at the door."
show ral stoic c with dissolve
ra "\"Don’t you know it’s closing time?\""
show ral frown c with dissolve
wi "\"It’s the sheriff.\""
show ral angry c with dis
ra "\"And I don’t care if you’re George Albert the fifth.\""
show ral frown c with dis
ra "\"We’re tired.\""
ra "\"Come back tomorrow.\""
show mur concerned d at right,sunset with dissolve
"I smell the scent of shoe polish and lemons before I see Murdoch Byrnes at the door, giving me a curious look."
"It’s probably better that he came to the door and not his father."
"He’s the one I work with most."
mu "\"William?\""
show ral stoic c with dissolve
wi "\"Afternoon.\""
show mur sideeye with dis
mu "\"This is a bit of a bad time.\""
mu "\"We have our hands full.\""
"I can tell by the sheen of his neck that he’s had a long day."
"Somehow I doubt it was anything like mine though."
show mur concerned d with dis
wi "\"I’m afraid it’s urgent.\""
mu "\"How urgent?\""
show mur fear d with dis
show ral angry c with dis
wi "\"Urgent enough to make a few arrests if I have to.\""
"The rat glares and me and the fox’s eyebrows lift."
show mur concerned d with dis
wi "\"But I know you’re more reasonable than that.\""
wi "\"That urgent enough?\""
"Murdoch’s brow furrows in confusion."
show mur eyes talking with dis
mu "\"Fine, come in.\""
show mur concerned d with dis
show ral stoic c with dissolve
"The fox opens the door and the rat exhales."
scene bg generalinterior at sunset with dissolve
show ral stoic c at left,sunset
show mur concerned d at right,sunset
with dissolve
wi "\"Take me somewhere we can talk where it’s just the two of us.\""
show mur sideeye with dis
mu "\"The darkroom will work for that.\""
show ral frown c with dis
"I feel Ralph’s eyes on me as Murdoch walks me to a dinky little closet and opens the door."
scene bg darkroom with dissolve
show mur concerned d red with dissolve
"It smells strongly of chemicals and him in here."
wi "\"Tell me where this is from?\""
"I pull out the cartridge I found on Marcy’s road."
show mur sideeye red with dis
mu "\"That’s a Kodak film canister.\""
mu "\"The kind our store uses.\""
show mur concerned d red with dis
wi "\"The kind your camera uses, right?\""
show mur eyes talking red with dis
mu "\"Yes, but we have several.\""
show mur concerned d red with dis
wi "\"Found it near Huxley Greene’s property in the woods by the road.\""
wi "\"Can’t recall them having many pictures, or a camera for that matter.\""
show mur sideeye red with dis
mu "\"They’ve never purchased any photography either.\""
show mur concerned d red with dis
mu "\"At least not to my knowledge.\""
wi "\"Where were you the day of the poker game?\""
show mur eyes talking red with dis
mu "\"I was at the store all day.\""
show mur concerned d red with dis
mu "\"Then I ate supper by myself before going over to Mr. Tibbits’ apartment.\""
wi "\"You didn’t eat at home?\""
show mur sideeye red with dis
mu "\"Not since it wasn’t a Sunday or a special occasion, no.\""
show mur concerned d red with dis
"Based on when Jimmy had the gun, Huxley had to have it taken from him either past the afternoon of the riot, or any part of the day before the poker game."
"That’s not a long time for somebody to get killed and have their gun taken from them."
"I saw Murdoch most of Thursday."
"I didn’t see him at all on Friday before the poker game though."
"He’s clean, unless he’s lying."
"I have to wonder if that’s the case."
"Or if he’s covering for any of his family."
wi "\"So you didn’t see your parents on Friday night?\""
show mur sideeye red with dis
mu "\"I didn’t.\""
wi "\"Or on Thursday, after all of the excitement.\""
mu "\"No.\""
show mur sad red with dissolve:
    xzoom -1
"He winces as he rolls his neck."
wi "\"How’s your shoulder?\""
mu "\"It stings still.\""
wi "\"You redressing it every day?\""
show mur fear d red with dissolve:
    xzoom 1
mu "\"Is there something you’re trying to get at with this?\""
mu "\"I thought you said this was urgent.\""
show mur concerned d red with dis
wi "\"I needed somewhere nobody would listen.\""
show mur fear d red with dis
mu "\"I don’t like being scared like that.\""
show mur concerned d red with dis
wi "\"...I’m sorry.\""
wi "\"Today has been too much.\""
show mur eyes talking red with dis
mu "\"You’re forgiven, then.\""
show mur concerned d red with dis
wi "\"And I had to go through a lot to get this far.\""
wi "\"Who in your family drives the company carriage?\""
show mur eyes talking red with dis
mu "\"Mostly my father.\""
show mur sideeye red with dis
mu "\"Sometimes my mother.\""
show mur concerned d red with dis
wi "\"How about your sisters?\""
show mur sideeye red with dis
mu "\"Holly’s taken it on joyrides before, but she’s not supposed to.\""
show mur concerned d red with dis
wi "\"Do you know where any of your family had been on those two nights?\""
show mur sideeye red with dis
mu "\"I have my guess, but no.\""
mu "\"Past six o’clock, my life is mine.\""
show mur concerned d red with dis
mu "\"If I ran into them before all of that they’d have favors and chores for me, and I try keep that all to the workday.\""
show mur sideeye red with dis
mu "\"Although...\""
wi "\"Don’t keep me waiting, fox.\""
show mur eyes talking red with dis
mu "\"Cordelia Hendricks threw a party on Thursday night.\""
show mur sideeye red with dis
mu "\"I saw the invitation.\""
show mur concerned d red with dis
$ update_unlocked_pages(1, 23)
$ renpy.notify("Notebook updated.")
"Interesting."
"Is this all leading back to the Hendricks mansion?"
"Now I have to check in on that next."
"No doubt in my mind."
"Not looking forward to talking to that prick again so soon."
wi "\"Do you know who attended this party?\""
show mur eyes talking red with dis
mu "\"My mother for sure.\""
show mur eyes red with dis
show mur eyes talking red with dis
mu "\"Perhaps my father.\""
show mur sideeye red with dis
mu "\"I’d have to ask my sisters if they did, though.\""
mu "\"I don’t know.\""
show mur concerned d red with dis
wi "\"I have just a few more questions...\""
show mur shock red with dis
grunk "\"If you have more questions then you should be asking me.\""
show gre f frown red at left with dissolve
show gre f frown talking red with dis
gr "\"The men have work to do at closing time.\""
show gre f frown red with dis
label williamroute3b:
scene black with slow_dissolve
"To be continued..."
window hide
scene credits with slow_dissolve
pause
scene credits2 with slow_dissolve
pause
scene black with slow_dissolve

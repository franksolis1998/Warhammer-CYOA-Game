'''' This a Warhammer inspired fantasy game some names and locations will be used'''
''''I am making this as a project for class out of passion for the universe no money was made from this game'''
from typing import Type


Human = "Mankind"
Dwarf = "Dawi"
Elf = "Elf"
Ork = "Ork"

character = Human, Dwarf, Elf, Ork

'''HitPoints'''
Human_hp = 1000
Dwarf_hp = 2000
Elf_hp = 1400
Ork_hp = 2500

'''Physical Damage'''
Human_pdamage = 80
Dwarf_pdamage = 150
Elf_pdamage = 130
Ork_pdamage = 200

'''Magical Damage'''
Human_mdamage = 100
Dwarf_mdamage = 0
Elf_mdamage = 200
Ork_mdamage = 130

'''Ranged damage'''
Human_rdamage = 130
Dwarf_rdamage = 150
Elf_rdamage = 200
Ork_rdamage = 80

'''Special traits Mankind'''
'''Since Humanity is the most widesoread race in all the world it has many nations for thier alligence'''
'''In the future i would like to give the Mage class the option to choose which lore of magic to use'''
'''Dwarfs are a sturdy people and one of the oldest, i will add their speical trait when i learn more python'''
''''I have classes/races set up now i need subclasses atleast three for each one'''
'''I also need to have damage setups for all of them.'''
while True:
    print("1) Mankind")
    print("2) Dawi")
    print("3) Elf")
    print("4) Ork")
    character = input("The Dark Gods already see what you choose but they want you to know if you'll join them or... Choose your Character and let The Great Game Begin:")
    if (character == "1") or (character == "Mankind"):
        print("Mankind is the youngest of all the races, but is one of the strongest, most populus and the most suseptable to Chaos...now your alligence")
        print("")
        print("Will you serve The Empire and thier living God-King who's holy light protects all?")
        print("")
        print("Will you Subjgate yourself to The Knights of Bretonnia and thier Lady of the Lake?")
        print("")
        print("Perhaps the frozen Fortesses of the Tzarinna and the Bear god Ursun hold your favor?")
        print("")
        print("Bring Chaos to the World ignite The End Times with the power of Chaos Undivided, if that so suits you?")
        print("")
      
        The_Empire = "The Empire"
        Bretonnia = "Bretonnia"
        Kislev = "Kislev"
        Chaos = "Chaos"

        print("1) The Empire")
        print("2) Bretonnia")
        print("3) Kislev") 
        print("4) Chaos")
        break
while True:
    alligence = input("Decide who you will serve:")
    if (alligence == "1") or (alligence == "The Empire"):
        print("Three things make the Empire great; faith, steel, and gunpowder -Emperor Magnus the Pious")

        Footman = "Footman"
        Archer = "Archer"
        Mage = "Mage"

        print("1) Footman")
        print("2) Archer")
        print("3) Mage")
        Type = input("Are you a footman, Archer or Mage, to which service do you choose?: ")
    if (Type == "1") or (Type == "Footman"):
        print("Great lad, now go and grab your equipment")
        character = Footman
        my_hp = Human_hp
        my_damage = Human_pdamage
        break
    elif (Type =="2") or (Type == "Archer"):
        print("Good now go form up with the Rangers")
        character = Archer
        my_hp = Human_hp
        my_damage = Human_rdamage
        break
    elif (Type == "3") or (Type == "Mage"):
        print("Oh? Truly ye are? Well good its about time we have one of you Magic Users with us go on and get ready.")
        character = Mage 
        my_hp = Human_hp
        my_damage = Human_mdamage
        my_range = Human_rdamage
        break
    if (alligence == "2") or (alligence == "Bretonnia"):
        print("Above all others, Bretonnia is the land of heroes... - The Kingdom of Bretonnia.")

        Squire = "Squire"
        Damsel = "Damsel"
        Bowman = "Bowman"

        print("1) Squire")
        print("2) Damsel")
        print("3) Bowman")
        Type = input("Reporting for the muster wonderful now report: ")
    if (Type == "1") or (Type == "Squire"):
        print("Ah yes i heard you were coming follow me mil Lord.")
        character = Squire
        my_hp = Human_hp
        my_damage = Human_pdamage
        break
    elif (Type == "2") or (Type == "Damsel"):
        print("Blessings of the Lady be upon us i will escort you towards the King and his Guards")
        character = Damsel
        my_hp = Human_hp
        my_damage = Human_mdamage
        my_range = Human_rdamage
        break
    elif (Type == "3") or (Type == "Bowman"):
        print("Ah yes good they are besides the stables go on ahead.")
        character = Bowman
        my_hp = Human_hp
        my_damage = Human_rdamage
        break

    if (alligence == "3") or (alligence == "Kislev"):
        print("They have courage, I'll give them that, but it's a wild courage. - Klaus Woerke")

        Kossar = "Kossar"
        Ice_Witch = "Ice Witch"

        print("1) Kossar")
        print("2) Ice Witch")
        Type = input("In service to the Ice Queen, Tzarina Katarin present yourself: ")
    if (Type == "1") or (Type == "Kossar"):
        print("Wonderful another strong Kossar mount up we move at dawn.")
        character = Kossar
        my_hp = Human_hp
        my_damage = Human_pdamage
        my_range = Human_rdamage
        break
    elif(Type == "2") or (Type == "Ice Witch"):
        print("Uhh yes of course Madam the rest of your comrades will be at the head of the colum")
        character = Ice_Witch
        my_hp = Human_hp
        my_damage = Human_mdamage
        break

    if (alligence == "4") or (alligence == "Chaos"):
        print("I see it now, the beast that will devour the world... —The Advisor")

        Chaos_Marauder = "Chaos Marauder"

        print("1) Chaos Marauder")
        Type = input("BLOOD FOR THE BLOOD GOD, SKULLS FOR THE SKULL THRONE!!!!: ")
    if (Type == "1") or (Type == "Chaos Marauder"):
        print("To the South lies plunder and the beginning of the End Times.")
        character = Chaos_Marauder
        my_hp = Human_hp
        my_damage = Human_pdamage
        my_range = Human_rdamage
        my_magic = Human_mdamage
        break





#############
#This is the Dawi class i havent been able to make this yet and i have commented out, that being said,
# i will probably just make a "Dawi" file and just import it that or another soloution i will find 



# if (character == "2") or (character == "Dawi"):
#         print("Whilst a single Dwarf draws breath, we will fight the evils that assail us, and we will never, ever give up. -Dwarf Longbeard")
#         Dwarf_Warrior = "Dwarf Warrior"
#         Dwarf_Ranger = "Dwarf Ranger"
#         Slayer = "Slayer"

#         print("1) Dwarf Warrior")
#         print("2) Dwarf Ranger")
#         print("3) Slayer")
#         Type = input("Great Lad another Dawi in the ranks, now tell me where are you suited?: ")
#     elif (Type == "1") or (Type == "Dwarf Warrior"):
#         print("Wonderful another good son of Grungi in a shieldwall!!")
#         character = Dwarf_Warrior
#         my_hp = Dwarf_hp
#         my_damage = Dwarf_pdamage
#         my_range = Dwarf_rdamage
#         break
#     elif (Type == "2") or (Type == "Dwarf Ranger"):
#         print("Wonderful, good Dawi arrows and bullets by the bagage train now go restock.")
#         character = Dwarf_Ranger
#         my_damage = Dwarf_pdamage
#         my_range = Dwarf_mdamage
#         break
#     elif (Type == "3") or (Type == "Slayer"):
#         print("A Slayer, i hope you finally achive the end of your oath brother.")
#         character = Slayer
#         my_damage = Dwarf_pdamage
#         break

     

    ''''after i can get the Dwarfs to work i will make the High, and Dark Elves '''
    ''' after that the Orks will be done'''
    '''then i am going to add enemies and a final boss'''
    




    



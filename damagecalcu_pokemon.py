import random

print("""
A Lv. 100 Pikachu (Electric, Sp. Atk: 218) attacks a Lv. 100
Pidgeotto (Normal/flying, Sp. Def: 262) with Thunderbolt, an Electric-type move
with a Power of 95 with a ten percent chance of paralyzing the target and 
gains a same-type attack bonus. It hits the target normally and deals super 
effective damage. The weather on the field is rainy. Given the following conditions,
determine how much damage Pikachu's attack will deal.
""")

level = 100
power = 95
s_attack = 218
s_def = 262


target = 1
weather = 1.5
crit = random.randint(1,2)
random_num = round(random.uniform(0.85,1.00),2)
stab = 1.5
type = 2
burn = 1
other = 1

modifiers =  round(target * weather * crit * random_num * stab * type * burn * other,2)
damage = round(((((((2*level)/5)+2)*power*(s_attack/s_def))/50)+2)*modifiers,2)

print("Target: ",target)
print("Weather: ",weather)
print("Crit: ",crit)
print("Random: ",random_num)
print("Stab: ",stab)
print("Type: ",type)
print("Burn: ",burn)
print("Other: ",other)
print("\nTotal modifiers: ",modifiers)
print("\nPikachu deals ",damage," to Pidgeotto ")
stun = random.randint(1,100)
if stun < 11:
    print("And paralized the target.")
else:
    print("But did not paralized the target.")

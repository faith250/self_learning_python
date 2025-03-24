family={'mother':'archana','elder_daughter':'aastha','younger_daughter':'aayushi'}
for post,name in family.copy().items():
    if name == 'aastha':
        del family[post]

family_ab={}
for post,name in family.items():
    if name=='aayushi':
        family_ab[post]=name 

print(family_ab)
print(family)
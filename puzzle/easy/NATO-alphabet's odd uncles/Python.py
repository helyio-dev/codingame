a1=["Authority","Bills","Capture","Destroy","Englishmen","Fractious","Galloping","High","Invariably","Juggling","Knights","Loose","Managing","Never","Owners","Play","Queen","Remarks","Support","The","Unless","Vindictive","When","Xpeditiously","Your","Zigzag"]
a2=["Apples","Butter","Charlie","Duff","Edward","Freddy","George","Harry","Ink","Johnnie","King","London","Monkey","Nuts","Orange","Pudding","Queenie","Robert","Sugar","Tommy","Uncle","Vinegar","Willie","Xerxes","Yellow","Zebra"]
a3=["Amsterdam","Baltimore","Casablanca","Denmark","Edison","Florida","Gallipoli","Havana","Italia","Jerusalem","Kilogramme","Liverpool","Madagascar","New-York","Oslo","Paris","Quebec","Roma","Santiago","Tripoli","Uppsala","Valencia","Washington","Xanthippe","Yokohama","Zurich"]
a4=["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
alph=[a1,a2,a3,a4]
t=input().strip().split()
idx=next((i for i in range(4) if all(x in alph[i] for x in t)),max(range(4),key=lambda i:sum(x in alph[i] for x in t)))
target=0 if idx==3 else idx+1
print(' '.join(alph[target][alph[idx].index(x)] for x in t))

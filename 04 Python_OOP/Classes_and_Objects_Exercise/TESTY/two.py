from typing import List
from three import Three
from one import One
class Two(Three):
    '''asfasafdjhjasjflkjafjajhflkjafkjhjd
    skdjgksdfksdf
    sdkglskdg;sdg;lksd
    sdgkl;sdgls'''
    def __init__(self, name, age, skills = []):
        '''sssjlghsdljskdglhsdlsdfks;ldk;skdg;lks;lgdk
        
        
        
        
        
        gs,mngm,dsnmgkmskgksd;lgksd';g
        
        
        
        
        
        sgjlksjlgks;lgk;ldg;kd;lgk;sllgsdgsdg'''
        super().__init__(name, age)
        self.skills: List[skills] = []
    def add_skills(self):
        self.skills.append(person.get_info())
        print("############################")
        print(person.name)
        print("############################")
        self.skills.append("slkdgl;sdkglksdk;g;sldaslf")
        print(''.join(str(x) for x in self.skills))

person = One("Pesho", 8, [])
print(person.skills)
person.upgrade_skills()
print(person.skills)
print(person.get_info())

person_2 = Two("Gosho", 7)
person_2.add_skills()
print(person_2.skills)
print(person.name)
# print(person_2.__init__.__doc__)

print(person_2.__dict__)
print(Two.__dict__)


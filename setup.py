from setuptools import find_packages,setup
from typing import List # this helps to return the List 

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return  the list of requirements 
    '''
# here we defined a funct parameter give is file path in str form  the 
# return type is List in the form of str
    requiremnts=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements




setup(
    name='ML_Project',
    version='0.0.1',
    author='Sahil',
    author_email='mohdsahila132@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  
    
)
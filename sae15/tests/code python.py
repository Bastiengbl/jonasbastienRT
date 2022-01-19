#il est nÃ©cessaire d'importer le module linkedin via le menu tools puis PYTHONPATH avant de run 

from linkedin import linkedin 
APPLICATON_KEY = '86b0nf997mm7o5'
APPLICATON_SECRET = '8wsiuCdHl6lRVcfx'
RETURN_URL = 'http://localhost:8000'
authentication = linkedin.LinkedInAthentication(
                         APPLICATON_KEY,
                         APPLICATON_SECRET,
                         RETURN_URL, 
                         linkedin.PERMISSIONS.enums.values()
                    )
print(authentication.authorization_url) #ouvre cet url dans le navigateur
authentication.authorization_code = 'A COMPLETER'
result = authentication.get_access_token()

print("Access Token:", result.access_token)
print("Expires in (seconds):", result.expires_in)

from linkedin import server 
application = server.quick_api(APPLICATON_KEY, APPLICATON_SECRET) #j'ai modifiÃ© le code de base qui etait: (KEY, SECRET)
application.get_profile()
#le code suivant sera a modifier pour remplacer les paramÃ¨tres par la liste des noms RT que l'on a trouvÃ©
#The Profile API returns a memberâ€™s LinkedIn profile:
{'firstname': u'ozgur',
 u'headline': u'This is my headline',
 u'Last Name': u'vatansever',
 u'siteStandardProfileRequest': {u'url': u'https://www.linkedin.com/profile/view?id=46113651&authType=name&authToken=Egbj&trk=api*a101945*s101945*'}}
 
 #code complémentaire pour récupérer des infos supplémentaires sur les anciens RT
 application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
 {u'distance': 0,
  u'educations': {u'_total': 1,
 u'values': [{u'activities': u'This is my activity and society field',
   u'degree': u'graduate',
   u'endDate': {u'year': 2009},
   u'fieldOfStudy': u'computer science',
   u'id': 42611838,
   u'notes': u'This is my additional notes field',
   u'schoolName': u'\u0130stanbul Bilgi \xdcniversitesi',
   u'startDate': {u'year': 2004}}]},
u'firstName': u'ozgur',
u'id': u'COjFALsKDP',
u'lastName': u'vatansever',
u'location': {u'country': {u'code': u'tr'}, u'name': u'Istanbul, Turkey'},
u'numConnections': 13}
  
  
  
  
  
  }
 





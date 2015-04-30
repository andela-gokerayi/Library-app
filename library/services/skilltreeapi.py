import requests
import json
from django.http import HttpResponse
from library.settings.base import SKILLTREE_API_URL
from library.core.utils import to_dict


class SkillTree():
    """docstring for SkillTree"""
    def __init__(self):
        self.url = SKILLTREE_API_URL
        # self.headers = {'page': SKILLTREE_API_PAGE}

    def fetch_data(self, url, **kwargs):
        ''' Method to fetch data fom skilltree
            :param url: The url to request data from, default is the instance url
            :param kwargs: Any other extra keyword parameters
        '''
        url = url or self.url
        result = []
        page = 1
        while True:
            params = {'page': page}
            response = requests.get(url, params=params, data=json.dumps(kwargs))
            if requests_status_code == 404 or not response.json():
                break
            result.extend(response.json())
            page += 1        
        return result


def get_fellow_info():
    from apps.libraryuser.models import Fellow
    skill = SkillTree()
    url = SKILLTREE_API_URL
    # headers = SKILLTREE_API_PAGE
    results = SkillTree.fetch_data(skill, url)
    num_results = len(results)
    print num_results
    for index in xrange(num_results):
        fellow = results[index]
        try:
            person = Fellow.objects.get(first_name=fellow.get('first_name'), last_name=fellow.get('last_name'))  
        except Exception, e:
            new_fellow = Fellow(first_name=fellow.get('first_name'), last_name=fellow.get('last_name'), email=fellow.get('email'))
            new_fellow.save()
            continue
    return 'done'
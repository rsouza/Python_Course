# Implementaçao de Problemas provenientes do site Rosetta Code
O site [Rosetta Code](http://www.rosettacode.org) coleciona implementaçoes em varias linguagens, para problemas diversos.

Neste diretorio vamos colecionar implementaçoes em Python para problemas do Rosetta code. 

Podemos utilizar o codigo abaixo (proveniente do Rosetta code), para encontrar problemas sem implementaçao:

```python
"""
Given the name of a language on Rosetta Code,
finds all tasks which are not implemented in that language.
"""
from functools import partial
from operator import itemgetter
from typing import (Dict,
                    Iterator,
                    Union)
 
import requests
 
URL = 'http://www.rosettacode.org/mw/api.php'
REQUEST_PARAMETERS = dict(action='query',
                          list='categorymembers',
                          cmlimit=500,
                          rawcontinue=True,
                          format='json')
 
 
def unimplemented_tasks(language,url,request_params):
    """Yields all unimplemented tasks for a specified language"""
    with requests.Session() as session:
        tasks = partial(tasks_titles,
                        session=session,
                        url=url,
                        **request_params)
        all_tasks = tasks(cmtitle='Category:Programming_Tasks')
        language_tasks = set(tasks(cmtitle=f'Category:{language}'))
        for task in all_tasks:
            if task not in language_tasks:
                yield task
 
 
def tasks_titles(session,url,**params):
    """Yields tasks names for a specified category"""
    while True:
        request = session.get(url, params=params)
        data = request.json()
        yield from map(itemgetter('title'), data['query']['categorymembers'])
        query_continue = data.get('query-continue')
        if query_continue is None:
            return
        params.update(query_continue['categorymembers'])
 
 
if __name__ == '__main__':
    tasks = unimplemented_tasks('Python',
                                url=URL,
                                request_params=REQUEST_PARAMETERS)
    print(*tasks, sep='\n')
```

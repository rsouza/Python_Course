"""
Given the name of a language on Rosetta Code,
finds all tasks which are not implemented in that language.
"""
from functools import partial
from operator import itemgetter
import requests

URL = 'http://www.rosettacode.org/mw/api.php'
REQUEST_PARAMETERS = dict(action='query',
                          list='categorymembers',
                          cmlimit=500,
                          rawcontinue=True,
                          format='json')


def unimplemented_tasks(language, url, request_params):
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


def tasks_titles(session, url, **params):
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
    tasksD = tuple(unimplemented_tasks('D',
                                       url=URL,
                                       request_params=REQUEST_PARAMETERS))
    taskspy = tuple(unimplemented_tasks('Python',
                                        url=URL,
                                        request_params=REQUEST_PARAMETERS))
    print("====\nProblemas sem soluçao em D:\n====\n")
    print(*tasksD, sep='\n')
    print("====\nProblemas sem soluçao em Python:\n====\n")
    print(*taskspy, sep='\n')
    print("====\nproblemas sem soluçao em D e nem Python:\n====\n")
    print(*list(set(tasksD) & set(taskspy)), sep='\n')

import requests


class ApiCall():
    def __init__(url, collection):
        self.url = url
        self.collection = collection

    def _url(path):
        return self.url + '/'+self.collection + path

    def _get():
        response = requests.get(_url('/'))
        return "OK!" if response.status_code == 200\
            else raise ApiError(response.status_code)

    def _get_byID(id):
        self.id = id
        response = requests.get(_url('/{0}/'.format(id)))
        return "OK!" if response.status_code == 200\
            else raise ApiError(response.status_code)

    def _post(summary, description):
        task = {'summary': summary, 'description': description}
        response = requests.post(_url('/'), json=task)
        return "OK!" if response.status_code == 200\
            else raise ApiError(response.status_code)

    def _put(id, summary, description):
        task = {'summary': summary, 'description': description}
        response = requests.put(_url('/{0}'.format(id)), json=task)
        return "OK!" if response.status_code == 200\
            else raise ApiError(response.status_code)

    def _delete(id):
        response = requests.delete(_url('/{0}'.format(id)))
        return "OK!" if response.status_code == 200\
            else raise ApiError(response.status_code)

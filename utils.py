import json

def extract_route(request):
    if request != '':
        route = request.split()[1]
        route = route[1:]
        return route
    else:
        return ''

def read_file(path):
    img = open(path, mode='rb')
    return img.read()

def load_data(json_filename):
    json_path = 'data/' + json_filename
    json_file = open(json_path, mode='r')
    notes = json.load(json_file)

    return notes

def load_template(template_filename):
    template_path = 'templates/' + template_filename
    template_file = open(template_path, mode='r')
    template_content = template_file.read()

    return template_content

def build_response(body='', code=200, reason='OK', headers=''):
    if(code == 302): response = f'HTTP/1.1 {code} {reason}\n{headers}\n{body}\n'
    else: response = f'HTTP/1.1 {code} {reason}\n{headers}\n{body}'
    return response.encode()

def add_note(dict):
    pass
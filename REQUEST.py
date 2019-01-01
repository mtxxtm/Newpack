import requests
r = requests.get('http://httpbin.org/ip')
print(r.url)
print("Status Code: ")
print('\t[-]'+str(r.status_code)+'\n')

print('Server Header')
print("*************************")
for x in r.headers:
    print('\t'+x+':'+r.headers[x])
print("*************************")

print("Content:\n")
print(r.text)
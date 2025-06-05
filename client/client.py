import requests

while True:
    sql = input("SQL girin (çıkmak için q): ")
    if sql.lower() == 'q':
        break
    response = requests.post("http://server:5000/query", data={"sql": sql})
    print("Sonuç:", response.json())

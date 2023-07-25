def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")

try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")

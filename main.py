import jwt

secret_key = 'slkf;jfdsjfjhdsjkjsa'
secret_key2 = 'dfgdshajkhskhjks'
from datetime import datetime, timedelta

payload = {
   'name':"Kairat",
   'exp': datetime.utcnow() + timedelta(days=1),
   'lat': datetime.utcnow()

}

token = jwt.encode(payload, secret_key, algorithm='HS256')

# print(token)

t = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiS2FpcmF0In0.GR5cRc5sN9omttY2gRkb5QwZhXcf2In_LoeyIkI4ueo'

decode_token = jwt.decode(t, secret_key2, algorithms=['HS256'])

print(decode_token)
first create DB: http://127.0.0.1:5000/create_db
other stetting about DB check in config.py

post room http://127.0.0.1:5000/rooms

[
  {
    "level": 1,
    "status": "open",
    "price": 300

  },
  {
    "level": 1,
    "status": "open",
    "price": 400

  },
  {
    "level": 2,
    "status": "open",
    "price": 400

  },
  {
    "level": 2,
    "status": "open",
    "price": 200

  }
]

post staff http://127.0.0.1:5000/staff


[
	{
	"passport_id": 20154856,
	"name": "Jane",
	"position": "Admin",
	"salary": "150"
	},
	{
	"passport_id": 584968465,
	"name": "Jack",
	"position": "waiters",
	"salary": "150"
	},
	{
	"passport_id": 25648595,
	"name": "John",
	"position": "Cook",
	"salary": "150"
	}
]

post tenants http://127.0.0.1:5000/tenants

[
	{
	 "name": "Vova",
	 "passport_id": 25444755,
	 "age": 44,
	 "sex": "male"
	},
	{
	 "name": "Kola",
	 "passport_id": 23669588,
	 "age": 34,
	 "sex": "male"
	}
]

post address http://127.0.0.1:5000/address
[
{
    "city": "Lviv",
    "street": "Kovelska",
	  "tenants_id": 1
}
]
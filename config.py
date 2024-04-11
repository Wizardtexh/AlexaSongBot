import os
API_ID = int(os.getenv("24082649"))
API_HASH = os.getenv("4f6228c17e85f8c1912bb5002de70ee2")
BOT_TOKEN = os.getenv("6856257820:AAFWnxu1U1kvE5ScXbcYchic3xEq4Et_DCA")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})

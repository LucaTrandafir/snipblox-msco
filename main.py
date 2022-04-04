from fastapi import FastAPI
import os
import requests
from ro_py.client import Client
from dotenv import load_dotenv
import asyncio
load_dotenv()


APIKEY = os.getenv("API_KEY")


app = FastAPI()


@app.get("/group/promote/")
async def read_items(user_name: str, groupid: int, role_number: int, cookie: str):
    client = Client(cookie)
    

     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.promote()
     return ("The user was promoted!")


@app.get("/group/demote/")
async def read_items(user_name: str, groupid: int, role_number: int, cookie: str):
    client = Client(cookie)
    
 
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.demote()
     return ("The user was demoted!")


@app.get("/group/rank/")
async def read_items(user_name: str, groupid: int, role_number: int, cookie: str):
    client = Client(cookie)
    

     group = await client.get_group(groupid)
     target = await group.get_member_by_username(user_name)
     await target.setrole(role_number)
     return ("The user had their ranked changed")
 

@app.get("/group/members/")
async def read_items(user_name: str, groupid: int, cookie: str):
    client = Client(cookie)
    
     group = await client.get_group(groupid)
     return (group.member_count)


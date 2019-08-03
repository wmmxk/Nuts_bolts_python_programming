import sys
import os
from agent import Agent

save_dir = "./out_data"
os.makedirs(save_dir, exist_ok=True)
sys.stdout = open(save_dir+"/agent.log.txt", "w")

print(" message from main")

agent = Agent()
agent.train()

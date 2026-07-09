import random
import time
attempt = 0
attempt_retries = 5
attempt_wait_time = 1
 
while True:
    print("Attempt = ",attempt+1," - Wait Time = ",attempt_wait_time)
    if random.choice([True,False]):
        print("Sucess")
        break
    else: 
        print("Failed, retrying...")
        time.sleep(attempt_wait_time)
        attempt_wait_time*=2
        attempt+=1
    if attempt==5:
        print("All retries failed. Exiting...")
        break

    

 
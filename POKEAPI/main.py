from fastapi import FastAPI
import random

app = FastAPI()

poke_waifus = [
    "https://media.tenor.com/aG6B69tbvpEAAAAi/tokyomewmew-bridget.gif",
    "https://media.tenor.com/6-RcwwS-_9MAAAAi/yagalari-aka.gif",
    "https://media1.tenor.com/m/hSP6oVG2dTMAAAAC/yonomori-kobeni-anime-girl.gif",
    "https://i.pinimg.com/originals/cc/12/2e/cc122ec2a513f519f94fa7d78a9a23e9.gif",
    "https://media1.tenor.com/m/3dOqO4vVlr8AAAAC/poke-anime.gif",
    "https://media1.tenor.com/m/iu_Lnd86GxAAAAAd/nekone-utawarerumono.gif",
    "https://media1.tenor.com/m/iSumE3JoYokAAAAC/vn-visual.gif",
    "https://media1.tenor.com/m/OgM0CeJcgd0AAAAC/zakuro-cat.gif",
    "https://media.tenor.com/hRULqLfKvQwAAAAi/point-anime.gif",
    "https://media1.tenor.com/m/APqauOtznp4AAAAC/boop-poke.gif",
    "https://media1.tenor.com/m/D5VvK6Ud-nAAAAAC/anime-anime-poke.gif",
    "https://media1.tenor.com/m/0wPms8tS0eoAAAAd/boop-poke.gif",
    "https://media1.tenor.com/m/HJa3EjH0iNMAAAAd/poke.gif",
    "https://media1.tenor.com/m/NFU6KXm582gAAAAC/anime-blend-s.gif",
    "https://media1.tenor.com/m/7iV_gBGrRAUAAAAC/boop-poke.gif",
    "https://media1.tenor.com/m/Ur9uVvSUd1oAAAAC/boop-rascal-does-not-dream-of-bunny-girl-senpai.gif",
    "https://media1.tenor.com/m/kRoi_NIiiX0AAAAC/mess.gif",
    "https://media1.tenor.com/m/gMqsQ1wwbhgAAAAC/anime-poke.gif",
    "https://media1.tenor.com/m/vVtDnV6IEGYAAAAC/my-deer.gif",
    "https://media1.tenor.com/m/5j7eivfftw8AAAAd/poke.gif",
    "https://media1.tenor.com/m/ZlisNbF5uh8AAAAd/toradora-attack.gif",
]

@app.get("/sfw/poke")
def poke():
    return {"url": random.choice(poke_waifus)}
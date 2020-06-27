def check_key(keyName, resolution):
    import data

    if(keyName == "w" and data.player["posY"] > 0):
        for obj in data.objects:
            if(data.player["body_rect"].colliderect(data.objects[obj][1])):
                print(data.objects[obj][1], "test")
        data.player["posY"] -= data.movement_speed * \
            float(resolution[1])
        data.player["body_rect"].y = data.player["posY"]

    elif(keyName == "s" and data.player["posY"] < resolution[1] - data.player["body_size"][1]):
        data.player["posY"] += data.movement_speed * float(resolution[1])
        data.player["body_rect"].y = data.player["posY"]

    elif(keyName == "a" and data.player["posX"] > 0):
        data.player["posX"] -= data.movement_speed * float(resolution[0])
        data.player["body_rect"].x = data.player["posX"]

    elif(keyName == "d" and data.player["posX"] < resolution[0] - data.player["body_size"][0]):
        data.player["posX"] += data.movement_speed * float(resolution[0])
        data.player["body_rect"].x = data.player["posX"]

    elif(keyName == "wa" and (data.player["posX"] > 0 and data.player["posY"] > 0)):
        data.player["posX"] -= data.movement_speed * float(resolution[0])
        data.player["posY"] -= data.movement_speed * float(resolution[1])
        data.player["body_rect"].x = data.player["posX"]
        data.player["body_rect"].y = data.player["posY"]

    elif(keyName == "wd" and (data.player["posX"] < resolution[0] - data.player["body_size"][0] and data.player["posY"] > 0)):
        data.player["posX"] += data.movement_speed * float(resolution[0])
        data.player["posY"] -= data.movement_speed * float(resolution[1])
        data.player["body_rect"].x = data.player["posX"]
        data.player["body_rect"].y = data.player["posY"]

    elif(keyName == "as"and (data.player["posX"] > 0 and data.player["posY"] < resolution[1] - data.player["body_size"][1])):
        data.player["posX"] -= data.movement_speed * float(resolution[0])
        data.player["posY"] += data.movement_speed * float(resolution[1])
        data.player["body_rect"].x = data.player["posX"]
        data.player["body_rect"].y = data.player["posY"]

    elif(keyName == "ds" and (data.player["posX"] < resolution[0] - data.player["body_size"][0] and data.player["posY"] < resolution[1] - data.player["body_size"][1])):
        data.player["posX"] += data.movement_speed * float(resolution[0])
        data.player["posY"] += data.movement_speed * float(resolution[1])
        data.player["body_rect"].x = data.player["posX"]
        data.player["body_rect"].y = data.player["posY"]

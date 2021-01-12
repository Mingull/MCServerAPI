from mcstatus import MinecraftServer
import json


class ServerStatus():
    def __init__(self, ip: str):
        self.ip = ip
        self.ping = ""
        self.onlinePlayer = ""
        self.MOTD = ""
        self.strMOTD = ""
        self.ServerData = ""

    def returnServerData(self):
        serverData = MinecraftServer.lookup(self.ip)
        status = serverData.status()
        self.ping = status.latency
        self.onlinePlayer = status.players.online
        self.MOTD = status.description
        for textMOTD in self.MOTD["extra"]:
            self.strMOTD = self.strMOTD + textMOTD["text"]
        pass
        serverJson = {
            "IP": self.ip,
            "Ping": self.ping,
            "OnlinePlayers": self.onlinePlayer,
            "MOTD": self.strMOTD,
            "fullMOTD": self.MOTD
        }
        serverJson = json.dumps(serverJson, indent=4)
        self.ServerData = serverJson
        return self.ServerData

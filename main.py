import requests
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9f325775-a5e1-48cd-9299-5a5a06e5558e"
jason = {
    "msgtype":"text",
    "text":{
        "contnet":"内容发送实验"
    }
}
requests.post(url, jason)
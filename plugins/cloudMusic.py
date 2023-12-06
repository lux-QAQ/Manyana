import httpx
import requests
import json
# 定义请求的URL
from punishingHelper import get_headers
import asyncio
from asyncio import sleep





async def cccdddm(musicname):
    # 导入selenium库
    url='https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s='+musicname+'&type=1&offset=0&total=true&limit=5'
    #DAT={'s': musicname,'offset': 1,'limit': 1,'type': 1}
    #url = "http://music.wandhi.com/?name=" + musicname + "&type=netease"
    #header=get_headers()

    #r=requests.post(url)
    #print(r.text)
    async with httpx.AsyncClient(timeout=None,headers=get_headers()) as client:
        r = await client.post(url)
        #print(r.json().get("result").get("songs")[0].get("id"))
        id=r.json().get("result").get("songs")[0].get("id")
        path='data/music/' + r.json().get("result").get("songs")[0].get("name") + '.mp3'
        url="http://music.163.com/song/media/outer/url?id="+str(id)+".mp3"
        await musicDown(url,path)
        #path=await convert_to_silk(path)
        return path
async def musicDown(url, path):
    waf = requests.get(url).content
    with open(path, "wb") as f:
        f.write(waf)

'''import os, pilk
from pydub import AudioSegment

async def convert_to_silk(media_path: str) -> str:
    """将输入的媒体文件转出为 silk, 并返回silk路径"""
    media = AudioSegment.from_file(media_path)
    pcm_path = os.path.basename(media_path)
    rrr=media_path.replace(pcm_path,"")
    #print(rrr)
    pcm_path = os.path.splitext(pcm_path)[0]
    silk_path = rrr+pcm_path + '.silk'
    pcm_path += '.pcm'
    pcm_path=rrr+pcm_path
    print(silk_path,pcm_path)
    media.export(pcm_path, 's16le', parameters=['-ar', str(media.frame_rate), '-ac', '1']).close()
    pilk.encode(pcm_path, silk_path, pcm_rate=media.frame_rate, tencent=True)

    return silk_path'''

#asyncio.run(cccdddm("starlight delight"))
# musicDown("http://music.163.com/song/media/outer/url?id=1940303073.mp3")

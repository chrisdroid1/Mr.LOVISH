@Client.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client,message: Message):
    global is_downloading
    if is_downloading:
        await message.reply_text("Another download is in process try after sometime.")
        return

    urlissed = get_text(message)

    pablo =  await client.send_message(
            message.chat.id,
            f"`Getting {urlissed} From Youtube Servers. Please Wait.`")
    if not urlissed:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
    try:
        is_downloading = True
        with youtube_dl.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > 8:
                await pablo.edit(
                    f"Video is logerthan 20 minutes arent allowes provided video was {duration} Minutes"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)
            
    
    except Exception as e:
        #await pablo.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return
    
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**vid name** `{thum}` \n**requested :** `{urlissed}` \n**channel :** `{thums}` \n**link :** `{mo}`"
    await client.send_video(message.chat.id, video = open(file_stark, "rb"), duration = int(ytdl_data["duration"]), file_name = str(ytdl_data["title"]), thumb = sedlyf, caption = capy, supports_streaming = True , progress=progress, progress_args=(pablo, c_time, f'`Uᴘʟᴏᴀᴅɪɴɢ {urlissed} Sᴏɴɢ Fʀᴏᴍ YᴏᴜTᴜʙᴇ Mᴜꜱɪᴄ!`', file_stark))
    await pablo.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
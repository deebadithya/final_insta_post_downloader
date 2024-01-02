import logging
import telebot
import re
import instaloader
import requests
import logging
from instaloader import Post
import azure.functions as func

ig = instaloader.Instaloader(download_video_thumbnails=False,
                                download_comments=False,
                                save_metadata=False,
                                compress_json=False,
                                download_geotags=False,
                                post_metadata_txt_pattern="")

ig.login(user="insta_post_downloader", passwd="Helloworld@123")

def downloader(message, POST_ID, link, file_extension, index=1):
    response = requests.get(link)
    byte_data = response.content
    return (f"post_{POST_ID}_{index}{file_extension}", byte_data)
    

WEBHOOK = "https://azureinstaposttelebot.azurewebsites.net"
TOKEN = "6464285421:AAFnmFFBNkZpsFvGOBUImklRNkQLzDxX-6U"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to InstaB0t"
                     "\nPaste Instagram post's link"
                     "\n and I will provide you the file!")

@bot.message_handler(func=lambda message: True)
def message_handling(message):
    val = message.text
    POST_ID = val.strip().rsplit("/")[-2]
    pattern = re.compile(r'^[A-Za-z0-9]{11}$')
    try:
        if pattern.match(POST_ID):
            post = Post.from_shortcode(context=ig.context, shortcode=POST_ID)
            counts = post.mediacount

            if counts > 1:
                for index, i in enumerate(post.get_sidecar_nodes()):
                    if i.is_video:
                        f_name,raw_data = downloader(message, POST_ID, i.video_url, file_extension='.mp4', index=index+1)
                        bot.send_document(message.chat.id, raw_data, visible_file_name=f_name)
                        print(f_name)
                    else:
                        f_name,raw_data = downloader(message, POST_ID, i.display_url, file_extension='.jpg', index=index+1)
                        bot.send_document(message.chat.id, raw_data, visible_file_name=f_name)
                        print(f_name)
            else:
                file_extension = ".jpg" if post.typename == "GraphImage" else ".mp4"
                if post.typename == "GraphImage":
                    f_name,raw_data =  downloader(message, POST_ID, post.url, file_extension)
                    bot.send_document(message.chat.id, raw_data, visible_file_name=f_name)
                    print(f_name)
                else:
                    f_name,raw_data = downloader(message, POST_ID, post.video_url, file_extension)
                    bot.send_document(message.chat.id, raw_data, visible_file_name=f_name)
                    print(f_name)
            bot.reply_to(message,"and that's it!")
        else:
            bot.reply_to(message,"Invalid Link!\nEX: https://www.instagram.com/p/C1ccr6fxtD1/")
    except Exception as e:
        logging.exception("An error occurred in the main function.")


def main(req: func.HttpRequest) -> func.HttpResponse:
    bot.set_webhook(url=WEBHOOK)
    request_body_dict = req.get_json()
    update = telebot.types.Update.de_json(request_body_dict)
    bot.process_new_messages([update.message])
    return func.HttpResponse(body='', status_code=200)
